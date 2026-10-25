#!/usr/bin/env python3
"""Independent stdlib checks of printed analytical examples, not native SAM runs."""
from fractions import Fraction as F
from math import pi, sqrt, isclose, exp
import json

checks = {}
def check(name, condition, values=None):
    assert condition, name
    checks[name] = {'passed': True, 'values': values}

R,theta,L,V,d = 12,18,162,27,3
ar,ai=F(theta*d,R*R),F(R,L-V)
check('count_identities', ar==F(3,8) and ai==F(4,45) and L-V==R*R-d*d,
      {'real':str(ar),'damping':str(ai),'quality_factor':str(ar/(2*ai))})
wr,wi=0.37367168,0.08896232
check('quality_factor',ar/(2*ai)==F(135,64),
      {'real_residual_percent':100*(float(ar)/wr-1),
       'damping_residual_percent':100*(float(ai)/wi-1),
       'GR_quality_factor':wr/(2*wi), 'mass_ratio':float(ar)/wr})
check('area_bound',isclose(1-sqrt(2)/2,1-1/sqrt(2)),
      {'equal_mass_bound':1-1/sqrt(2)})
# Numerical midpoint integration independently checks the analytic pulse integral.
B,T,N=2.0,3.0,100000
pulse_integral=sum((B*pi/T)**2*__import__('math').sin(2*pi*(i+.5)/N)**2*T/N for i in range(N))
pulse_exact=B*B*pi*pi/(2*T)
check('finite_pulse_energy',isclose(pulse_integral,pulse_exact,rel_tol=1e-10),
      {'quadrature':pulse_integral,'exact':pulse_exact})
f=1-1/pi
rows=[{'H0':h,'native_limit':h*sqrt(f),'conditional_fit_limit':h*f**1.5}
      for h in (67.2504,68.76,73.04)]
check('conditional_fate_numbers',isclose(f**1.5,.5628342188801616),rows)
road=lambda z:(1-(1+z)**-3)/pi
check('road_domain',road(0)==0 and 0<road(1)<road(10)<1/pi,
      {'road_z1':road(1),'survival_z1':1-road(1),'q_shift':-6/pi})
# Check readout differentiation for a simple constant-H distance D=z in c/H units.
z=.7;h=1e-6
f_of=lambda z:1-road(z)
Dread=lambda z:z/f_of(z)
deriv=(Dread(z+h)-Dread(z-h))/(2*h)
fprime=-3/pi/(1+z)**4
inferred=f_of(z)**2/(f_of(z)-z*fprime)
check('distance_derivative',isclose(1/deriv,inferred,rel_tol=1e-8),
      {'finite_difference_inferred_H':1/deriv,'formula':inferred})
# A constant distance rescaling cancels in a logarithmic expansion rate.
t=.5;H=.8;scale=.7
D=lambda t:exp(H*t)/scale
lograte=(D(t+h)-D(t-h))/(2*h)/D(t)
check('constant_road_fractional_rate',isclose(lograte,H,rel_tol=1e-8),
      {'logarithmic_rate':lograte,'H':H,'different_fit_coefficient':scale*H})
Mform,E=10,2;states=[{'E':E,'M':Mform+E}]
ins,outs=[3,0,0],[1,3,1]
for incoming,outgoing in zip(ins,outs):
    assert 0<=outgoing<=E+incoming
    E+=incoming-outgoing
    states.append({'E':E,'M':Mform+E,'area_ratio':((Mform+E)/Mform)**2})
check('home_recurrence', [s['M'] for s in states]==[12,14,11,10] and sum(outs)==2+sum(ins),states)
check('handoff',isclose(12/(4*pi*3),1/pi),{'A0':1/(12*pi),'RA0':1/pi})


# Boundary oscillator: scattering loss equals explicit bath payment.
for omega in (0.1,0.4,1.0):
    ms,bs,ks=2.0,0.7,0.8
    Z=ks-ms*omega**2-1j*bs*omega
    RR=(1j*omega+Z)/(1j*omega-Z)
    absorb=4*bs*omega**2/((ks-ms*omega**2)**2+(1+bs)**2*omega**2)
    check('oscillator_flux_'+str(omega),
          isclose(1-abs(RR)**2,absorb,abs_tol=1e-12) and
          isclose(bs*abs(1+RR)**2,absorb,abs_tol=1e-12))
ms,bs=45/4,1
ks=ms*((3/8)**2+(4/45)**2)
pole=complex(sqrt(4*ms*ks-(1+bs)**2),-(1+bs))/(2*ms)
check('inverse_designed_pole',isclose(pole.real,3/8) and isclose(-pole.imag,4/45),
      {'mass':ms,'damping':bs,'spring':ks,'pole_real':pole.real,'pole_imag':pole.imag})
overlap=2*sqrt(wi*float(ai))/sqrt((wi+float(ai))**2+(float(ar)-wr)**2)
check('ideal_template_overlap',isclose(overlap,.9999720250822158),
      {'overlap':overlap,'mismatch':1-overlap})
check('quadrupole_angular_integral',isclose(2*pi*(2-4/3+2/5),32*pi/15))
# Formation transfer and its pressure-work continuity relation.
lam,beta=0.5,0.25
u=lambda a:a**(-3-lam)
home=lambda a:a**-3*(1-beta)*(1-a**-lam)
rad=lambda a:a**-4*beta*lam*(a**(1-lam)-1)/(1-lam)
a=4.0
check('formation_densities',isclose(u(a),1/128) and isclose(home(a),3/512) and isclose(rad(a),1/1024),
      {'unbound':u(a),'home':home(a),'radiation':rad(a),'total':u(a)+home(a)+rad(a)})
dN=1e-5
derivative=lambda fn:(fn(a*exp(dN))-fn(a*exp(-dN)))/(2*dN)
check('formation_continuity',abs(derivative(u)+derivative(home)+derivative(rad)+3*(u(a)+home(a))+4*rad(a))<1e-10)
# Interacting vacuum analytic solution obeys both exchange equations.
xi=.2;rx0=1-1/pi;rm0=1/pi
rx=lambda a:rx0*a**(-3*xi)
rm=lambda a:rm0*a**-3+xi*rx0/(1-xi)*(a**(-3*xi)-a**-3)
check('interacting_vacuum_continuity',abs(derivative(rx)+3*xi*rx(a))<1e-10 and abs(derivative(rm)+3*rm(a)-3*xi*rx(a))<1e-10,
      {'xi':xi,'future_power':2/(3*xi),'event_horizon_exists':2/(3*xi)>1})
print(json.dumps({'description':__doc__,'checks':checks},indent=2))
