"""Gera os dados da Bíblia inteira: textos de todos os livros e as conexões (referências cruzadas).

Uso: python3 ferramentas/gerar_biblia.py caminho/cross_references.txt
  - Texto: data/fonte-original/biblialivre.json (Bíblia Livre, CC BY 4.0 Brasil)
  - Referências cruzadas: OpenBible.info (CC BY), baseadas no Treasury of Scripture
    Knowledge (domínio público). Baixe em https://a.openbible.info/data/cross-references.zip
Escreve:
  data/biblia/estrutura.json            66 livros, grupo e nº de versículos por capítulo
  data/textos/blivre/livros/<slug>.json texto compacto de cada livro
  data/conexoes/livros.json             matriz 66x66 de ligações entre livros
  data/conexoes/capitulos.json          ligações mais fortes entre capítulos (toda a Bíblia)
  data/conexoes/livro/<slug>.json       ligações de um livro com os demais (para o livro-tema)
  data/conexoes/versos/<slug>.json      até 10 ligações por versículo (botão ↔ na leitura)
"""
import json, sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
D = RAIZ / "data"
OSIS = "Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal Matt Mark Luke John Acts Rom 1Cor 2Cor Gal Eph Phil Col 1Thess 2Thess 1Tim 2Tim Titus Phlm Heb Jas 1Pet 2Pet 1John 2John 3John Jude Rev".split()
IDX = {o: i for i, o in enumerate(OSIS)}
def grupo(i):
    if i < 5: return "lei"
    if i < 17: return "historicos"
    if i < 22: return "poeticos"
    if i < 27: return "maiores"
    if i < 39: return "menores"
    if i < 44: return "evangelhos"
    if i < 57: return "paulinas"
    if i < 65: return "gerais"
    return "apocalipse"

livros = json.loads((D / "livros.json").read_text(encoding="utf-8"))["livros"]
biblia = json.loads((D / "fonte-original/biblialivre.json").read_text(encoding="utf-8-sig"))[1:]
assert len(biblia) == 66 and len(livros) == 66

estr = []
(D / "textos/blivre/livros").mkdir(parents=True, exist_ok=True)
for i, (l, b) in enumerate(zip(livros, biblia)):
    caps = [[v.strip() for v in c] for c in b["capitulos"]]
    estr.append({"i": i, "slug": l["slug"], "nome": l["nome"], "abrev": b["abrev"].strip(), "testamento": l["testamento"],
                 "grupo": grupo(i), "versos": [len(c) for c in caps]})
    (D / f"textos/blivre/livros/{l['slug']}.json").write_text(json.dumps({"versao": "blivre", "livro": l["slug"], "nome": l["nome"], "c": caps}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

grupos = [{"id": "lei", "nome": "Lei (Pentateuco)"}, {"id": "historicos", "nome": "Históricos"}, {"id": "poeticos", "nome": "Poéticos"},
          {"id": "maiores", "nome": "Profetas maiores"}, {"id": "menores", "nome": "Profetas menores"}, {"id": "evangelhos", "nome": "Evangelhos e Atos"},
          {"id": "paulinas", "nome": "Cartas de Paulo"}, {"id": "gerais", "nome": "Hebreus e cartas gerais"}, {"id": "apocalipse", "nome": "Apocalipse"}]
total_v = sum(sum(e["versos"]) for e in estr)
(D / "biblia").mkdir(exist_ok=True)
(D / "biblia/estrutura.json").write_text(json.dumps({"grupos": grupos, "total_versiculos": total_v, "livros": estr}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

# índice global de capítulo
cap0, g = [], 0
for e in estr: cap0.append(g); g += len(e["versos"])
TOTAL_CAPS = g

def parse(ref):
    ref = ref.split("-")[0]
    b, c, v = ref.split(".")
    return IDX[b], int(c), int(v)

matriz = [[0] * 66 for _ in range(66)]
capw = defaultdict(int)
porlivro = defaultdict(lambda: defaultdict(list))   # foco -> alvo -> [(votos, fc, fv, ac, av)]
fococap = defaultdict(lambda: defaultdict(int))     # foco -> (fc, cap global alvo) -> votos
porverso = defaultdict(lambda: defaultdict(list))   # livro -> "c.v" -> [(votos, alvo, tc, tv)]
linhas = Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()[1:]
vistos = set()
for ln in linhas:
    a, b, votos = ln.split("\t")[:3]; votos = int(votos)
    if votos <= 0: continue
    (ba, ca, va), (bb, cb, vb) = parse(a), parse(b)
    if ba == bb: continue
    if ca > len(estr[ba]["versos"]) or cb > len(estr[bb]["versos"]): continue
    k = (min((ba, ca, va), (bb, cb, vb)), max((ba, ca, va), (bb, cb, vb)))
    if k in vistos: continue          # a mesma ligação nos dois sentidos conta uma vez
    vistos.add(k)
    matriz[ba][bb] += 1; matriz[bb][ba] += 1
    ga, gb = cap0[ba] + ca - 1, cap0[bb] + cb - 1
    capw[(min(ga, gb), max(ga, gb))] += votos
    for f, fc, fv, t, tc, tv in ((ba, ca, va, bb, cb, vb), (bb, cb, vb, ba, ca, va)):
        porlivro[f][t].append((votos, fc, fv, tc, tv))
        fococap[f][(fc, cap0[t] + tc - 1)] += votos
        porverso[f][f"{fc}.{fv}"].append((votos, t, tc, tv))

(D / "conexoes/livro").mkdir(parents=True, exist_ok=True)
(D / "conexoes/livros.json").write_text(json.dumps({"fonte": "OpenBible.info (CC BY), a partir do Treasury of Scripture Knowledge (domínio público)", "matriz": matriz}, separators=(",", ":")), encoding="utf-8")
top = sorted(capw.items(), key=lambda x: -x[1])[:24000]
plano = []
for (x, y), w in sorted(top): plano += [x, y, w]
(D / "conexoes/capitulos.json").write_text(json.dumps({"total_capitulos": TOTAL_CAPS, "ligacoes": len(top), "dados": plano}, separators=(",", ":")), encoding="utf-8")

for f in range(66):
    alvos = {}
    for t, lst in porlivro[f].items():
        lst.sort(key=lambda x: -x[0])
        alvos[t] = {"n": len(lst), "top": [[fc, fv, tc, tv, v] for v, fc, fv, tc, tv in lst[:40]]}
    arcos = sorted(fococap[f].items(), key=lambda x: -x[1])[:3500]
    plano = []
    for (fc, gc), w in sorted(arcos): plano += [fc, gc, w]
    (D / f"conexoes/livro/{estr[f]['slug']}.json").write_text(json.dumps({"livro": f, "alvos": alvos, "arcos": plano}, separators=(",", ":")), encoding="utf-8")
(D / "conexoes/versos").mkdir(parents=True, exist_ok=True)
for f in range(66):
    idx = {k: [[t, tc, tv] for v, t, tc, tv in sorted(lst, key=lambda x: -x[0])[:10]] for k, lst in porverso[f].items()}
    (D / f"conexoes/versos/{estr[f]['slug']}.json").write_text(json.dumps(idx, separators=(",", ":")), encoding="utf-8")
print("livros", len(estr), "versículos", total_v, "capítulos", TOTAL_CAPS, "ligações únicas", len(vistos), "pares de capítulos", len(capw))
