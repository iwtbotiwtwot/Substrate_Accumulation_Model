from pathlib import Path
import json,hashlib
from fractions import Fraction as Q
from flint import arb,fmpq,ctx
ctx.prec=512;ctx.threads=1
root=Path(__file__).resolve().parents[1]
P=Path('/home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/01_atoms/peers/REFERENCES/attempts/002/output/NUCLEAR_RECONSTRUCTION.json')
sources=json.loads(P.read_text())['sources']
def a(q):return arb(str(q))
def box(x):return {'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq())}
def mid(x):return float(x.mid())
def ahullmin(vals):return arb(min(x.lower() for x in vals)).union(arb(min(x.upper() for x in vals)))
def ahullmax(vals):return arb(max(x.lower() for x in vals)).union(arb(max(x.upper() for x in vals)))
def flatw(n):return Q(min(n,2))+Q(max(n-2,0),4)
def exactw(n,nu):
 if not n:return a(0)
 if nu==1:return a(flatw(n))
 if n<=2:return a(n)
 if n<=4:return a(2)+a(Q(n-2,4))
 if nu==Q(1,2):return a(Q(5,2))+a(Q(n-4,9))
 d=(a(137).sqrt()+3)/6
 return a(Q(5,2))+a(n-4)/d**2
rows=[];full=[];shells={};coh=[]
for nu in [Q(1),Q(3,4),Q(1,2)]:
 # Independent fresh source-bound evaluation of the published explicit upper formula, not the historical bank.
 for Z in [2,6]:
  for g in [Q(1,10),Q(1)]:
   J=30*(4*a(2).log()-a(Q(11,4)));alpha=((1+8/a(nu)**2).sqrt()-1)/2
   M=a(0);rr=Q(2);E=a(0);out=[a(0)];rrs=[]
   for n in range(1,Z+1):
    for k in range(32):
     change=a(10*nu**3/rr**2)-a(Q(Z-n+1,1)/rr)*J+a(g)*M/((2*alpha+1)*a(rr)**(alpha+1))
     if change<0:break
     rr*=2
    else:raise RuntimeError('search failed')
    E+=change;out.append(E);rrs.append(str(rr));M+=a(2*rr)**alpha;rr*=4
   shells[(str(nu),Z,str(g))]=out
   full.append({'kind':'spherical_upper_formula','nu':str(nu),'Z':Z,'g':str(g),'radii':rrs,'energy_boxes':[box(x)for x in out]})
 for ss in sources:
  Z=2 if ss['source'].startswith('He') else 6
  for g in [Q(1,10),Q(1)]:
   qrows=ss['q_roster'];sep=min(Q(t['I'])+Q(Z*Z,2)+g*Q(t['q'],2)for t in qrows)
   cache=[]
   for n in range(Z+1):
    wf=a(flatw(n));w=exactw(n,nu);terms=[]
    for t in qrows:
     q=t['q'];A=a(g)*a(q).sqrt();C=a(Z);core=a(Q(t['I'])+Q(Z*Z,2)+g*Q(q,2))
     old=-w*(C+A)**2/(4*a(nu)**3)
     floor=-n*(C+A)
     flat=-(C*wf.sqrt()+A*a(nu)*a(n).sqrt()/(a(nu)+1))**2/(4*a(nu)**3)
     new=-(C*w.sqrt()+A*a(nu)*a(n).sqrt()/(a(nu)+1))**2/(4*a(nu)**3)
     b0=ahullmax([old,floor]);b1=ahullmax([flat,old,floor]);b2=ahullmax([new,old,floor])
     terms.append({'q':q,'I':t['I'],'core':core,'old':core+b0,'prior_max':core+b1,'new':core+b2,'newbranch':new,'floor':floor,'oldbranch':old,'flatbranch':flat})
    L0=ahullmin([t['old']for t in terms]);L1=ahullmin([t['prior_max']for t in terms]);L2=ahullmin([t['new']for t in terms]);U=a(sep)+shells[(str(nu),Z,str(g))][n]
    qm=[t['q']for t in terms if not (t['new']>L2)]
    del0=L2-L0;del1=L2-L1
    row={'nu':str(nu),'source':ss['source'],'g':str(g),'N':n,'weight':box(w),'separated':str(sep),'old_joint_lower':box(L0),'old_directional_max_joint_lower':box(L1),'upgraded_joint_lower':box(L2),'new_minus_original':box(del0),'exact_weight_increment_over_previous_max':box(del1),'candidate_minimizing_q':qm,'spherical_upper':box(U),'upper_custody':'published explicit shell formula, freshly evaluated; original retained CI upper portfolio absent locally at nu1'}
    cache.append((L0,L1,L2,U,row))
    if n:
     Il=cache[n-1][2]-U;row['fresh_spherical_ionization_lower']={'lower':str(cache[n-1][2].lower().fmpq()-U.upper().fmpq()),'upper':str(cache[n-1][2].upper().fmpq()-U.lower().fmpq())};row['fresh_spherical_ionization_positive']=Il>0
     row['lower_improvement_affects_next_ionization']=n<Z and del0>a(Q(1,10**80))
     rows.append(row)
    full.append({'kind':'full_pointwise_lower_table','nu':str(nu),'source':ss['source'],'g':str(g),'N':n,'terms':[{k:box(v)if isinstance(v,arb)else v for k,v in t.items()}for t in terms]})
   coh.append({'nu':str(nu),'source':ss['source'],'g':str(g),'lower_changed_inventory':[i for i,t in enumerate(cache)if t[2]-t[0]>a(Q(1,10**80))]})
summary={'populated_accounts':len(rows),'strict_improved_vs_original_geometric':sum(Q(r['new_minus_original']['lower'])>Q(1,10**80)for r in rows),'strict_improved_by_exact_weight_vs_previous_three_way_max':sum(Q(r['exact_weight_increment_over_previous_max']['lower'])>Q(1,10**80)for r in rows),'fresh_spherical_positive_ionization':sum(r['fresh_spherical_ionization_positive']for r in rows),'by_nu':{str(nu):{'improved_vs_original':sum(r['nu']==str(nu)and Q(r['new_minus_original']['lower'])>Q(1,10**80)for r in rows),'spherical_positive_ionization':sum(r['nu']==str(nu)and r['fresh_spherical_ionization_positive']for r in rows)}for nu in [1,Q(3,4),Q(1,2)]}}
out={'precision_bits':512,'source_path':str(P),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'summary':summary,'cohorts':coh,'rows':rows,'full_pointwise':full}
(root/'gen/PANEL.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2));print('changed',coh)
