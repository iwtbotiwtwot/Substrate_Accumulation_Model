# TRANSFER derivation: C4–C6

The signed trial, actual-source preimage, finite polar transfer, and both
certified margins rebuild exactly. C6 uses C3 as a conditional input. Numerical
evidence is in `attempts/001/output/`; the arguments below supply the finite
linear-algebra, infinite-cell, and full-Fock steps that enumeration alone does
not supply. This is I1 work: separate derivation and code within the same
inherited model, without external-model or human replay.

## 1. Fixed definitions and coordinate convention

Sites of the internal cube are the three-bit words 0 through 7, with edges
`x -> x xor d`, `d in {1,2,4}`. A local species word orders modes as
`2*x+spin`, spin 0 up and spin 1 down; proton modes precede neutron modes.
The four CAR populations are `(2,1,2,1)`. Each species therefore has
`choose(8,2)*8=224` determinants and the one-cell parent has 50,176. Hopping
always acts in this full parent. Neither the physical 125 nor physical 600 trial space is used
as the operator-action parent.

Let `A` denote the sum of all signed, flavor-preserving internal adjacency
operators. The physical internal kinetic term is `36*tau I - 2*tau A`.
The replay applies annihilation and creation successively to an occupied
32-bit word, with sign equal to the parity of the occupied modes below each
operator. This reconstructs the CAR matrix entries directly.

Set `omega=I+L_Q3`, `G=omega^-1`. Exact Gaussian elimination gives

```
G[x,y] = [36,13,8,6][HammingDistance(x,y)] / 105.
V(D)   = sum_(x,y) rho_D(x) G[x,y] rho_D(y).
```

Every diagonal self term and both orders of every mixed term occur. Exact
enumeration gives 1,652 distinct density profiles, maximum `928/105` with
multiplicity 24, and the next level `882/105`. All 24 maximum states are the
legal adjacent 4+2 determinants `D_xy`: four flavors at x, the two up flavors
at y, with y adjacent to x. `parent.json` retains the complete spectrum count
and all maximum states.

## 2. Complete field expectation and the common energy zero

For a matter configuration D in all cells, put
`f_D=-g*(direct_sum_cells G)*rho_D`. Its coherent field state is `W(f_D)|0>`.
The density-conditioned direct sum of these Weyl operators is unitary on
the full matter/Fock parent. No photon truncation is involved. For fixed six
particles, `||rho_D||_2<=6`, while `1<=omega<=7`, so both the displacement
norm and its field-energy norm are uniformly finite. Every finite linear
combination used here is in the common Hamiltonian form domain. This also
gives the ordinary fixed-particle form construction of the interaction:
the linear field term is relatively form bounded with arbitrarily small
field coefficient and a finite fixed-particle remainder.

The field and interaction expectations on D are respectively `+g² V(D)`
and `-2g² V(D)`. Thus their sum is `-g² V(D)`, with the normal-ordered vacuum
zero unchanged. A matter hop D to E has coherent overlap

```
exp(-g² ||G*(rho_D-rho_E)||² / 2).
```

For an internal edge, the density change is one adjacent delta difference.
The exact reconstructed G² matrix gives

```
(G²[0,0]+G²[1,1]-2G²[0,1])/2 = 583/11025.
```

All six particles are initially localized in a single cell. Each external
cell Laplacian has diagonal 6, and every offdiagonal cell hop leaves the
one-cell trial subspace. The complete external expectation is consequently
`36*t_cell`, not zero. For any one-cell matter vector u, the full-Fock
expectation pullback is exactly

```
K_g = 36*(tau+t_cell) I - 2*tau*r*A - g²*V,
r   = exp(-583*g²/11025).
```

This is an expectation identity for a specified Weyl-dressed family. It is
not an operator equality replacing H, and the later norm bound is a bound
on this finite matter operator K_g, never on the unbounded full-Fock H.
No boundary condition in the external cells is needed: the same compactly
supported matter trial belongs to the infinite-cell Hilbert space. The
breakup comparison remains conditional on C3; no full essential-spectrum
or fiber-HVZ conclusion is made here.

## 3. Signed hopping trial (C4)

Write `c=D_01+D_10` and `chi=c/sqrt(2)`. Build `A*c` in the full parent and
split it by potential. The only resulting V105 levels are 882, 842, and
770. In the ordered columns

```
c, P882*A*c, P842*A*c, P770*A*c
```

the replay obtains the exact Gram and adjacency forms

```
Gram = diag(2,8,8,16),
Aform = [[0,8,8,16], [8,0,0,0], [8,0,0,0], [16,0,0,0]].
```

