from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent;T=H/'tasks';O=H/'results'
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [enc(v)for v in x]
 if isinstance(x,dict):return {k:enc(v)for k,v in x.items()}
 return x
def st(n,op,*ii,**kw):return dict(name=n,op=op,inputs=list(ii),**kw)
def wp(name,n,ops,pr,out):return dict(name=name,context=dict(basis=list(range(n)),field=dict(radicand=0),units=dict(reference='Source factor units'),history=dict(source='Original four-pole He3 intrinsic preparation',scope='Independent pointwise factor and reachable q-zero control'),spectral_coordinate='SOURCE_RESPONSE'),data=dict(operators=enc(ops),program=pr,output=out))
def native(k,op,payload,purpose):
 p=dict(kind='native',key=k,operation=op,purpose=purpose,payload=payload);(T/(k+'.json')).write_text(json.dumps(p,indent=2)+'\n')
ch=json.loads((O/'GRAMMAR_CHART.json').read_text())['chart'];Hb=[[F(0)for _ in range(24)]for _ in range(24)];V=[[F(0)for _ in range(6)]for _ in range(24)];D=[[F(0)for _ in range(6)]for _ in range(6)]
for j,c in enumerate(ch):
 theta=F(c['theta']);d=F(c['delta_over_epsilon']);D[j][j]=d
 for k in range(4):
  V[4*j+k][j]=F(c['a'][k])
  for l in range(4):Hb[4*j+k][4*j+l]=4*theta*k*F(k==l)-F(1,4)
native('FOUR_HE3_POINTWISE_V2','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_HE3_POINTWISE_V2',24,dict(H=Hb,V=V,D=D),[st('hv','multiply','H','V'),st('vd','multiply','V','D'),st('res','add','hv','vd')],'res'),'Pointwise six-block He3 eigen-equation certificate; each individual residual is separately retained, supplementing completed aggregate V1')
c=ch[3];a=[F(x)for x in c['a']];S2=sum(x*x for x in a);d=F(c['delta_over_epsilon']);Bad=[[d*F(i==j)-F(1,4)for j in range(4)]for i in range(4)]
native('FOUR_HE3_BROKEN_V1','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_HE3_BROKEN_V1',1,dict(B=Bad,a=[[x]for x in a]),[st('ba','multiply','B','a'),st('at','transpose','a'),st('r','multiply','at','ba'),st('out','scale','r',factor=str(1/S2))],'out'),'Precommitted q-zero replacement at r1; expected_failed_check=formation consistency; predicted−5727442/52966485')
native('FOUR_ROLE_ENTROPY_V1','GEN5_ENTROPY',dict(precision_bits=256,data=dict(probabilities=['1/4','1/2','1/4'])),'Uniform24role minimal three-action policy has record entropy3log2/2; this adds no physical reset/heat price')
# Independent exact triangular-kernel free energy from the original97 difference events.
w=json.loads((O/'WAVE_RAW.json').read_text());data=w['data'];times=list(map(F,data['times']));ds=[[F(a)-F(b)for a,b in zip(x,y)]for x,y in zip(data['increments'][1],data['increments'][2])]
G=[[F((i%2==j%2)*(1+2*(i==j)))+F(i%2==j%2,10)for j in range(8)]for i in range(8)]
coeff=[[sum((ds[k][i]*G[k][l] for k in range(8)),F(0))for l in range(8)]for i in range(97)]
energy=F(0)
for i,t in enumerate(times):
 for j,s in enumerate(times):
  kernel=max(F(0),1-abs(t-s)/2)
  if kernel:energy+=kernel*sum(coeff[i][l]*ds[l][j]for l in range(8))/2
assert energy==F(3535,4)
(O/'TRIANGLE_ENERGY_EXACT.json').write_text(json.dumps(dict(value=str(energy),method='HOST_EXACT_RAT',formula='(1/2)sum_ij Delta_ui^T G Delta_uj (1−|ti−tj|/2)+',source_sha256=hashlib.sha256((O/'WAVE_RAW.json').read_bytes()).hexdigest()),indent=2)+'\n')
print('Built3 final native checks and exact triangle energy',energy)
