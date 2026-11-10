# CHANNEL derivation: C1–C3

All three submitted claims hold under the fixed contract. The proof below was
written separately from the retained campaign generators. The exact replay is
`replay.py`; its first registered execution is `attempts/001/REPLAY.json`.
No original generator was executed, imported, copied, or translated into this
code. The inherited model plus separate code gives I1 independence.

## 1. Model, common domain, and full scalar field

Let X = Z^3 × Q3. There are four CAR flavors, with fixed total counts
μ = (2,1,2,1). A fragment has nonzero counts m ≤ μ and N = |m| ≤ 5.
The six-particle parent has N = 6. The matter space is the fixed-count sector
of the fermionic Fock space over ℓ²(X) ⊗ C^4, with no receiver projection
inserted into an operator. The scalar space is the full symmetric Fock space
over ℓ²(X). In particular, field occupation is not restricted to zero or one.

For each cell, L denotes the combinatorial cube Laplacian, and

    ω = direct sum over cells of (I + L),       G = (I + L)^(-1),
    T = sum over particles [2τ L + t_cell L_Z3],
    H = T + dΓ(ω) + g sum_(R,x) ρ_(R,x)(b_(R,x) + b_(R,x)^†).

Here τ > 0, t_cell ≥ 0, and g is real. All terms, including particle self
terms, are present; there is no density counterterm and the vacuum field
energy is zero. The same parameters and zero are used in every fragment.
The source-wide maps and their coordinate metrics do not change this H.

For a matter determinant D, ρ_D is a finitely supported nonnegative integer
vector, with sum N and ||ρ_D||₂ ≤ N. The field operator satisfies
I ≤ ω ≤ 7I, so its form domain is D(N_b^(1/2)). On the algebraic core of
finitely supported matter and finite field-particle vectors, annihilation
estimates give, uniformly in D,

    |<ψ, g φ(ρ) ψ>| ≤ 2|g|N ||N_b^(1/2)ψ|| ||ψ||.

The coupling is therefore infinitesimally form bounded relative to dΓ(ω).
It is also infinitesimally operator bounded on D(dΓ(ω)), using
||a(f)ψ|| ≤ ||f|| ||N_b^(1/2)ψ|| and the corresponding creation estimate.
The finite-particle T is bounded, nonnegative, and has norm at most
12N(τ+t_cell). Thus H has the self-adjoint realization on D(dΓ(ω)); its
closed semibounded form has the common domain D(N_b^(1/2)). These estimates
do not depend on the number or positions of occupied cells.

Define the bounded matter multiplication operator

    V(D) = sum_R ρ_(D,R)^T G ρ_(D,R),       0 ≤ V ≤ N² I.

On the core, completing the full field square gives

    H = T + (b + gGρ)^† ω (b + gGρ) - g² V.                 (1)

The square is interpreted as its nonnegative closed form. Finite support of
each ρ_D and the preceding uniform estimates extend (1) to the common form
domain. In particular,

    H ≥ T - g² V.                                           (2)

Equivalently, put α_D = -gGρ_D and

    W_g = direct sum_D W(α_D).

This is a unitary: every fiber is a Weyl unitary and the matter basis is
countable. The uniform estimate ||α_D|| ≤ |g|N shows that W_g preserves the
form domain. The field part of (1) is exactly
W_g dΓ(ω) W_g^† - g²V. This is a full-Fock statement. The transformed
kinetic operator is W_g^† T W_g, not T, and must be retained.

## 2. Exact cube Green matrix and one-cell dressed expectation (C1)

Label cube vertices by binary integers 0,…,7, with edges differing in one
bit. Then ω has diagonal 4 and edge entries -1. The Walsh vectors
χ_k(x)=(-1)^(k·x) have squared norm 8 and ω-eigenvalue 1+2|k|. Consequently

    G_xy = (1/8) sum_k χ_k(x)χ_k(y)/(1+2|k|)

