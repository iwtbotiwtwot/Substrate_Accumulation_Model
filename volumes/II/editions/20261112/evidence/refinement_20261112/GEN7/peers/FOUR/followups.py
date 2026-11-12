from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent;O=H/'results';T=H/'tasks'
R=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/native_returns')
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [enc(v)for v in x]
 if isinstance(x,dict):return {k:enc(v)for k,v in x.items()}
 return x
def matrix(a,rb=None,cb=None,herm=False):return dict(entries=enc(a),row_basis=rb or list(range(len(a))),column_basis=cb or list(range(len(a[0]))),structure='HERMITIAN'if herm else 'GENERAL')
def read(k):
 p=R/(k+'.json');d=json.loads(p.read_text())
 if 'returned' not in d:d=json.loads(Path(d['record_file']).read_text())
 return d
def out(k):
 d=read(k)['returned'];return d.get('result',{}).get('output',d)
def write(k,op,data,purpose,word=False):
 x=dict(kind='native',key=k,operation=op,purpose=purpose,payload=data if word else dict(precision_bits=256,data=data));(T/(k+'.json')).write_text(json.dumps(enc(x),indent=2)+'\n')
def wp(k,n,ops,pr,output):return dict(name=k,context=dict(basis=list(range(n)),field=dict(radicand=0),units=dict(reference='Original source units'),history=dict(precommit_sha256=hashlib.sha256((H/'PRECOMMIT.md').read_bytes()).hexdigest(),scope='Actual nonzero control or Schur reconstruction'),spectral_coordinate='EXACT_CONTROL'),data=dict(operators=enc(ops),program=pr,output=output))
def st(n,op,*ii,**kw):return dict(name=n,op=op,inputs=list(ii),**kw)
# Native DP diagonal-only control: actual canonical path source increments.
d=json.loads((O/'C12_DP.json').read_text());B=[[F(x)for x in row]for row in d['role_mean_B']];can=next(r for r in d['paths']if r['word']=='ABABCC')
def port(s):
 u=[F(s[0],6),F(s[1],6),F(s[2],6),F(2*s[3],6)];return [u[i%4]*u[i//4]for i in range(16)]
vs=[port(s)for s in can['states']];D=[[vs[j+1][i]-vs[j][i]for j in range(6)]for i in range(16)]
diag=[[B[i][j]if i==j else F(0)for j in range(16)]for i in range(16)]
ops=dict(B=B,D=D,diag=diag);pr=[st('Dt','transpose','D'),st('BD','multiply','B','D'),st('DX','multiply','diag','D'),st('full','multiply','Dt','BD'),st('bad','multiply','Dt','DX'),st('res','subtract','bad','full')]
write('FOUR_DP_BROKEN_V1','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_DP_BROKEN_V1',6,ops,pr,'res'),'Reachable source control: omit original B cross terms on actual canonical path; expected_failed_check=source variation reproduction',True)
# Full fixed-alphabet thirteen norm collisions: exact native witness differences.
g=json.loads((O/'GRAMMAR_CHART.json').read_text());fib=list(g['collision_fibers'].values());A=[];C=[]
for pair in fib:
 A.append([F(v)for v in pair[0]]);C.append([F(v)for v in pair[1]])
# Sum of squared coordinates from diagonal of A A^T and C C^T remains an exact full Gram witness.
ops=dict(A=A,C=C);pr=[st('At','transpose','A'),st('Ct','transpose','C'),st('AA','multiply','A','At'),st('CC','multiply','C','Ct'),st('difference','subtract','AA','CC')]
write('FOUR_GRAMMAR_FIBERS_V1','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_GRAMMAR_FIBERS_V1',13,ops,pr,'difference'),'All13 double-fiber exact source norm collisions; every diagonal must vanish, offdiagonal differences retain distinguishable information',True)
# Broken reference stencil on an actually present fixed-Z triple.
rf=json.loads((O/'REFERENCES.json').read_text());c=rf['contrasts'][0];val=[[1,z,n]for z,n in c['coords']]
write('FOUR_REFERENCE_BROKEN_V1','GEN3_COMPLEX_PRODUCT',dict(matrix=matrix([[1,-1,1]],['BROKEN'],['L','C','R']),right=matrix(val,['L','C','R'],['1','Z','N'])),'Reachable affine-reference control: center coefficient−1 instead of−2; expected_failed_check=constant annihilation, predicted1')
# Rice source exact Schur covariance and a smooth-surrogate control at six finite lags.
hs=[F(1,2**k)for k in range(1,7)];n=12
S=[[F(0)for _ in range(n)]for _ in range(n)];I=[x.copy()for x in S];X=[x.copy()for x in S];V=[x.copy()for x in S];W=[x.copy()for x in S]
for j,h in enumerate(hs):
 r=1-F(3,8)*h*h+F(3,32)*h**3;rp=-F(3,4)*h+F(9,32)*h*h;rpp=-F(3,4)+F(9,16)*h
 a=[[1,r],[r,1]];b=[[1/(1-r*r),-r/(1-r*r)],[-r/(1-r*r),1/(1-r*r)]];x=[[0,-rp],[rp,0]];v=[[F(3,4),-rpp],[-rpp,F(3,4)]]
 for k in range(2):
  W[2*j+k][2*j+k]=1/h
  for l in range(2):S[2*j+k][2*j+l]=a[k][l];I[2*j+k][2*j+l]=b[k][l];X[2*j+k][2*j+l]=x[k][l];V[2*j+k][2*j+l]=v[k][l]
