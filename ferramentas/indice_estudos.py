"""Gera data/biblia/estudos-indice.json: para cada capítulo, os itens dos estudos temáticos que o citam.
Formato: {"itens": [[estudo, id, titulo]], "caps": {"<slug>": {"<c>": [indices]}}}
Uso: python3 ferramentas/indice_estudos.py"""
import json, os, re
B = os.path.join(os.path.dirname(__file__), '..', 'data', 'biblia')
J = lambda n: json.load(open(os.path.join(B, n + '.json')))
itens, caps = [], {}
RX = re.compile(r'^(\S+) (\d+)(?::\d+)?(?:-(?:(\d+):)?\d+)?$')
def add(est, id_, tit, refs):
    k = len(itens); usado = False
    for r in refs or []:
        m = RX.match(r)
        if not m: continue
        s, c1 = m.group(1), int(m.group(2)); c2 = int(m.group(3) or c1)
        for c in range(c1, c2 + 1):
            L = caps.setdefault(s, {}).setdefault(str(c), [])
            if k not in L: L.append(k); usado = True
    if usado: itens.append([est, id_, tit])
A = J('animais')
for a in A['animais']: add('animais', a['id'], a['nome'], a['refs'] + [p['ref'] for p in a.get('passagens', [])])
N = J('anjos')
for sec in ('tipos', 'nomeados', 'caidos'):
    for x in N[sec]: add('anjos', x['id'], x['nome'], x.get('refs', []) + [p['ref'] for p in x.get('aparicoes', [])])
for x in N['aparicoes']: add('anjos', x['id'], x['titulo'], x.get('refs', []) + [x['ref']])
T = J('tabernaculo')
for x in T['partes']: add('tabernaculo', x['id'], x['nome'], x.get('refs', []) + x.get('refs_nt', []))
NJ = J('nova-jerusalem')
for x in NJ['elementos']: add('nova-jerusalem', x['id'], x['nome'], x.get('refs', []) + x.get('raiz_at', []))
P = J('paulo')
for x in P['temas']: add('paulo', x['id'], x['titulo'], [r for p in x['pontos'] for r in p['refs']] + [r for rs in x.get('por_carta', {}).values() for r in rs])
L = J('leis')
for x in L['leis']: add('leis', x['id'], x['titulo'], x['refs'] + x.get('paralelos', []) + [r for c in x.get('casos', []) for r in c['refs']])
for x in L.get('casos', []): add('leis', x['id'], 'Caso: ' + x['titulo'], x['refs'])
# os índices precisam apontar para a posição final em itens
json.dump({'itens': itens, 'caps': caps}, open(os.path.join(B, 'estudos-indice.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(itens), 'itens,', sum(len(v) for v in caps.values()), 'capítulos')
