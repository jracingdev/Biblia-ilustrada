"""Gera data/original/nt/<livro>.json (grego palavra por palavra) a partir do STEPBible TAGNT (CC BY 4.0).
Uso: python3 ferramentas/original_nt.py <pasta 'Translators Amalgamated OT+NT'> [pt_0.json pt_1.json ...]  (glosas espanhol normalizado -> português)
Formato: {"livro":slug,"caps":{"1":{"1":[[grego,translit,strong,morf,glosa], ...]}}}
Só entram palavras presentes nas edições críticas (tipo começando por N: NA27/NA28)."""
import sys, re, json, glob, collections
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
AB = "Mat Mrk Luk Jhn Act Rom 1Co 2Co Gal Eph Php Col 1Th 2Th 1Ti 2Ti Tit Phm Heb Jas 1Pe 2Pe 1Jn 2Jn 3Jn Jud Rev".split()
SL = "mateus marcos lucas joao atos romanos 1-corintios 2-corintios galatas efesios filipenses colossenses 1-tessalonicenses 2-tessalonicenses 1-timoteo 2-timoteo tito filemom hebreus tiago 1-pedro 2-pedro 1-joao 2-joao 3-joao judas apocalipse".split()
MAPA = dict(zip(AB, SL))
pasta = Path(sys.argv[1]); glosas = {}
for g in sys.argv[2:]: glosas.update(json.loads(Path(g).read_text()))
MIN = {"de","do","da","dos","das","a","o","as","os","e","para","em","no","na","com","por","ao","à","pelo","pela","dentro","procedente","sobre","entre"}
norm = lambda t: re.sub(r'[\s¶.,;:!?¿¡"“”()\[\]]+', ' ', t).strip().lower()
livros = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
usos = collections.Counter(); pares = collections.Counter(); ex = {}
for f in sorted(glob.glob(str(pasta / "TAGNT*.txt"))):
    for l in open(f, encoding="utf-8"):
        m = re.match(r"^(\w{3})\.(\d+)\.(\d+)#\d+=([^\t]*)\t", l)
        if not m or not m.group(4).startswith("N"): continue
        c = l.rstrip("\n").split("\t")
        gr, tr = re.match(r"^(.+?)\s*\((.*)\)$", c[1].strip()).groups() if "(" in c[1] else (c[1].strip(), "")
        st, mo = (c[3].split("=") + [""])[:2]
        st = re.sub(r"^G0*", "G", st)
        es = c[8].strip(); en = c[2].strip()
        chave = st + "|" + es
        pares[(st, es)] += 1; ex.setdefault((st, es), en); usos[st] += 1
        g = glosas.get(norm(es), "")
        if g and (re.search(r"-(P|L|T|PRI|LG|PG)\b", mo) or st == "G2316"): g = " ".join(x if x in MIN else x[:1].upper() + x[1:] for x in g.split(" "))
        livros[MAPA[m.group(1)]][m.group(2)][m.group(3)].append([gr, tr, st, mo, g])
saida = RAIZ / "data/original/nt"; saida.mkdir(parents=True, exist_ok=True)
for sl, caps in livros.items():
    (saida / f"{sl}.json").write_text(json.dumps({"livro": sl, "fonte": "STEPBible TAGNT (CC BY 4.0)", "caps": caps}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
Path("/tmp/claude-0/-home-user/4eb9774a-1cc7-54c1-88d7-461b3e94bef6/scratchpad/step/out/pares.json").write_text(json.dumps([[s, e, ex[(s, e)], k] for (s, e), k in pares.most_common()], ensure_ascii=False))
Path("/tmp/claude-0/-home-user/4eb9774a-1cc7-54c1-88d7-461b3e94bef6/scratchpad/step/out/usos.json").write_text(json.dumps(usos))
print(len(livros), "livros,", sum(usos.values()), "palavras,", len(usos), "Strong,", len(pares), "glosas")
