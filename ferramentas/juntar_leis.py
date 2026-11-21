"""Junta data/biblia/leis-a.json ... leis-d.json em data/biblia/leis.json (o site lê só leis.json).
Uso: python3 ferramentas/juntar_leis.py"""
import json, os
B = os.path.join(os.path.dirname(__file__), '..', 'data', 'biblia')
partes = [json.load(open(os.path.join(B, f'leis-{l}.json'))) for l in 'abcd' if os.path.exists(os.path.join(B, f'leis-{l}.json'))]
out = {'grupos': [], 'leis': [], 'notas': [], 'fonte_extra_intro': []}
for p in partes:
    for k in ('introducao', 'decalogo', 'decalogo_nota', 'sancoes', 'casos'):
        if k in p: out[k] = p[k]
    for k in ('nota', 'nota_geral'):
        if p.get(k): out['notas'].append(p[k])
    out['fonte_extra_intro'] += p.get('fonte_extra_intro', []) + p.get('fonte_extra', [])
    out['grupos'] += p['grupos']; out['leis'] += p['leis']
vistos = set(); fx = []
for f in out['fonte_extra_intro']:
    if f['referencia'] not in vistos: vistos.add(f['referencia']); fx.append(f)
out['fonte_extra_intro'] = fx
for g in out['grupos']:
    for sg in g['subgrupos']: sg['id'] = g['id'] + '--' + sg['id']
for l in out['leis']: l['subgrupo'] = l['grupo'] + '--' + l['subgrupo']
ids = [l['id'] for l in out['leis']]; assert len(ids) == len(set(ids)), 'ids repetidos'
json.dump(out, open(os.path.join(B, 'leis.json'), 'w'), ensure_ascii=False, indent=1)
print(len(out['grupos']), 'grupos,', len(out['leis']), 'leis')
