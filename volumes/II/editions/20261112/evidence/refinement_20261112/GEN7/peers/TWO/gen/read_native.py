from pathlib import Path
import json,hashlib
R=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/native_returns')
expected={'TWO_GEO_WEIGHT_V1':[['49/18']],'TWO_GEO_PROFILE_V1':[['0'],['0'],['0']],'TWO_GEO_CONTROL_V3':[['6']],'TWO_ROTOR_CARBON_V1':[['-27/25']],'TWO_ROTOR_GENERAL_V1':[['-673/600']],'TWO_ROTOR_CONTROL_V3':[['-27/25']],'TWO_TAYLOR_PAIR_V1':[['714/625']],'TWO_NEUTRALITY_CONTROL_V3':[['1']],'TWO_ROTOR_THERMAL_V3':[['-1321/600']]}
out=[]
for k,e in expected.items():
 p=R/(k+'.json');x=json.loads(p.read_text());v=x['returned']['matrix'];assert x['status']=='COMPLETED' and v==e,(k,v,e)
 receipt=Path(x['receipt']);sha=hashlib.sha256(receipt.read_bytes()).hexdigest();assert sha==x['receipt_sha256']
 out.append({'key':k,'status':x['status'],'matrix':v,'receipt':str(receipt),'receipt_sha256':sha,'record_sha256':x['returned']['record_sha256'],'completed_utc':x['completed_utc']})
print(json.dumps(out,indent=2));Path('gen/NATIVE_READBACK.json').write_text(json.dumps(out,indent=2)+'\n')
