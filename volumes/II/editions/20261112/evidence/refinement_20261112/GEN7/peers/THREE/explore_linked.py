from pathlib import Path
import json
from interval_tools import *
d=json.loads(Path('evidence/residual_host.json').read_text());r=next(x for x in d['profiles'] if x['id']=='V000_BASE')
G=arr(r['G5']);D=arr(r['D5']);B=arr(r['B']);H=arr(r['H']);M=arr(r['core']);ds=[aa(x) for x in r['delta']];bg=[aa(x) for x in r['background']];V=arr(r['coefficients']);R=[dot([sup(x) for x in col],[arb(a) for a in [2,2,4,12,160,480,6400]]) for col in tr(V)];E0=aa(r['beta'])/int(r['N'])/(arb.pi()/4)**2
# Entrywise analytic physical core transfer, retaining cross sign.
P=[[M[i][j]+arb(0,sup(40*R[i]*R[j]*E0)) for j in range(2)] for i in range(2)]
# Bilinear full correction from both remainders and background Cauchy.
err=(20*ds[1]*upper(P[0][0])).sqrt()+(20*ds[0]*upper(P[1][1])).sqrt()+20*(ds[0]*ds[1]).sqrt()+(bg[0]*bg[1]).sqrt()
mixed=P[0][1]+arb(0,upper(err));a11=(upper(P[0][0]).sqrt()+(20*ds[0]).sqrt())**2+bg[0]
cap=aa(r['original_scalar_cap']);out={'mixed_core':wi(M[0][1]),'mixed_physical_core':wi(P[0][1]),'mixed_full':wi(mixed),'mixed_error':wi(err),'d11_upper':wi(a11),'histories':[]}
for ix in [0,18,36]:
 xi=aa(r['histories'][[0,18,36].index(ix)]['xi']);K=[[xi*G[i][j]+D[i][j] for j in range(5)] for i in range(5)];kiH=solve(K,H);kig=solve(K,[[v[0]] for v in G]);v=tr(mm(tr(H),kig))[0];T=mm(tr(H),kiH);s22=xi*B[1][1]+cap-T[1][1];s12=xi*B[0][1]+mixed-T[0][1];q=v[0]-s12*v[1]/s22
 # An admissible uncertain mixed action can exactly cancel the innovation.
 cancel=v[0]*s22/v[1]-xi*B[0][1]+T[0][1]
 pointcancel=mid(cancel);qmid=fl(q);out['histories'].append({'index':ix,'xi':r['histories'][[0,18,36].index(ix)]['xi'],'v1_over_v2':wi(v[0]/v[1]),'s22':wi(s22),'innovation_q':wi(q),'cancelling_D12':wi(cancel),'cancelling_midpoint':wi(pointcancel),'cancel_within_full_mixed_interval':bool(mixed.contains(cancel)),'q_contains_zero':bool(q.contains(0))})
 print('history',ix,'v1/v2',fl(v[0]/v[1]),'s22',fl(s22),'q',q,'cancel',cancel,'mix',mixed)
Path('evidence/linked_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
