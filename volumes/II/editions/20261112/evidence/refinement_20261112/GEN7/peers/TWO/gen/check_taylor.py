from pathlib import Path
import sympy as sp,json
z,r,c=sp.symbols('z r c',real=True)
a=1-2*z*r*c+2*z*z*r*r;b=-z*r
norm2=sp.expand(a*a+b*b+2*a*b*c)
h=sp.series(norm2**sp.Rational(-1,2),z,0,3).removeO()
n=sp.series(a*h,z,0,3).removeO();e=sp.series(b*h,z,0,3).removeO()
pn=1+z*r*c+z*z*r*r*(7*c*c-1)/2;pe=-z*r-3*z*z*r*r*c
res=[sp.simplify(n-pn),sp.simplify(e-pe)]
unit=sp.simplify(2*(r*r*((7*c*c-1)/2-3*c*c))+r*r*(1-c*c))
assert res==[0,0]and unit==0
out={'status':'PASS','n_coefficient':str(n),'e_coefficient':str(e),'Taylor_residuals':list(map(str,res)),'unit_norm_second_order_residual':str(unit),'method':'independent symbolic expansion of the original normalized direction; not native'}
Path('gen/TAYLOR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
