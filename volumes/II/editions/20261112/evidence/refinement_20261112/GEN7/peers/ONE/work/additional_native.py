from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import numpy as np
import sympy as S
P=Path.cwd();template=json.loads((P/'tasks/ONE7_ROBUSTNESS.job.json').read_text());bind=template['source_binding'];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def wmat(x):return [[str(v) for v in row] for row in (x.tolist() if hasattr(x,'tolist') else x)]
def mat(a,r=None,c=None):
 a=wmat(a);return {'entries':a,'row_basis':r or list(range(len(a))),'column_basis':c or list(range(len(a[0]))),'structure':'GENERAL'}
def word(k,ops,pg,out,n):
 z=json.loads(json.dumps(template['steps'][0]));z['id']=k;z['payload']['name']='ONE7_'+k;z['payload']['context']['basis']=list(range(n));z['payload']['data']={'operators':{x:wmat(v) for x,v in ops.items()},'program':pg,'output':out};return z
def st(k,op,data):return {'id':k,'operation':op,'purpose':'New one-hop cloud-dressed density observable and exact source certification; locked baseline not replayed.','payload':{'source_binding':{'$source':True},'precision_bits':256,'data':data},'checks':[{'predicate':'native_contract'}]}
def save(key,steps,src):
 j={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':key+' source-bound new-observable verification','source_binding':bind,'law_namespace':'SAM_land','precision_bits':256,'sources':[{'path':str(p.resolve()),'sha256':sha(p)} for p in src+[P/'PRECOMMIT.md',Path(__file__).resolve()]],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}}
 f=P/'tasks'/f'{key}.job.json';f.write_text(json.dumps(j,separators=(',',':'))+'\n');(P/'tasks'/f'{key}.json').write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':j['objective'],'job_path':str(f)},indent=2)+'\n')
steps=[]
for label in ['phase9','source11']:
 z=np.load(P/'results'/f'{label}_certificate.npz');C=z['design'];N=z['null']
 for k,start in enumerate(range(0,len(C),33)):
  A=C[start:start+33];steps.append(word(label+'_exact_null_'+str(k),{'C':A,'N':N},[{'name':'out','op':'multiply','inputs':['C','N']}],'out',len(A)))
save('ONE7_EXACT_NULLS',steps,[P/'results/TOMOGRAPHY.json'])
# Exact36x36 LU residuals and scalar diagonal products certify the two full determinants natively.
tomo=json.loads((P/'results/TOMOGRAPHY.json').read_text());steps=[]
for label in ['real8','complex6']:
 C=S.Matrix(tomo['designs'][label]['design']);L,U,sw=C.LUdecomposition();PP=S.eye(36)
 for i,j in sw:PP.row_swap(i,j)
 assert PP*C==L*U
 steps.append(word(label+'_LU',{'P':PP,'C':C,'L':L,'U':U},[{'name':'pc','op':'multiply','inputs':['P','C']},{'name':'lu','op':'multiply','inputs':['L','U']},{'name':'out','op':'subtract','inputs':['pc','lu']}],'out',36))
 ops={'sgn':[[(-1)**len(sw)]]};pg=[];prev='sgn'
 for i in range(36):
  ops['d'+str(i)]=[[U[i,i]]];n='prod'+str(i);pg.append({'name':n,'op':'multiply','inputs':[prev,'d'+str(i)]});prev=n
 steps.append(word(label+'_determinant',ops,pg,prev,1))
save('ONE7_DETERMINANTS',steps,[P/'results/TOMOGRAPHY.json'])
S0=Path('/home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6');imfile=S0/'PHYSICAL_IMAGES.json';momfile=S0/'MOMENTS.json';imgs=json.loads(imfile.read_text());moms=json.loads(momfile.read_text());dress=json.loads((P/'results/DRESSED_DENSITY.json').read_text());steps=[]
for lam in ['42','33','321']:
 n=moms['sectors'][lam]['target_orbital_dimension'];images=imgs[lam]['internal'];A=np.zeros((len(images),n),dtype=np.int64);DA=A.copy()
 for k,row in enumerate(images):
  ds=sum(x*x for x in row['density'])
  for j,sgn in row['entries']:A[k,j]=sgn;DA[k,j]=sgn*ds
 steps.append(st('D2_image_'+lam,'GEN3_COMPLEX_PRODUCT',{'matrix':mat(A.T),'right':mat(DA)}))
 # All exact exponent-class coefficients remain source operands, including signed mixed terms.
 coeff=dress['sectors'][lam]['density_square_internal_exponent_coefficients'];ops={'W'+str(k):v for k,v in enumerate(coeff.values())};pg=[];prev='W0'
 for k in range(1,len(ops)):
  name='sum'+str(k);pg.append({'name':name,'op':'add','inputs':[prev,'W'+str(k)]});prev=name
 if not pg:pg=[{'name':'out','op':'scale','inputs':['W0'],'factor':'1'}];prev='out'
 steps.append(word('D2_classes_'+lam,ops,pg,prev,n))
 steps.append(word('D2_cell_'+lam,{'W':dress['sectors'][lam]['cell_density_square_moment']},[{'name':'out','op':'scale','inputs':['W'],'factor':'1'}],'out',n))
 # Exact bound arithmetic assembled as multiplication of numerator and normalization reciprocal.
 d=dress['sectors'][lam];a=F(d['alpha']);numer=F(d['base_density_square'])+a*a*F(d['W_upper']);den=1+a*a*F(d['V_lower_locked']);assert numer/den==F(d['dressed_D2_upper'])
 steps.append(word('D2_bound_'+lam,{'n':[[str(numer)]],'r':[[str(1/den)]]},[{'name':'out','op':'multiply','inputs':['n','r']}],'out',1))
steps.append(st('cloud_exponential_ceiling','GEN3_COMPLEX_EXP',{'matrix':mat([['-16324/2205','0'],['0','-119/45']])}))
# A nonzero cell-density control shows why old all-in-one-cell uniform slope is changed.
pc=F(dress['uniform_cell_probability_upper']);steps.append(word('uniform_dressed_slope',{'a':[['5/4']],'b':[[str(1-pc)]]},[{'name':'out','op':'multiply','inputs':['a','b']}],'out',1))
save('ONE7_DRESSED_DENSITY',steps,[imfile,momfile,P/'work/dressed_moments.py',P/'results/DRESSED_DENSITY.json'])
print('built exact-null, determinant and new cloud-density jobs',flush=True)