The first-image vectors have cube parity opposite to c. Thus no internal
hop joins any two first-image vectors. All full physical hopping images are
retained in `hopping.json`; compression occurs only after those images are
formed.

Take

```
phi = chi + (1/9)P882*A*chi + (3/50)P842*A*chi + (1/30)P770*A*chi.
```

The 28-determinant trial has

```
||phi||²                 = 54304/50625,
<phi,V phi>             = 619078/65625,
<V>_(phi/||phi||)        = 8357553/950320,
2 <A>_(phi/||phi||)      = 24075/6788.
```

Consequently the complete normalized energy is

```
36*(tau+t_cell) - (8357553/950320)*g²
               - (24075/6788)*tau*exp(-583*g²/11025).
```

The raw replay columns omit `1/sqrt(2)` so all their quadratic numerators
and norms are doubled together; the reported normalized values include
the correct division. A registered negative-edge mutation changes
`<A>` from `24075/13576` to `9225/6788`. Omitting trial normalization instead
substitutes `619078/65625` for `8357553/950320`. Both errors are detected
arithmetically, with the actual edge and states retained in `controls.json`.

## 4. Actual 600-dimensional source and its raw Pauli metric (C5)

Use normalized Walsh orbitals
`w_a(x)=(-1)^popcount(a&x)/sqrt(8)`, a=0,...,4. For species p and n, the
raw source column `(a,b,i,d)` is the product of the exterior states

```
(w0_up wedge wa_down wedge delta_i_up)_p
    tensor
(w0_up wedge wb_down wedge delta_(i xor d)_up)_n.
```

This is the replacement physical receiver's five down-core modes per
species and all 24 oriented adjacent placements. In particular it is not
the earlier rank-deficient literal pod map. The source definition is tied
to the frozen window1 receiver and the original pod Pauli-gluing definition
listed in `SOURCE_MANIFEST.json`.

The inner product of the two up-particle wedges is
`Q[i,j]=delta[i,j]-1/8`. Orthogonality of the down Walsh orbitals therefore
gives the full raw source metric

```
M = I25 tensor G00,
G00[(i,d),(j,e)] = Q[i,j] Q[i xor d,j xor e].
```

The replay rebuilds all entries and retains an exact positive LDL
factorization witness for G00. Thus M is positive definite and the raw
source map A600 has rank 600. The original polar source map is
`F0=A600 M^(-1/2)` and satisfies `F0* F0=I600`.

For a maximal determinant D_(x,x xor d), the exterior coefficient is

```
C[(x,d),(a,b,i,e)] = -(-1)^popcount((a xor b)&x)/64
                     if e=d and i is x or x xor d;
                    0 otherwise.
```

The minus sign follows from the actual creation ordering: one residual
up particle occupies the base and the other the neighbor, so the paired
exterior signs multiply to minus. The replay derives each coefficient by
counting creation-order inversions, not by evaluating this closed formula.
All 14,400 entries agree with the frozen projection data.

The row Gram consists of 2 by 2 blocks with diagonal `25/2048` and
offdiagonal `1/2048` for d=1,2 or `9/2048` for d=4. Their eigenvalues are
`(24,26)/2048` or `(16,34)/2048`, all positive. The replay also obtains an
independent exact LDL witness. Hence C is surjective onto all 24 maxima;
the polar-coordinate projection `C M^(-1/2)` has the same row rank.

Set the raw 600-dimensional coordinate y to `-32/13` when a and b have the same lowest
bit, i is 0 or 1, and d=1, and zero otherwise. Direct multiplication gives
`C*y=c`. Define

```
x   = M^(1/2)*y/sqrt(2),
eta = F0*x = A600*y/sqrt(2).
```

Then `Pmax eta=chi` and `||eta||²=800/13`. There are 13 allowed core pairs.
For each pair the two selected placements have diagonal `49/64` and cross
entry `1/64` in G00, giving

```
||eta||² = (13/2)*(32/13)² * [2*(49+1)/64] = 800/13.
```

Complete position-space assembly separately obtains the same norm, using
6,208 nonzero determinants. The complete vector is retained. Dropping G00
would give `1024/13`, an error of `224/13`, so the raw metric is essential.
The orthogonal remainder obeys
`||(I-Pmax)eta||²=787/13`. The reconstructed incoming bare kinetic is
`6976/325`; no incoming-source preparation energy is identified with a free
autonomous transition.

## 5. Finite source-wide polar transfer

Let P=Pmax and define operators on the complete one-cell parent by

```
L = (1/9)P882*A*P + (3/50)P842*A*P + (1/30)P770*A*P,
B = I+L,
K_lambda = exp(lambda*(V-928/105)),
T_lambda = B*K_lambda*F0.
```

