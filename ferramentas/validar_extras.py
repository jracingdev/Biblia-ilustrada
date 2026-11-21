"""Valida as camadas extras de cada livro: data/estudo/extras/<slug>.json

Uso: python3 ferramentas/validar_extras.py [slug ...]

Todas as referências "cap:vers" ou "cap:vers-vers" são do PRÓPRIO livro e têm de existir no texto.
{
  "livro": "<slug>",
  "quadros": [   # cenas figurativas para ilustração realista (arte sacra). Ver quantidade no guia.
    {"id": "q01", "capitulo": 1, "ref": "1:1-5", "titulo": "...", "descricao": "1-2 frases em português",
     "alt": "texto alternativo para leitor de tela, 1 frase",
     "prompt": "English image prompt: scene only (o estilo é adicionado pelo site)"}
  ],
  "simbolos": [  # símbolos, imagens e figuras recorrentes do livro
    {"id": "kebab", "termo": "...", "ref": "1:1", "explicado": true|false, "significado": "1-3 frases"}
  ],
  "palavras": [  # palavras-chave nas línguas originais (mesmo formato de data/estudo/apocalipse-palavras.json)
    {"id": "kebab", "pt": "...", "refs": ["1:1"], "grego"?: {"lema","translit","strong"},
     "hebraico"?: {"lema","translit","strong"}, "aramaico"?: {...}, "sentido": "...",
     "latim": {"forma": "...", "nota": ""}, "outras": [{"lingua","forma","nota"}], "explicacao": "...", "interpretacao": false}
  ],
  "historia": [  # fontes EXTRABÍBLICAS (mesmo formato de data/estudo/apocalipse-historia.json)
    {"id","titulo","refs":["1:1"],"tipo": "historiador antigo"|"arqueologia"|"documento antigo"|"imprensa e arqueologia",
     "fonte","referencia","data_fonte","data_evento","resumo","relacao","grau": "documentado"|"associacao", "link"?: "https://..."}
  ]
}
"""
import json, re, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
estr = {l["slug"]: l for l in json.loads((RAIZ / "data/biblia/estrutura.json").read_text(encoding="utf-8"))["livros"]}
REF = re.compile(r"^(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$")
def ok_ref(r, vs):
    m = REF.match(r or "")
    if not m: return False
    c, v = int(m[1]), int(m[2]); c2 = int(m[3] or c); f = int(m[4] or v)
    return 1 <= c <= len(vs) and 1 <= v <= vs[c - 1] and c <= c2 <= len(vs) and 1 <= f <= vs[c2 - 1] and (c2, f) >= (c, v)
def nonempty(x): return isinstance(x, str) and x.strip() != ""
def validar(slug):
    p = RAIZ / f"data/estudo/extras/{slug}.json"; E = []
    try: d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: return [f"JSON inválido/ausente: {e}"]
    vs = estr[slug]["versos"]; N = len(vs)
    if d.get("livro") != slug: E.append("livro != slug")
    ids = set()
    Q = d.get("quadros", [])
    if not Q: E.append("sem quadros")
    for q in Q:
        k = q.get("id"); 
        if k in ids: E.append(f"id repetido {k}")
        ids.add(k)
        for c in ("titulo", "descricao", "alt", "prompt"):
            if not nonempty(q.get(c)): E.append(f"quadro {k}: falta {c}")
        if not isinstance(q.get("capitulo"), int) or not 1 <= q["capitulo"] <= N: E.append(f"quadro {k}: capitulo")
        if not ok_ref(q.get("ref"), vs) or int(q["ref"].split(":")[0]) != q.get("capitulo"): E.append(f"quadro {k}: ref {q.get('ref')}")
        if re.search(r"[áéíóúãõç]", q.get("prompt", "")): E.append(f"quadro {k}: prompt deve ser em inglês")
    caps = [q.get("capitulo") for q in Q]
    if caps != sorted(caps): E.append("quadros fora de ordem")
    for s in d.get("simbolos", []):
        if not nonempty(s.get("id")) or not nonempty(s.get("termo")) or not nonempty(s.get("significado")) or not isinstance(s.get("explicado"), bool): E.append(f"símbolo incompleto {s.get('id')}")
        if not ok_ref(s.get("ref"), vs): E.append(f"símbolo {s.get('id')}: ref {s.get('ref')}")
    for w in d.get("palavras", []):
        k = w.get("id")
        if not any(isinstance(w.get(l), dict) and nonempty(w[l].get("lema")) for l in ("grego", "hebraico", "aramaico")): E.append(f"palavra {k}: sem lema original")
        for l in ("grego", "hebraico", "aramaico"):
            x = w.get(l)
            if isinstance(x, dict):
                if not nonempty(x.get("translit")): E.append(f"palavra {k}: {l} sem translit")
                if x.get("strong") and not re.match(r"^[GH]\d+(, [GH]\d+)*$", x["strong"]): E.append(f"palavra {k}: strong '{x['strong']}'")
        for c in ("pt", "sentido", "explicacao"):
            if not nonempty(w.get(c)): E.append(f"palavra {k}: falta {c}")
        if not isinstance(w.get("latim"), dict) or not nonempty(w["latim"].get("forma")): E.append(f"palavra {k}: latim")
        if not w.get("refs") or not all(ok_ref(r, vs) for r in w["refs"]): E.append(f"palavra {k}: refs {w.get('refs')}")
    for h in d.get("historia", []):
        k = h.get("id")
        for c in ("titulo", "tipo", "fonte", "referencia", "data_fonte", "data_evento", "resumo", "relacao"):
            if not nonempty(h.get(c)): E.append(f"historia {k}: falta {c}")
        if h.get("grau") not in ("documentado", "associacao"): E.append(f"historia {k}: grau")
        if not h.get("refs") or not all(ok_ref(r, vs) for r in h["refs"]): E.append(f"historia {k}: refs {h.get('refs')}")
        if h.get("link") and not str(h["link"]).startswith("https://"): E.append(f"historia {k}: link")
    return E
if __name__ == "__main__":
    slugs = sys.argv[1:] or sorted(p.stem for p in (RAIZ / "data/estudo/extras").glob("*.json"))
    ruim = 0
    for s in slugs:
        e = validar(s); ruim += bool(e)
        print(("OK  " if not e else "ERRO") + f" {s}" + ("" if not e else ": " + "; ".join(e[:12]) + (f" (+{len(e)-12})" if len(e) > 12 else "")))
    sys.exit(1 if ruim else 0)
