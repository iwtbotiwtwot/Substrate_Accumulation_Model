from pathlib import Path
import json,hashlib
import sympy as S
P=Path.cwd();src=Path('/home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/sources/receiving_action/peers/ONE/gen/SPATIAL_FLAVOR_DISCOVERY.json');d=json.loads(src.read_text());C2=S.Matrix(d['C2']);C3=S.Matrix(d['C3']);E=S.Matrix(d['pair_source']);L=100*C2+C3;labels={'42':1446,'33':1854,'411':1890,'321':2511};base=json.loads((P/'tasks/ONE7_ROBUSTNESS.job.json').read_text());steps=[];w=lambda A:[[str(x) for x in row] for row in A.tolist()];res={}
for name,ell in labels.items():
 PP=S.eye(8)
 for k,x in labels.items():
  if k!=name:PP=PP*(L-x*S.eye(8))/(ell-x)
 assert PP*PP==PP
 gram=E.T*PP*E;res[name]={'projector_rank':PP.rank(),'pair_Gram':w(gram)}
 z=json.loads(json.dumps(base['steps'][0]));z['id']='pair_'+name;z['payload']['name']='ONE7_PAIR_'+name;z['payload']['context']['basis']=[0,1]
 ops={'C2':w(C2),'C3':w(C3),'I':w(S.eye(8)),'E':w(E)};pg=[{'name':'c2s','op':'scale','inputs':['C2'],'factor':'100'},{'name':'L','op':'add','inputs':['c2s','C3']}];prev='I'
 for k,x in labels.items():
  if k==name:continue
  pg.extend([{'name':'d'+k,'op':'scale','inputs':['I'],'factor':str(x)},{'name':'f'+k,'op':'subtract','inputs':['L','d'+k]},{'name':'n'+k,'op':'scale','inputs':['f'+k],'factor':str(S.Rational(1,ell-x))},{'name':'p'+k,'op':'multiply','inputs':[prev,'n'+k]}]);prev='p'+k
 pg.extend([{'name':'pe','op':'multiply','inputs':[prev,'E']},{'name':'et','op':'transpose','inputs':['E']},{'name':'out','op':'multiply','inputs':['et','pe']}]);z['payload']['data']={'operators':ops,'program':pg,'output':'out'};steps.append(z)
 if name=='411':
  j=next(j for j in range(8) if PP[j,j]);res['C3_omission_control']={'basis_index':j,'nonzero_411_weight':str(PP[j,j]),'pair_source_411_Gram':w(gram)}
  z=json.loads(json.dumps(base['steps'][0]));z['id']='C3_control';z['payload']['name']='ONE7_C3_control';z['payload']['context']['basis']=list(range(8));z['payload']['data']={'operators':{'P411':w(PP)},'program':[{'name':'out','op':'scale','inputs':['P411'],'factor':'1'}],'output':'out'};steps.append(z)
key='ONE7_PAIR_SECTORS';files=[src,P/'PRECOMMIT_PAIR.md',Path(__file__).resolve()];j={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'Reconstruct actual separated full-flavor pair-sector Grams from central CAR operators and demonstrate a reachable C3-omission control.','source_binding':base['source_binding'],'law_namespace':'SAM_land','precision_bits':256,'sources':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}};f=P/'tasks'/f'{key}.job.json';f.write_text(json.dumps(j,separators=(',',':'))+'\n');(P/'tasks'/f'{key}.json').write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':j['objective'],'job_path':str(f)},indent=2)+'\n');(P/'results/PAIR_SECTORS.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