The left projectors are orthogonal to P, so `P L=0`, `L=L P`, `L²=0`.
The replay checks this support property on all 24 P columns and verifies
the image of c explicitly. Thus `B^-1=I-L`. For every finite real lambda,
K_lambda is invertible on the finite parent, since every eigenvalue is
strictly positive. Consequently T_lambda is injective on all 600 source
directions. For lambda>=0, the spectral gap further supplies the residual
bound below.

Set

```
S_lambda = T_lambda* T_lambda > 0,
F_lambda = T_lambda S_lambda^(-1/2).
```

The positive square root exists uniquely and
`F_lambda* F_lambda=I600`. In raw coordinates the new map is
`F_lambda M^(1/2)`, whose Gram is exactly M. This is one common linear
isometry, retaining all 600 coordinates and their original correlations.
For any original source unitary U (or a raw-metric unitary converted into
these polar coordinates),

```
F_lambda U F_lambda* + I - F_lambda F_lambda*
```

is a unitary extension on the physical parent. Thus the source Writes are
preserved as transported observables. The same expression applies after
embedding into full Fock space with the density-conditioned Weyl unitary.
This is a variational construction, not an assertion that autonomous
evolution under the fixed H realizes the map or pays for its preparation.

The limiting filter at infinite lambda has rank 24 after composition with
the actual source, so it cannot itself be a 600-dimensional isometry.
Finite lambda and the single source-wide polar normalization are essential.
The proof does not require numerically inverting an ill-conditioned 600 by
600 matrix. The positive-definite definition establishes the finite map
and its metric identity exactly.

## 6. Finite residual and energy payment

For the explicit x above,

```
K_lambda*eta = chi + r_lambda,
P r_lambda = 0,
||r_lambda|| <= sqrt(787/13) exp(-lambda*46/105).
```

Because `L r_lambda=0`,

```
T_lambda*x = phi+r_lambda.
```

At lambda=30 the exponential argument is `-92/7`. The replay uses the
positive Taylor series for `exp(92/7)` through degree 80. For general
positive x and degree N, with `x/(N+2)<1`, the finite sum S_N is a lower
bound and

```
S_N + [x^(N+1)/(N+1)!] / [1-x/(N+2)]
```

is an upper bound. Every term and comparison is rational. The retained
lower exceeds 500,000, establishing
`exp(-92/7)<1/500000`. Since `787/13<64`, this gives

```
||r_30|| < 8/500000 = 1/62500.
```

The one-particle cube adjacency has eigenvalues `3-2*popcount(k)`.
The largest sum for two same-flavor up particles is 4; a single down
particle contributes at most 3. For both species this gives `||A||=14`.
Therefore

```
||K_g|| <= 36*(tau+t_cell)+28*tau+g²*(928/105).
```

At `(tau,t_cell,g²)=(1,1/1000,33/2)` this is `367263/1750<210`.
The same upper 210 holds on the box in Section 8. Write `a=||phi||>=1`,
`epsilon=||r_30||<1/62500`, and normalize both phi and phi+r. The triangle
inequality gives

```
|| (phi+r)/||phi+r|| - phi/||phi|| || <= 2*epsilon/(a-epsilon)
                                                   <= 2*epsilon/(1-epsilon).
```

For normalized u,v, the Rayleigh difference is at most
`2*||K_g||*||u-v||`. Hence the finite transfer costs at most

```
4*210*(1/62500)/(1-1/62500) = 840/62499 = 280/20833.
```

The exact selected unit source vector is

```
v_lambda = S_lambda^(1/2)*x / ||T_lambda*x||,
F_lambda*v_lambda = (phi+r_lambda)/||phi+r_lambda||.
```

A nonzero remainder is not merely hypothetical: the retained control word
`p=[0,1,4], n=[0,1,2]` has raw seed amplitude 1/2, potential `872/105`, and
is outside phi's support. At lambda 30 it retains the strictly positive
multiplier `exp(-16)`. Thus finite and limiting states differ. The error
payment bounds that difference; it is not claimed to be the actual error
or to have a prescribed sign.

## 7. Main conditional margin (C6)

The same elementary exponential bound, now through degree 24 at
`583*(33/2)/11025`, gives `2/5<r<1/2`. C4 therefore supplies the upper

```
U = -5250104649/47516000.
```

Use C3 only in its flexible-shift form:

```
L_proper >= -(752/105)*g²+(79/10)*tau
when g² >= (22323/1360)*tau.
```

The main point satisfies this hypothesis and the lower is `-7719/70`.
The stronger shift 8, whose threshold is different, is not used. Exact
subtraction yields

```
L_proper-U                  >= 10447449/47516000,
L_proper-(U+280/20833)       >= 204347225017/989900828000 > 0.
```