ops=dict(S=S,I=I,X=X,V=V,W=W);pr=[st('xt','transpose','X'),st('xi','multiply','X','I'),st('pay','multiply','xi','xt'),st('cond','subtract','V','pay'),st('scaled','multiply','W','cond')]
write('FOUR_RICE_SCHUR_V1','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_RICE_SCHUR_V1',12,ops,pr,'scaled'),'Exact actual shell two-time conditioned derivative covariance/h across six nonzero lags; anchors Rice diagonal law',True)
# The control uses the analytic smooth surrogate r=1−a h², rpp=−2a; it is a local malformed replacement, not an admitted all-time covariance.
h=F(1,64);a=F(3,8);r=1-a*h*h;rp=-2*a*h;rpp=-2*a
ops=dict(S=[[1,r],[r,1]],I=[[1/(1-r*r),-r/(1-r*r)],[-r/(1-r*r),1/(1-r*r)]],X=[[0,-rp],[rp,0]],V=[[2*a,-rpp],[-rpp,2*a]])
pr=[st('xt','transpose','X'),st('xi','multiply','X','I'),st('pay','multiply','xi','xt'),st('cond','subtract','V','pay'),st('scaled','scale','cond',factor=str(1/h))]
write('FOUR_RICE_BROKEN_V1','GEN3_SOURCE_OPERATOR_WORD',wp('FOUR_RICE_BROKEN_V1',2,ops,pr,'scaled'),'Omit actual cubic covariance term; expected_failed_check=positive actual conditional velocity covariance/h and nonzero Rice limit; local surrogate can fail positivity',True)
# Native log and transfer: calibrated and uncalibrated local crossing laws.
A=[['-1/4','3/4'],['1/4','-3/4']]
steps=[]
def step(i,op,data,purpose):steps.append(dict(id=i,operation=op,purpose=purpose,payload=dict(source_binding={'$source':True},precision_bits=256,data=data),checks=[dict(predicate='native_contract')]))
step('depth','GEN3_COMPLEX_LOG',dict(matrix=matrix([['47/48','0'],['0','47/48']],['BEFORE','AFTER'],['BEFORE','AFTER'],True)),'Shared modular negative log gives positive depth log48/47')
step('logquad','GEN5_LOG_QUADRATIC_FORM',dict(matrix=matrix([['48/47']],['DEPTH'],['DEPTH'],True),source=['1']),'Independent ordinary plus-log quadratic form for calibrated depth')
step('calibrated_generator','GEN3_COMPLEX_PRODUCT',dict(matrix=matrix(A,['BEFORE','AFTER'],['BEFORE','AFTER']),right={'$step':'depth','path':['result','output','matrix']}),'Original full-gap two-state heatbath generator times calibrated depth')
step('calibrated','GEN3_COMPLEX_EXP',dict(matrix={'$step':'calibrated_generator','path':['result','output','matrix']}),'Calibrated isolated transfer equalsI+A/48')
step('uncalibrated','GEN3_COMPLEX_EXP',dict(matrix=matrix([['-1/192','1/64'],['1/192','-1/64']],['BEFORE','AFTER'],['BEFORE','AFTER'])),'Reachable expected_failed_check=marked-transfer equality at actual a1/4, depth1/48')
job=dict(schema='SAM_ONE_PRINCIPLE_NATIVE_JOB_V1',objective='Exact isolated marked crossing versus regularized hazard, including independent logarithmic form and reachable failing uncalibrated control',precision_bits=256,sources=[dict(path=str(H/'PRECOMMIT.md'),sha256=hashlib.sha256((H/'PRECOMMIT.md').read_bytes()).hexdigest())],steps=steps,readouts={s['id']:dict(status='DERIVED_NATIVE',value={'$step':s['id'],'path':[]})for s in steps})
jp=T/'FOUR_CONTACT_TRANSFER_V1.job.json';jp.write_text(json.dumps(job,indent=2)+'\n');(T/'FOUR_CONTACT_TRANSFER_V1.json').write_text(json.dumps(dict(kind='gen6_job',key='FOUR_CONTACT_TRANSFER_V1',job_path=str(jp),purpose=job['objective']),indent=2)+'\n')
# Actual difference-dictionary native contractions from the just-completed full continuum return.
w=out('FOUR_WAVE_REBUILD_V1');bb=[['-1','-1'],['1','0'],['0','1']];bt=[['-1','1','0'],['-1','0','1']];rb=['HELD','FORWARD','REVERSE'];cb=['F-H','R-H'];steps=[]
for key,k in [('normal_Gram','N'),('free_energy_Gram','E')]:
 step(k+'B','GEN3_COMPLEX_PRODUCT',dict(matrix=matrix(w[key],rb,rb),right=matrix(bb,rb,cb)),'Full continuum'+key+' times original dictionary difference map')
 step(k+'DICT','GEN3_COMPLEX_PRODUCT',dict(matrix=matrix(bt,cb,rb),right={'$step':k+'B','path':['result','output','matrix']}),'Complete original dictionary two-mode Gram')
step('rank','GEN3_COMPLEX_RANK',dict(matrix={'$step':'NDICT','path':['result','output','matrix']}),'Bounded2by2 interval determinant/rank certification; no large rational rank')
job=dict(schema='SAM_ONE_PRINCIPLE_NATIVE_JOB_V1',objective='Native minimal amplitude span of actual HELD/FORWARD/REVERSE full continuum dictionary',precision_bits=256,sources=[dict(path=str(R/'FOUR_WAVE_REBUILD_V1.json'),sha256=hashlib.sha256((R/'FOUR_WAVE_REBUILD_V1.json').read_bytes()).hexdigest())],steps=steps,readouts={s['id']:dict(status='DERIVED_NATIVE',value={'$step':s['id'],'path':[]})for s in steps})
jp=T/'FOUR_DICTIONARY_V1.job.json';jp.write_text(json.dumps(job,indent=2)+'\n');(T/'FOUR_DICTIONARY_V1.json').write_text(json.dumps(dict(kind='gen6_job',key='FOUR_DICTIONARY_V1',job_path=str(jp),purpose=job['objective']),indent=2)+'\n')
print('Built7 independent checks plus2native programs')
