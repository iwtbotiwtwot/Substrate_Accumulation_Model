from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,hashlib,itertools
import numpy as np
from flint import arb,ctx
ctx.prec=256
P=Path.cwd();S=Path('/home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6')
files=[S/'PHYSICAL_IMAGES.json',S/'MOMENTS.json',S/'BOUNDS.json'];imgs,moms,bounds=[json.loads(p.read_text()) for p in files];G=[[F(x) for x in row] for row in moms['G']]
res={'source_hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'sectors':{}}
weights=list(map(F,bounds['weights']));slist=[];pclist=[]
for lam in ['42','33','321']:
 sec=moms['sectors'][lam];rho=sec['source_density'];n=len(rho);alpha=F(1,40 if lam=='321' else 56);s0=sum(x*x for x in rho[0]);assert all(sum(x*x for x in r)==s0 for r in rho)
 # Novel observable D2=sum_R,x rho_R,x^2. Retained source/hop images are locked inputs.
 W=defaultdict(lambda:[[0]*n for _ in range(n)])
 for im in imgs[lam]['internal']:
  d2=sum(x*x for x in im['density'])
  for i,si in im['entries']:
   for j,sj in im['entries']:
    dr=[F(a-b) for a,b in zip(rho[i],rho[j])];gdr=[sum(a*b for a,b in zip(row,dr)) for row in G];ex=sum(x*x for x in gdr)/2
    W[ex][i][j]+=si*sj*d2
 # cell image uniquely identifies source; density has five central+one remote.
 Wcell=[[0]*n for _ in range(n)]
 for im in imgs[lam]['cell']:
  i=im['source'];Wcell[i][i]+=sum(x*x for x in im['central_density'])+1
 # Each sector is translation/orientation symmetric. Bound full W with exact class-wise row sums and original exponential ceilings.
 upper={F(0):F(1),F(2332,11025):F(1,1000),F(17,225):F(1,10),F(34,225):F(1,100)}
 diag=[W[F(0)][i][i] for i in range(n)];assert len(set(diag))==1
 off=max(sum(abs(A[i][j])*upper[e] for e,A in W.items() for j in range(n) if j!=i) for i in range(n))
 wup=4*(F(diag[0])+off)+F(1,1000000)*max(Wcell[i][i] for i in range(n))
 vmin=F(bounds['benchmark']['V_lowers'][['42','33','321'].index(lam)])
 smax=(s0+alpha*alpha*wup)/(1+alpha*alpha*vmin)
 # This ratio bound valid through W<=wup I, V>=vminI and s0+a²wup>0.
 pcmax=alpha*alpha*F(36,1000000)/(1+alpha*alpha*vmin)
 smin=F(0) # no lower needed for generic norm error
 slist.append(smax);pclist.append(pcmax)
 res['sectors'][lam]={'dimension':n,'alpha':str(alpha),'base_density_square':s0,'density_square_internal_exponent_coefficients':{str(e):[[str(x) for x in row] for row in A] for e,A in W.items()},'cell_density_square_moment':[[str(x) for x in row] for row in Wcell],'row_sum_offdiag_upper':str(off),'W_upper':str(wup),'V_lower_locked':str(vmin),'dressed_D2_upper':str(smax),'dressed_D2_upper_decimal':float(smax),'cell_probability_upper':str(pcmax),'cell_probability_upper_decimal':float(pcmax)}
 print(lam,'Wclasses',[(str(e),A[0][0],sum(x!=0 for row in A for x in row)) for e,A in W.items()],'D2up',float(smax),'cell',float(pcmax),flush=True)
sbar=sum(w*s for w,s in zip(weights,slist));pcbar=sum(w*p for w,p in zip(weights,pclist));margin=F(bounds['benchmark']['proper_margin']);coef=18+sbar
res.update(weighted_dressed_D2_upper=str(sbar),weighted_dressed_D2_upper_decimal=float(sbar),generic_margin_lower=str(margin),kernel_error_coefficient=str(coef),kernel_error_coefficient_decimal=float(coef),sufficient_delta=str(margin/coef),sufficient_delta_decimal=float(margin/coef),uniform_positive_slope_lower=str(F(5,4)*(1-pcbar)),uniform_cell_probability_upper=str(pcbar),old_target_D2='11144/675',old_target_D2_decimal=float(F(11144,675)))
(P/'results/DRESSED_DENSITY.json').write_text(json.dumps(res,indent=2)+'\n')
print('weighted',float(sbar),'coef',float(coef),'delta',float(margin/coef),'pcbar',float(pcbar),flush=True)
