from pathlib import Path
from fractions import Fraction as F
import json,itertools,hashlib
import sympy as S
from flint import arb,ctx
ctx.prec=256
P=Path.cwd();B={'kind':'GEN7_DUCK','campaign':'20261112T043202Z','law_namespace':'SAM_land','target_sha256':'821ae35dfa3c40c1cec69487ee426ac1215d6859cce16a64c48c8d477c0a3721'}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def wire(A):return [[str(x) for x in row] for row in A.tolist()] if hasattr(A,'tolist') else [[str(x) for x in row] for row in A]
def mat(A,rb=None,cb=None,h=False):
 A=wire(A);return {'entries':A,'row_basis':rb or list(range(len(A))),'column_basis':cb or list(range(len(A[0]))),'structure':'HERMITIAN' if h else 'GENERAL'}
def st(k,op,data):return {'id':k,'operation':op,'purpose':'Independent actual-source arrival/robustness certificate in lane ONE.','payload':{'source_binding':{'$source':True},'precision_bits':256,'data':data},'checks':[{'predicate':'native_contract'}]}
def word(k,ops,prog,out,n):return {'id':k,'operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Exact source/branch arithmetic and hypothesis-breaking control.','payload':{'name':'ONE7_'+k,'source_binding':{'$source':True},'context':{'basis':list(range(n)),'field':{'radicand':0},'units':{'norm':'normalized phase9 or common model energy, stated per output'},'history':{'source':'Literal projectors and retained proper branch lower inputs','baseline':'H003006 locked; no base script executed'},'spectral_coordinate':'Static source calibration'},'data':{'operators':{k:wire(v) for k,v in ops.items()},'program':prog,'output':out}},'checks':[{'predicate':'native_contract'}]}
def job(key,steps,src):
 j={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':key+' independent lane ONE verification','source_binding':B,'law_namespace':'SAM_land','precision_bits':256,'sources':[{'path':str(x.resolve()),'sha256':sha(x)} for x in src+[P/'PRECOMMIT.md',Path(__file__).resolve()]],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}}
 f=P/'tasks'/f'{key}.job.json';f.write_text(json.dumps(j,separators=(',',':'))+'\n');(P/'tasks'/f'{key}.json').write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':j['objective'],'job_path':str(f)},indent=2)+'\n')
Ps=S.zeros(9);Pa=S.zeros(9);Pe=S.zeros(9);Pe[7,7]=1
for i,j in [(0,5),(1,4),(2,6),(3,8)]:
 for a in [i,j]:Ps[a,a]=Pa[a,a]=S.Rational(1,2)
 Ps[i,j]=Ps[j,i]=S.Rational(1,2);Pa[i,j]=Pa[j,i]=-S.Rational(1,2)
z=S.Matrix([1,1,-1,-1,-1,1,1,1,1])/3
Gs=[3*Ps/5+Pe,Pa/3,2*Ps/5+2*Pa/3];Gc=[S.Rational(47,45)*(Gs[0]-Pe)+Pe,S.Rational(17,15)*Gs[1],S.Rational(14,15)*Gs[2]]
assert sum(Gs,S.zeros(9))==S.eye(9) and sum(Gc,S.zeros(9))==S.eye(9)
ws=[(z.T*g*z)[0] for g in Gs];wc=[(z.T*g*z)[0] for g in Gc]
steps=[]
for name,projs in [('sep',Gs),('contact',Gc)]:
 steps.append(word(name+'_sum',{'A':projs[0],'B':projs[1],'C':projs[2],'I':S.eye(9)},[{'name':'ab','op':'add','inputs':['A','B']},{'name':'abc','op':'add','inputs':['ab','C']},{'name':'out','op':'subtract','inputs':['abc','I']}],'out',9))
steps.append(word('projector_orthogonality',{'S':Ps,'A':Pa},[{'name':'out','op':'multiply','inputs':['S','A']}],'out',9))
ratios=[S.Rational(47,45),S.Rational(17,15),S.Rational(14,15)]+[a*b for a,b in zip(ws,wc)]+[S.Rational(1)]
b=list(range(7));ref=lambda k:{'$step':k,'path':['result','output','matrix']}
steps.append(st('negative_log','GEN3_COMPLEX_LOG',{'matrix':mat(S.diag(*ratios),b,b,True),'tolerance':'1/1000000000000000000000000000000000000000000000000000000000000','max_terms':1024}))
steps.append(st('half_log','GEN3_COMPLEX_PRODUCT',{'matrix':mat(-S.eye(7)/2,b,b),'right':ref('negative_log')}))
steps.append(st('roots','GEN3_COMPLEX_EXP',{'matrix':ref('half_log')}))
steps.append(st('root_column','GEN3_COMPLEX_PRODUCT',{'matrix':ref('roots'),'right':mat(S.ones(7,1),b,['scalar'])}))
coef=S.Matrix([[S.Rational(3,5),0,S.Rational(2,5),0,0,0,0],[0,S.Rational(1,3),S.Rational(2,3),0,0,0,0],[S.Rational(2,15),S.Rational(2,9),S.Rational(8,15),0,0,0,S.Rational(1,9)],[0,0,0,1,1,1,0]])
dcoef=-2*coef
for i in range(4):dcoef[i,6]+=2
steps.append(st('distance_squared','GEN3_COMPLEX_PRODUCT',{'matrix':mat(dcoef,['sym','minimax','fixed','known'],b),'right':ref('root_column')}))
job('ONE7_ARRIVAL',steps,[])
AA=lambda x:arb(str(x.p))/arb(str(x.q)) if hasattr(x,'p') else arb(str(x))
rr=[AA(r).sqrt() for r in ratios];ds=[sum(AA(dcoef[i,j])*rr[j] for j in range(7)) for i in range(4)]
knownminimaxdiff=ds[2]-ds[3]
assert knownminimaxdiff>0
out={'weights_sep':list(map(str,ws)),'weights_contact':list(map(str,wc)),'projector_input_weights':[str((z.T*g*z)[0]) for g in [Ps,Pa,Pe]],'distance_squared':list(map(str,ds)),'distances':[str(d.sqrt()) for d in ds],'universal_fixed_minus_known_squared':str(knownminimaxdiff),'trace_distance_lower':'8/225'}
(P/'results/ARRIVAL.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
# Independent integer partitions and exact endpoints; original five one-fragment lower lines are locked inputs.
def parts(n,m=1):
 if not n:yield ()
 for a in range(m,n+1):
  for tail in parts(n-a,a):yield (a,)+tail
E={1:F(-12),2:F(-48),3:F(-108),4:F(-188),5:F(-692,3)};L=E[5]+E[1];S2=lambda n:16*(n//4)+(n%4)**2
rows=[]
for p in parts(6):
 if p==(6,):continue
 lo=sum(E[n] for n in p);cap=sum(S2(n) for n in p);n2=sum(n*n for n in p)
 slack=[lo-L-(cap-18)*d for d in [F(0),F(10,3)]];uniform=[lo-L-F(n2-26,8)*d for d in [F(-1,2),F(1,2)]]
 assert min(slack)>=0 and min(uniform)>=0
 rows.append({'partition':p,'lower':str(lo),'D2cap':cap,'Ncell2cap':n2,'generic_endpoint_slack':list(map(str,slack)),'uniform_endpoint_slack':list(map(str,uniform))})
branch_control=F(20,3)-2*(F(10,3)+F(1,100));assert branch_control<0
oldM=F(11191,20250);oldcoef=18+F(11144,675)
dress=json.loads((P/'results/DRESSED_DENSITY.json').read_text());M=F(dress['generic_margin_lower']);s=F(dress['weighted_dressed_D2_upper']);coefnew=18+s
tomo=json.loads((P/'results/TOMOGRAPHY.json').read_text());eps={k:str(M/(coefnew*F(v['error_constant']))) for k,v in tomo['designs'].items()}
rob={'partitions':rows,'old_margin':str(oldM),'old_error_coefficient':str(oldcoef),'old_sufficient_delta':str(oldM/oldcoef),'branch_break_slack':str(branch_control),'uniform_old_slope':'5/4','uniform_old_negative_tolerance':str(-oldM/F(5,4)),'dressed_margin':str(M),'dressed_D2_upper':str(s),'dressed_error_coefficient':str(coefnew),'dressed_sufficient_delta':str(M/coefnew),'dressed_eps_sufficient':eps,'dressed_eps_decimal':{k:float(F(v)) for k,v in eps.items()},'affine_reference_control_joining_shift_per_Delta':'-5/4'}
(P/'results/ROBUSTNESS.json').write_text(json.dumps(rob,indent=2)+'\n')
slackmatrix=[[r['generic_endpoint_slack'][j] for r in rows] for j in range(2)]+[[r['uniform_endpoint_slack'][j] for r in rows] for j in range(2)]
steps=[word('branch_flanks',{'A':slackmatrix},[{'name':'out','op':'scale','inputs':['A'],'factor':'1'}],'out',4),word('branch_beyond_control',{'A':[[str(branch_control),str(F(-5,4))]]},[{'name':'out','op':'scale','inputs':['A'],'factor':'1'}],'out',1)]
# Exact rational scalar calibration arithmetic including the new cloud-dressed moment.
vals=[[str(oldM),str(oldcoef),str(M),str(coefnew),str(M/coefnew)]]
steps.append(word('calibration_constants',{'A':vals},[{'name':'out','op':'scale','inputs':['A'],'factor':'1'}],'out',1))
job('ONE7_ROBUSTNESS',steps,[P/'results/DRESSED_DENSITY.json',P/'results/TOMOGRAPHY.json'])
# Exact (not interval-zero) rank upper certificates, split to honor64-row word contract.
steps=[]
for label in ['phase9','source11']:
 z=np.load(P/'results'/f'{label}_certificate.npz');C=z['design'];N=z['null']
 for k,start in enumerate(range(0,len(C),33)):
  A=C[start:start+33];steps.append(word(label+'_exact_null_'+str(k),{'C':A,'N':N},[{'name':'out','op':'multiply','inputs':['C','N']}],'out',len(A)))
job('ONE7_EXACT_NULLS',steps,[P/'results/TOMOGRAPHY.json'])
print('robust',rob['dressed_eps_decimal'],flush=True)
