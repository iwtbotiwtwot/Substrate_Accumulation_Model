from pathlib import Path
import json,gzip,hashlib
from fractions import Fraction as F
from flint import fmpq_mat
from interval_tools import *
ROOT=Path.cwd();r=next(x for x in json.loads((ROOT/'evidence/residual_host.json').read_text())['profiles'] if x['id']=='V000_BASE');ex=json.loads((ROOT/'evidence/linked_exploration.json').read_text());BASE=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4');oldp=BASE/'spin_difference_fifth1/native1/V000/V000_BASE_RESULT.json.gz';upp=BASE/'spin_upper_source1_20261014/pilot3/V000/V000_BASE_RESULT.json.gz';old=json.loads(gzip.decompress(oldp.read_bytes()))['output'];up=json.loads(gzip.decompress(upp.read_bytes()))['output']
def q(v):return F(str(aa(v).mid().fmpq()))
def qmat(A):return [[q(x) for x in z] for z in A]
def qm(A,B):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def qs(A,B):
 a=fmpq_mat([[str(x) for x in z] for z in A]);b=fmpq_mat([[str(x) for x in z] for z in B]);return [[F(str(x)) for x in z] for z in a.solve(b).tolist()]
def dotq(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def trans(A):return list(map(list,zip(*A)))
G4=qmat([z[:4] for z in old['G5']['entries'][:4]]);D4=qmat([z[:4] for z in old['D5']['entries'][:4]]);W=qmat(old['projected_matrices']['W']['entries']);W[1][0]=W[0][1]=(W[0][1]+W[1][0])/2
# One shared primitive point: matrices are symmetrized before all dependent operations.
for A in [G4,D4]:
 for i in range(4):
  for j in range(i):A[i][j]=A[j][i]=(A[i][j]+A[j][i])/2
G=[z+[F(0)] for z in G4]+[[F(0)]*4+[W[0][0]]];k=[F(0),F(0),W[0][0],W[0][1]];D=[D4[i]+[k[i]] for i in range(4)]+[k+[q(old['J'])]];c=[z[0] for z in qs(G,[[v] for v in k+[D[4][4]]])];lam=W[0][1]/W[0][0];cross=q(up['J21'])-lam*q(old['J']);beta=q(up['F11'])-dotq(k+[D[4][4]],c);delta=W[1][1]-W[0][1]**2/W[0][0];B=[[delta,cross],[cross,beta]];H=[[F(0),F(0)],[F(0),F(0)],[F(0),F(0)],[delta,cross],[cross,beta]];g=[z[0] for z in G];C11=F(str(aa(ex['d11_upper']).upper().fmpq()));C22=F(r['original_scalar_cap']);mix=aa(ex['mixed_full']);rows=[]
for i,hist in enumerate(old['rows']):
 xi=F(hist['xi_exact']);K=[[xi*G[a][b]+D[a][b] for b in range(5)] for a in range(5)];kiH=qs(K,H);kig=qs(K,[[x] for x in g]);v=[z[0] for z in qm(trans(H),kig)];T=qm(trans(H),kiH);s22=xi*B[1][1]+C22-T[1][1];cc=v[0]*s22/v[1]-xi*B[0][1]+T[0][1];s12=xi*B[0][1]+cc-T[0][1];s11=xi*B[0][0]+C11-T[0][0];det=s11*s22-s12*s12;K7=[K[a]+H[a] for a in range(5)]+[[H[a][b] for a in range(5)]+[xi*B[b][j]+([[C11,cc],[cc,C22]][b][j]) for j in range(2)] for b in range(2)];sol=qs(K7,[[x] for x in g+[F(0),F(0)]]);vfull=dotq(g+[F(0),F(0)],[z[0] for z in sol]);base=dotq(g,[z[0] for z in kig])+v[1]*v[1]/s22
 assert det>0 and vfull==base and mix.contains(arb(str(cc)))
 row={'index':i,'xi':str(xi),'cancelling_mixed_action':str(cc),'mixed_within_paid_interval':True,'schur_leading':str(s11),'schur_determinant':str(det),'exact_linked_gain':str(vfull-base),'matrix':{'entries':[[str(x) for x in z] for z in K7],'row_basis':[str(j) for j in range(7)],'column_basis':[str(j) for j in range(7)],'structure':'GENERAL'},'rhs':{'entries':[[str(x)] for x in g+[F(0),F(0)]],'row_basis':[str(j) for j in range(7)],'column_basis':['g'],'structure':'GENERAL'}};rows.append(row)
print('37 shared-point histories:',len(rows),'all exact gain0; cancelling D12 range',min(float(F(z['cancelling_mixed_action'])) for z in rows),max(float(F(z['cancelling_mixed_action'])) for z in rows))
out={'scope':'Linked upstream midpoint of retained moment boxes, exact dependent G5,D5,B,H; paid mixed-action interval relaxation. Not a second physical source or physical no-gain theorem.','primitive_point':{'G':[[str(x) for x in z] for z in G],'D':[[str(x) for x in z] for z in D],'B':[[str(x) for x in z] for z in B],'H':[[str(x) for x in z] for z in H]},'mixed_interval':ex['mixed_full'],'C11':str(C11),'C22':str(C22),'rows':rows};(ROOT/'evidence/linked_point.json').write_text(json.dumps(out,indent=2)+'\n')
