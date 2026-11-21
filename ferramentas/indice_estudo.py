"""Escreve data/estudo/livros/indice.json com os livros cujo estudo passa no validador."""
import json, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
from validar_estudo import validar
ordem = [l["slug"] for l in json.loads((RAIZ / "data/biblia/estrutura.json").read_text(encoding="utf-8"))["livros"]]
ok = [s for s in ordem if (RAIZ / f"data/estudo/livros/{s}.json").exists() and not validar(s)]
(RAIZ / "data/estudo/livros/indice.json").write_text(json.dumps({"livros": ok}, ensure_ascii=False), encoding="utf-8")
print(len(ok), "livros com estudo:", ", ".join(ok))
