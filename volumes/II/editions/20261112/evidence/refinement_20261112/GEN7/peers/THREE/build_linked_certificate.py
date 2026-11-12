from pathlib import Path
import json,hashlib
from fractions import Fraction as F
from flint import fmpq_mat
ROOT=Path.cwd();p=ROOT/'evidence/linked_point.json';d=json.loads(p.read_text());steps=[]
def mul(A,B):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def solve(A,B):return [[F(str(x)) for x in z] for z in fmpq_mat([[str(x) for x in z] for z in A]).solve(fmpq_mat([[str(x) for x in z] for z in B])).tolist()]
def word(name,ops,prog,out,basis):return {'name':name,'source_binding':{'$source':True},'context':{'basis':basis,'field':{'radicand':0},'units':{'time':'original A-time','response':'unnormalized resolvent'},'history':{'source':'V000_BASE original retained moment boxes','scope':'shared primitive point; mixed-action interval relaxation; not a physical counterexample'},'spectral_coordinate':'xi'},'data':{'operators':{k:[[str(x) for x in z] for z in A] for k,A in ops.items()},'program':prog,'output':out}}
def nativeword(row,changed=False):
 K=[[F(x) for x in z] for z in row['matrix']['entries']];g=[[F(z[0])] for z in row['rhs']['entries']];idx=[0,1,2,3,4,6];K6=[[K[a][b] for b in idx] for a in idx];g6=[g[a] for a in idx];x6=solve(K6,g6)
 if changed:K[5][6]+=F(1,1000);K[6][5]+=F(1,1000)
 x7=solve(K,g);ops={'K7':K,'x7':x7,'g7':g,'K6':K6,'x6':x6,'g6':g6,'e1':[[1],[0]],'e2':[[0],[1]]};prog=[]
 def op(n,o,inputs,**kw):prog.append({'name':n,'op':o,'inputs':inputs,**kw})
 for n in ['7','6']:
  op('ax'+n,'multiply',['K'+n,'x'+n]);op('res'+n,'subtract',['ax'+n,'g'+n]);op('rt'+n,'transpose',['res'+n]);op('norm'+n,'multiply',['rt'+n,'res'+n]);op('gt'+n,'transpose',['g'+n]);op('value'+n,'multiply',['gt'+n,'x'+n])
 op('gain','subtract',['value7','value6']);op('rss','add',['norm7','norm6']);op('z1','multiply',['e1','rss']);op('z2','multiply',['e2','gain']);op('out','add',['z1','z2']);payload=word('THREE_LINKED_'+str(row['index'])+('_CONTROL' if changed else ''),ops,prog,'out',['solve_residual_squared','new_minus_old']);return payload
for row in d['rows']:steps.append({'id':'linked_'+str(row['index']),'operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Exact full7 versus retained6 equality under one linked primitive point and an admissible cancelling mixed action','payload':nativeword(row),'checks':[{'predicate':'native_contract'}]})
# Reachable hypothesis control, with all other primitive quantities fixed: change the mixed action by1/1000.
steps.append({'id':'mixed_control','operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'expected_failed_check: zero-gain witness after changing mixed action; positive gain must result on history18','payload':nativeword(d['rows'][18],True),'checks':[{'predicate':'native_contract'}]})
key='THREE_LINKED_CERTIFICATE';job={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'All37 linked V000_BASE interval-relaxation nonseparation witnesses and reachable mixed-action control','precision_bits':384,'sources':[{'path':str(q),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()} for q in [ROOT/'PREDICTIONS.md',ROOT/'build_linked_certificate.py',ROOT/'linked_point.py',ROOT/'evidence/linked_point.json',ROOT/'evidence/linked_exploration.json']],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}}
(ROOT/(key+'.job.json')).write_text(json.dumps(job,indent=2)+'\n');(ROOT/(key+'.task.json')).write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':'Native exact certificates for linked residual uncertainty obstruction; no claim of physical no-gain','job_path':str(ROOT/(key+'.job.json'))},indent=2)+'\n')
print('built',len(steps),'exact7x7 word certificates')
