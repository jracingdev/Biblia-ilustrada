"""Valida os arquivos de estudo dos livros: data/estudo/livros/<slug>.json

Uso: python3 ferramentas/validar_estudo.py [slug ...]   (sem argumentos valida todos)

Esquema (todas as referências são "cap:vers" ou "cap:vers-vers" DENTRO do próprio livro):
{
  "livro": "genesis", "nome": "Gênesis",
  "subtitulo": "frase curta",
  "introducao": "2 a 4 frases: do que trata o livro e por que importa",
  "fatos": [{"rotulo": "Autor"|"Quando"|"Onde"|"Para quem"|"Gênero"|"Tamanho", "valor": "..."}],   # 4 a 6
  "chave": "1:1",                                   # versículo-chave do livro
  "temas": ["...", "..."],                          # 3 a 6 temas centrais, frases curtas
  "cristo": "1 a 3 frases: como o livro aponta para Cristo / se liga ao evangelho (sem forçar)",
  "secoes": [{"id": "kebab", "titulo": "...", "capitulos": [1,2,3], "resumo": "1 frase"}],  # cobrem todos os capítulos, em ordem, sem repetir
  "capitulos": [                                    # um por capítulo, n = 1..N
    {"n": 1, "titulo": "...", "chave": "1:26-27",
     "resumo": "2 a 4 frases fiéis ao texto",
     "licoes": ["frase com referência entre parênteses (1:27)", "...", "..."],   # 2 a 4, cada uma com ao menos uma (c:v)
     "reflexao": "1 pergunta pessoal",
     "quiz": [{"pergunta": "...", "opcoes": ["a","b","c","d"], "correta": 0..3, "ref": "1:3"}]}  # exatamente 1, 4 opções
  ]
}
"""
import json, re, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
estr = {l["slug"]: l for l in json.loads((RAIZ / "data/biblia/estrutura.json").read_text(encoding="utf-8"))["livros"]}
REF = re.compile(r"^(\d+):(\d+)(?:-(\d+))?$")
def ok_ref(r, vs):
    m = REF.match(r or "")
    if not m: return False
    c, v, f = int(m[1]), int(m[2]), int(m[3] or m[2])
    return 1 <= c <= len(vs) and 1 <= v <= vs[c - 1] and v <= f <= vs[c - 1]
def validar(slug):
    p = RAIZ / f"data/estudo/livros/{slug}.json"; erros = []
    try: d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: return [f"JSON inválido ou ausente: {e}"]
    vs = estr[slug]["versos"]; N = len(vs)
    if d.get("livro") != slug: erros.append("campo livro difere do slug")
    for k in ("nome", "subtitulo", "introducao", "chave", "cristo"):
        if not isinstance(d.get(k), str) or not d[k].strip(): erros.append(f"falta {k}")
    if not ok_ref(d.get("chave"), vs): erros.append(f"chave inválida {d.get('chave')}")
    if not (3 <= len(d.get("fatos", [])) <= 7): erros.append("fatos: 4 a 6 itens")
    if not (2 <= len(d.get("temas", [])) <= 7): erros.append("temas: 3 a 6 itens")
    caps_sec = [c for s in d.get("secoes", []) for c in s.get("capitulos", [])]
    if caps_sec != list(range(1, N + 1)): erros.append(f"seções devem cobrir 1..{N} em ordem sem repetir")
    for s in d.get("secoes", []):
        if not s.get("id") or not s.get("titulo") or not s.get("resumo"): erros.append(f"seção incompleta {s.get('id')}")
    caps = d.get("capitulos", [])
    if [c.get("n") for c in caps] != list(range(1, N + 1)): erros.append(f"capitulos devem ser n=1..{N} (tem {len(caps)})")
    for c in caps:
        n = c.get("n")
        for k in ("titulo", "resumo", "reflexao"):
            if not isinstance(c.get(k), str) or len(c[k].strip()) < 8: erros.append(f"cap {n}: falta {k}")
        if c.get("chave") and not ok_ref(c["chave"], vs): erros.append(f"cap {n}: chave inválida {c['chave']}")
        lic = c.get("licoes", [])
        if not (2 <= len(lic) <= 4): erros.append(f"cap {n}: 2 a 4 lições")
        for l in lic:
            grupos = re.findall(r"\((\d+:\d+(?:-\d+)?(?:[,;] ?\d+:\d+(?:-\d+)?)*)\)", l)
            if not grupos: erros.append(f"cap {n}: lição sem (c:v): {l[:50]}")
            for g in grupos:
                for r in re.findall(r"\d+:\d+(?:-\d+)?", g):
                    if not ok_ref(r, vs): erros.append(f"cap {n}: ref inválida {r}")
        qz = c.get("quiz", [])
        if len(qz) != 1: erros.append(f"cap {n}: exatamente 1 quiz")
        for q in qz:
            if len(q.get("opcoes", [])) != 4 or q.get("correta") not in (0, 1, 2, 3) or not q.get("pergunta"): erros.append(f"cap {n}: quiz malformado")
            if not ok_ref(q.get("ref"), vs): erros.append(f"cap {n}: quiz ref inválida {q.get('ref')}")
    return erros
if __name__ == "__main__":
    slugs = sys.argv[1:] or sorted(p.stem for p in (RAIZ / "data/estudo/livros").glob("*.json") if p.stem != "indice")
    ruim = 0
    for s in slugs:
        e = validar(s)
        print(("OK  " if not e else "ERRO") + f" {s}" + ("" if not e else ": " + "; ".join(e[:12]) + (f" (+{len(e)-12})" if len(e) > 12 else "")))
        ruim += bool(e)
    sys.exit(1 if ruim else 0)
