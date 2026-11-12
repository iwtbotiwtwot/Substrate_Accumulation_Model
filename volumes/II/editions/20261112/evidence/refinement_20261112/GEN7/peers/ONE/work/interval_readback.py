import json,decimal,pathlib
from fractions import Fraction as Q
decimal.getcontext().prec=100
root=pathlib.Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/workers/G6_01/tasks/ONE7_ARRIVAL/gen6')
m=json.load(open(root/'007_distance_squared.output.json'))['result']['output']['matrix'];bounds=[]
for label,row in zip(m['row_basis'],m['entries']):
 lo=Q(row[0]['re']['lower']);hi=Q(row[0]['re']['upper']);x=(decimal.Decimal(lo.numerator)/decimal.Decimal(lo.denominator)).sqrt();n=int(x*10**16);a=Q(n,10**16);b=Q(n+1,10**16)
 assert a*a<=lo and b*b>=hi
 bounds.append({'label':label,'lower':format(decimal.Decimal(n)/10**16,'.16f'),'upper':format(decimal.Decimal(n+1)/10**16,'.16f'),'exact_square_comparison':True})
print(bounds);pathlib.Path('results/ARRIVAL_READBACK.json').write_text(json.dumps(bounds,indent=2)+'\n')
s='\nNative squared-distance enclosures additionally imply the following outward decimal norm intervals. Each decimal endpoint was checked by an exact rational square comparison against the native lower/upper endpoint; no untracked decimal rounding enters these bounds.\n\n| Quantity | Certified enclosing norm interval |\n|---|---|\n'
for b in bounds:s+='| '+b['label']+' | ['+b['lower']+', '+b['upper']+'] |\n'
p=pathlib.Path('REPORT.md');r=p.read_text();r=r.replace('\n## Branch-aware and signed uniform robustness',s+'\n## Branch-aware and signed uniform robustness');p.write_text(r)
