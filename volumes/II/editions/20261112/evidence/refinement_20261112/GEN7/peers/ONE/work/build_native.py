from pathlib import Path
import json,hashlib,itertools
import numpy as np
P=Path.cwd();R=json.loads((P/'results/TOMOGRAPHY.json').read_text());B=json.loads((P/'native').read_text().split('BINDING = ')[1].split('\nUSAGE')[0].replace("'",'"')) if False else {'kind':'GEN7_DUCK','campaign':'20261112T043202Z','law_namespace':'SAM_land','target_sha256':'821ae35dfa3c40c1cec69487ee426ac1215d6859cce16a64c48c8d477c0a3721'}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();sources=[P/'PRECOMMIT.md',P/'work/reconstruct.py',P/'results/TOMOGRAPHY.json',P/'results/base_images.npz',Path(__file__).resolve()]
meta=[{'path':str(p),'sha256':sha(p)} for p in sources]
def mat(a,rows=None,cols=None):
 a=a.tolist() if hasattr(a,'tolist') else a
 return {'entries':a,'row_basis':rows or list(range(len(a))),'column_basis':cols or list(range(len(a[0]))),'structure':'GENERAL'}
def st(k,op,data,purpose):return {'id':k,'operation':op,'purpose':purpose,'payload':{'source_binding':{'$source':True},'precision_bits':256,'data':data},'checks':[{'predicate':'native_contract'}]}
def word(k,ops,program,out,n):return {'id':k,'operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Exact lane ONE source operator certificate reconstructed independently from full CAR density images.','payload':{'name':'ONE7_'+k,'source_binding':{'$source':True},'context':{'basis':list(range(n)),'field':{'radicand':0},'units':{'energy':'Unnormalized pinned-source matrix; static energy convention -sum Bqr rhoq rhor/8'},'history':{'source':'GEN7 lane ONE independent density-image reconstruction','control':'Original raw physical source columns and retained full density images'},'spectral_coordinate':'Exact static kernel coefficient'},'data':{'operators':ops,'program':program,'output':out}},'checks':[{'predicate':'native_contract'}]}
def job(key,steps):
 j={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':key+' lane ONE source-bound verification','law_namespace':'SAM_land','source_binding':B,'precision_bits':256,'sources':meta,'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}}
 f=P/'tasks'/f'{key}.job.json';f.write_text(json.dumps(j,separators=(',',':'))+'\n');(P/'tasks'/f'{key}.json').write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':j['objective'],'job_path':str(f),'estimated_memory_bytes':150000000},indent=2)+'\n')
steps=[]
for label in ['phase9','source11']:
 minor=R['ranks'][label]['minor_matrix'];n=len(minor)
 steps.append(word('rank_'+label,{'A':minor},[{'name':'out','op':'scale','inputs':['A'],'factor':'1'}],'out',n))
 a=np.load(P/'results'/f'{label}_certificate.npz');des=a['design'];null=a['null']
 steps.append(st('null_upper_'+label,'GEN3_COMPLEX_PRODUCT',{'matrix':mat([[str(x) for x in row] for row in des]),'right':mat(null)},'All source-kernel null vectors annihilated, certifying the rank upper with a native full matrix product.'))
v=R['reachable_null_control'];steps.append(word('reachable_null',{'A':v['full_null_matrix']},[{'name':'out','op':'scale','inputs':['A'],'factor':'1/6'}],'out',18))
c=R['compressed_density_control'];steps.append(word('compressed_square_control',{'F':c['full_matrix'],'W':c['bad_matrix']},[{'name':'out','op':'subtract','inputs':['F','W']}],'out',9))
job('ONE7_RANK_CONTROLS',steps)
for label,n in [('real8',8),('complex6',6)]:
 z=np.load(P/'results'/f'{label}_images.npz');steps=[];cb=[f's{i}' for i in range(n)];rb=[f'CAR{i}' for i in range(z['Xr'].shape[0])]
 def wire(re,im):return [[str(int(x)) if int(y)==0 else {'re':str(int(x)),'im':str(int(y))} for x,y in zip(a,b)] for a,b in zip(re,im)]
 for q,r in itertools.combinations_with_replacement(range(8),2):
  steps.append(st(f'cross_{q}_{r}','GEN3_COMPLEX_PRODUCT',{'matrix':mat(wire(z['Dr'][q].T,-z['Di'][q].T),cb,rb),'right':mat(wire(z['Dr'][r],z['Di'][r]),rb,cb)},'Complete physical Walsh density-image product before source compression; no compressed-square shortcut.'))
 steps.append(st('raw_Gram','GEN3_COMPLEX_PRODUCT',{'matrix':mat(wire(z['Xr'].T,-z['Xi'].T),cb,rb),'right':mat(wire(z['Xr'],z['Xi']),rb,cb)},'Common raw source Gram including all complex relative-phase correlations.'))
 d=R['designs'][label]
 steps.append(word('inverse_'+label,{'C':d['design'],'Inv':d['inverse']},[{'name':'out','op':'multiply','inputs':['C','Inv']}],'out',36))
 steps.append(st('solve_'+label,'GEN3_COMPLEX_SOLVE',{'matrix':mat(d['design']),'rhs':mat([['1' if i==j else '0' for j in range(36)] for i in range(36)])},'Certified36x36 inverse of the independently reconstructed exact design.'))
 job('ONE7_'+label.upper(),steps)
# Singular source preparation is reachable: duplicate first two literal source superpositions.
C=R['designs']['real8']['design'];Cbad=[row[:] for row in C];Cbad[1]=Cbad[0][:]
f=P/'tasks/ONE7_SINGULAR_CONTROL.json';f.write_text(json.dumps({'kind':'native','key':'ONE7_SINGULAR_CONTROL','operation':'GEN3_COMPLEX_SOLVE','purpose':'Hypothesis-breaking repeated scalar source observable; singular design must return unresolved invertibility, not a successful inverse.','expected_status':'COMPLETED','expected_reason':'INVERTIBILITY_UNRESOLVED on an explicitly duplicated nonzero design row','payload':{'precision_bits':256,'data':{'matrix':mat(Cbad),'rhs':mat([['1' if i==j else '0' for j in range(36)] for i in range(36)])}}},indent=2)+'\n')
print('native jobs built',[(f.name,f.stat().st_size) for f in (P/'tasks').glob('*.job.json')])
