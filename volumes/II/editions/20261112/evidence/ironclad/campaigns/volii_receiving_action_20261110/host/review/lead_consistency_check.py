"""Post-window consistency review; not a new Duck run or independent CR2 case."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib, json, math
import numpy as np
import sympy as sp
import mpmath as mp

C = Path(__file__).resolve().parents[2]
checks, inputs = [], {}
def read(rel):
    p = C / rel
    inputs[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text())
def record(name, **details):
    checks.append(dict(name=name, status='PASS', **details))
def mat(rows):
    return sp.Matrix([[sp.Rational(x) for x in row] for row in rows])

# Recompute image Grams before compression, independently of native readouts.
o = read('peers/FOUR/gen/STATIC_KERNEL_IDENTIFICATION.json')
raw = np.array(o['raw_source'], dtype=np.int64)
assert len(raw) == 1503
def gram(rows):
    a = np.array(rows, dtype=np.int64)
    bound = int(np.max(np.abs(a))) ** 2 * len(a)
    assert bound < np.iinfo(np.int64).max
    return a.T @ a
g = gram(o['raw_source'])
assert np.array_equal(g, np.array(o['raw_Gram'], dtype=np.int64))
grams = []
for image, expected in zip(o['raw_density_images'], o['raw_density_square_grams']):
    got = gram(image)
    assert np.array_equal(got, np.array(expected, dtype=np.int64))
    grams.append(sp.Matrix(got))
design = sp.Matrix([[grams[q][x['source_row'], x['source_column']]
                    for q in range(8)] for x in o['independent_observables']])
assert design == mat(o['design_minor'])
assert design.det() == -940584960000
old = sp.Matrix(81, 8, lambda row, q: grams[q][row // 9, row % 9])
assert old.rank() == 6
assert grams[6][:9,:9] == grams[5][:9,:9]
assert -sp.Rational(59,126)*grams[0][:9,:9]+sp.Rational(18,7)*grams[5][:9,:9]+grams[7][:9,:9] == sp.zeros(9)
# Normalized observation errors are multiplied by raw-source norm products.
# AM-GM bounds each sqrt(g_ii*g_jj) by (g_ii+g_jj)/2 exactly.
scale = [sp.Rational(int(g[x['source_row'],x['source_row']])+int(g[x['source_column'],x['source_column']]),2)
         for x in o['independent_observables']]
inv = design.inv()
row_bounds = [8*sum(abs(inv[q,k])*scale[k] for k in range(8)) for q in range(8)]
assert max(row_bounds) <= sp.Rational(356,7)
record('Full physical image Grams and static response design', rows=1503,
       density_gram_entries=8*121, old_rank=6, new_rank=8,
       determinant=str(design.det()), calibration_norm_bound=str(max(row_bounds)))

o = read('peers/FOUR/gen/RESPONSE_DISCOVERY.json')
B, N, V = mat(o['incidence_B']), mat(o['null_basis']), mat(o['phase9_V'])
assert B.rank()==5 and N.rank()==4 and B*N==sp.zeros(6,4)
NG, NV = N.T*N, N.T*V*N
assert NG==mat(o['null_Gram']) and NV==mat(o['null_V'])
positive=NV-5*NG
assert all(positive[:k,:k].det()>0 for k in range(1,5))
a=sp.Matrix([1,1,-1,1,1,1,-1,1,1])/3
b=sp.Matrix([1,1,-1,1,1,-1,1,1,-1])/3
assert B*a==B*b and (a.T*b)[0]==sp.Rational(1,3)
assert (b.T*V*b-a.T*V*a)[0]==-sp.Rational(13,135)
record('Legal current-dark source pair and positive null response', delta_V='-13/135', overlap='1/3', null_dimension=4)

L=sp.zeros(8)
for x in range(8):
    for bit in range(3): L[x,x]+=1; L[x,x^(1<<bit)]-=1
G=(sp.eye(8)+L).inv()
weights=[sp.Rational(169,675),sp.Rational(34,135),sp.Rational(112,225)]
profiles=[sp.Matrix([4,2,0,0,0,0,0,0]),sp.Matrix([3,3,0,0,0,0,0,0]),sp.Matrix([3,2,1,0,0,0,0,0])]
values=[(r.T*G*r)[0] for r in profiles]
assert values==[sp.Rational(928,105),sp.Rational(882,105),sp.Rational(770,105)]
v=sum(w*q for w,q in zip(weights,values))
assert v==sp.Rational(565492,70875)
Ei=sp.Rational(1028,45)+sp.Rational(36,1000)
Ef=sp.Rational(36*1001,1000)-35*v
lower=-sp.Rational(728,3); margin=lower-Ef
assert margin==sp.Rational(11191,20250)
assert Ef-Ei==-sp.Rational(538852,2025)
calibrated=margin-sp.Rational(24644,675)*sp.Rational(356,7)/10000
assert calibrated==sp.Rational(6502151,17718750)
record('Complete endpoint and calibration ledger', margin=str(margin), net_work=str(Ef-Ei), calibrated_margin=str(calibrated))

o=read('peers/ONE/gen/SPATIAL_FLAVOR_DISCOVERY.json')
SG={k:mat(v) for k,v in o['phase_Grams'].items()}
z=sp.Matrix([1,1,-1,-1,-1,1,1,1,1])/3
sw=[(z.T*SG[k]*z)[0] for k in ['42','33','321']]
assert sw==[sp.Rational(11,45),sp.Rational(2,9),sp.Rational(8,15)]
assert all(ev>=0 for ev in (SG['321']-2*SG['33']).eigenvals())
assert all(ev>=0 for ev in (sp.eye(9)-SG['42']-3*SG['33']).eigenvals())
assert weights[2]-2*weights[1]==-sp.Rational(4,675)
p=sp.Rational(15,17)
failure=[sp.simplify((s-p*w)/(1-p)) for s,w in zip(sw,weights)]
assert failure==[sp.Rational(1,5),0,sp.Rational(4,5)]
assert p*(sp.Rational(1028,45)-sp.Rational(148,9))==sp.Rational(96,17)
record('Spatial weights, obstruction and instrument mean ledger', weights=list(map(str,sw)), success_probability=str(p), failure_weights=list(map(str,failure)), limitation='Checks sector data and accounting, not an independently reconstructed full-flavor instrument.')

# Independently evaluate the scalar allowance formulae; this is not a proof
# of their operator hypotheses. Native interval certificates remain authority.
e0=sp.Rational(565492,2025)*sp.Rational(83,15625)**2
width=sp.Rational(72*1001,1000)+35*sp.Rational(928,105)
allowance=margin-width/1000-2*e0-sp.Rational(10080,10**6)
assert allowance==sp.Rational(575056319167,3955078125000)>0
R,W=sp.Integer(10**8),sp.Integer(10**20)
Ci,Cf=sp.Integer(409),sp.Integer(382)
di,df=Ci/R,Cf/R
battery=(Ci**2+Cf**2)/R+Cf*(3*di**2+df**2)/(1-df**2)+2*sp.Rational(22,7)*R**2/W
assert battery<sp.Rational(3761,10**6)
assert sum(F(14**k,math.factorial(k)) for k in range(21))>10**6
record('Finite timing and conservative battery scalar budgets', timing_allowance=str(allowance), battery_energy_bound=str(battery), limitation='No claim that collective hardware or a reusable restoration cycle has been supplied.')
mp.mp.dps=80
log=mp.log
thermal=18-mp.mpf(4567)/125*log(mp.mpf(7)/6)-sum(mp.mpf(str(w))*log(mp.mpf(d)) for w,d in zip(weights,[231,210,112]))+log(mp.mpf(1)/7)+3*log(mp.mpf(127)/343)+3*log(mp.mpf(9031)/16807)+log(mp.mpf(543607)/823543)
assert thermal>mp.mpf('.1045')
for excess,m in [(F(1,2),F(533,10125)),(F(13,25),F(661,20250)),(F(53,100),F(917,40500)),(F(54,100),F(128,10125))]:
    assert F(11191,20250)-excess==m
record('Thermal allowance consistency', log_allowance=mp.nstr(thermal,60), method='80-digit numerical cross-check plus exact rational margin ladder; rigorous logarithmic bounds are in retained native certificates.')

result=dict(status='PASS',checked_utc=datetime.now(timezone.utc).isoformat(),
            scope='Post-window internal lead consistency review on retained operands. No new scientific window, external verification, CR2 classification, physical calibration or reusable-work claim.',
            input_sha256=inputs,checks=checks)
(C/'host/review/LEAD_CONSISTENCY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