These are certified allowances, not equalities for the actual ground
energy or actual spectral gap. The single localized determinant is above
this same lower by `419/875`; the signed hopping improvement matters to the
displayed certificate. The source transfer and the distinct U4 construction
in the other submitted claims are not added together.

## 8. Frozen profile and nonempty parameter box

The G² matrix rebuilt from the same omega matches every frozen profile
entry. Direct contraction of the reconstructed 28-determinant trial gives

```
<rho G² rho> = 192038691/33261200,
<N_b>       = 6337276803/66522400 at g²=33/2,
<H_field>   = 275799249/1900640,
<H_int>     = -275799249/950320.
```

Thus the profile hypotheses match: the same fixed scalar omega, vertex,
trial normalization, and field zero are used throughout. No density
counterterm or frequency rescaling is introduced.

Keep lambda 30 and the same B and source seed, and take

```
tau    in [1,1001/1000],
t_cell in [1/1000,1/500],
g²     in [1649/100,33/2].
```

At the adverse endpoints, the C3 hypothesis retains slack
`81077/1360000`, the K_g norm bound is `183719/875<210`, and the hopping
factor remains at least 2/5. Put `v=8357553/950320` and `k=24075/6788`.
Since `v-752/105>0` and `36-79/10-(2/5)k>0`, an all-box lower is

```
(v-752/105)*(1649/100)
 -(36-79/10-(2/5)*k)*(1001/1000)
 -36*(1/500) - 280/20833
= 3784147145591/29697024840000 > 0.
```

The receiver in matter space is fixed on this box. Its full-Fock Weyl
dressing uses the indicated g, as required by the common scalar model.

## 9. Actual-source scope controls

Three additional controls distinguish the quantified constructions.

First, let R exchange the proton and neutron three-particle tensor factors;
in the fixed sector it differs only by an irrelevant overall phase from
the CAR species permutation. On raw source coordinates it sends
`(a,b,i,d)` to `(b,a,i xor d,d)`. The metric M and F0 intertwine R. V, A,
all P_v, B, and K_lambda commute with it. Thus S_lambda and its positive
square root commute with source exchange. The explicit y and x are even,
so the selected v_lambda is even as well.

The frozen normalized 14336 phase signs are
`(1,1,-1,-1,-1,1,1,1,1)/3`. The actual source injection uses the uniform 24-vector on
the eight excited-core lanes and the offset contrast on lane 7; both pair
vectors are unchanged by pair exchange. Exchange swaps source lanes
`(0,5),(2,6),(3,8),(1,4)` and fixes lane 7. Its expectation in 14336 is
`-1/3`, so the odd weight is `2/3`. Therefore unchanged 14336 is not the
selected optimizer; its squared overlap with any exchange-even vector is
at most `1/3`. This conclusion uses the actual phase-source embedding,
not a generic distinction between two unnamed source vectors.

Second, consider actual raw columns `(0,0,0,1)` and `(1,1,0,1)`. They are
orthogonal, with squared norm `49/64`, and both have top projection
`-c/64`. After finite transfer their raw inner product is strictly larger
than `678693683531/1296000000000000`, by bounding the two tails using
`(7/8)/500000` and `||sqrt(2)*phi||<3/2`. Normalizing these columns
individually cannot make their inner product zero. Their normalized source
preimages can be included in an orthonormal source basis, so this is a
direct failure of the separate-column replacement for the common polar map.

Third, the full parent contains only 120 potential eigenvectors above
`842/105`. Any 600-dimensional receiving image has at least 480 directions
in the complementary potential subspace. For a normalized vector in that
intersection, the established `r<1/2` and `||A||=14` imply at the main point

```
<K_g> > 36*(1001/1000)-14-(33/2)*(842/105)
      = -192987/1750.
```

This exceeds the asserted finite selected upper
`-109362125672617/989900828000` by
`1580474669/7919206624>0`. Thus a promotion to all 600 directions is arithmetically
impossible at this point, for this dressed one-cell family. The selected
source upper does not imply one.

## 10. Scope and completion

C4 and C5 are HELD. C6 is HELD conditional on C3 with the same Hamiltonian,
field, zero, allowed populations, and proper matter-particle channel scope.
All selected-input, finite-error, and parameter-box quantifiers are retained.
The unchanged 14336 and U4-preserving nine-source certificate is a separate
construction for the lead to integrate after its independent track finishes.
No physical Li6 parameters, empirical binding, implemented preparation
protocol, or full essential-spectrum theorem follows from this track.

The next step is lead integration of the sealed C3 verdict and the other
track's scope, preserving these exact source and error operands.
