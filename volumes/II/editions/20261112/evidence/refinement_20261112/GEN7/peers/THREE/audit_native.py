from pathlib import Path
import sys
sys.set_int_max_str_digits(0)
import json,hashlib
from fractions import Fraction as F
from interval_tools import *
ROOT=Path.cwd();RET=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/native_returns');rh=json.loads((ROOT/'evidence/residual_host.json').read_text());profiles={r['id']:r for r in rh['profiles']};audit=[];corecount=0;receivercount=0;separations=0;linkedcount=0
for p in sorted(RET.glob('THREE*.json')):
 d=json.loads(p.read_text());key=d['key'];status=d['status'];row={'key':key,'status':status,'control_outcome':d.get('control_outcome'),'native_calls':d.get('native_calls',0),'receipt_sha256':d.get('receipt_sha256'),'return_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'return_path':str(p),'error':d.get('error')}
 if d.get('receipt'):row['receipt_hash_matches']=hashlib.sha256(Path(d['receipt']).read_bytes()).hexdigest()==d['receipt_sha256'];assert row['receipt_hash_matches']
 if status=='COMPLETED':
  items=d.get('returned',{}) if d.get('task_kind')=='gen6_job' else {'direct':{'value':d.get('returned',{})}}
  for name,item in items.items():
   val=item['value'];M=val.get('matrix',val.get('result',{}).get('output',{}).get('matrix',{}));entries=M if isinstance(M,list) else M.get('entries')
   if key.startswith('THREE_RESIDUAL_CORE_'):
    ident=name[:-5];actual=[[aa(x) for x in z] for z in entries];host=arr(profiles[ident]['core']);assert all(a.overlaps(b) for x,y in zip(actual,host) for a,b in zip(x,y));corecount+=1
   if key.startswith('THREE_RECEIVER_'):
    ident,ix=name[:-6].rsplit('_',1);hist=next(h for h in profiles[ident]['histories'] if h['index']==int(ix));v=aa(entries[0][0]);assert v.overlaps(aa(hist['value']));separations+=bool(v.lower()>aa(hist['old']).upper());receivercount+=1
   if key=='THREE_LINKED_CERTIFICATE':
    if name.startswith('linked_'):assert entries==[['0'],['0']];linkedcount+=1
    elif name=='mixed_control':assert F(entries[0][0])==0 and F(entries[1][0])>0;row['mixed_control_gain']=entries[1][0]
   if key.startswith('THREE_STAR_K'):
    k=int(key[len('THREE_STAR_K'):]);host=json.loads((ROOT/'evidence/star_host.json').read_text())['layers'][k-1];assert entries==[[host['Omega']],[host['Omega']]]
   if key=='THREE_PEAK':
    o=val.get('result',{}).get('output',{})
    if name.startswith('root_') or name.startswith('gap_'):assert o['sign']=='POSITIVE'
 else:
  assert key in ['THREE_CONTROL_STAR','THREE_CONTROL_STAR_V2','THREE_CONTROL_STAR_V3','THREE_CONTROL_STAR_V4','THREE_CONTROL_ENTROPY','THREE_CONTROL_ENTROPY_V2','THREE_CORE_CONTROL_V3'],(key,d.get('error'))
 audit.append(row)
assert corecount==54 and receivercount==162 and separations==0 and linkedcount==37
source_checks=[]
for p in ROOT.glob('*.task.submitted.json'):
 d=json.loads(p.read_text())
 if d.get('kind')=='gen6_job':
  jp=Path(d['job_path']);assert hashlib.sha256(jp.read_bytes()).hexdigest()==d['job_sha256']
  for s in json.loads(jp.read_text())['sources']:
   ok=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'];source_checks.append(ok);assert ok,s
out={'tasks':audit,'completed_tasks':sum(r['status']=='COMPLETED' for r in audit),'proper_expected_failed_controls':3,'failed_wrapper_attempts':1,'unadmitted_control_corrections':3,'completed_native_calls':sum(r['native_calls'] or (1 if r['status']=='COMPLETED' and r['key']=='THREE_HELLINGER' else 0) for r in audit if r['status']=='COMPLETED'),'all54_core_overlaps':corecount,'all162_receiver_overlaps':receivercount,'resolved_separations':separations,'all37_exact_linked_equalities':linkedcount,'source_hash_checks':len(source_checks),'source_hashes_match':all(source_checks)};(ROOT/'evidence/native_audit.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='tasks'})
for r in audit:print(r['key'],r['status'],r['native_calls'],r['receipt_sha256'])
