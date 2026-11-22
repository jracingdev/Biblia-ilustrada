"""Texto hebraico/aramaico do AT (STEPBible TAHOT, CC BY 4.0) e léxico (TBESH).
Uso:
  python3 ferramentas/original_at.py extrair <pasta TAHOT> <arquivo TBESH> <trabalho>
      grava em <trabalho>: partes_en.txt (glosas únicas, uma por linha) e lex_en.json
  python3 ferramentas/original_at.py gerar <pasta TAHOT> <arquivo TBESH> <trabalho>
      lê <trabalho>/partes_pt.json {en: pt} e lexpt_*.json {strong: {g, d}}
      grava data/original/at/<slug>.json, lexico-hebraico.json e at-strong.json
Cada palavra: [hebraico, transliteração, strong, morfologia, glosa]. Versificação em
português (a do texto em inglês do TAHOT; títulos dos Salmos entram no versículo 1)."""
import sys, re, json, glob, html, collections
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
COD = "Gen Exo Lev Num Deu Jos Jdg Rut 1Sa 2Sa 1Ki 2Ki 1Ch 2Ch Ezr Neh Est Job Psa Pro Ecc Sng Isa Jer Lam Ezk Dan Hos Jol Amo Oba Jon Mic Nam Hab Zep Hag Zec Mal".split()
SL = "genesis exodo levitico numeros deuteronomio josue juizes rute 1-samuel 2-samuel 1-reis 2-reis 1-cronicas 2-cronicas esdras neemias ester jo salmos proverbios eclesiastes cantares isaias jeremias lamentacoes ezequiel daniel oseias joel amos obadias jonas miqueias naum habacuque sofonias ageu zacarias malaquias".split()
CANT = re.compile("[\u0591-\u05AF\u05BD\u05C0\u05C3\u05C6]")  # acentos de cantilação, meteg, paseq, sof pasuq
def palavras(pasta):
    for f in sorted(glob.glob(str(Path(pasta) / "TAHOT*.txt"))):
        for linha in open(f, encoding="utf-8-sig"):
            m = re.match(r"^(\w{3})\.(\d+)\.(\d+)(?:\([\d.]+\))?#\d+=([^\t]*)\t", linha)
            if not m or m.group(1) not in COD: continue
            t = m.group(4)
            if not (t.startswith("L") or t.startswith("Q")): continue
            c = linha.rstrip("\n").split("\t")
            heb = CANT.sub("", c[1].split("\\")[0]).replace("/", "").strip()
            if not heb: continue
            tr = re.sub(r"[./\\]", "", c[2]).lower().strip()
            st = re.findall(r"\{(H\d+[A-Z]?)\}", c[4])
            st = re.sub(r"^H0*", "H", st[0]) if st else ""
            morf = c[5].split("\\")[0].strip()
            partes = [p.strip() for p in c[3].split("\\")[0].split("/") if p.strip()]
            v = max(1, int(m.group(3)))
            yield COD.index(m.group(1)), int(m.group(2)), v, heb, tr, st, morf, partes
def lexico(arq):
    lex = {}
    for linha in open(arq, encoding="utf-8-sig"):
        c = linha.rstrip("\n").split("\t")
        if len(c) < 8 or not re.match(r"^H\d+", c[0]): continue
        k = re.sub(r"^H0*", "H", c[1].split("=")[0].strip())
        if not re.match(r"^H\d+[A-Z]?$", k) or k in lex: continue
        d = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?i)<br\s*/?>", " | ", c[7])))
        d = re.sub(r"\s+", " ", d).strip(" |")
        lex[k] = {"lema": CANT.sub("", c[3]), "translit": c[4].replace(".", ""), "morf": c[5], "en": c[6], "def": d[:320]}
    return lex

FEM = set("terra noite luz mulher cidade mão árvore fonte casa porta lei palavra vida morte alma carne mesa voz paz guerra fé água semente filha mãe irmã esposa serva rainha arca tenda glória justiça verdade bênção maldição oferta oferenda aliança face boca língua cabeça espada lança pedra rocha montanha colina terra-firme congregação assembleia tribo família nação gente sabedoria força ira lua estrela nuvem chuva neve chama brasa cinza pele carne veste túnica coroa parede torre cerca vinha figueira oliveira videira ovelha vaca novilha jumenta pomba águia serpente fera besta mosca praga peste fome sede herança porção parte medida cova sepultura estrada rua viagem manhã tarde hora semana festa páscoa iniquidade transgressão maldade bondade misericórdia graça salvação libertação redenção honra vergonha nudez sombra imagem semelhança promessa ordem visão profecia mensagem resposta oração canção música harpa trombeta corda rede vara coluna base".split())
def art_pt(art, nxt):
    w = re.sub(r"^[\[<(]+", "", nxt.split(" ")[0]).lower().strip("]>)")
    if not w: return art
    pl = w.endswith("s") and len(w) > 3
    base = w[:-1] if pl and w.endswith("s") else w
    if base.endswith("e") and pl and w.endswith("es"): base = w[:-2]
    fem = base in FEM or w in FEM or re.search(r"(a|ção|dade|gem|ez|ude|ice)$", base) and not re.search(r"(ma|ta|eta|ista|dia|pa)$", base)
    a = ("as" if pl else "a") if fem else ("os" if pl else "o")
    return art.replace("o", a, 1)
