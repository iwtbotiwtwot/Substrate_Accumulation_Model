from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from itertools import product
import json,hashlib
ctx.prec=384
root=Path.cwd();host=json.loads((root/'evidence/star_host.json').read_text());steps=[]
def wm(x,r=None,c=None,structure='GENERAL'):return {'entries':x,'row_basis':r or [str(i) for i in range(len(x))],'column_basis':c or [str(i) for i in range(len(x[0]))],'structure':structure}
def step(i,op,data,purpose):steps.append({'id':i,'operation':op,'purpose':purpose,'payload':{'source_binding':{'$source':True},'precision_bits':384,'data':data},'checks':[{'predicate':'native_contract'}]})
def evalexpr(i,terms,constant='0'):step(i,'GEN5_LOG_EVALUATE',{'expression':{'terms':terms,'constant':str(constant)}},'Certified exact rational logarithmic coefficient/witness')
def cexpr(a):return [{'argument':str(a),'coefficient':str(-a/4)}],a*(a-1)/4
lo=F(20318786997997,10**14);hi=F(20318786998000,10**14)
# Fixed precommitted root bracket, no target-value search.
vals={f'k{z["k"]}':F(z['Omega']) for z in host['layers'][:4]};vals['h5']=F(59049,85000)**5
for name,a in vals.items():evalexpr('C_'+name,*cexpr(a))
for name,a,sgn in [('lo',lo,1),('hi',hi,-1)]:evalexpr('root_'+name,[{'argument':str(a),'coefficient':str(-sgn)}],sgn*(-2+2*a))
a3=vals['k3']
for name,a in vals.items():
 if name=='k3':continue
 terms,c=cexpr(a3);tt,cc=cexpr(a);terms+= [{'argument':t['argument'],'coefficient':str(-F(t['coefficient']))} for t in tt];evalexpr('gap_'+name,terms,c-cc)
Cmin=lo*(1-lo)/4;Cmax=hi*(1-hi)/4
step('ratio','GEN3_COMPLEX_SOLVE',{'matrix':wm([[{'lower':str(Cmin),'upper':str(Cmax)}]],['q'],['q']),'rhs':wm([[{'$step':'C_k3','path':['result','output','value']}]],['q'],['q'])},'Native bound on fraction of universal coefficient maximum')
# Explicit non-null control: C''(3/4)=1/6>0 rejects global concavity.
step('curvature_control','GEN3_COMPLEX_PRODUCT',{'matrix':wm([[F(1,4).__str__(),F(-1,4).__str__()]],['curvature'],['two','reciprocal']),'right':wm([[2],['4/3']],['two','reciprocal'],['curvature'])},'Expected failed check: global-concavity hypothesis; actual curvature is positive1/6')
rays=[(1,)+p for p in product((-1,1),repeat=3)];Z=F(10625,8);probs=[]
for hs in product((-1,1),repeat=8):probs.append(str(F(2)**(sum(h*sum(p) for h,p in zip(hs,rays))//2)/Z))
step('conditional_entropy','GEN5_ENTROPY',{'probabilities':probs},'Complete256-state conditional hidden Gibbs entropy with absolute partition retained')
evalexpr('entropy_ledger',[{'argument':'10625/8','coefficient':'1'},{'argument':'2','coefficient':'-354/85'}])
job={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'Sharp short-time coefficient and global integer-layer optimum; absolute conditional entropy check','precision_bits':384,'sources':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [root/'PREDICTIONS.md',root/'build_peak.py',root/'evidence/star_host.json']],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}}
(root/'THREE_PEAK.job.json').write_text(json.dumps(job,indent=2)+'\n');(root/'THREE_PEAK.task.json').write_text(json.dumps({'kind':'gen6_job','key':'THREE_PEAK','purpose':'Native sharp coefficient root signs, all-k domination and entropy ledger from fresh source operands','job_path':str(root/'THREE_PEAK.job.json')},indent=2)+'\n')
res={'rootlo':str(lo),'roothi':str(hi),'Cstar_lower':str(Cmin),'Cstar_upper':str(Cmax),'host_values':{k:str(arb(str(a))*(-arb(str(a)).log()-1+arb(str(a)))/4) for k,a in vals.items()},'ratio':str(arb(str(a3))*(-arb(str(a3)).log()-1+arb(str(a3)))/4/arb(str((Cmin+Cmax)/2)))}
(root/'evidence/peak_host.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
