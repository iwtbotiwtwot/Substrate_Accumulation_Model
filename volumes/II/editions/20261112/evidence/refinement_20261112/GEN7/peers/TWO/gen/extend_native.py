import runpy
from pathlib import Path
from fractions import Fraction as Q
m=runpy.run_path('gen/build_native.py');word=m['word'];step=m['step'];mat=m['mat'];diag=m['diag']
# Do not submit overwritten original files: their exact submitted copies remain immutable.
word('TWO_GEO_MID_WEIGHT_V1',{'DINV':[[{'a':'-9/64','b':'3/64'}]],'BASE':[[{'a':'5/2','b':'0'}]]},[step('sq','multiply',['DINV','DINV']),step('tw','scale',['sq'],factor='2'),step('w','add',['BASE','tw'])],'w',['w6_three_quarters'],'Complete geometric weight at nu3/4,N6 in Q(sqrt137), expected(3217-27sqrt137)/1024',rad=137)
# Exact floor dominance flint certificate: 96/49 >27/16,16/9 >1/2.
word('TWO_GEO_FLOOR_DOMINANCE_V1',{'LOW':mat([[Q(96,49),0],[0,Q(16,9)]]),'RHS':mat([[Q(27,16),0],[0,Q(1,2)]])},[step('margin','subtract',['LOW','RHS'])],'margin',['nu3/4','nu1/2'],'Uniform lower margin in charge-scaled spectral-cost/core-floor comparison for all132 source accounts')
n=[Q(3,5),Q(4,5),0]
word('TWO_TAYLOR_OWN_V1',{'N':mat([[v]for v in n]),'M':diag([Q(1,3)]*3),'U':mat([[12,0,0]])},[step('mn','multiply',['M','N']),step('first','scale',['N'],factor='2/3'),step('second','scale',['mn'],factor='3'),step('b','subtract',['first','second']),step('r2b','scale',['b'],factor='4'),step('ub','multiply',['U','r2b']),step('own','scale',['ub'],factor='-1/20')],'own',['own_C2'],'Actual Haar-averaged own-core second-order coefficient, r2,dc2,U12,gp1/10; predicted+12/25')
# The second-order pair numerator changes sign on open physical configuration neighborhoods.
word('TWO_TAYLOR_SIGN_CONTROL_V1',{'SQUARE':[['13']],'TWOPROD':[['12']]},[step('negative','subtract',['TWOPROD','SQUARE'])],'negative',['pair_numerator'],'Parallel separated electron radii2,3 yield pair C2 numerator-1, unlike the positive714/625 witness',True)
# Native certified complex solve on the complete 15-coordinate rigid rotor image.
import json
x=json.loads(Path('tasks/TWO_ROTOR_GENERAL_V1.json').read_text());ops=x['payload']['data']['operators'];labels=[str(i)for i in range(15)]
matr={'entries':diag([4]*9+[2]*6),'row_basis':labels,'column_basis':labels,'structure':'HERMITIAN'}
rhs={'entries':ops['J'],'row_basis':labels,'column_basis':['singlet'],'structure':'GENERAL'}
t={'kind':'native','key':'TWO_ROTOR_RESOLVENT_V1','operation':'GEN3_COMPLEX_SOLVE','purpose':'Certified reduced rotor resolvent on every nonzero C1 singlet image, including both single and pair gaps','payload':{'precision_bits':256,'data':{'matrix':matr,'rhs':rhs}}};Path('tasks/TWO_ROTOR_RESOLVENT_V1.json').write_text(json.dumps(t,indent=2)+'\n')