and 105G has entries 36,13,8,6 at distances 0,1,2,3. The replay obtains
the same matrix by rational Gauss–Jordan inversion, then separately checks
the Walsh identities. It does not assume those four entries as input.

Let Jψ = W_g(ψ⊗Ω), restricted here to all six matter particles in a fixed
cell. For D,E connected by one internal hop x→y, the coherent overlap is

    <W(α_D)Ω, W(α_E)Ω>
      = exp[-g² ||G(e_x-e_y)||²/2].

There is no phase because the displacements are real. For an edge,

    (1/2)||G(e_x-e_y)||²
      = (1/4)(1/9 + 2/25 + 1/49) = 583/11025.              (3)

The replay checks (3) on all twelve cube edges. For each determinant the
field energy is +g²V(D), and the interaction is -2g²V(D); their sum is
-g²V(D). The six-particle internal diagonal is 6×6τ=36τ. The cell diagonal
is 6×6t_cell=36t_cell. One cell hop leaves the all-six-in-one-cell subspace,
so its off-diagonal expectation vanishes. If A is the signed CAR lift of
the cube adjacency, then the exact pullback is

    J^* H J = 36(τ+t_cell)I
              - 2τ exp[-583g²/11025] A - g²V.              (4)

Equation (4) is a bounded expectation/form compression on that matter
space; it is not an operator identity replacing H on full Fock space.
Adding one dressed boson in an ω-eigenmode of eigenvalue 1, while keeping
a localized matter determinant, adds exactly 1 to the full expectation.
That state is outside J's vacuum-dressed range.

## 3. All one-cell potential maxima, without a receiver truncation

For a flavor vector m let N=|m| and let k be its number of nonzero entries.
Every allowed entry is 1 or 2. A site occupancy r_x is at most k, and
sum_x r_x=N. Using the largest off-site Green entry gives

    105V = 36 sum_x r_x² + sum_(x≠y) 105G_xy r_x r_y
           ≤ 13N² + 23 sum_x r_x²
           ≤ 13N² + 23[k²+(N-k)²].                        (5)

The last inequality follows by moving mass toward the fullest site until
it has k particles, then concentrating the remaining N-k≤k particles.
It is attained: put one particle of every active flavor at one vertex,
and the second copies, if present, together at an adjacent vertex. This
respects CAR because the second copies have distinct flavors. Thus (5)
is an exact maximum for every proper flavor allocation.

| Nonzero flavor counts, up to permutation | N | 105 max V |
|---|---:|---:|
| 1 | 1 | 36 |
| 2 | 2 | 98 |
| 1,1 | 2 | 144 |
| 2,1 | 3 | 232 |
| 1,1,1 | 3 | 324 |
| 2,2 | 4 | 392 |
| 2,1,1 | 4 | 438 |
| 1,1,1,1 | 4 | 576 |
| 2,2,1 | 5 | 624 |
| 2,1,1,1 | 5 | 716 |

The code independently enumerates every determinant in each of the 34
nonempty proper sub-counts of μ: 60,712 determinants in total. Each
determinant uses the site-major ordering orbital=4×site+flavor. A hop is
computed by removing and inserting an exterior factor, including both
permutation signs. All complete potential histograms, maximum determinants,
first-image columns, PTP matrices, and first-image Gram matrices are retained.

## 4. The noncommuting factors (C2)

Write h_m=T_internal-g²V on a one-cell fragment. Let M=max V, let P be
the complete maximum eigenspace of V, and Q=I-P. No compressed receiver is
used. The internal one-particle energies are 0,4τ,4τ,4τ,8τ,8τ,8τ,12τ.
Filling them separately for each flavor gives the full one-cell free floor.

For m=(2,1,1,1) and its allowed flavor exchange (1,1,2,1), the maximum
configurations have four particles at x and the repeated flavor at a
neighbor y. There are 8×3=24 such determinants. The next distinct potential
is 676/105: the 4+1 pattern with distance two. A pattern without occupancy
four has at most 3+2, so (5) bounds it by 624/105. The gap is therefore
40/105, exactly.

