from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations,combinations_with_replacement
from functools import lru_cache
import json,gzip,csv,hashlib
import sympy as sy

HERE=Path(__file__).resolve().parent
ROOT=Path('/home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111')
ONE=ROOT/'peers/ONE'; FOUR=ROOT/'peers/FOUR'
OUT=HERE/'results'; TASK=HERE/'tasks';OUT.mkdir(exist_ok=True);TASK.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x
def save(n,x): (OUT/n).write_text(json.dumps(encode(x),indent=2)+'\n')
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def ident(n):return [[F(i==j) for j in range(n)]for i in range(n)]
def mat(a,rb=None,cb=None,herm=False):return {'entries':encode(a),'row_basis':list(range(len(a))) if rb is None else rb,'column_basis':list(range(len(a[0]))) if cb is None else cb,'structure':'HERMITIAN' if herm else 'GENERAL'}
def st(name,op,*inputs,**kw):return dict(name=name,op=op,inputs=list(inputs),**kw)
def task(key,op,data,purpose,sources=None,word=False):
 payload=data if word else dict(precision_bits=256,data=data)
 obj=dict(kind='native',key=key,operation=op,purpose=purpose,payload=payload)
 (TASK/(key+'.json')).write_text(json.dumps(encode(obj),indent=2)+'\n')
def wordpayload(name,n,ops,program,output):
 return dict(name=name,context=dict(basis=list(range(n)),field=dict(radicand=0),units=dict(reference='Original source units, physical calibration unassigned'),history=dict(source_hashes=manifest,scope='Lane FOUR independent raw operand reconstruction'),spectral_coordinate='RETAINED_SOURCE'),data=dict(operators=encode(ops),program=program,output=output))

