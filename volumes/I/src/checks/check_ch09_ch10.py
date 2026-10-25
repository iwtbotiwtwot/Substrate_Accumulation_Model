"""Independent analytic/arithmetic checks only. No SPARC or CMB empirical rerun."""
import math
import json

x = 10/math.pi
f = x/(1+x)
n, scatter = 173, .38
se_log = math.sqrt(math.pi/2)*scatter/math.sqrt(n)
se_f = math.log(10)*x/(1+x)**2*se_log
G, r, vb = 4.30091e-6, 20., 100.
mb = r*vb**2/G
# Odd-sample median inversion is an algebraic identity, checked synthetically.
sample = [.2, .5, 1., 2., 3., 4., 9.]
med = lambda a: sorted(a)[len(a)//2]
assert math.isclose(med([x/a for a in sample]), x/med(sample))
# Uniform finite sphere: 4 pi G rho r^2/3 with rho=3 Omega H^2/(8 pi G).
omega, h0 = .27, 67.25/1000 # H0 in km/s/kpc
uniform_v = h0*r*math.sqrt(omega/2)
# Verify derivatives of support ratio and support fraction against finite differences.
vobs, D, gas, ups = 200., 10000., 3000., .5
B = lambda u: gas+u*D
X = lambda u: vobs**2/B(u)-1
F = lambda u: 1-B(u)/vobs**2
step=1e-5
assert math.isclose((X(ups+step)-X(ups-step))/(2*step), -vobs**2*D/B(ups)**2, rel_tol=1e-8)
assert math.isclose((F(ups+step)-F(ups-step))/(2*step), -D/vobs**2, rel_tol=1e-8)
# Check reported rounded angle/geometric values are mutually approximate, not exact.
angle = 143.299/13532.742
out = {
 'scope':'Analytic and illustrative arithmetic checks; no historical empirical replay',
 'X_infinity':x, 'f_infinity':f, 'median_log_SE_dex':se_log,
 'linear_fractional_SE':math.log(10)*se_log,
 'upper_fractional_SE':10**se_log-1, 'support_fraction_SE':se_f,
 'fraction_residual_in_approx_SE':abs(f-.760699)/se_f,
 'scatter_multiplicative_factor':10**scatter,
 'illustrative_baryonic_equivalent_mass_solar':mb,
 'illustrative_halo_mass_solar':x*mb, 'illustrative_speed_km_s':vb*math.sqrt(1+x),
 'uniform_component_speed_km_s':uniform_v,
 'native_100theta_from_rounded_distances':100*angle,
 'native_lA_from_rounded_distances':math.pi/angle,
 'ruler_difference_Mpc':147.769-144.806,
 'second_peak_fractional_difference':535/537.5-1,
 'monte_carlo_plus_one_p':1/1001,
 'synthetic_median_identity':'PASS', 'analytic_derivatives':'PASS'
}

# Additional illustrative checks for expanded acoustic, opacity and radial examples.
rho_corr = .8
assert math.isclose(2/(1+rho_corr), 10/9)
assert math.isclose(2/(1-rho_corr), 10)
# Toy opacity derivative and visibility maximum, in units n_e0 sigma c = H_m = 1.
a_peak = (1/2)**(2/3)
tau_peak = (2/3)*a_peak**(-1.5)
assert math.isclose(tau_peak,4/3)
# Spherical toy profile in units b=M_b=G=1.
mhalo = lambda r: x*r**3/(r+1)**3
density = lambda r: 3*x/(4*math.pi*(r+1)**4)
for rr in (.1,.5,1,2,9):
 h=1e-5*rr
 numerical=(mhalo(rr+h)-mhalo(rr-h))/(2*h)/(4*math.pi*rr**2)
 assert math.isclose(numerical,density(rr),rel_tol=1e-8)
rhalf=1/(2**(1/3)-1)
assert math.isclose(mhalo(rhalf), x/2)
out.update({'additional_checks':'PASS', 'toy_visibility_peak_tau':tau_peak,
 'covariance_same_sign_chi2':2/(1+rho_corr),'covariance_opposite_sign_chi2':2/(1-rho_corr),
 'toy_support_fraction_at_b':x/(2+x),'toy_halo_half_mass_radius_over_b':rhalf,
 'individual_68_interval':[10**(-.38),10**.38],
 'individual_95_interval':[10**(-1.96*.38),10**(1.96*.38)],
 'median_SE_dex_n100':math.sqrt(math.pi/2)*.38/10})
print(json.dumps(out,indent=2))
