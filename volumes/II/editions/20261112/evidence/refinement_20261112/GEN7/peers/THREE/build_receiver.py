from pathlib import Path
import json,hashlib
from interval_tools import *
ROOT=Path.cwd();p=ROOT/'evidence/residual_host.json';d=json.loads(p.read_text());steps=[];norms={}
for r in d['profiles']:
    ident=r['id']
    for h in r['histories']:
        name=ident+'_'+str(h['index']);steps.append({'id':name+'_solve','operation':'GEN3_COMPLEX_SOLVE','purpose':'Full seven-coordinate conservative Young/Cauchy receiver','payload':{'source_binding':{'$source':True},'precision_bits':384,'data':{'matrix':h['matrix'],'rhs':h['rhs']}},'checks':[{'predicate':'native_contract'}]})
        gg=arr(h['rhs']);left=wm([[aa(h['normalization'])*v[0] for v in gg]],['norm'],h['rhs']['row_basis']);steps.append({'id':name+'_value','operation':'GEN3_COMPLEX_PRODUCT','purpose':'Original N/xi-clock normalized lower and162-history negative comparison','payload':{'source_binding':{'$source':True},'precision_bits':384,'data':{'matrix':left,'right':{'$step':name+'_solve','path':['result','output','matrix']}}},'checks':[{'predicate':'native_contract'}]})
# Four batches bounded54 calls each:164? two per history=324, split6x54.
for j in range(6):
    ss=steps[j*54:(j+1)*54];key='THREE_RECEIVER_'+str(j);job={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'Independent162-history seven-coordinate cap receiver, batch'+str(j),'precision_bits':384,'sources':[{'path':str(q),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()} for q in [ROOT/'PREDICTIONS.md',ROOT/'build_receiver.py',ROOT/'interval_tools.py',p]],'steps':ss,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in ss if s['id'].endswith('_value')}};(ROOT/(key+'.job.json')).write_text(json.dumps(job,indent=2)+'\n');(ROOT/(key+'.task.json')).write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':'Certify complete162-history negative result for conservative paid2x2 cap','job_path':str(ROOT/(key+'.job.json'))},indent=2)+'\n')
print('generated',len(steps),'native calls')
