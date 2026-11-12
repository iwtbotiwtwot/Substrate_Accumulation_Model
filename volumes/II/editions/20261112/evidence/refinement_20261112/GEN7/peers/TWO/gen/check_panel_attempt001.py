from pathlib import Path
import json
from fractions import Fraction as Q
x=json.loads(Path('gen/PANEL.json').read_text());rows=x['rows'];assert len(rows)==132
assert len({(r['nu'],r['source'],r['g'],r['N'])for r in rows})==132
positive=0;overlap=0;last={};candidates=[]
for r in rows:
 key=(r['nu'],r['source'],r['g']);n=r['N'];L=r['upgraded_joint_lower'];U=r['spherical_upper'];assert Q(L['upper'])<Q(U['lower'])
 prev=last.get(key,{'upgraded_joint_lower':{'lower':r['separated'],'upper':r['separated']},'spherical_upper':{'lower':r['separated'],'upper':r['separated']}})
 I=r['fresh_spherical_ionization_lower'];assert Q(I['lower'])<=Q(prev['upgraded_joint_lower']['lower'])-Q(U['upper']) and Q(I['upper'])>=Q(prev['upgraded_joint_lower']['upper'])-Q(U['lower'])
 Iupper_lower=Q(prev['spherical_upper']['lower'])-Q(L['upper']);assert Iupper_lower>0
 if Q(I['lower'])>0:positive+=1
 else:assert Q(I['upper'])<0;overlap+=1
 if Q(prev['upgraded_joint_lower']['lower'])-Q(prev.get('old_joint_lower',prev['upgraded_joint_lower'])['upper'])>Q(1,10**80):candidates.append([*key,n])
 last[key]=r
assert (positive,overlap)==(30,102)
assert len(candidates)==10
out={'status':'PASS','populated_accounts':132,'positive_ionization':positive,'overlap_zero':overlap,'exact_original_portfolio_candidates':candidates,'independent_rational_endpoint_check':True}
Path('gen/PANEL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
