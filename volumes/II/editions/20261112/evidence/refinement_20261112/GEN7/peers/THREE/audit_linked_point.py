from pathlib import Path
from fractions import Fraction as F
import json,gzip,hashlib,sys
from interval_tools import *
sys.set_int_max_str_digits(0);R=Path.cwd();d=json.loads((R/'evidence/linked_point.json').read_text());r=next(x for x in json.loads((R/'evidence/residual_host.json').read_text())['profiles'] if x['id']=='V000_BASE');base=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4');oldp=base/'spin_difference_fifth1/native1/V000/V000_BASE_RESULT.json.gz';old=json.loads(gzip.decompress(oldp.read_bytes()))['output'];point={k:[[F(x) for x in z] for z in A] for k,A in d['primitive_point'].items()}
def ldl(A):
 n=len(A);L=[[F(i==j) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  v=A[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),F(0));assert v>0;D.append(v)
  for i in range(j+1,n):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),F(0)))/v
 return D
checks=0
for k,src in [('G',old['G5']),('D',old['D5']),('B',r['B']),('H',r['H'])]:
 A=point[k]
 for i in range(len(A)):
  for j in range(len(A[0])):assert aa(src['entries'][i][j]).contains(arb(str(A[i][j]))),(k,i,j);checks+=1
G7=[z+[F(0),F(0)] for z in point['G']]+[[F(0)]*5+z for z in point['B']];G7p=ldl(G7);mins=[]
for row in d['rows']:
 K=[[F(x) for x in z] for z in row['matrix']['entries']];piv=ldl(K);mins.append(min(piv));C12=F(row['cancelling_mixed_action']);assert aa(d['mixed_interval']).contains(arb(str(C12)))
 # Complete residual cap positive and changed control remains positive.
 ldl([[F(d['C11']),C12],[C12,F(d['C22'])]])
 if row['index']==18:K[5][6]+=F(1,1000);K[6][5]+=F(1,1000);ldl(K)
out={'primitive_entry_containment_checks':checks,'G7_positive':True,'all37_K7_positive':True,'all37_residual_caps_positive':True,'history18_changed_control_positive':True,'minimum_exact_LDL_pivot':str(min(mins)),'minimum_pivot_display':float(min(mins)),'scope':'Interval-relaxation feasibility only; no assertion that the shared primitive point is a second physical Gibbs source','source_hashes':[{'path':str(oldp),'sha256':hashlib.sha256(oldp.read_bytes()).hexdigest()}]};(R/'evidence/linked_point_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
