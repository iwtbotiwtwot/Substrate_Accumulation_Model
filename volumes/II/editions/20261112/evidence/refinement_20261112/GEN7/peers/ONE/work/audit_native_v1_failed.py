from pathlib import Path
from fractions import Fraction as F
import json,hashlib,itertools
import numpy as np
P=Path.cwd();ROOT=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();audit=[];checks=0
T=json.loads((P/'results/TOMOGRAPHY.json').read_text())
def contains(entry,re,im=0):
 global checks
 if not isinstance(entry,dict):assert F(str(entry))==F(str(re)) and im==0
 else:
  for k,v in [('re',re),('im',im)]:
   x=entry[k];assert F(x['lower'])<=F(str(v))<=F(x['upper'])
 checks+=1
for p in sorted((ROOT/'native_returns').glob('ONE7*.json')):
 small=json.loads(p.read_text());d=json.loads(Path(small['record_file']).read_text()) if 'record_file' in small else small
 assert small['status']=='COMPLETED',(p,small.get('error'));base=ROOT/'workers/G6_01/tasks'/small['key']/'gen6'
 for tr in d.get('gen6_execution',{}).get('trace',[]):
  out=base/tr['output'];inp=base/tr['input'];assert sha(out)==tr['output_sha256'] and sha(inp)==tr['input_sha256']
  v=json.loads(out.read_text());k=tr['id']
  if small['key'] in ['ONE7_REAL8','ONE7_COMPLEX6']:
   label='real8' if 'REAL8' in small['key'] else 'complex6';z=np.load(P/'results'/f'{label}_images.npz')
   if k.startswith('cross_'):
    _,q,r=k.split('_');idx=list(itertools.combinations_with_replacement(range(8),2)).index((int(q),int(r)));re=z['Mr'][idx];im=z['Mi'][idx]
   elif k=='raw_Gram':re=z['Xr'].T@z['Xr']+z['Xi'].T@z['Xi'];im=z['Xr'].T@z['Xi']-z['Xi'].T@z['Xr']
   elif k.startswith('inverse_'):
    assert v['matrix']==[['1' if i==j else '0' for j in range(36)] for i in range(36)];checks+=1296;continue
   elif k.startswith('solve_'):
    o=v['result']['output'];assert o['status']=='CERTIFIED';entries=o['solution']['entries'];inv=T['designs'][label]['inverse']
    for i,row in enumerate(entries):
     for j,x in enumerate(row):contains(x,inv[i][j])
    continue
   else:continue
   entries=v['result']['output']['matrix']['entries']
   for i,row in enumerate(entries):
    for j,x in enumerate(row):contains(x,int(re[i,j]),int(im[i,j]))
  if small['key']=='ONE7_EXACT_NULLS':
   assert all(F(x)==0 for row in v['matrix'] for x in row);checks+=sum(map(len,v['matrix']))
  if small['key']=='ONE7_DETERMINANTS':
   if k.endswith('_LU'):assert all(F(x)==0 for row in v['matrix'] for x in row)
   else:
    label=k.replace('_determinant','');assert v['matrix'][0][0]==T['designs'][label]['determinant']
   checks+=1
  if small['key']=='ONE7_DRESSED_DENSITY' and k.startswith('D2_image_'):
   lam=k[len('D2_image_'):];dr=json.loads((P/'results/DRESSED_DENSITY.json').read_text())['sectors'][lam];A=[[[F(x) for x in row] for row in a] for a in dr['density_square_internal_exponent_coefficients'].values()];entries=v['result']['output']['matrix']['entries']
   for i,row in enumerate(entries):
    for j,x in enumerate(row):contains(x,sum(a[i][j] for a in A))
 if small['key']=='ONE7_SINGULAR_CONTROL_V3':assert d['returned']['result']['output']['status']=='INVERTIBILITY_UNRESOLVED';checks+=1
 dest=P/'native_receipts'/p.name;dest.write_bytes(p.read_bytes())
 audit.append({'key':small['key'],'status':small['status'],'native_calls':small.get('native_calls',1),'receipt_sha256':small.get('receipt_sha256'),'full_return_path':str(Path(small.get('record_file',p))),'full_return_sha256':sha(Path(small.get('record_file',p))),'trace_operations':len(d.get('gen6_execution',{}).get('trace',[])),'completed_utc':small['completed_utc']})
(P/'results/NATIVE_AUDIT.json').write_text(json.dumps({'checks':checks,'completed_submissions':len(audit),'native_operations':sum(x['native_calls'] for x in audit),'receipts':audit},indent=2)+'\n');print('all completed receipts/readbacks checked',len(audit),'ops',sum(x['native_calls'] for x in audit),'entries',checks)
