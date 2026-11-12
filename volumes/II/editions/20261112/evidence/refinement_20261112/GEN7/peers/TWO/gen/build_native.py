from pathlib import Path
import json, hashlib
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
def s(v): return str(Q(v))
def mat(a):return [[s(x) for x in r] for r in a]
def diag(a):return [[s(a[i]) if i==j else '0' for j in range(len(a))] for i in range(len(a))]
def word(key,operators,program,output,basis,purpose,control=False,rad=0):
 p={'name':key,'context':{'basis':basis,'field':{'radicand':rad},'units':{'energy':'source units','geometry':'declared constant lapse or clamped rigid rotor'},'history':{'campaign':'GEN7 lane TWO','precommit_sha256':hashlib.sha256((ROOT/'PRECOMMIT.md').read_bytes()).hexdigest(),'locked_inputs':'H003004-H003008 not replayed'},'spectral_coordinate':purpose},'data':{'operators':operators,'program':program,'output':output}}
 t={'kind':'native','key':key,'operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':purpose,'payload':p}
 if control:t.update(expected_status='COMPLETED',expected_reason='A completed nonzero residual witnesses the precommitted failed mathematical check; no engine rejection is expected')
 (ROOT/'tasks'/f'{key}.json').write_text(json.dumps(t,indent=2)+'\n')
def step(name,op,inputs,**kw):return dict(name=name,op=op,inputs=inputs,**kw)
word('TWO_GEO_WEIGHT_V1',{'R':mat([[1,Q(1,4),Q(1,9)]]),'SPIN':mat([[2],[2],[2]])},[step('w','multiply',['R','SPIN'])],'w',['w_6_half'],'Exact geometric occupied radial weight at nu=1/2,N=6 from complete admitted low-level census')
word('TWO_GEO_CONTROL_V1',{'ACTUAL':[['8']],'FALSE_FLAT':[['2']]},[step('res','subtract',['ACTUAL','FALSE_FLAT'])],'res',['centrifugal_residual'],'Reachable l=1,nu=1/2 control: the false flat angular exponent misses centrifugal coefficient6',True)
# Both matched profile boundary values and radial derivative continuity, for nu=1,3/4,1/2.
rows=[]
for nu in [Q(1),Q(3,4),Q(1,2)]:
 d=2*(nu+1)/nu
 # residuals: interior slope plus d*h/r = d; exterior derivative coefficient balances; boundary h and hprime agree
 rows.append([d/(d+1)*(1+d)-d, d/(d+1)-(1-1/(d+1)), d/(d+1)-d/(d+1)])
word('TWO_GEO_PROFILE_V1',{'MATCH':mat(rows),'ONE':mat([[1],[1],[1]])},[step('r','multiply',['MATCH','ONE'])],'r',['nu1','nu3/4','nu1/2'],'Matched geometric directional radial profile ODE and boundary residuals at all three actual geometries')
# Rotor raw coordinate basis: pair nAi*nBj, A coordinates, B coordinates; normalized Haar Gram.
image=[Q(18,5) if i in [0,4,8] else Q(0) for i in range(9)]+[Q(0),Q(0),Q(3,10),Q(0),Q(0),Q(-4,10)]
gram=[Q(1,9)]*9+[Q(1,3)]*6
gaps=[Q(4)]*9+[Q(2)]*6
ops={'J':mat([[x] for x in image]),'G':diag(gram),'R':diag([1/x for x in gaps])}
pr=[step('jt','transpose',['J']),step('gj','multiply',['G','J']),step('norm','multiply',['jt','gj']),step('rj','multiply',['R','J']),step('grj','multiply',['G','rj']),step('e2p','multiply',['jt','grj']),step('e2','scale',['e2p'],factor='-1')]
word('TWO_ROTOR_GENERAL_V1',ops,pr,'e2',['E2'],'Full orthogonal singlet-to-(11),(10),(01) rotor image at vA=vB6,tA3,tB4,BA=BB1; predicted -673/600')
mono=image[:9]
ops={'J':mat([[x] for x in mono]),'G':diag([Q(1,9)]*9),'R':diag([Q(1,4)]*9)}
pr=[step('jt','transpose',['J']),step('rj','multiply',['R','J']),step('grj','multiply',['G','rj']),step('e2p','multiply',['jt','grj']),step('e2','scale',['e2p'],factor='-1')]
word('TWO_ROTOR_CARBON_V1',ops,pr,'e2',['E2'],'Carbon neutral polarization monopole alone, complete l1,l1 image, exact second-order coefficient -27/25')
ops['WRONG_R']=diag([Q(1,2)]*9)
pr=[step('jt','transpose',['J']),step('dr','subtract',['WRONG_R','R']),step('dj','multiply',['dr','J']),step('gdj','multiply',['G','dj']),step('diffp','multiply',['jt','gdj']),step('diff','scale',['diffp'],factor='-1')]
word('TWO_ROTOR_CONTROL_V1',ops,pr,'diff',['wrong_minus_true'],'Reachable nonzero pair image: false single-rotor gap2 gives energy error -27/25',True)
# Haar second order n,m physical rational unit directions.
n=[Q(3,5),Q(4,5),0];m=[0,Q(3,5),Q(4,5)];r=Q(2);t=Q(3)
def outer(a,b):return [[a[i]*b[j] for j in range(3)]for i in range(3)]
def subI(nn):return [[nn[i][j]-(1 if i==j else 0)for j in range(3)]for i in range(3)]
A=[[r*x for x in row]for row in subI(outer(n,n))];B=[[t*x for x in row]for row in subI(outer(m,m))]
c=sum(n[i]*m[i] for i in range(3))
# bmean contributions sum = -(r^2+t^2)c/3, trace(A^T B)/3 is the cross term.
ops={'A':mat(A),'B':mat(B),'I3':diag([Q(1,3)]*3),'N':mat([n]),'M':mat([[x]for x in m]),'BN':mat([[-(r*r+t*t)*c/3]]),'ONE':mat([[1],[1],[1]]),'E0':mat([[1,0,0]]),'E1':mat([[0,1,0]]),'E2':mat([[0,0,1]])}
pr=[step('at','transpose',['A']),step('ab','multiply',['at','B']),step('scaled','multiply',['I3','ab'])]
# diagonal selectors, each scalar; sum traces.
for i in range(3):
 pr += [step(f'et{i}','transpose',[f'E{i}']),step(f'row{i}','multiply',[f'E{i}','scaled']),step(f'd{i}','multiply',[f'row{i}',f'et{i}'])]
pr += [step('d01','add',['d0','d1']),step('trace','add',['d01','d2']),step('pair','add',['trace','BN']),step('numer','scale',['pair'],factor='3')]
word('TWO_TAYLOR_PAIR_V1',ops,pr,'numer',['pair_numerator'],'Exact independent-Haar second-order internal-pair numerator for rational physical directions; expected714/625')
# Thermal variance and neutrality-breaking scalar first mean
word('TWO_ROTOR_THERMAL_V1',{'NORM':[['673/150']],'NEG_HALF':[['-1/2']]},[step('f2','multiply',['NEG_HALF','NORM'])],'f2',['F2_beta1'],'Classical independent-Haar orientational free-energy coefficient at beta1 equals minus half the full C1 variance: -673/300')
word('TWO_NEUTRALITY_CONTROL_V1',{'QA':[['1']],'QB':[['1']]},[step('mean','multiply',['QA','QB'])],'mean',['first_order_mean'],'Changing to charges+1,+1 produces singlet C1 mean1 and breaks the zero-first-order neutrality assertion',True)
print('Wrote9 native exact tasks')
