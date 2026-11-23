"""Preenche "imagem" e "credito" dos quadros em data/estudo/extras/*.json
conforme os arquivos existentes em img/quadros/<livro>/qNN.webp.
Uso: python3 ferramentas/imagens_extras.py"""
import json, pathlib
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CRED = "Ilustração gerada por IA (Gemini 2.5 Flash Image, Google)"
n = 0
for f in sorted((RAIZ / "data/estudo/extras").glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8")); mudou = False
    for q in d.get("quadros", []):
        img = RAIZ / f"img/quadros/{f.stem}/{q['id']}.webp"
        novo = (f"img/quadros/{f.stem}/{q['id']}.webp", CRED) if img.exists() else (None, None)
        if (q.get("imagem"), q.get("credito")) != novo:
            if novo[0]: q["imagem"], q["credito"] = novo
            else: q.pop("imagem", None); q.pop("credito", None)
            mudou = True
        n += bool(novo[0])
    if mudou:
        raw = f.read_text(encoding="utf-8")
        ind = 2 if raw.startswith('{\n  ') else (1 if raw.startswith('{\n ') else None)
        f.write_text(json.dumps(d, ensure_ascii=False, indent=ind, separators=None if ind else (",", ":")) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
print(n, "quadros com imagem")
