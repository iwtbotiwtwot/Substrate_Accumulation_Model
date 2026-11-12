"""Fresh directed compact-support Rice integral; no subtraction at h=0."""
from pathlib import Path
import json,time
from flint import arb,acb,ctx
ctx.prec=192
O=Path(__file__).resolve().parent/'results'
pi=arb.pi();lam=arb(3)/4;nu=lam.sqrt()/pi
def first(h,analytic):
 # Factor det=h² d and S=h [[s,c],[c,s]] before evaluation.
 common=(h-4)*(3*h**3-12*h*h+64)
 det=-3*common/1024
 s=3*(3*h**3-24*h*h+84*h-128)/(4*common)
 c=3*(9*h**4-84*h**3+288*h*h-480*h+512)/(32*common)
 rho=c/s
 return s/(acb(pi)**2*det.sqrt(analytic=analytic))*((1-rho*rho).sqrt(analytic=analytic)+rho*rho.asin(analytic=analytic))
def second(h,analytic):
 z=4-h;r=z**3/32;rp=-3*z*z/32;rpp=3*z/16
 det=1-r*r;s=acb(lam)-rp*rp/det;c=-rpp-r*rp*rp/det;rho=c/s
 return s/(acb(pi)**2*det.sqrt(analytic=analytic))*((1-rho*rho).sqrt(analytic=analytic)+rho*rho.asin(analytic=analytic))
def ratio(x):
 a,b=x.lower().fmpq(),x.upper().fmpq();return dict(lower=str(a),upper=str(b),display=str(x))
started=time.monotonic();parts=[]
for a,b,fn in [(0,1,first),(1,2,first),(2,3,second),(3,4,second)]:
 J=acb.integral(lambda x,analytic:fn(x,analytic)-acb(nu*nu),a,b,rel_tol=arb(2)**-150,abs_tol=arb(2)**-150,eval_limit=100000,depth_limit=30)
 K=acb.integral(lambda x,analytic:x*(fn(x,analytic)-acb(nu*nu)),a,b,rel_tol=arb(2)**-150,abs_tol=arb(2)**-150,eval_limit=100000,depth_limit=30)
 assert J.is_finite() and K.is_finite() and J.imag.contains(0) and K.imag.contains(0)
 parts.append((J.real,K.real));print(a,b,str(J.real),str(K.real),flush=True)
J=sum(j for j,k in parts);K=sum(k for j,k in parts);slope=nu+2*J;intercept=-2*K
result=dict(precision_bits=192,method='HOST_DIRECTED_ARB_ACB_ANALYTIC_INTEGRATION',source='Original normalized held same-shell Gaussian low field tau1, level0',mean_rate=ratio(nu),diagonal=ratio(3/(8*pi*pi)+arb(3).sqrt()/(48*pi)),slope=ratio(slope),intercept=ratio(intercept),variance16=ratio(16*slope+intercept),parts=[dict(J=ratio(j),K=ratio(k))for j,k in parts],seconds=time.monotonic()-started,scope='Held fixed Gaussian crossing count, not endogenous/Palm source process. Analytic branch flags passed through sqrt/asin; cubic det and covariance factors remove cancellation at0; covariance vanishes for lag≥4 exactly.')
(O/'RICE_ARB.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['slope','intercept','variance16','seconds']},indent=2),flush=True)
