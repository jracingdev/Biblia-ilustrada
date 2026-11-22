"""Gera o léxico grego em português e o índice de ocorrências por número Strong.
Uso: python3 ferramentas/strong_nt.py <pasta de trabalho com lexico_en.json, alias.json, lexpt_*.json>
Saídas: data/original/lexico-grego.json  {strong: [lema, translit, glosa, definição, ocorrências]}
        data/original/nt-strong.json     {strong: "livro.cap.vers;..."} (livro = índice 0-26 do NT)"""
import sys, json, glob, collections
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent; W = Path(sys.argv[1])
SL = "mateus marcos lucas joao atos romanos 1-corintios 2-corintios galatas efesios filipenses colossenses 1-tessalonicenses 2-tessalonicenses 1-timoteo 2-timoteo tito filemom hebreus tiago 1-pedro 2-pedro 1-joao 2-joao 3-joao judas apocalipse".split()
en = json.loads((W / "lexico_en.json").read_text()); alias = json.loads((W / "alias.json").read_text())
pt = {}
for f in sorted(glob.glob(str(W / "lexpt_[0-9].json"))): pt.update(json.loads(Path(f).read_text()))
occ = collections.defaultdict(list); cont = collections.Counter()
for i, sl in enumerate(SL):
    d = json.loads((RAIZ / f"data/original/nt/{sl}.json").read_text())
    for c, vs in d["caps"].items():
        for v, ws in vs.items():
            for w in ws:
                k = alias.get(w[2], w[2]); cont[k] += 1
                ref = f"{i}.{c}.{v}"
                if not occ[k] or occ[k][-1] != ref: occ[k].append(ref)
lex = {}
for k, e in en.items():
    p = pt.get(k, {})
    lex[k] = [e["lema"], e["translit"], p.get("g") or e["en"], p.get("d", ""), cont[k]]
out = RAIZ / "data/original"
(out / "lexico-grego.json").write_text(json.dumps({"fonte": "Abbott-Smith (domínio público) via STEPBible TBESG (CC BY 4.0); definições resumidas em português", "alias": alias, "lex": lex}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
(out / "nt-strong.json").write_text(json.dumps({"livros": SL, "occ": {k: ";".join(v) for k, v in occ.items()}}, separators=(",", ":")), encoding="utf-8")
print(len(lex), "verbetes;", sum(1 for k in lex if k in pt), "em português;", len(occ), "com ocorrências")
