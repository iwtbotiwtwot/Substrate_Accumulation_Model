#!/usr/bin/env python3
"""Independent arithmetic checks only; not native-source or cosmological runs."""
import math
from pathlib import Path
c=299792458.; G=6.67430e-11; hb=1.054571817e-34
kb=1.380649e-23; mp=1.67262192595e-27
Mpc=3.085677581491367e22; T=2.7255; zeta3=1.202056903159594
A=1/(12*math.pi); chi=8*A/3
om=12*A; ob=2*A*(1-chi); oc=om-ob; ol=1-om
eta=7*A**6/4; eff=om-2*A*(chi+3*chi**2)
ng=2*zeta3/math.pi**2*(kb*T/(hb*c))**3
rho=3*(1e5/Mpc)**2/(8*math.pi*G); K=rho/(mp*ng)
wb=eta/K; H0=100*math.sqrt(wb/ob)
assert math.isclose(om,1/math.pi)
assert math.isclose(126/(4*18),7/4)
assert 162/27 == 6
assert math.isclose(om,ob+oc) and math.isclose(om+ol,1)
assert math.isclose(eff,0.3137609155690572)
assert math.isclose(H0,67.2504,abs_tol=.0001)
print('Inventory',dict(A0=A,chi=chi,Om=om,Ob=ob,Oc=oc,Ol=ol,fb=ob/om,eta=eta,Om_eff=eff))
print('Cascade',dict(ngamma_cm3=ng/1e6,K=K,wb=wb,H0=H0,h2=wb/ob))
print('Sensitivity',dict(floor=.5*(5+chi/(1-chi)),temperature_only_sigma=H0*1.5*.00057/T))
print('Planck rounded residuals', (H0-67.4)/.5, (om-.315)/.007)
print('Grammar tuples',17*13*3*9)
for N in [1,2,10,100,1.05e77]:
 ratio=2/(1+math.sqrt(1-1/N))
 assert 1 <= ratio <= 2
 assert math.isclose(ratio,1+ratio**2/(4*N))
 print('One entry',N,ratio)
for N,j in [(10,1),(10,4),(10,10),(100,20)]:
 s=math.sqrt(1-j/N)
 ratio=2*j/(1+s)
 assert math.isclose(ratio,j+j*j/(N*(1+s)**2))
for N in [2,10,100]:
 q=1/N; exact=2/(1+math.sqrt(1-q))
 for m in range(6):
  partial=sum(math.comb(2*j,j)/(j+1)/4**j*q**j for j in range(m+1))
  assert -1e-14 <= exact-partial <= q**(m+1)/(1-q)+1e-14
# Finite geometric mean and total variation versus exact tail mass.
for q in [.1,.5,.9]:
 for k in [0,1,5,20]:
  Z=sum(q**n for n in range(k+1))
  mean=sum(n*q**n for n in range(k+1))/Z
  formula=q/(1-q)-(k+1)*q**(k+1)/(1-q**(k+1))
  assert math.isclose(mean,formula,abs_tol=1e-12)
  tv=(sum(abs(q**n/Z-(1-q)*q**n) for n in range(k+1))+q**(k+1))/2
  assert math.isclose(tv,q**(k+1),abs_tol=1e-12)
for Gm,Hm in [((252.754,-785.399,17867.308),(7.753,-6.015,445.393)),((110.500,-516.332,7083.046),(4.095,-11.510,-24.842))]:
 a,b,d=Gm; x,y,z=Hm
 assert a>0 and a*d-b*b>0
 assert not math.isclose(x/a,z/d,rel_tol=.01)
 print('Hessian determinants',a*d-b*b,x*z-y*y)
print('PASS: analytic identities and printed new numerical examples checked.')
# Expanded worked examples, all illustrative rather than empirical.
E=[2-math.sqrt(3),math.sqrt(3)-math.sqrt(2),math.sqrt(2)-1]
assert math.isclose(sum(E),1)
print('Finite 4 -> 1 step energies',E,'fixed-initial-bath entropy/kB',1/.25-3)
pin=[8/15,4/15,2/15,1/15]
pout=[sum(pin[n]*math.comb(n,m)*.5**n for n in range(m,4)) for m in range(4)]
assert all(math.isclose(x,y/120) for x,y in zip(pout,[85,27,7,1]))
mean=sum(n*p for n,p in enumerate(pin)); var=sum(n*n*p for n,p in enumerate(pin))-mean**2
mo=sum(n*p for n,p in enumerate(pout)); vo=sum(n*n*p for n,p in enumerate(pout))-mo**2
assert math.isclose(mean,11/15) and math.isclose(var,194/225)
assert math.isclose(mo,11/30) and math.isclose(vo,359/900)
assert math.isclose(vo/mo,359/330)
print('Finite counts',dict(input_mean=mean,input_var=var,output=pout,output_mean=mo,output_var=vo,Fano=vo/mo))
r=.01; D=.5*((1+r)*math.log1p(r)+(1-r)*math.log1p(-r))
assert abs(D-(r*r/2+r**4/12)) < 1e-12
for lam in [.1,.5,.9]:
 eig=[(1+r)/2,(1-r)/2]
 Dout=sum(lam*v*math.log((lam*v)/(lam*.5)) for v in eig)
 assert math.isclose(Dout,lam*D,abs_tol=1e-14)
nb=eta*ng; rhob=mp*nb
assert math.isclose(rhob/(3*(H0*1e3/Mpc)**2/(8*math.pi*G)),ob)
print('Physical densities',dict(n_b_per_m3=nb,rho_b_kg_m3=rhob,rho_crit100=rho,H100_per_s=1e5/Mpc))
for p in [5,6,7]:
 for w in [1,7/4,2]:
  er=w*A**p
  hv=H0*math.sqrt(er/eta)
  print('Nine candidates',dict(power=p,weight=w,eta=er,H0=hv))
for corr in [.8,-.8,0]:
 sig=.5*math.sqrt(.01**2+.01**2-2*corr*.01**2)
 print('Illustrative covariance fractional sigma_H',corr,sig)
assert math.isclose(2/(1+.8),10/9) and math.isclose(2/(1-.8),10)
Hsec=H0*1e3/Mpc
age=2/(3*Hsec*math.sqrt(ol))*math.asinh(math.sqrt(ol/om))
zacc=(2*ol/om)**(1/3)-1
print('Conditional flat matter-Lambda diagnostics',dict(age_Gyr=age/(365.25*86400*1e9),zacc=zacc,Hinf=H0*math.sqrt(ol)))
# Simpson check of age after a=u^2 removes endpoint square-root behavior.
steps=10000
f=lambda u: 2*u*u/math.sqrt(om+ol*u**6) if u else 0.
integral=(f(0)+f(1)+sum((4 if i%2 else 2)*f(i/steps) for i in range(1,steps)))/(3*steps)/Hsec
assert math.isclose(integral,age,rel_tol=1e-11)
print('PASS: expanded finite-ledger, channel, grammar, covariance, and background examples.')
