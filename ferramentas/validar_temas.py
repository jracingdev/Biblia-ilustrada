"""Valida os arquivos temáticos da Bíblia inteira (reis, calendário, costumes, objetos, lugares, rotas).

Uso: python3 ferramentas/validar_temas.py data/biblia/reis.json [...]

Regra comum: todo campo chamado "refs" (em qualquer nível) é uma lista de referências
no formato "<slug> c:v", "<slug> c:v-v" ou "<slug> c:v-c:v" (slug de data/biblia/estrutura.json,
ex.: "1-reis 12:20"). Cada referência tem de existir no texto da Bíblia Livre.
Todo item de lista com "id" precisa de id único no arquivo.
Campos "fonte_extra" (quando existirem) precisam de "fonte", "referencia" e "data".
"""
import json, re, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
E = {l["slug"]: l for l in json.loads((RAIZ / "data/biblia/estrutura.json").read_text(encoding="utf-8"))["livros"]}
REF = re.compile(r"^([a-z0-9-]+) (\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$")
def ok_ref(r):
    m = REF.match(r or "")
    if not m or m[1] not in E: return False
    vs = E[m[1]]["versos"]; c, v = int(m[2]), int(m[3]); c2 = int(m[4] or c); f = int(m[5] or v)
    return 1 <= c <= len(vs) and 1 <= v <= vs[c-1] and c <= c2 <= len(vs) and 1 <= f <= vs[c2-1] and (c2, f) >= (c, v)
def andar(x, cam, erros, ids):
    if isinstance(x, dict):
        if "id" in x and isinstance(x["id"], str):
            if x["id"] in ids: erros.append(f"id repetido {x['id']}")
            ids.add(x["id"])
        for k, v in x.items():
            if k == "refs":
                if not isinstance(v, list): erros.append(f"{cam}.refs não é lista")
                else:
                    for r in v:
                        if not ok_ref(r): erros.append(f"{cam}: ref inválida '{r}'")
            elif k == "fonte_extra":
                for it in (v if isinstance(v, list) else [v]):
                    if not all(isinstance(it, dict) and str(it.get(c, "")).strip() for c in ("fonte", "referencia", "data")): erros.append(f"{cam}: fonte_extra incompleta")
            else: andar(v, f"{cam}.{k}", erros, ids)
    elif isinstance(x, list):
        for i, v in enumerate(x): andar(v, f"{cam}[{x[i].get('id', i) if isinstance(v, dict) else i}]", erros, ids)
if __name__ == "__main__":
    ruim = 0
    for p in sys.argv[1:]:
        try: d = json.loads(Path(p).read_text(encoding="utf-8"))
        except Exception as e: print("ERRO", p, e); ruim = 1; continue
        erros = []; andar(d, Path(p).stem, erros, set())
        print(("OK  " if not erros else "ERRO") + " " + p + ("" if not erros else ": " + "; ".join(erros[:15]) + (f" (+{len(erros)-15})" if len(erros) > 15 else "")))
        ruim |= bool(erros)
    sys.exit(ruim)
