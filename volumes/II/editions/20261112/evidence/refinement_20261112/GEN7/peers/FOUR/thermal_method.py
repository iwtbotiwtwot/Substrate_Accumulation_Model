from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;T=H/'tasks'
def mat(a):return dict(entries=a,row_basis=list(range(len(a))),column_basis=list(range(len(a[0]))),structure='GENERAL')
def ref(i,*p):return {'$step':i,'field':['result','output',*p]}
def step(i,op,data):return dict(id=i,operation=op,payload=dict(source_binding={'$source':True},precision_bits={'$precision':True},data=data))
steps=[step('hyperbolic','GEN3_COMPLEX_EXP',dict(matrix={'$param':'generator'})),step('tanh','GEN3_COMPLEX_SOLVE',dict(matrix=mat([[ref('hyperbolic','matrix','entries',0,0)]]),rhs=mat([[ref('hyperbolic','matrix','entries',1,0)]]))),step('Q','GEN3_COMPLEX_PRODUCT',dict(matrix={'$param':'signal_weight'},right=ref('tanh','matrix'))),step('exponent','GEN3_COMPLEX_PRODUCT',dict(matrix=mat([['-1/2']]),right=ref('Q','matrix'))),step('tail','GEN3_COMPLEX_EXP',dict(matrix=ref('exponent','matrix'))),step('Pe','GEN3_COMPLEX_PRODUCT',dict(matrix=mat([['1/2']]),right=ref('tail','matrix')))]
recipe=dict(schema='GEN5_METHOD_RECIPE_V1',name='four.thermal_band_receiver',revision=1,law_namespace='SAM_land',task_type='four.thermal_band_receiver',parameters=dict(generator=dict(type='matrix',dimension=2),signal_weight=dict(type='matrix',dimension=1)),assumptions=[dict(parameter='generator',predicate='square'),dict(parameter='signal_weight',predicate='square')],steps=steps,checks=[dict(step=s['id'],predicate='native_contract')for s in steps],returns=dict(Q=ref('Q','matrix'),Pe_upper=ref('Pe','matrix')),description='Supplied nonnegative band signal norm times calibrated eta and tanh(beta*w0/2), then homodyne Chernoff upper; source proof and covariance hypotheses remain external analytic premises',provenance=dict(source='FOUR O16 actual97event spectral moment cancellation',scope='Finite scalar receiving inequality; physical covariance/collection/phase reference not inferred'))
def outer(i,op,data):return dict(id=i,operation=op,purpose=i,payload=dict(source_binding={'$source':True},precision_bits=256,data=data),checks=[dict(predicate='native_contract')])
steps=[outer('admit','GEN5_METHOD_ADMIT',dict(recipe={'$literal':recipe}))]
for name,band in [('original','9554899/25000'),('sharper','382443/1000')]:
 from fractions import Fraction as F
 inputs=dict(generator=mat([['0','1'],['1','0']]),signal_weight=mat([[str(F(band)/40)]]))
 steps += [outer('compile_'+name,'GEN5_METHOD_COMPILE',dict(method_ref={'$step':'admit','path':['result','output','method','result_ref']},inputs=inputs)),outer('execute_'+name,'GEN5_METHOD_EXECUTE',dict(compiled_ref={'$step':'compile_'+name,'path':['result','output','compiled','result_ref']}))]
job=dict(schema='SAM_ONE_PRINCIPLE_NATIVE_JOB_V1',objective='Admit, compile and execute reusable actual O16 thermal-band error receiver for inherited conservative band382.19596 and sharpened382.443 at beta200 eta1/40',precision_bits=256,sources=[dict(path=str(H/'PRECOMMIT.md'),sha256=hashlib.sha256((H/'PRECOMMIT.md').read_bytes()).hexdigest())],steps=steps,readouts={s['id']:dict(status='DERIVED_NATIVE',value={'$step':s['id'],'path':[]})for s in steps})
p=T/'FOUR_THERMAL_METHOD_V1.job.json';p.write_text(json.dumps(job,indent=2)+'\n');(T/'FOUR_THERMAL_METHOD_V1.json').write_text(json.dumps(dict(kind='gen6_job',key='FOUR_THERMAL_METHOD_V1',purpose=job['objective'],job_path=str(p)),indent=2)+'\n')
print('Built native receiver method')
