from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,hashlib,shutil
H=Path(__file__).resolve().parent;O=H/'results';E=H/'native_evidence';E.mkdir(exist_ok=True)
R=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/native_returns')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
index={};checks=[]
def read(k):
 p=R/(k+'.json');d=json.loads(p.read_text());wrapper=d
 if 'returned'not in d and d.get('record_file'):p=Path(d['record_file']);d=json.loads(p.read_text())
 index[k]=dict(status=wrapper['status'],receipt_sha256=wrapper.get('receipt_sha256'),return_sha256=sha(R/(k+'.json')),complete_record_sha256=sha(p),record=str(p),completed_utc=wrapper.get('completed_utc'),operation=wrapper.get('operation'),native_calls=wrapper.get('native_calls'))
 shutil.copyfile(R/(k+'.json'),E/(k+'.return.json'))
 if p!=R/(k+'.json'):shutil.copyfile(p,E/(k+'.record.json'))
 return d
def output(k):
 d=read(k)['returned'];return d.get('result',{}).get('output',d)
def jout(k,step):
 v=read(k)['returned'][step]['value'];return v.get('result',{}).get('output',v)
def ri(z):
 if 're'in z:z=z['re']
 return F(z['lower']),F(z['upper'])
def contains(z,q):
 a,b=ri(z);return a<=q<=b
def display(z):
 a,b=ri(z)
 with localcontext()as ctx:
  ctx.prec=45
  return [str(Decimal(a.numerator)/Decimal(a.denominator)),str(Decimal(b.numerator)/Decimal(b.denominator))]
def ck(name,value):
 assert value,name;checks.append(name)
dp=json.loads((O/'C12_DP.json').read_text());g=output('FOUR_DP_GRAM_V1')
ck('all324C12GramEntries',g['matrix']==dp['full_Gram']);ck('nativeDP_rank10',g['rank']==10)
ref=json.loads((O/'REFERENCES.json').read_text());vals=output('FOUR_REFERENCE_BANK_V1')['matrix']['entries']
for i,c in enumerate(ref['contrasts']):
 for j,q in enumerate(c['contractions']):ck('reference_%d_%d'%(i,j),contains(vals[i][j],F(q)))
for i,q in enumerate(ref['anchor_coefficients']):ck('anchor_%d'%i,contains(output('FOUR_ANCHOR_SOLVE_V1')['solution'][i][0],F(q)))
cg=output('FOUR_HE3_CHART_V1');ck('nativeHe3eigenResidual',all(F(x)==0 for row in cg['matrix']for x in row))
pointwise=output('FOUR_HE3_POINTWISE_V2');ck('nativeHe3sixSeparateBlocks',pointwise['rank']==0 and all(F(x)==0 for row in pointwise['matrix']for x in row))
brokenHe3=output('FOUR_HE3_BROKEN_V1');ck('nativeHe3qZeroBreaks',F(brokenHe3['matrix'][0][0])==F(-5727442,52966485) and brokenHe3['rank']==1)
role_entropy=output('FOUR_ROLE_ENTROPY_V1');ck('nativeRoleEntropy',role_entropy['status']=='CERTIFIED_ENTROPY')
fib=output('FOUR_GRAMMAR_FIBERS_V1')['matrix'];ck('thirteenNativeNormFiberDiagonals',all(F(fib[i][i])==0 for i in range(13)))
br=output('FOUR_REFERENCE_BROKEN_V1')['matrix']['entries'];ck('brokenReferenceResidual1',contains(br[0][0],F(1)))
dg=output('FOUR_DP_BROKEN_V1')['matrix'];ck('nativeDiagonalSourceControl',sum(F(dg[i][i])for i in range(6))==F(dp['control_residual'])!=0)
wa=json.loads((O/'WAVE_RAW.json').read_text());mom=output('FOUR_WAVE_MOMENTS_V1')['matrix']['entries'];bad=output('FOUR_WAVE_BROKEN_V1')['matrix']['entries']
for i in range(8):
 for j in range(4):ck('waveMoment_%d_%d'%(i,j),contains(mom[i][j],F(wa['moments'][i][j])))
