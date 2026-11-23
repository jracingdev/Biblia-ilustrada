"""Atualiza data/site/contador.json com os números do serviço (só aumenta).
Uso: python3 ferramentas/contador_copia.py <visitantes> <acessos>"""
import json, sys, datetime, pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "data/site/contador.json"
d = json.loads(p.read_text(encoding="utf-8")); novo = dict(d)
for k, v in zip(("visitantes", "acessos"), sys.argv[1:3]):
    if v.isdigit() and int(v) > int(d.get(k, 0)): novo[k] = int(v)
if novo != d:
    novo["atualizado"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    p.write_text(json.dumps(novo, ensure_ascii=False) + "\n", encoding="utf-8")
    print("atualizado", novo)
else:
    print("sem mudança")
