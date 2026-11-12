from pathlib import Path
import json,hashlib,itertools,time
from fractions import Fraction as Q
from collections import defaultdict
import numpy as np
import sympy as S
from flint import fmpz_mat, fmpq_mat, arb, ctx
ctx.prec=256
OUT=Path.cwd(); OLD=Path('/home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/peers/THREE/gen')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
rawfile=OLD/'ANISOTROPIC_REPAIR_OPERANDS.json'; raw=json.loads(rawfile.read_text())
keys=[tuple(x) for x in raw['complete_image_basis']]
# Literal Fourier-basis source operands are read; every density action below is newly assembled.
cols=[{d:int(raw['raw_source'][i][j]) for i,d in enumerate(keys) if int(raw['raw_source'][i][j])} for j in range(18)]
def density(v,q):
 out=defaultdict(int)
 for words,amp in v.items():
  for f,bits in enumerate(words):
   for k in range(8):
    if not(bits>>k&1):continue
    l=k^q; after=bits^(1<<k)
    if after>>l&1:continue
    sign=-1 if ((bits&((1<<k)-1)).bit_count()+(after&((1<<l)-1)).bit_count())%2 else 1
    nxt=list(words);nxt[f]=after|(1<<l);out[tuple(nxt)]+=sign*amp
 return {d:a for d,a in out.items() if a}
images=[[density(v,q) for v in cols] for q in range(8)]
basis=sorted(set().union(*(set(v) for v in cols),*(set(v) for row in images for v in row)))
X=np.array([[v.get(d,0) for v in cols] for d in basis],dtype=np.int64)
D=[np.array([[v.get(d,0) for v in row] for d in basis],dtype=np.int64) for row in images]
G=X.T@X; pairs=list(itertools.combinations_with_replacement(range(8),2)); M=[D[q].T@D[r] for q,r in pairs]
assert all(np.array_equal(a,a.T) for a in M)
assert int(max(np.max(abs(x)) for x in M))<100000000 # exact int64 summation safely bounded here
ms=lambda a:[[str(int(x)) for x in row] for row in a]
results={'raw_source_sha256':sha(rawfile),'source_columns':18,'full_image_rows':len(basis),'source_Gram':ms(G),'source_labels':raw['source_labels'],'ranks':{},'designs':{}}
for n,label in [(9,'phase9'),(11,'source11'),(18,'source18')]:
 obs=list(itertools.combinations_with_replacement(range(n),2))
 C=S.Matrix([[int(A[i,j])*(1 if q==r else 2) for A,(q,r) in zip(M,pairs)] for i,j in obs])
 _,pc=C.rref(); _,pr=C.T.rref();rank=len(pc);null=C.nullspace()
 assert all(C*v==S.zeros(len(obs),1) for v in null)
 minor=C.extract(list(pr),list(pc));det=minor.det()
 results['ranks'][label]={'rank':rank,'nullity':36-rank,'minor_rows':list(pr),'minor_cols':list(pc),'minor_det':str(det),'nullspace':[[str(x) for x in v] for v in null]}
 # rank lower via selected square minor; all kernel columns give exact rank upper
 np.savez(OUT/'results'/f'{label}_rank.npz',design=np.array(C.tolist(),dtype=np.int64))
 if n in [9,11]:
  np.savez(OUT/'results'/f'{label}_certificate.npz',minor=np.array(minor.tolist(),dtype=np.int64),null=np.array([[str(x) for x in row] for row in S.Matrix.hstack(*null).tolist()]),design=np.array(C.tolist(),dtype=np.int64))
 results['ranks'][label]['minor_matrix']=[[str(x) for x in row] for row in minor.tolist()]
 print(label,rank,flush=True)
