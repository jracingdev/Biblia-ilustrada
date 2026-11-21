"""Gera data/biblia/lugares.json a partir da base do OpenBible.info (CC BY 4.0) e dos nomes em português.

Uso: python3 ferramentas/lugares.py <lugares-base2.json>
Entrada extra (opcional): data/biblia/lugares-nomes.json {id: {pt, tipo_pt, resumo?}}
Saída compacta: {"fonte":..., "lugares":[{id, n, en, t, ll:[lon,lat], c:confiança 0-1000, r:[b*1000000+c*1000+v...], f:{a:autor, l:licença, u:url, d:descrição, s:satélite}}]}
"""
import json, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
base = json.load(open(sys.argv[1]))
np = RAIZ / "data/biblia/lugares-nomes.json"
nomes = json.loads(np.read_text(encoding="utf-8")) if np.exists() else {}
TIPO = {"settlement": "cidade", "region": "região", "mountain": "monte", "campsite": "acampamento", "river": "rio", "valley": "vale", "gate": "porta", "island": "ilha", "hill": "colina", "body of water": "mar ou lago", "natural area": "área natural", "structure": "construção", "spring": "fonte", "well": "poço", "road": "estrada", "people group": "povo", "field": "campo", "tower": "torre", "garden": "jardim", "pool": "tanque", "district": "bairro", "cave": "caverna", "forest": "bosque", "rock": "rocha", "fortification": "fortaleza", "wadi": "ribeiro", "canal": "canal", "altar": "altar", "mountain range": "cordilheira", "stone": "pedra", "tree": "árvore", "landmark": "marco"}
out = []
for p in base:
    if not p["ll"] or not p["refs"]: continue
    nm = nomes.get(p["id"], {})
    x = {"id": p["id"], "n": nm.get("pt") or p["en"].rsplit(" ", 1)[0] if p["en"][-1:].isdigit() else (nm.get("pt") or p["en"]), "en": p["en"], "t": nm.get("tipo_pt") or TIPO.get(p["tipo"], p["tipo"]), "ll": p["ll"], "c": p["conf"], "r": sorted({b * 1000000 + c * 1000 + v for b, c, v in p["refs"]})}
    if nm.get("pt"): x["n"] = nm["pt"]
    if nm.get("resumo"): x["s"] = nm["resumo"]
    im = p.get("img")
    if p.get("foto") and im:
        x["f"] = {"a": im.get("autor") or im["credit"], "l": im.get("lic") or ("Copernicus Sentinel, uso livre com atribuição" if im.get("sat") else ""), "u": im.get("url", ""), "d": im.get("desc", ""), "s": bool(im.get("sat"))}
    out.append(x)
d = {"fonte": "OpenBible.info Bible Geocoding Data, CC BY 4.0 (openbible.info/geo). Fotos: Wikimedia Commons e Copernicus Sentinel, com autor e licença em cada item.", "lugares": out}
(RAIZ / "data/biblia/lugares.json").write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(len(out), "lugares;", sum(1 for x in out if "f" in x), "com foto")