qpath=ONE/'sources/INDUCED_INPUT_H002423.json'
ipath=ONE/'sources/isotope_residuals_253_20261017/INPUT_ROWS.json.gz'
spath=ONE/'sources/isotope_residuals_253_20261017/ISOTOPE_PREDICTIONS.csv'
tpath=ONE/'sources/isotope_residuals_240_tensor_20261017/ISOTOPE_PREDICTIONS.csv'
manifest={str(p):sha(p) for p in [qpath,ipath,spath,tpath,HERE/'PRECOMMIT.md',HERE/'reconstruct.py']}
save('SOURCE_MANIFEST.json',manifest)
Q=[[F(x)for x in r]for r in json.loads(qpath.read_text())['data']['operator']]
den=(1+Q[0][0])**2
B=[[ (Q[i%4][j%4]*Q[i//4][j//4]+(i//4==j//4)*Q[i%4][j%4]+(i%4==j%4)*Q[i//4][j//4]+F(i%4==j//4 and i//4==j%4))/den for j in range(16)]for i in range(16)]
perms=list(permutations(range(4)))
Bs=[[[B[p[i%4]+4*p[i//4]][p[j%4]+4*p[j//4]]for j in range(16)]for i in range(16)]for p in perms]
mean=[[sum(b[i][j]for b in Bs)/24 for j in range(16)]for i in range(16)]
start=(6,0,0,0); end=(0,0,2,2)
def nxt(s):
 a,b,c,d=s;ans=[]
 if a>0 and b+c<2:ans.append(('A',(a-1,b+1,c,d)))
 if b>0 and c<2:ans.append(('B',(a,b-1,c+1,d)))
 if a>=2 and d<2:ans.append(('C',(a-2,b,c,d+1)))
 return ans
@lru_cache(None)
def paths(s):
 if s==end:return [((),(s,))]
 return [((a,)+w,(s,)+ss)for a,t in nxt(s) for w,ss in paths(t)]
ps=paths(start);states=sorted({s for _,ss in ps for s in ss},key=lambda s:(s[1]+2*s[2]+s[3],s))
def port(s):
 u=[F(s[0],6),F(s[1],6),F(s[2],6),F(2*s[3],6)]
 return [u[i%4]*u[i//4]for i in range(16)]
P=tr([port(s)for s in states]);Gram=mm(tr(P),mm(mean,P));idx={s:i for i,s in enumerate(states)}
def summarize(ss,G):
 ii=[idx[s]for s in ss]; ee=[G[i][i]for i in ii];ww=[v-u for u,v in zip(ee,ee[1:])]
 return dict(variation=sum(G[j][j]+G[i][i]-2*G[i][j]for i,j in zip(ii,ii[1:])),work=sum(ww),gross=sum(max(F(0),w)for w in ww),capital=max(F(0),max(ee)-ee[0]),storage=ee[0]-min(ee),energies=ee)
records=[dict(word=''.join(w),states=ss,**summarize(ss,Gram))for w,ss in ps]
rolegrams=[mm(tr(P),mm(b,P))for b in Bs]
cost=[[summarize(ss,g)['variation']for g in rolegrams]for _,ss in ps]
rolemins=[min(col)for col in zip(*cost)]
coverage=[{j for j in range(24)if row[j]==rolemins[j]}for row in cost]
covers=[]
for k in range(1,4):
 covers=[c for c in combinations(range(30),k)if set.union(*(coverage[i]for i in c))==set(range(24))]
 if covers:break
pareto=[]
for i,a in enumerate(records):
 if not any(all(b[x]<=a[x]for x in ['variation','gross','storage'])and any(b[x]<a[x]for x in ['variation','gross','storage'])for b in records):pareto.append(i)
# Independently evaluate shortest-path recurrence as well as complete enumeration.
@lru_cache(None)
def bellman(s):
 if s==end:return F(0)
 i=idx[s];return min(Gram[i][i]+Gram[idx[t]][idx[t]]-2*Gram[i][idx[t]]+bellman(t)for _,t in nxt(s))
minimum=min(r['variation']for r in records);assert bellman(start)==minimum
diag=[[mean[i][j]if i==j else F(0)for j in range(16)]for i in range(16)]
badgram=mm(tr(P),mm(diag,P));can=next(r for r in records if r['word']=='ABABCC');badcan=summarize(can['states'],badgram)
dp=dict(denominator=den,states=states,path_count=len(ps),B=B,role_mean_B=mean,full_Gram=Gram,rank=int(sy.Matrix(Gram).rank()),paths=records,role_costs=cost,role_minima=rolemins,rolewise_mean=sum(rolemins)/24,min_variation=minimum,min_gross=min(r['gross']for r in records),min_storage=min(r['storage']for r in records),value_of_information=minimum-sum(rolemins)/24,minimum_policy_actions=k,covers=covers,fibers=[[len(coverage[i])for i in c]for c in covers],pareto_indices=pareto,control_diagonal_canonical=badcan,control_residual=badcan['variation']-can['variation'])
save('C12_DP.json',dp)
# Native reconstructs Q-derived literal form and the full role-averaged state Gram.
swap=[[F(i%4==j//4 and i//4==j%4)for j in range(16)]for i in range(16)]
ops=dict(Q=Q,I=ident(4),Swap=swap,P=P);prog=[st('QQ','tensor','Q','Q'),st('QI','tensor','Q','I'),st('IQ','tensor','I','Q'),st('s1','add','QQ','QI'),st('s2','add','s1','IQ'),st('s3','add','s2','Swap'),st('B','scale','s3',factor=str(1/den))]
names=[]
for k0,p in enumerate(perms):
 pp=[[F(i==p[j%4]+4*p[j//4])for j in range(16)]for i in range(16)];ops['R'+str(k0)]=pp
 prog += [st('rt'+str(k0),'transpose','R'+str(k0)),st('br'+str(k0),'multiply','B','R'+str(k0)),st('o'+str(k0),'multiply','rt'+str(k0),'br'+str(k0))];names.append('o'+str(k0))
cur=names[0]
for j,n in enumerate(names[1:]):prog.append(st('add'+str(j),'add',cur,n));cur='add'+str(j)
prog +=[st('mean','scale',cur,factor='1/24'),st('mp','multiply','mean','P'),st('pt','transpose','P'),st('G','multiply','pt','mp')]
task('FOUR_DP_GRAM_V1','GEN3_SOURCE_OPERATOR_WORD',wordpayload('FOUR_DP_GRAM_V1',18,ops,prog,'G'),'Rebuild original Q, all24 role conjugations and all18 state self/cross Grams for independently enumerated30paths',word=True)

rows=json.load(gzip.open(ipath,'rt'))['rows'];coord={(r['Z'],r['N']):i for i,r in enumerate(rows)}
spin={r['id']:r for r in csv.DictReader(spath.open())};ten={r['id']:r for r in csv.DictReader(tpath.open())}
tk=next(k for k in next(iter(ten.values()))if k.endswith('_prediction_MeV'))
contr=[]
for h in [1,2]:
 for z,n in sorted(coord):
  cs=[(z,n-h),(z,n),(z,n+h)]
  if all(c in coord for c in cs):contr.append(dict(kind='N'+str(h),coords=cs,weights=[1,-2,1]))
for z,n in sorted(coord):
 cs=[(z,n),(z+2,n),(z,n+2),(z+2,n+2)]
 if all(c in coord for c in cs):contr.append(dict(kind='ZN2',coords=cs,weights=[1,-1,-1,1]))
W=[];values=[]
for r in rows:
 values.append([F(1),F(r['Z']),F(r['N']),F(r['B_reference_MeV_exact']),F(spin[r['id']]['BULK_NORMALIZED_SPIN_prediction_MeV']),F(ten[r['id']][tk])if r['id']in ten and ten[r['id']][tk]else F(0)])
for c in contr:
 w=[F(0)]*len(rows)
 for co,ww in zip(c['coords'],c['weights']):w[coord[co]]=F(ww)
 W.append(w);res=mm([w],values)[0];assert res[:3]==[0,0,0];c['contractions']=res
 if c['kind'].startswith('N'):
  z,n=c['coords'][1];h=c['coords'][2][1]-n;A=z+n
  direct=sum(F(ww)*F((nn-zz)**2,nn+zz)for (zz,nn),ww in zip(c['coords'],c['weights']))
  assert direct==F(8*z*z*h*h,A*(A*A-h*h));c['curvature']=direct
anchors=[r for r in rows if r['split']=='constituent_anchor'];am=[[F(r['features'][k])for k in ['A','surface','C']]for r in anchors];rhs=[[F(r['B_reference_MeV_exact'])]for r in anchors]
sol=sy.Matrix(am).inv()*sy.Matrix(rhs);coef=[F(int(v.p),int(v.q))for v in sol]
ref=dict(roster=len(rows),counts={k:sum(c['kind']==k for c in contr)for k in ['N1','N2','ZN2']},contrasts=contr,anchor_matrix=am,anchor_rhs=rhs,anchor_coefficients=coef,anchor_determinant=F(sy.det(sy.Matrix(am))),control_reference_residual=[1,contr[0]['coords'][1][0],contr[0]['coords'][1][1]])
save('REFERENCES.json',ref)
task('FOUR_REFERENCE_BANK_V1','GEN3_COMPLEX_PRODUCT',dict(matrix=mat(W,list(range(176)),list(range(253))),right=mat(values,list(range(253)),['1','Z','N','REF','SPIN','TENSOR'])),'All176 actual roster stencil contractions against affine nuisance and three unchanged frozen value columns')
task('FOUR_ANCHOR_SOLVE_V1','GEN3_COMPLEX_SOLVE',dict(matrix=mat(am,['H1','H2','He3'],['A','surface','C']),rhs=mat(rhs,['H1','H2','He3'],['BINDING'])),'Exact rank3 anchor interpolation on original source decimals; no global fit or refit')

alphabet=[1,2,3,4,6,8,9,12];triples=list(combinations_with_replacement(alphabet,3));fib={}
for a in triples:fib.setdefault(sum(v*v for v in a),[]).append(a)
collisions={k:v for k,v in fib.items()if len(v)>1};sig={(sum(x*x for x in a),a[0]*a[1]*a[2])for a in triples}
chart=[]
for r in map(F,['0','1/100','1/10','1','10','100']):
 a=[1/(1+4*k*r)for k in range(4)];S1=sum(a);S2=sum(x*x for x in a);theta=r*S1/4;d=S1/4;p=S1*S1/(4*S2);q=4*sum(k*a[k]**2 for k in range(4))/S2
 chart.append(dict(r=r,a=a,theta=theta,delta_over_epsilon=d,p=p,q=q,residual=theta*q-p+d));assert theta*q-p+d==0
save('GRAMMAR_CHART.json',dict(candidate_count=len(triples),norm_count=len(fib),collision_fibers=collisions,norm_product_count=len(sig),sum_norm_collision=[[1,6,8],[2,4,9]],chart=chart,control_q_zero_residual=-(chart[3]['p']-chart[3]['delta_over_epsilon'])))
# Exact source recurrence checks on the4-pole factor, without rerunning locked full-source proof.
ops={};prog=[];combined=[]
for j,c in enumerate(chart):
 r=c['r'];H=[[4*r*k*F(k==l)-F(1,4)for l in range(4)]for k in range(4)]
 v=[[x]for x in c['a']];d=c['delta_over_epsilon'];theta=c['theta']
 # Physical dimensionless factor is4theta*diag(k)-P; use source theta, not r.
 H=[[4*theta*k*F(k==l)-F(1,4)for l in range(4)]for k in range(4)]
 ops['H'+str(j)]=H;ops['v'+str(j)]=v
 prog +=[st('hv'+str(j),'multiply','H'+str(j),'v'+str(j)),st('dv'+str(j),'scale','v'+str(j),factor=str(-d)),st('r'+str(j),'subtract','hv'+str(j),'dv'+str(j))]
 combined.append('r'+str(j))
cur=combined[0]
for j,n in enumerate(combined[1:]):prog.append(st('sum'+str(j),'add',cur,n));cur='sum'+str(j)
task('FOUR_HE3_CHART_V1','GEN3_SOURCE_OPERATOR_WORD',wordpayload('FOUR_HE3_CHART_V1',4,ops,prog,cur),'Six exact four-pole factor eigen-equations and independent scale-free response identities, full192 theorem retained as locked input',word=True)

# Rebuild source from literal six C4 digits, then all original Gray flips.
origin=[]
for core in range(4):
 xy=[[(1,0),(0,1),(-1,0),(0,-1)][(32//4**k)%4]for k in range(6)]
 origin += [x+y for x,y in xy]+[x-y for x,y in xy]
def currents(s):return [F(sum(s[12*c:12*c+6])+sgn*sum(s[12*c+6:12*c+12]),2)for c in range(4)for sgn in [1,-1]]
# Above y requiresS−T, xS+T, and sgn formulation outputs correct x,y.
times=[F(j,8)for j in range(97)];histories=[];inc=[]
for word in [[],list(range(48))*2,list(reversed(range(48)))*2]:
 s=origin.copy();hist=[currents(s)]
 if not word:hist=hist*97
 else:
  for k in word:s[k]*=-1;hist.append(currents(s))
 assert hist[0]==hist[-1]==[4,0]*4
 histories.append(hist);inc.append([[hist[j][k]-(hist[j-1][k]if j else 0)for j in range(97)]for k in range(8)])
G=[[F((i%2==j%2)*(1+2*(i==j)))+F(i%2==j%2,10)for j in range(8)]for i in range(8)]
d=[[x-y for x,y in zip(a,b)]for a,b in zip(inc[1],inc[2])]
mom=mm(d,[[t**k for k in range(4)]for t in times]);assert all(row[:2]==[0,0]for row in mom)
cap=sum(t*t for t in times)*sum(t*t*mm([list(col)],mm(G,[[x]for x in col]))[0][0]for t,col in zip(times,zip(*d)))
nonzero=next(j for j in range(97)if any(d[k][j]for k in range(8)));bad=[row.copy()for row in d]
for k in range(8):bad[k][nonzero]=F(0)
badmom=mm(bad,[[t**k for k in range(2)]for t in times]);assert any(row[0]for row in badmom)
data=dict(times=encode(times),end='16',increments=encode(inc),Cs=[['0']*97 for _ in range(3)],names=['HELD','FORWARD','REVERSE'],model='EDGE',radius_ratio='1',components=[dict(name='NUCLEAR_EDGE',tau='1',G=encode([[F((i%2==j%2)*(1+2*(i==j)))for j in range(8)]for i in range(8)])),dict(name='OUTER',tau='1',G=encode([[F(i%2==j%2,10)for j in range(8)]for i in range(8)]))])
save('WAVE_RAW.json',dict(origin=origin,histories=histories,data=data,moments=mom,cauchy_M2_square=cap,removed_event=nonzero,control_moments=badmom,scope='Cs0 removes only scalar classical-alternative phase; full quantum nuclear phase is separately retained input, not recomputed here'))
task('FOUR_WAVE_REBUILD_V1','GEN3_MODULAR_QUANTUM_WAVE_HISTORY',data,'Actual O16 HELD/FORWARD/REVERSE full continuum amplitudes, number/energy Grams and work; scalar nuclear phase explicitly removed for classical hypotheses only')
task('FOUR_WAVE_MOMENTS_V1','GEN3_COMPLEX_PRODUCT',dict(matrix=mat(d,list(range(8)),list(range(97))),right=mat([[t**k for k in range(4)]for t in times],list(range(97)),list(range(4)))),'Full8by97 original source difference times all four exact Fourier moments')
task('FOUR_WAVE_BROKEN_V1','GEN3_COMPLEX_PRODUCT',dict(matrix=mat(bad,list(range(8)),list(range(97))),right=mat([[1]for t in times],list(range(97)),['M0'])),'Hypothesis-breaking control: remove one actual nonzero event; expected_failed_check=zeroth Fourier cancellation')

save('HOST_SUMMARY.json',dict(dp={k:dp[k]for k in ['path_count','rank','min_variation','min_gross','min_storage','rolewise_mean','value_of_information','minimum_policy_actions','fibers','control_residual']},reference_counts=ref['counts'],anchors=coef,grammar_norm_count=len(fib),grammar_double_fibers=len(collisions),wave_cap=cap))
print(json.dumps(encode(json.loads((OUT/'HOST_SUMMARY.json').read_text())),indent=2))