nullvec=np.zeros(36,dtype=np.int64);nullvec[pairs.index((1,5))]=6;nullvec[pairs.index((0,4))]=-1
nullmat=sum(int(x)*a*(1 if q==r else 2) for x,a,(q,r) in zip(nullvec,M,pairs))
assert not np.any(nullmat[:11,:11]);where=np.argwhere(nullmat)
i,j=map(int,where[0]);results['reachable_null_control']={'scaled_B15':6,'scaled_B04':-1,'new_source_indices':[i,j],'response':int(nullmat[i,j]),'full_null_matrix':ms(nullmat)}
# P rho0 P comparison is trivial; choose q=4, using actual unnormalized phase metric.
G9=S.Matrix(G[:9,:9].tolist());Rq=S.Matrix((X[:,:9].T@D[4][:,:9]).tolist());full=S.Matrix(M[pairs.index((4,4))][:9,:9].tolist());bad=Rq*G9.inv()*Rq
err=full-bad;w=next((i,j,err[i,j]) for i in range(9) for j in range(9) if err[i,j])
results['compressed_density_control']={'q':4,'index':[w[0],w[1]],'full_minus_compressed_square':str(w[2]),'full_matrix':[[str(x) for x in row] for row in full.tolist()],'bad_matrix':[[str(x) for x in row] for row in bad.tolist()]}
for name,file,n in [('real8','ANISOTROPIC_SOURCE8_OPTIMIZED.json',8),('complex6','ANISOTROPIC_SOURCE6_COMPLEX_V2.json',6)]:
 prior=json.loads((OLD/file).read_text());A=prior['source_transform'];Ar=np.array([[int(x['re'] if isinstance(x,dict) else x) for x in row] for row in A],dtype=np.int64);Ai=np.array([[int(x['im']) if isinstance(x,dict) else 0 for x in row] for row in A],dtype=np.int64)
 Dr=[x@Ar for x in D];Di=[x@Ai for x in D];Xr=X@Ar;Xi=X@Ai
 Gr=Xr.T@Xr+Xi.T@Xi;Gi=Xr.T@Xi-Xi.T@Xr
 Mr=[a.T@b+c.T@d for a,b,c,d in [(Dr[q],Dr[r],Di[q],Di[r]) for q,r in []]] if False else [Dr[q].T@Dr[r]+Di[q].T@Di[r] for q,r in pairs]
 Mi=[Dr[q].T@Di[r]-Di[q].T@Dr[r] for q,r in pairs]
 obs=([(i,j,'re') for i,j in itertools.combinations_with_replacement(range(n),2)] if name=='real8' else [(i,i,'re') for i in range(n)]+[(i,j,k) for i,j in itertools.combinations(range(n),2) for k in ['re','im']])
 C=[[int((Mr if k=='re' else Mi)[a][i,j])*(1 if q==r else 2) for a,(q,r) in enumerate(pairs)] for i,j,k in obs]
 Z=fmpz_mat(C);det=Z.det(); inv=Z.inv(); assert fmpq_mat(Z)*inv==fmpq_mat(36,36,[1 if i==j else 0 for i in range(36) for j in range(36)])
 assert str(det)==prior['determinant']; assert [[str(inv[i,j]) for j in range(36)] for i in range(36)]==prior['inverse_design']
 weights=[Q(int(Gr[i,i])) if i==j else Q(int(Gr[i,i]+Gr[j,j]),2) for i,j,k in obs]
 beta=[sum(abs(Q(str(inv[i,j])))*weights[j] for j in range(36)) for i in range(36)]
 rowbounds=[8*sum(beta[pairs.index(tuple(sorted((q,r))))] for r in range(8)) for q in range(8)];K=max(rowbounds)
 assert str(K)==prior['error_norm_constant_pm']
 entry=lambda re,im:[ [str(int(x)) if int(y)==0 else {'re':str(int(x)),'im':str(int(y))} for x,y in zip(a,b)] for a,b in zip(re,im)]
 out={'source_transform':A,'source_operand_sha256':sha(OLD/file),'coefficient_order':pairs,'observables':obs,'Gram':entry(Gr,Gi),'design':ms(np.array(C)),'inverse':[[str(inv[i,j]) for j in range(36)] for i in range(36)],'determinant':str(det),'weights':list(map(str,weights)),'error_constant':str(K),'error_decimal':str(arb(str(K.numerator))/arb(str(K.denominator))),'row_bounds':list(map(str,rowbounds)),'readings':n+ (2 if name=='real8' else 4)*n*(n-1)//2}
 results['designs'][name]=out
 np.savez(OUT/'results'/f'{name}_images.npz',Xr=Xr,Xi=Xi,Dr=np.array(Dr),Di=np.array(Di),Mr=np.array(Mr),Mi=np.array(Mi))
 print(name,'det',det,'K',out['error_decimal'],flush=True)
(OUT/'results'/'TOMOGRAPHY.json').write_text(json.dumps(results,indent=2)+'\n')
# Complete small products kept for new native certification. No inherited arithmetic outputs enter these tasks.
np.savez(OUT/'results'/'base_images.npz',X=X,D=np.array(D),M=np.array(M),G=G,basis=np.array(basis))
(OUT/'results'/'SOURCE_CUSTODY.json').write_text(json.dumps({str(p):sha(p) for p in [rawfile,OLD/'ANISOTROPIC_SOURCE8_OPTIMIZED.json',OLD/'ANISOTROPIC_SOURCE6_COMPLEX_V2.json',Path(__file__).resolve(),OUT/'PRECOMMIT.md']},indent=2)+'\n')