ck('waveBreakingM0',any(not contains(bad[i][0],F(0))for i in range(8)))
w=output('FOUR_WAVE_REBUILD_V1');N=w['normal_Gram'];EN=w['free_energy_Gram']
def lin(mat):
 terms=[(1,mat[1][1]),(1,mat[2][2]),(-2,mat[1][2])];lo=hi=F(0)
 for c,v in terms:
  a,b=ri(v);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return dict(lower=str(lo),upper=str(hi))
D2=lin(N);Ed=lin(EN)
ck('actualDifferenceEnergy',contains(Ed,F(3535,4)))
ck('fullContinuum',w['full_continuum']and not w['cutoff_used'])
ck('all48meanAgreement',w['core_new_receiver_mean'][0]==w['core_new_receiver_mean'][1]==w['core_new_receiver_mean'][2])
ck('forwardWork',w['energy_ledger'][1]['switching_work']=='26111/40');ck('reverseWork',w['energy_ledger'][2]['switching_work']=='25727/40')
rank=jout('FOUR_DICTIONARY_V1','rank');ck('dictionaryNativeRank2',rank['rank_lower']==rank['rank_upper']==2)
contact={s:jout('FOUR_CONTACT_TRANSFER_V1',s)for s in ['calibrated','uncalibrated','depth','logquad']}
correct=contact['calibrated']['matrix']['entries'][1][0];wrong=contact['uncalibrated']['matrix']['entries'][1][0]
ck('calibratedMarkedTransfer',contains(correct,F(1,192)));ck('uncalibratedTransferBreaks',not contains(wrong,F(1,192)))
cv=output('FOUR_RICE_SCHUR_V1');cb=output('FOUR_RICE_BROKEN_V1');ck('riceActualDiagonalPositive',all(F(cv['matrix'][i][i])>0 for i in range(12)));ck('riceSmoothSurrogateNotPositive',F(cb['matrix'][0][0])<0)
therm={s:jout('FOUR_THERMAL_METHOD_V1',s)for s in ['execute_original','execute_sharper']}
for s,t in therm.items():ck('thermalMethod_'+s,t['status']=='PASSED')
ck('originalErrorBelow01315',ri(therm['execute_original']['output']['Pe_upper']['entries'][0][0])[1]<F(1315,100000))
ck('sharperErrorBelow01312',ri(therm['execute_sharper']['output']['Pe_upper']['entries'][0][0])[1]<F(1312,100000))
# Deterministic band improvement follows from full directed native Gram, not a rounded midpoint.
ck('sharperBand382443',ri(D2)[0]-ri(Ed)[1]-F(54037,1000000)>F(382443,1000))
expected=read('FOUR_REACHABLE_CONTROL_V1');ck('expectedNativeFailure',expected['status']=='FAILED')
details=dict(native_difference_norm_squared=D2,native_difference_energy=Ed,displays=dict(norm_squared=display(D2),energy=display(Ed),marked_correct=display(correct),marked_uncorrected=display(wrong)),dictionary_rank=rank,contact_depth_display=display(contact['depth']['matrix']['entries'][0][0]),rice_scaled_first_block=[row[:2]for row in cv['matrix'][:2]],rice_broken=cb['matrix'],thermal={s:dict(Q=display(t['output']['Q']['entries'][0][0]),Pe_upper=display(t['output']['Pe_upper']['entries'][0][0]))for s,t in therm.items()},checks=len(checks),all_passed=True)
(O/'NATIVE_CHECKS.json').write_text(json.dumps(details,indent=2)+'\n');(O/'NATIVE_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(O/'CHECK_NAMES.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({k:details[k]for k in ['checks','all_passed','displays','contact_depth_display','rice_broken','thermal']},indent=2));print('native completed',sum(x['status']=='COMPLETED'for x in index.values()),'expected failed',sum(x['status']=='FAILED'for x in index.values()))