One hop cannot connect two maximum configurations: the cube has no
triangles, and moving a particle from the four-particle site changes its
occupancy. Hence PTP=30τP. There are 5×3-2=13 allowed directed hops from
each maximum determinant; the two blocked hops would move the repeated
flavor onto itself. Every hopping coefficient has magnitude 2τ, giving
the Gram diagonal 52τ². Distinct maximum determinants with different dense
vertices cannot be connected in two hops: at least the three unrepeated
flavors must move. With the dense vertex fixed and residual neighbors y,z
different, there are precisely two common first-image paths. One moves the
residual particle via the opposite corner of the square; the other moves
the repeated flavor at x to z and then y to x. Their CAR signs are opposite,
so they cancel. Thus the entire off-diagonal Gram vanishes:

    M=716/105,  δ=40/105,  PTP=30τP,
    QTQ≥4τQ,                 PTQTP=52τ²P.                 (6)

The last lower is the full one-cell Pauli floor compressed to Q, not a
commutation assertion. Each sector has dimension 14,336; its first Q image
has dimension 264. The replay checks the exact 24×24 matrices in (6).

For m=(1,1,1,1), the eight maxima have all four flavors at one vertex.
The next pattern 3+1 at adjacent vertices has value 438/105, by (5).
No one- or two-hop path connects different four-particle maximum vertices.
There are 4×3=12 allowed first hops. Consequently

    M=576/105,  δ=138/105,  PTP=24τP,
    QTQ≥0,                   PTQTP=48τ²P.                 (7)

This sector has dimension 4,096 and first Q image dimension 96. All other
flavor allocations have the maxima in the preceding table; no allocation
is discarded on spin or species grounds.

For arbitrary u=Pψ and v=Qψ, (6) or (7) and Cauchy–Schwarz imply

    <ψ,(h_m+g²M)ψ>
       ≥ aτ||u||² - 2√b τ||u||||v|| + (eτ+g²δ)||v||².

Thus the lower is the smaller eigenvalue of

    [[aτ, -√b τ], [-√b τ, eτ+g²δ]],                       (8)

with (a,e,b)=(30,4,52) or (24,0,48). This is a form comparison, not a
simultaneous diagonalization. Independently, h_m+g²M≥eτ by the full free
floor and nonnegative potential deficit.

## 5. Extension to arbitrary cell allocations

By (2), discard the nonnegative cell hopping and the nonnegative completed
field square. The remaining operator is a direct sum over per-cell flavor
occupations. For any such occupation pattern, it is a sum of finite
one-cell h_m operators, each tensored with identities on other cells. Fermion
sign conventions do not alter this decomposition: each local Hamiltonian
is even and preserves every cell's flavor counts.

At most N cells are occupied. Their positions range over a countable set,
but each allocation has one of the finitely many unordered vector
partitions of m. A uniform lower for every count pattern is therefore a
lower for the direct sum and its closed form. Empty cells contribute zero;
the positive field square permits arbitrary field states. This proves the
all-cell extension, rather than sampling a spatial cutoff.

In particular, a split five-particle fragment has static coefficient at
most M4+M1=(576+36)/105=612/105. A split four-particle fragment has
coefficient at most M3+M1=(324+36)/105=360/105. All finer partitions are
smaller, as follows either from the size table or the exhaustive vector
partition output. Other one-cell five-particle flavor allocations have
coefficient 624/105; other four-particle allocations have coefficient at
most 438/105.

The one-cell Pauli floor 4τ is never applied directly to a fragment whose
particles may occupy arbitrary cells. For example, five disjoint spatial
boxes of side L, with constant normalized spatial wavefunctions and the
constant internal Walsh orbital, have zero internal kinetic energy and
cell energy 30t_cell/L. At τ=t_cell=1 and L=10 this equals 3<4. The separate
split-cell potential bounds above are essential to the extension.

