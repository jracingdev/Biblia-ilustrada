"""Gera os arquivos de dados de um livro a partir da Bíblia Livre original.

Uso: python3 ferramentas/gerar_dados.py
Lê data/fonte-original/biblialivre.json e as listas em ferramentas/referencias_at.py
e ferramentas/quadros.py, e escreve:
  data/textos/blivre/apocalipse.json      texto por capítulo e versículo
  data/textos/blivre/at-apocalipse.json   trechos do AT citados nas conexões
  data/estudo/apocalipse-at.json          conexões com o Antigo Testamento
  data/estudo/apocalipse-quadros.json     quadros figurativos e prompts de ilustração
"""
import json, re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"
ns = {}
exec((RAIZ / "ferramentas/referencias_at.py").read_text(encoding="utf-8"), ns)
exec((RAIZ / "ferramentas/quadros.py").read_text(encoding="utf-8"), ns)
R, Q, ESTILO, REGRAS = ns["R"], ns["Q"], ns["ESTILO"], ns["REGRAS"]

biblia = json.loads((DADOS / "fonte-original/biblialivre.json").read_text(encoding="utf-8-sig"))
livros = {b["nome"]: b for b in biblia[1:]}
# Erros de digitação da fonte ("água" por "águia"), registrados em data/fontes.json
for _l, _c, _v in [("Êxodo", 19, 4), ("Levítico", 11, 13), ("Deuteronômio", 14, 12), ("Deuteronômio", 28, 49),
                   ("Deuteronômio", 32, 11), ("2 Samuel", 1, 23), ("Jó", 39, 27), ("Apocalipse", 12, 14)]:
    _cap = livros[_l]["capitulos"][_c - 1]
    _cap[_v - 1] = re.sub(r"\bágua(s?)\b", r"águia\1", _cap[_v - 1])
ABREV = {"Gn": "Gênesis", "Êx": "Êxodo", "Lv": "Levítico", "Nm": "Números", "Dt": "Deuteronômio", "Js": "Josué",
         "Jz": "Juízes", "2Sm": "2 Samuel", "1Rs": "1 Reis", "2Rs": "2 Reis", "Jó": "Jó", "Sl": "Salmos",
         "Pv": "Provérbios", "Ct": "Cantares", "Is": "Isaías", "Jr": "Jeremias", "Lm": "Lamentações",
         "Ez": "Ezequiel", "Dn": "Daniel", "Os": "Oséias", "Jl": "Joel", "Am": "Amós", "Mq": "Miqueias",
         "Na": "Naum", "Hc": "Habacuque", "Sf": "Sofonias", "Zc": "Zacarias", "Ml": "Malaquias"}

def trecho(ref):
    a, c, v, e1, e2 = re.match(r"^(\S+) (\d+):(\d+)(?:-(\d+)(?::(\d+))?)?$", ref).groups()
    caps = livros[ABREV[a]]["capitulos"]; c, v = int(c), int(v)
    fim = (int(e1), int(e2)) if e2 else ((c, int(e1)) if e1 else (c, v))
    out, cc, vv = [], c, v
    while (cc, vv) <= fim:
        if vv > len(caps[cc - 1]): cc, vv = cc + 1, 1; continue
        out.append({"c": cc, "v": vv, "t": caps[cc - 1][vv - 1].strip()}); vv += 1
    return {"livro": ABREV[a], "ref": ref, "versos": out}

trechos = {}
def refs(texto):
    lista = [x.strip() for x in texto.split(";") if x.strip()]
    for r in lista:
        trechos.setdefault(r, trecho(r))
    return lista

def salvar(caminho, obj, compacto=False):
    p = DADOS / caminho; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, **({"separators": (",", ":")} if compacto else {"indent": 1})), encoding="utf-8")

ap = livros["Apocalipse"]
salvar("textos/blivre/apocalipse.json", {"versao": "blivre", "livro": "apocalipse", "nome": "Apocalipse",
       "capitulos": [{"numero": i + 1, "versiculos": [{"n": j + 1, "texto": t.strip()} for j, t in enumerate(c)]}
                     for i, c in enumerate(ap["capitulos"])]}, compacto=True)
salvar("estudo/apocalipse-at.json", {"livro": "apocalipse",
       "descricao": "Alusões, citações e ecos do Antigo Testamento em Apocalipse, por versículo. Apocalipse não cita o AT com fórmulas; ele usa suas imagens.",
       "capitulos": [{"capitulo": c, "itens": [{"versos": vs, "refs": refs(rs), "nota": n} for vs, rs, n in it]} for c, it in R.items()]})
salvar("estudo/apocalipse-quadros.json", {"livro": "apocalipse", "estilo": "Realismo pictórico cinematográfico, na tradição da arte sacra clássica.",
       "prompt_estilo": ESTILO, "regras": REGRAS,
       "quadros": [{"id": f"q{i:02d}", "capitulo": int(ref.split(":")[0]), "ref": ref, "titulo": t, "descricao": d,
                    "at": refs(at), "prompt": ESTILO + p, "imagem": (f"img/quadros/q{i:02d}.webp" if (RAIZ / f"img/quadros/q{i:02d}.webp").exists() else None),
                    "credito": ("Ilustração gerada por IA (FLUX.1 Krea, via Hugging Face) a partir do prompt abaixo" if (RAIZ / f"img/quadros/q{i:02d}.webp").exists() else None), "alt": d} for i, (ref, t, d, p, at) in enumerate(Q, 1)]})
salvar("textos/blivre/at-apocalipse.json", {"versao": "blivre", "trechos": trechos}, compacto=True)
print(f"{len(Q)} quadros, {sum(len(x) for x in R.values())} conexões, {len(trechos)} trechos do AT")
