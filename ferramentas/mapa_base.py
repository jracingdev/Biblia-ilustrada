"""Gera data/biblia/mapa-base.json (contornos em SVG) a partir do Natural Earth (domínio público).

Uso: python3 ferramentas/mapa_base.py <pasta com ne_10m_land.geojson, ne_10m_lakes.geojson, ne_10m_rivers_lake_centerlines.geojson>
Projeção equiretangular com escala cos(32°) na longitude. O site usa os mesmos parâmetros para projetar os lugares.
"""
import json, math, sys
from pathlib import Path
from shapely.geometry import shape, box, mapping
from shapely.ops import unary_union
SRC = Path(sys.argv[1]); RAIZ = Path(__file__).resolve().parent.parent
LON0, LAT1, K = 8.0, 46.0, math.cos(math.radians(32))
VIS = {"geral": (8, 12, 62, 46, 0.03), "levante": (33.0, 28.5, 38.5, 34.6, 0.004)}
RIOS = {"Nile", "Euphrates", "Tigris", "Jordan", "Orontes", "Kura", "Araks", "Halys", "Kizilirmak", "Karun", "Diyala", "Khabur", "Balikh", "Litani", "Tiber", "Arno", "Po", "Danube", "Yarmuk", "Kızılırmak", "Sakarya", "Menderes", "Great Zab", "Little Zab", "Rosetta", "Damietta"}
def P(lon, lat): return ((lon - LON0) * K * 10, (LAT1 - lat) * 10)
def caminho(g, fechar):
    out = []
    def anel(cs):
        pts = [P(x, y) for x, y in cs]
        if len(pts) < 2: return
        out.append("M" + "L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + ("Z" if fechar else ""))
    t = g.geom_type
    if t == "Polygon": anel(g.exterior.coords); [anel(i.coords) for i in g.interiors]
    elif t == "MultiPolygon": [caminho_poly(p, anel) for p in g.geoms]
    elif t == "LineString": anel(g.coords)
    elif t in ("MultiLineString", "GeometryCollection"):
        for x in g.geoms: out.append(caminho(x, fechar))
    return "".join(out)
def caminho_poly(p, anel): anel(p.exterior.coords); [anel(i.coords) for i in p.interiors]
land = [shape(f["geometry"]) for f in json.load(open(SRC / "ne_10m_land.geojson"))["features"]]
lakes = [(f["properties"].get("name") or "", shape(f["geometry"])) for f in json.load(open(SRC / "ne_10m_lakes.geojson"))["features"]]
rivers = [(f["properties"].get("name") or "", f["properties"].get("scalerank", 9), shape(f["geometry"])) for f in json.load(open(SRC / "ne_10m_rivers_lake_centerlines.geojson"))["features"]]
saida = {"projecao": {"lon0": LON0, "lat1": LAT1, "k": K, "escala": 10}, "fonte": "Natural Earth (naturalearthdata.com), domínio público", "vistas": {}}
for nome, (a, b, c, d, tol) in VIS.items():
    bx = box(a, b, c, d)
    terra = unary_union([g.intersection(bx) for g in land if g.intersects(bx)]).simplify(tol, preserve_topology=True)
    lag = unary_union([g.intersection(bx) for n, g in lakes if g.intersects(bx)]).simplify(tol, preserve_topology=True)
    rs = [g.intersection(bx).simplify(tol) for n, sr, g in rivers if g.intersects(bx) and (n in RIOS or sr <= (6 if nome == "geral" else 9))]
    x0, y0 = P(a, d); x1, y1 = P(c, b)
    saida["vistas"][nome] = {"viewBox": [round(x0, 2), round(y0, 2), round(x1 - x0, 2), round(y1 - y0, 2)], "terra": caminho(terra, True), "lagos": caminho(lag, True) if not lag.is_empty else "", "rios": "".join(caminho(r, False) for r in rs if not r.is_empty)}
p = RAIZ / "data/biblia/mapa-base.json"; p.write_text(json.dumps(saida, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(p, p.stat().st_size, {k: len(v["terra"]) for k, v in saida["vistas"].items()})