CONTR = {("em","o"):"no",("em","a"):"na",("em","os"):"nos",("em","as"):"nas",("de","o"):"do",("de","a"):"da",("de","os"):"dos",("de","as"):"das",("a","o"):"ao",("a","a"):"à",("a","os"):"aos",("a","as"):"às",("por","o"):"pelo",("por","a"):"pela",("por","os"):"pelos",("por","as"):"pelas"}
def juntar(ps):
    ps = list(ps)
    for i in range(len(ps) - 1):
        if ps[i] in ("o", "[o]", "<o>"): ps[i] = art_pt(ps[i], ps[i + 1])
    out = []
    for p in ps:
        if out and (out[-1], p) in CONTR: out[-1] = CONTR[(out[-1], p)]; continue
        out.append(p)
    return " ".join(out)
modo, pasta, tbesh, W = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
ws = list(palavras(pasta)); lex = lexico(tbesh)
usados = collections.Counter(w[5] for w in ws)
if modo == "extrair":
    pc = collections.Counter(p for w in ws for p in w[7])
    (W / "partes_en.txt").write_text("\n".join(k for k, _ in pc.most_common()) + "\n", encoding="utf-8")
    faltam = [k for k in usados if k and k not in lex]
    (W / "lex_en.json").write_text(json.dumps({k: lex[k] for k in usados if k in lex}, ensure_ascii=False, indent=0), encoding="utf-8")
    print(len(ws), "palavras;", len(pc), "glosas únicas;", len(usados), "strongs;", len(faltam), "sem verbete", faltam[:20])
else:
    pt = json.loads((W / "partes_pt.json").read_text())
    lpt = {}
    for f in sorted(glob.glob(str(W / "lexpt_[0-9]*.json"))):
        if "part" not in f: lpt.update(json.loads(Path(f).read_text()))
    livros = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    occ = collections.defaultdict(list); semg = 0
    for b, c, v, heb, tr, st, morf, partes in ws:
        g = juntar(pt.get(p, p) for p in partes); semg += any(p not in pt for p in partes)
        livros[b][c][v].append([heb, tr, st, morf, g])
        ref = f"{b}.{c}.{v}"
        if st and (not occ[st] or occ[st][-1] != ref): occ[st].append(ref)
    out = RAIZ / "data/original"; (out / "at").mkdir(parents=True, exist_ok=True)
    for b, caps in livros.items():
        (out / "at" / f"{SL[b]}.json").write_text(json.dumps({"livro": SL[b], "fonte": "STEPBible TAHOT (Tyndale House, CC BY 4.0); glosas traduzidas para o português", "caps": {c: {v: ws for v, ws in sorted(vs.items())} for c, vs in sorted(caps.items())}}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    L = {}
    for k, e in lex.items():
        if k not in usados: continue
        p = lpt.get(k, {})
        L[k] = [e["lema"], e["translit"], p.get("g") or e["en"], p.get("d", ""), usados[k]]
    alias = {}
    for k in usados:
        if k and k not in L:
            base = re.sub(r"[A-Z]$", "", k); cand = sorted(x for x in L if re.sub(r"[A-Z]$", "", x) == base)
            if cand: alias[k] = cand[0]
    (out / "lexico-hebraico.json").write_text(json.dumps({"fonte": "STEPBible TBESH (Tyndale House, CC BY 4.0), baseado em BDB/Gesenius; definições resumidas em português", "alias": alias, "lex": L}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (out / "at-strong.json").write_text(json.dumps({"livros": SL, "occ": {k: ";".join(v) for k, v in occ.items()}}, separators=(",", ":")), encoding="utf-8")
    print(len(livros), "livros;", len(ws), "palavras;", semg, "palavras com glosa em inglês;", len(L), "verbetes;", sum(1 for k in L if k in lpt), "em português")