## 6. Universal proper-particle lower (C3)

Define the proper-channel comparison as the infimum, over all proper
partitions μ=m_1+…+m_r with r≥2, of the sum of the bottoms of the fragment
Hamiltonians H_(m_j), each with the same field, parameters, domain, and
zero. Each fragment may occupy arbitrary cells. This defines the submitted
matter-particle breakup comparison; it does not identify the essential
spectrum of the unfibered H.

Put s=g²/τ. For 0<c<30, the five-particle matrix (8) minus cτI is positive
semidefinite if

    s ≥ s5(c) = (105/40)[c-4 + 52/(30-c)].                  (9)

Indeed its first diagonal is 30-c>0, and (9) makes its second diagonal at
least 52/(30-c), so the determinant is nonnegative. The other one-cell
five-particle allocations and split cells satisfy the same global bound

    E5 ≥ -716g²/105 + cτ                                  (10)

provided respectively s≥105c/92 and s≥105c/104.

For the four-particle matrix, subtract 4τI. Its diagonals are 20 and
138s/105-4; the determinant is 20(138s/105-4)-48. This is nonnegative
exactly at and above s=112/23. The other four-particle flavor sectors
require only s≥420/138=70/23, and split cells only s≥420/216=35/18.
Thus

    E4 ≥ -576g²/105 + 4τ      for s≥112/23.                (11)

For A=1,2,3, the global static bounds are -36g²/105, -144g²/105,
-324g²/105, respectively. Their all-cell extensions follow in the same
way from the size maxima. Equations (10)–(11) give

    5+1:  -752g²/105 + cτ,
    4+2:  -720g²/105 + 4τ.

The second exceeds the first whenever s≥105(c-4)/32. Every remaining
proper partition has coefficient at most 648/105, so the static lower
alone suffices when s≥105c/104.

There are exactly 91 unordered proper flavor partitions in this fixed μ
sector. The recursive enumeration chooses the next nonzero flavor vector
lexicographically at or after the previous one and subtracts it from the
remaining population. Every multiset partition has exactly one sorted
ordering, so induction on the remaining particle number proves both
completeness and uniqueness. Each fragment is further enumerated over all
its cell-count partitions. The retained exact comparisons at each stated
threshold cover all 91 channels, not just the maximizing size type.

| Sizes | Flavor partitions | Largest static numerator, denominator 105 |
|---|---:|---:|
| 5+1 | 4 | 752 |
| 4+2 | 8 | 720 |
| 4+1+1 | 8 | 648 |
| 3+3 | 5 | 648 |
| 3+2+1 | 24 | 504 |
| 3+1+1+1 | 10 | 432 |
| 2+2+2 | 6 | 432 |
| 2+2+1+1 | 17 | 360 |
| 2+1+1+1+1 | 8 | 288 |
| 1+1+1+1+1+1 | 1 | 216 |

Therefore the sufficient condition for the claimed universal lower is

    L_proper ≥ -752g²/105 + cτ,
    s ≥ max{s5(c), 105c/92, 105c/104, 112/23,
            105(c-4)/32}.                                 (12)

At c=8, the maximum is 735/44. The five-particle PSD diagonals are
22 and 26/11; their product is 52. The other nontrivial thresholds are
210/23, 105/13, 112/23, and 105/8, all smaller. Thus

    L_proper ≥ -752g²/105 + 8τ
        for g² ≥ (735/44)τ.                               (13)

At c=79/10, the maximum is 22323/1360. The five-particle PSD diagonals
are 221/10 and 40/17; their product is again 52. The other thresholds are
1659/184, 1659/208, 112/23, and 819/64. Thus

    L_proper ≥ -752g²/105 + (79/10)τ
        for g² ≥ (22323/1360)τ.                           (14)

