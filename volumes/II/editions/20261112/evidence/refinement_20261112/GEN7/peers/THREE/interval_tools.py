from flint import arb,arb_mat,ctx
from fractions import Fraction
ctx.prec=384

def aa(v):
    if isinstance(v,dict):
        if 're'in v:return aa(v['re'])
        if 'entries'in v:return aa(v['entries'][0][0])
        return arb(str(v['lower'])).union(arb(str(v['upper'])))
    return arb(str(v))
def arr(m):return [[aa(v) for v in row] for row in m['entries']]
def upper(x):return arb(str(x.upper().fmpq()))
def sup(x):return upper(abs(x))
def dot(x,y):return sum((a*b for a,b in zip(x,y)),arb(0))
def mm(A,B):return [[dot(A[i],[r[j] for r in B]) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(r) for r in zip(*A)]
def solve(A,B):return [list(r) for r in arb_mat(A).solve(arb_mat(B)).tolist()]
def wi(x):return {'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq())}
def wm(A,rb=None,cb=None,hermitian=False):return {'entries':[[wi(x) if isinstance(x,arb) else x for x in r] for r in A],'row_basis':rb or [str(i) for i in range(len(A))],'column_basis':cb or [str(i) for i in range(len(A[0]))],'structure':'HERMITIAN' if hermitian else 'GENERAL'}
def mid(x):return arb(str(x.mid().fmpq()))
def fl(x):return float(x.mid())