The source expression 290199/17680 equals 22323/1360 exactly; it needs
no correction. Equality in a sufficient PSD condition establishes validity
of the lower, not sharpness of the physical fragment ground energy.

## 7. Piecewise form of the sufficient condition

For completeness, (12) simplifies to a two-piece condition. Let

    c0 = (1237 - sqrt(941461))/69,      19/5 < c0 < 4.

It is the smaller root of 69c²-2474c+8532=0 and the unique crossing in
(0,30) of s5(c) and 112/23. The function s5 is strictly increasing, since
s5'(c)=(105/40)[1+52/(30-c)²]>0. The rational endpoint checks isolate c0.

The condition 105c/104 is smaller than 105c/92. Moreover

    s5(c) - 105(c-4)/32
      = 105[(c-17)²+39]/[160(30-c)] > 0.

For c≤c0<4, 105c/92<105/23<112/23. For c≥c0>19/5, the sign of
s5(c)-105c/92 is the opposite of q(c)=13c²-482c+1564. This convex
quadratic is negative at both 19/5 and 30, hence on that entire interval.
It follows that the maximum in (12) is exactly

    112/23,                         0<c≤c0;
    (105/40)[c-4+52/(30-c)],         c0≤c<30.               (15)

This describes this sufficient proof family. It is not a claim of optimal
spectral thresholds.

## 8. Breaking controls and the conclusion's boundary

All six controls were specified before computation and retained as actual
counterexamples or exact arithmetic checks.

* **Field and ordered density account.** For the legal adjacent 4+2
  density, V=928/105. Its density self terms contribute 720/105; each
  ordered mixed term contributes 104/105. Dropping one order gives
  824/105. At g²=1 the field energy is +928/105, the interaction -1856/105,
  and the complete sum -928/105. Dropping the field energy doubles the
  attraction incorrectly.
* **Noncommutation.** In the deep five-particle sector at τ=g²=1, take
  D=(0,1,2,3,4) and E=(0,1,2,3,12) in the site-major orbital ordering.
  Their hopping entry is -2 and potential deficit 8/21. The normalized
  vector proportional to D+(21/29)E has expectation 18096/641<30 for
  h+g²M. This breaks an invalid global use of the restricted P kinetic
  value 30. Adding the full-operator minima is mathematically valid but
  only yields 4; the defect is not the general sum-of-minima inequality.
* **Separated cells.** The five disjoint spatial boxes above give the
  exact value 3 below the one-cell Pauli floor 4.
* **4+2 is not universal.** At τ=1, t_cell=1/1000, g²=210, a coherent
  determinant with a deep five-particle cluster and the remaining particle
  in a remote cell has exact energy -366991/250. The purported universal
  4+2 lower -720g²/105+4τ is -1436. Their difference is -7991/250<0.
* **Counterterm changes the model.** Adding +g²V changes (1) to T plus
  the positive field square. At the same 4+2 density, the dressed scalar
  energy becomes exactly zero, not -928/105. Both trial and comparison
  must be recalculated for that changed Hamiltonian.
* **Spectrum and compression.** The translation-invariant scalar example
  L_Z3-7I has localized delta expectation -1 below the stipulated threshold
  zero, yet Fourier spectrum [-7,5] and no point spectrum. Each energy
  level of its cosine dispersion has measure zero, by fixing two momenta
  and applying the one-dimensional level-set fact and Fubini. This is a
  control on the invalid inference, not a spectral assertion about the
  submitted H. In the actual model an extra dressed ground-mode boson
  also distinguishes the full operator from (4), by the exact added cost 1.

The proofs establish the common full-Fock inequality, the exact finite
noncommuting fragment factors, and the universal proper-matter-channel
lower. An isolated eigenvalue of the full translation-invariant operator,
a fiber-HVZ theorem, physical isotope binding, and an autonomous paid
preparation are not conclusions of C1–C3. No correction to their submitted
scope or numbers was needed.
