# Atomic CR2 — complete reports and proofs

All original verifier text follows without selection or rewriting. Bare paths in each document refer to its original peer folder. Code, inputs, attempts, controls and exact data remain in the same complete case.

## FORM/REPORT.md

[Original document](peers/FORM/REPORT.md)

<!-- BEGIN FORM/REPORT.md -->
# FORM outcome

A05 needs one source-comparison correction: its constant-lapse full-domain bound holds, but the prior note's blanket claim of strict improvement over the original geometric Pauli bound is false. A01–A04 are HELD. A05 is HELD WITH CORRECTION. All three controls detected the intended failures. The complete written proof, fresh exact/directed runner and byte-identical relocated replay are retained. Next, review the corrected A05 wording and replay the complete public case before synthesis.

One implementation failure is retained: attempt 002 used structural SymPy matrix equality for the curl and stopped on equivalent expressions. Attempt 003 changed only that comparison to algebraic zero residuals. Attempts 004 and 007 added independently integrated control terms and the original-geometric-weight comparison. Every version, seal, log and result remains under `attempts/`. There are no controls that failed to behave as predicted. Attempt 008 matched the final reference hashes, but one inherited criterion sentence named the older attempt 004; its label amendment is retained, and consistently labeled attempt 009 independently repeats the same byte-identical relocation.

## Assigned outcomes

| Claim | Result | Established scope |
|---|---|---|
| A01 | HELD | Original point operator, source units, universal dilation, zero-coupling branch and full H1 form domain |
| A02 | HELD | Exact bounded-field norm/divergence; no origin delta; exact full-domain square and spin-two occupied lower before antisymmetric restriction |
| A03 | HELD | Matched finite-core multiplier and h-squared remainder; full distributional identity and anisotropic lower without C>=A |
| A04 | HELD | Complete Coulomb occupation, optimized split of the original quadratic kinetic, positive pair law and maximum with the independent core floor |
| A05 | HELD WITH CORRECTION | Actual constant-lapse metric/domain and displayed lower hold; universal strict-improvement comparison must use the original geometric occupation weight |

Full arguments and source definitions are in `DERIVATION.md` and `HYPOTHESES.md`. Per-claim and per-control evidence is in `OUTCOMES.json`; no assigned substatement is left unresolved.

## Exact findings and controls

The point lower is `-A^2/(16*tau)` per electron, with universal occupied lower `-N/16`. Exact point norm/divergence residuals and the direct H1-state form residual are zero. The finite-core proof retains its exact h-squared remainder; it does not replace that remainder by a false constant identity. The full N=1,...,6 Coulomb weights are 1, 2, 9/4, 5/2, 11/4 and 3, derived from the complete spin spectrum. These fields are in `attempts/007_final_replay_v4/output/RESULTS.json` at A01–A04.

AF01 retains the same field norm but loses the source divergence; the exact source-minus-wrong-square discrepancy is `-1/3`. AF02 detects bulk residual `1/rc`, normal jump `-1/5`, a strictly negative surface pairing and a strictly positive total defect, with direct density integrals and rational outward enclosures. AF03 refuses pair-negative, kinetic-coefficient-changed and massive-law transfers. Its explicit pair toy has admissible energy `-1/2` below the copied zero lower; the independently integrated finite-core kinetic toy lies strictly below the copied -1/4 lower. The exact/directed fields and their signs are at AF01–AF03 in the same results file.

## A05 correction and what it means

The source fixes constant 0<nu<=1, metric nu^-2 dr^2+r^2 dOmega^2 and measure nu^-1 r^2 dr dOmega. On that complete weighted H1 form domain, the submitted divergence, matching and optimized lower hold. A varying lapse instead requires div_g(nu F), including a nu*nu' radial term and derivatives of lapse-dependent amplitudes/profiles; no variable-lapse result is asserted.

The old source already fills the exact geometric Coulomb denominators. At nu=1/2,N=6 its complete weight is `49/18`, because the two spins in the 1s, 2s and 3s levels precede every angular complement. At C=1,A=1/100,tau=rc=1, the old branch is `-499849/90000`. The submitted new branch `-6-1/7500-sqrt(2)/25` is strictly weaker, and both exceed the core floor `-303/50`. This is an exact counterexample to the prior note's universal comparison over its parameter family, not a failure of the displayed lower or a claim that an existing numerical panel fails. It is retained first in attempt 006 and incorporated into final attempt 007.

Corrected wording: keep the valid directional bound, the original geometric Pauli branch and the core floor, and use their maximum. Strict improvement is account dependent. The form identity and its full domain are unchanged.

## Replay, custody and limits

`replay.py` uses only public case files, the standard library and the pinned SymPy dependency in `requirements.txt`. It accepts a clean output directory, uses one arithmetic process and no research engine. `INPUT_MANIFEST.json` seals 23 necessary public files. Four omitted but needed original notes were recovered into `recovered_sources/`; their original/copy hashes and seal precede dependent execution.

The final exact/directed output is `attempts/007_final_replay_v4/output/RESULTS.json`; its SHA-256 is `199ea928ed9b03be7a2eca04373380daccf5c129da67ed760772de762cd665f6`. The relocated execution in `attempts/009_final_relocation_record` ran from a different working directory with the complete required public execution-input closure. All four deterministic files are byte-identical. `REPLAY.json` gives the portable command, dependencies, exact comparison fields, rational interval rules and reference hashes. This is local replay evidence; no outside-party classification is assigned.

Analytic proofs establish the full-domain statements. Exact host algebra, finite state/occupation cross-checks and directed rational enclosures have their separate roles. Original reports are inherited definitions/submissions. FORM makes no new source-minimum, phase/binding panel, massive-kinetic, physical-ionization or calibrated-energy claim. No manuscript, installed engine, Git or other peer folder was changed.

The next step is case-level review of the proof and A05 comparison correction, followed by a fresh relocated replay and integration with the other assigned tracks.
<!-- END FORM/REPORT.md -->

## FORM/DERIVATION.md

[Original document](peers/FORM/DERIVATION.md)

<!-- BEGIN FORM/DERIVATION.md -->
# Independent reconstruction of the FORM claims

The point, finite-core and constant-lapse quadratic bounds hold on their full form domains. The prior geometry note's universal strict-improvement comparison needs the correction proved below. The replay checks exact identities and exposes the three declared control failures. The proof below establishes the domain and occupation statements; finite calculations do not replace those arguments. The next step is a relocated replay of this folder in the complete public case, followed by the case-level review.

All statements here are EXACT mathematical statements under the hypotheses in `HYPOTHESES.md`. The source definitions are the copied `atoms_01.tex`, `atoms_02.tex`, `volii_pair_source1/{DERIVATION,ATOMIC_DERIVATION}.md`, and `volii_lapse_field1/DERIVATION.md`. The submitted arguments are the FOUR notes in `prior/FOUR` and the two recovered FOUR notes. `recovered_sources/RADIAL_DERIVATION.md` and `PAULI_BOUND.md` recover omitted original definitions. Their original and copied hashes were sealed before this reconstruction. This proof and the replay were authored afresh; no original implementation was executed or incorporated.

## A01: original operator, units, dilation and full domain

Let tau>0, A=g|U|>=0 and e be a fixed unit vector when A>0. On `L2(R3;C2)` the source one-body quadratic form is

    q_A[psi] = tau int |grad psi|^2 dx - A int (e.x)/|x|^2 |psi|^2 dx,
    D(q_A)=H1(R3;C2).

The spin components are summed. No pair law, scalar charge or core radius belongs to this point predecessor. The original separated electronic infimum is zero for a free electron. Nuclear source energies remain separate until their own minimization; this track proves the electronic form bounds.

Here tau has mathematical dimensions energy times length squared, while A has energy times length. They are source units. No calibrated physical unit is inferred. For A>0 set L=tau/A and `psi(x)=L^(-3/2) phi(x/L)`. This is unitary, maps H1 to H1, and sends q_A to `(A^2/tau) q_1`. Thus the universal point operator is `-Delta-cos(theta)/r`. The N-electron antisymmetric space, including two spin labels, has the analogous product dilation; its ground infimum is `(A^2/tau)e_N`. If A=0, keep the unscaled free form, whose infimum is zero. There is no division by A in that branch.

The potential form is well defined and continuous on H1. The three-dimensional Hardy inequality gives `||psi/r||_2 <= 2||grad psi||_2`, hence

    int |psi|^2/r <= 2 ||psi||_2 ||grad psi||_2.

For two H1 functions the same estimate and polarization control the difference and mixed forms. Young's inequality makes the Coulomb term infinitesimally form bounded with respect to the kinetic form. Consequently q_A is closed, semibounded and defines its Friedrichs selfadjoint operator. H1 is the form domain; it is not being asserted to equal the operator domain.

The punctured smooth compact core is dense in H1. For a smooth compact f, multiply by a radial cutoff vanishing for r<epsilon and equal to one for r>2epsilon. The squared L2 error is O(epsilon^3); the extra squared gradient term is O(epsilon), since the cutoff gradient is O(1/epsilon) in a volume O(epsilon^3). Ordinary smooth approximation and then this construction prove density. The Coulomb estimate also gives density in the form norm. Every angular and radial direction is retained.

## A02: the divergence-matched point field

For r>0 put n=x/r, c=e.n and

    F = A/(4 tau) (2 c n-e).

The bracket is a reflection of e, so its squared norm is `4c^2-4c^2+1=1`. In the spherical orthonormal frame aligned with e, it has components `(c,sin(theta),0)`. Its divergence is `4c/r`. Equivalently, in Cartesian coordinates with e=e_z the unscaled field is

    F0 = (2xz/r^2, 2yz/r^2, 2z^2/r^2-1)/4,
    div F0=z/r^2, |F0|^2=1/16,
    F=(A/tau)F0.

These are identities for every x!=0. In the distributional integration by parts the absolute boundary flux on a sphere of radius epsilon is at most a constant times epsilon squared times the supremum of a smooth test. It vanishes as epsilon tends to zero. Thus `div F=(A/tau)c/r` distributionally on all space, with no origin delta. Boundedness also gives `F psi in L2` for all H1 psi.

For a complex smooth spinor away from the origin, `2 Re(psi* grad psi)=grad|psi|^2`. Integration by parts and the preceding identities give

    tau ||(grad+F)psi||^2
      = q_A[psi] + A^2/(16 tau) ||psi||^2.

Both sides are H1-continuous, so density extends the exact identity to the full form domain. In particular `q_A[psi]>=-A^2/(16 tau)||psi||^2`.

The estimate sums over electron coordinates on the entire distinguishable product H1 space, with arbitrary spin components, before restricting to the antisymmetric subspace. Fubini/density or the corresponding tensor form argument therefore gives `e_N>=-N/16` in the universal spin-two sector. There is no angular or radial cutoff and no occupation assumption in this summation.

The field need not be a gradient for integration by parts to be valid. In fact

    curl F = A/(2 tau r^2) (-y,x,0)

when e=e_z. For A>0 it is nonzero off the axis. Equality would require `(grad+F)psi=0`; commuting local weak derivatives away from the origin forces `(curl F)psi=0`, so a nonzero H1 state cannot saturate it. This does not identify the ground infimum or prove a uniform strict gap above the bound.

The exact H1 state `(1+z)exp(-r)`, normalized by its norm squared `2 pi`, provides a replay cross-check: its kinetic expectation is 1, its `c/r` expectation is 1/3, and its completed-square expectation at A=tau=1 is 35/48. The point energy is 2/3. Those finite checks illustrate the identity; the proof above gives the full-domain result.

## A03: the original finite-core potential

Let rc>0 and `d_c(r)=max(r,rc)`. The anisotropic potential is `-A c/d_c(r)`. With the same bracket choose

    h(r)=4r/(5rc)                         (r<=rc),
         1-rc^4/(5r^4)                    (r>=rc),
    F_c=A/(4tau) h(r)(2cn-e).

On each region `h'+4h/r=4/d_c(r)`. The one-sided values at rc are both 4/5 and the one-sided derivatives both `4/(5rc)`. The profile is increasing, vanishes at zero, tends to one, and lies in [0,1]. Hence

    div F_c=(A/tau)c/d_c(r),
    |F_c|^2=A^2 h(r)^2/(16tau^2).

The field is continuous across the interface, so its normal jump and the distributional interface term are zero. It is O(r) near the origin, so its absolute small-sphere flux is O(r^3) and no origin distribution remains. The angular dependence at the origin does not require assigning a direction to n there.

The exact full-domain form identity is

    q_aniso,c[psi]
      =tau ||(grad+F_c)psi||^2
        -A^2/(16tau) int h(r)^2 |psi|^2,

or, after adding `A^2/(16tau)||psi||^2`, a sum of the square and the nonnegative remainder `A^2/(16tau) int (1-h^2)|psi|^2`. This gives the same uniform lower `-A^2/(16tau)`. The bounded core potential makes extension from smooth functions immediate; the preceding H1 density argument also applies.

No condition C>=A or pointwise attractive sign is used. In the actual scalar-plus-anisotropic atom one treats the scalar and directional pieces separately. In particular, replacing the signed core potential by its point version pointwise is not part of this proof.

## A04: complete Coulomb occupation, kinetic split, pair law and core floor

The original electronic N-body operator has exactly quadratic kinetic `tau sum_i(-Delta_i)`, potential `-(C+A e.n_i)/d_c(r_i)` with C=gc Z>=0, A=gp|U|>=0, and pair multiplication

    W_ij=(vc+vp n_i.n_j)/|x_i-x_j|,
    vc>=vp>=0.

Thus `W_ij>=(vc-vp)/|x_i-x_j|>=0` almost everywhere. Values at coordinate zeros are irrelevant sets of measure zero. The usual relative-coordinate Coulomb form estimate makes its finite-N form well defined on the many-body H1 domain. Discarding this positive form is valid for a lower estimate; it does not discard pair or exchange terms from an upper witness. Source core self terms are not part of this electronic estimate and remain inside both later nuclear minima.

For a>0 the scalar Coulomb operator `a(-Delta)-C/r` has negative energies

    -C^2/(4a k^2), k=1,2,...,

with spatial degeneracy k^2 and spin-two degeneracy 2k^2. Here is the full-space spectrum argument, including the omitted modes. Spherical harmonic completeness separates every l=0,1,... and m=-l,...,l. In a fixed l the radial Friedrichs operator on L2(0,infinity;dr) is

    a[-d^2/dr^2+l(l+1)/r^2]-C/r.

For energy `-a kappa^2`, setting `t=2 kappa r` and `u=t^(l+1) exp(-t/2)v` gives

    t v''+(2l+2-t)v'+[C/(2a kappa)-l-1]v=0.

The origin-admissible solution is the regular confluent series. The other solution has the excluded `r^(-l)` radial behavior (or its singular limiting form for l=0), which is outside the Friedrichs H1 condition. The regular solution has an exponentially growing asymptotic branch unless its series terminates. Termination requires `C/(2a kappa)-l-1=j` for integer j>=0; then it is the generalized Laguerre polynomial and is square integrable at infinity. Therefore the complete negative spectrum is labeled by k=j+l+1, and no negative l/radial mode is missing. The decaying potential is a relatively compact form perturbation of the free Laplacian, so the essential spectrum is [0,infinity). Sturm-Liouville exhaustion gives no further negative spectrum. Summing `2l+1` for l=0,...,k-1 yields k^2. At C=0 all these lower energies have the zero limiting value and the free comparison suffices.

For any normalized antisymmetric N-electron state its one-body density matrix satisfies `0<=gamma<=1` and `Tr gamma=N`, including spin. Resolving it against the full one-body spectrum shows that the minimum of `Tr(h gamma)` is the sum of the N lowest spin-orbital energies: moving a fractional occupation from a higher energy to an unfilled lower energy cannot increase the sum. The nonnegative continuum cannot improve that minimum. This proves the occupation principle for correlated states as well as determinants.

For arbitrary finite N, let K be the smallest positive integer with

    M_K=2 sum_{k=1}^K k^2=K(K+1)(2K+1)/3 >=N,
    w_N=2(K-1)+(N-M_(K-1))/K^2.

Then the complete scalar Coulomb sum is `-w_N C^2/(4a)`. For N=0 set w_0=0; for N=1, w_1=1; for 2<=N<=10, `w_N=2+(N-2)/4`. In particular the assigned N=1,...,6 weights are `1,2,9/4,5/2,11/4,3`.

Since C>=0, `-C/d_c(r)>=-C/r`, so this Coulomb sum bounds the scalar core form. For 0<theta<1 split the same original kinetic into theta and 1-theta. Apply the scalar Pauli comparison with `a=theta tau`, and apply A03 per particle to the anisotropic part with kinetic `(1-theta)tau`. The result is

    E_e,N >= -1/(4tau) [C^2 w_N/theta + (A^2 N/4)/(1-theta)].

Put alpha=C sqrt(w_N), beta=A sqrt(N)/2. The identity

    alpha^2/theta+beta^2/(1-theta)-(alpha+beta)^2
      =[alpha-(alpha+beta)theta]^2/[theta(1-theta)]

gives the best split at theta=alpha/(alpha+beta) when both are positive. Endpoint limits cover alpha=0 or beta=0; when both vanish the bound is zero. Therefore

    E_e,N >= -[C sqrt(w_N)+(A/2)sqrt(N)]^2/(4tau).

Independently `-(C+A c)/d_c(r)>=-(C+A)/rc`, and the original kinetic and pair forms are nonnegative. Thus the full lower is the maximum of the optimized spectral branch and `-N(C+A)/rc`. This argument covers C<A as well. The spectral branch is strictly stronger than the old scalar-magnitude branch when `A>0` and `N<4w_N`; the final maximum can still tie if the core floor dominates. The weak carbon example and that competition are exact/directed replay fields, not an independent source-minimum claim.

The quadratic kinetic law is essential. The massive source kinetic is a smaller square-root operator; a lower bound derived for the larger quadratic kinetic cannot be copied to it. This track assigns no new ionization, physical-unit, source-minimum or massive lower result.

## A05: actual common geometry and its domain

The source metric and measure are

    ds_g^2=nu^(-2)dr^2+r^2dOmega^2,
    dvol_g=nu^(-1)r^2dr dOmega, 0<nu<=1 constant.

Use the Friedrichs H1 form domain, equivalently the closure of smooth compact functions away from the cone vertex under norm plus `||grad_g||_2`. For each fixed positive nu its norm is equivalent to ordinary H1 under the constant measure normalization, so the vertex has no additional form boundary condition. The kinetic form is

    K_nu=tau nu int |grad_g psi|^2 dvol_g
          =int [tau nu^3|partial_r psi|^2
                +tau nu/r^2|grad_Omega psi|^2] dvol_g.

The unitary map `psi -> psi/sqrt(nu)` to flat L2(dx) preserves multiplication potentials. Since nu>=nu^3 in the source range, `K_nu>=tau nu^3(-Delta)` as flat forms. It supplies a valid scalar Pauli comparison; it is not an assertion that the exact geometric scalar spectrum equals the ordinary hydrogenic spectrum.

In the orthonormal spherical frame put

    F=a h(r)[cos(theta)e_r+sin(theta)e_theta],
    a=A/[2tau nu(nu+1)], d=2(nu+1)/nu,
    h=d r/[(d+1)rc]                         (r<=rc),
      1-(rc/r)^d/(d+1)                      (r>=rc).

Coordinate divergence using the original measure, with contravariant components `F^r=nu a h cos(theta)` and `F^theta=a h sin(theta)/r`, is exactly

    div_g F=a[nu h'+2(nu+1)h/r]cos(theta).

Both profiles satisfy `h'+d h/r=d/d_c(r)`. Values and first derivatives agree at rc; the profile is in [0,1], O(r) at zero and tends to one. Thus

    tau nu div_g F=A cos(theta)/d_c(r),
    |F|_g^2=a^2 h^2.

The small-sphere flux again vanishes, and matching removes the interface term. Completing the geometric gradient square gives the exact identity with remainder `-tau nu a^2 int h^2|psi|^2`, and the lower

    K_nu-A cos(theta)/d_c(r) >= -A^2/[4tau nu(nu+1)^2].

The same scalar/anisotropic kinetic split, occupation proof and nonnegative pair argument now yield

    E_e,N >= -[C sqrt(w_N)+A nu sqrt(N)/(nu+1)]^2/(4tau nu^3).

Keep the independent core floor. At nu=1 the radial multiplier and bound reduce exactly to A03/A04. The source's same complete positive Green kernel multiplies the scalar-plus-polarization pair numerator, so its stated `vc>=vp>=0` condition remains sufficient. No truncated angular kernel is substituted.

No additional radial derivative term is required for this constant-nu source. A varying lapse is a different calculation. To state the precise missing term, write b(r)=a(r)h(r), nu=nu(r). Then

    div_g F=[nu b'+2(nu+1)b/r]cos(theta),
    div_g(nu F)=[nu^2 b'+nu nu' b+2nu(nu+1)b/r]cos(theta).

Completion of the variable-weight kinetic uses `tau div_g(nu F)`, not `tau nu div_g F`. The extra `nu nu' b` term must be retained, and b' differentiates any lapse-dependent amplitude and profile. Constant measure normalization is also unavailable in that case. The submitted bound is held on the actual declared constant-lapse geometry; no variable-lapse extension is asserted.

## A05 correction: compare the original geometric occupation weight

The submitted lower formula is valid, but the recovered `LAPSE_PAULI_WORKING.md` also states that it improves the old isotropic-charge spectral branch on all three retained quadratic geometries for N<=8 and every A>0. That comparison is false over the declared parameter family. The original source `volii_lapse_field1/DERIVATION.md` uses its exact geometric Coulomb weight w_(N,nu), which can be smaller than ordinary w_N. It is therefore necessary to compare the new branch with that original branch rather than with a weakened flat-weight surrogate.

After constant measure normalization the original scalar geometric Coulomb radial operator has the coefficient tau nu^3 and centrifugal term l(l+1)/nu^2. Set `alpha_l(alpha_l+1)=l(l+1)/nu^2`. The same regular/decaying radial argument from A04 gives denominators `n_r+alpha_l+1`, with spin-two degeneracy `2(2l+1)`. This reconstructs the source's complete geometric occupation, rather than a finite angular cutoff.

At nu=1/2 and N=6, `alpha_1=(sqrt(33)-1)/2>2`, and alpha_l is increasing. Consequently every l>=1 has denominator greater than 3. The full six lowest slots are precisely the two spins in the l=0 radial levels n_r=0,1,2, of denominators 1,2,3. Every further l=0 radial level has denominator at least 4. The exact weight is therefore `w_(6,1/2)=2+2/4+2/9=49/18`, while ordinary w_6=3.

Choose the declared member tau=rc=C=1, A=1/100, nu=1/2, N=6. It can be realized on an original q=144,Z=6 sector with gc=vc=1/6 and gp=vp=1/1200, retaining vc>=vp>=0. This is a comparison within the declared parameter family, not a claim about a failed weak/strong numerical panel. The old original geometric branch is

    -w_(6,1/2)(C+A)^2/(4tau nu^3) = -499849/90000.

The submitted new valid branch is

    -[C sqrt(3)+A sqrt(6)/3]^2/(4tau nu^3)
      = -6-1/7500-sqrt(2)/25.

Exact rational root enclosures place the new branch strictly below the old one. Both exceed the core floor -303/50, so taking the maximum with that floor does not remove this counterexample. The new branch remains a correct lower; the assertion that it is always the stronger branch requires correction.

The corrected wording is: the divergence bound and kinetic split hold for every constant 0<nu<=1 under their stated hypotheses; compare the resulting branch with the original geometric Pauli branch and retain their maximum with the core floor. Strict improvement is account dependent. One can also apply the same split with the source's exact scalar geometric occupation weight, but no additional panel of that refinement is needed or claimed here.

The A05 outcome is HELD WITH CORRECTION: its form/domain identity and displayed lower are held; the blanket comparison in its full source note is replaced by the preceding account-dependent statement. No other assigned claim needs a correction.

## Controls and their exact failures

AF01 uses the incorrect constant field `F_bad=-e_z/4` at A=tau=1. It retains the correct norm but has zero divergence. On the normalized `(1+z)exp(-r)` state its proposed square reconstruction gives 1 while the source form is 2/3, a residual -1/3. A norm check alone would miss it; the source divergence and exact form check detect it.

AF02 uses h_bad=r/rc inside and the original exterior h outside. Its interior ODE residual is `1/rc`, and its interface jump is -1/5. Therefore divergence has both a bulk error and an omitted surface distribution. At rc=A=tau=1 the surface distribution paired with the same normalized density is `-exp(-2)/15`, which is nonzero. The total divergence defect paired with that density is `1/8-(103/120)exp(-2)`, strictly positive. For example `exp(2)>7>103/15` proves the sign. The matched source profile has zero bulk residual and zero normal jump. A derivative jump alone would not itself be a delta in first-order divergence; this control actually has a normal field jump.

AF03 has two explicit toy counterexamples. For N=2, C=A=0, tau=1, replace the nonnegative pair by a constant -1. Two opposite spin labels in the normalized radial exponential with rate 1/2 are a legal determinant and have total energy `2(1/2)^2-1=-1/2`, below the would-be lower zero. This transfer is refused because pair nonnegativity fails. Separately take N=1,C=1,A=0,rc=1/100 and replace the assumed tau=1 kinetic by `(1/4)(-Delta)`. The normalized exponential of rate 2 has kinetic expectation 1 and exact energy `-99+102 exp(-1/25)`, below -1/4, the claimed tau=1 bound. This transfer is refused because the quadratic kinetic coefficient fails. The replay also refuses the source's massive square-root law. These failures establish why the hypotheses matter; neither toy alters the source claims.
<!-- END FORM/DERIVATION.md -->

## FORM/HYPOTHESES.md

[Original document](peers/FORM/HYPOTHESES.md)

<!-- BEGIN FORM/HYPOTHESES.md -->
# Hypotheses map

The reconstruction retains the submitted source and separates its point predecessor, finite-core interacting atom and constant-lapse quadratic geometry. Every assigned claim has a full-domain proof in `DERIVATION.md`; the exact replay checks their algebra and the declared breaking controls. A05 is HELD WITH CORRECTION because the prior note's universal strict-improvement comparison overlooks the original lapse-dependent Pauli weight; the bound itself holds.

| Claim | Required hypotheses | Domain and preserved scope | What breaks the transfer |
|---|---|---|---|
| A01 | tau>0; original `-A cos(theta)/r`, A=g|U|>=0; fixed U within an electronic sector | H1(R3;C2), Friedrichs form; spin-two product/antisymmetric spaces; A=0 treated freely; source units only | Changing to scalar, core, pair, calibrated or massive operator without its source proof |
| A02 | Same point form; real bounded divergence-matched F; no origin delta | Every angular/radial direction; complex spinors; sum before antisymmetric restriction | Correct norm but wrong divergence; saturation inferred from a nongradient field |
| A03 | rc>0; original signed anisotropic `-A cos(theta)/max(r,rc)`; matched h | Full H1; exact h^2 remainder; no condition C>=A; no interface or origin distribution | Changed interior profile, normal interface jump or omitted radial derivative |
| A04 | Quadratic kinetic tau(-Delta); spin multiplicity two and antisymmetry; C>=0,A>=0; finite rc>0; `vc>=vp>=0` for the original pair law | Complete scalar Coulomb spectrum and Pauli occupation; arbitrary finite N formula and original N<=6; kinetic split limits; maximum with core floor | Negative pair or smaller/different kinetic; illegal occupation; cancellation of source self across unmatched minima |
| A05 | Constant 0<nu<=1; source metric `nu^-2 dr^2+r^2 dOmega^2`; original measure; quadratic `tau nu |grad_g|^2`; same positive complete Green pair law | Weighted Friedrichs H1 on the cone; constant unitary measure normalization; all radial/angular directions | Variable lapse requires `div_g(nu F)` and derivatives; nu>1 invalidates the stated scalar comparison; massive law is separate |

The scalar core comparison requires C>=0, but never C>=A. The sufficient original pair condition is retained literally. The more general algebraic numerator condition would be `vc>=|vp|`; no larger source family is assumed here. Neither source reference minima nor physical ionization/energy transfer are newly proved by FORM.

AF01 must expose a missing source term despite matching field norm. AF02 must expose both a bulk radial error and an interface distribution while the original profile has neither. AF03 must reject a pair-negative member and a member whose kinetic differs from the declared form, with explicit admissible states showing that the copied lower could fail.

Analytic proof, exact symbolic host replay and rational directed enclosures are labeled separately in `OUTCOMES.json`. Original reports are inherited definitions/submissions, not independent outcome evidence. No I2, I3 or R3 classification is assigned here. The next step is case-level source review and relocated public replay.

A05 comparison correction: the actual old geometric reference fills denominators n_r+alpha_l+1 and need not have ordinary w_N. The declared nu=1/2,N=6,C=1,A=1/100,tau=rc=1 member gives original w=49/18. It disproves the blanket strict-improvement wording, with both spectral branches above the core floor. This source comparison and its full complement proof are in `DERIVATION.md` and the final replay A05 fields.
<!-- END FORM/HYPOTHESES.md -->

## ORBITALS/REPORT.md

[Original document](peers/ORBITALS/REPORT.md)

<!-- BEGIN ORBITALS/REPORT.md -->
# ORBITALS verification report

The complete logarithmic and occupied trial witnesses held. Two prose energy displays require last-digit corrections; their underlying directed intervals and every safe prefix agree. All three planned controls exposed the intended error. The public replay also ran from a relocated source closure and reproduced all eight output files byte for byte. The next step is to use these certified orbital inputs in the separate form/reference synthesis.

No fresh scientific attempt failed. Retained earlier failures are the decimal parser predecessor, the six-electron V1 partial-trace interface, and the cusp-only exponential lower-certificate shortcut. They are listed in `FAILURES.json`; the failed native job was recovered byte-for-byte into `recovered_sources` and sealed before dependent execution. A metadata orientation read found that `CUSP_VALIDATION.json` contains a Python literal rather than strict JSON; it was read as text and never became a scientific input.

## Claim outcomes

**B01 — HELD.** `DERIVATION.md` reconstructs the regular/log definitions, the unitary common dilation, all complete Gram/gradient/potential integrals, angular couplings, radius and fourth momentum integrability, and the full Slater normalization formula. `DERIVATION_SUPPLEMENT.md` gives a general finite-family linear-independence/positive-Gram argument. The proof covers every finite L in the stated family. It establishes legal all-space variational states. The numerical witness is finite; no Ritz lower, basis-completeness or exact-ground regularity conclusion is inferred.

**B02 — HELD WITH CORRECTION (display precision).** The normalized exact frozen one-electron Rayleigh value has display **-0.04735264960221189793807378413284**. The complete physical norm has display 0.999999999999999999416673548073807790, and is divided out. The original prose's -0.047352649602211895... was a binary64 midpoint display. The fresh interval overlaps the actual inherited directed interval; no submitted interval was widened. Improvement against the earlier displayed -0.04720781977 is 0.0001448298322118979380737841. The independently rebuilt regular-only frozen comparison has directed display -0.04726522124843130995569721582831; the log ray is strictly better.

**B03 — HELD WITH CORRECTION (display precision).** The exact frozen six-electron trace is **-0.16329578569671925116100439108172**, replacing the earlier prose's floating-discovery display -0.163295785696720.... The full trace is tr(S^-1 H), with every same-spin overlap and Hamiltonian cross term retained. Positive LDL pivots certify each occupied prefix. The same-spin first/second-level overlap is -0.0000000000000007077058235491994725, so rounded columns are handled with the full Gram instead of an exact orthogonality assumption. The fresh regular six-electron comparison is -0.16248000988013438718113682649610.

|Electron count|Directed prefix energy display|Safe positive c_n|
|---:|---:|---:|
|1|-0.04734664715301689880470279102995|2367/50000|
|2|-0.09469329430603379760940558205989|9469/100000|
|3|-0.11534522224532311317215023834785|5767/50000|
|4|-0.13599715018461242873489489463581|13599/100000|
|5|-0.14964646794066583994794964285876|3741/25000|
|6|-0.16329578569671925116100439108172|16329/100000|

The table uses the six-electron file's common fixed a, not the separately optimized N-dependent floating discovery states. All six energy upper endpoints lie below or equal to their declared -c_n. The original determinant has M=-2,Sz=0; the explicitly separate balanced determinant has M=0,Sz=0. Their full one-body Gram and Hamiltonian matrices agree. No preparation was averaged or relabeled. Exact intervals, determinants, pivots and all occupied cross terms are in `attempts/A02_DIRECTED_V1/output/OCCUPIED.json`.

## Control outcomes

**AO01 — HELD.** Omitting the log derivative changed the exact unnormalized l=1,t=1 kinetic integral by -0.0574092886346304574940639471 (correct minus omitted), matching (gamma+log2)/4-3/8. On the actual one-electron witness the wrong derivative produces the invalid energy -0.0515666227970170687951590701. Dropping off-diagonal Gram entries changes its norm to 2.5462129334254237838913156078; the dropped kinetic cross contribution is also nonzero. These are detected changed integrals, not candidate improvements.

**AO02 — HELD.** For the exact nonorthogonal same-spin s-wave toy, full normalization gives1597/868, whereas the independently normalized-column sum is5/4; the exact difference is128/217. Duplicate same-spin columns and a third claimed occupant of one spatial ray with only two spin labels are refused by singular Gram. Actual supplied nonorthogonal but independent occupied columns pass the full determinant treatment.

**AO03 — HELD.** A separately authored regular-only discovery retained every signed m through L=16 and both spins in the occupied sorting, then froze exact decimal rays. Those states received their own directed check. The genuine full-cross-term log computation is separately retained. Neither floating optimization nor L-prefix numerical agreement substitutes for the directed witness proof.

## Evidence and reproducibility

`attempts/A01_REGULAR_DISCOVERY` retains the pre-execution predictions/hashes, independent floating runner, exact frozen comparison files and logs. `attempts/A02_DIRECTED_V1` retains the independently authored directed runner's pre-execution predictions, all source/code/proof hashes and results. `attempts/A03_RELOCATED_REPLAY` retains the relocation preregistration and byte comparison. No original runner was used as the fresh implementation.

The numerical replay made 23485 checks, including all 10512 inherited raw one-electron/occupied image entries. These finite checks verify the stated matrices and witness arithmetic. The written formulas/domain and determinant arguments supply the full-family statements. Complete one-electron G/T/C and moment matrices are retained in `COMPLETE_ONE_MATRICES.json`; the replay generates the |m|=1 primitive matrices and retains their full occupied images. Every number in this report comes from the cited result files or the exact analytic control definitions.

The engine-free replay requires Python3.12+ and python-flint0.8.0. Run from this peer folder:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 scripts/replay_v1.py --out /path/to/clean_output
```

The output directory may be absent or existing empty. `REPLAY.json` specifies every deterministic output and exact/interval comparison rule. Its eight output files were byte-identical after relocating the public scientific source closure. The input seal uses relative paths; no original location or installed research engine is queried. This is a local separately authored code/replay record; no I2, I3 or R3 label is assigned.

## Hypotheses and remaining scope

`HYPOTHESES.md` maps each statement to its assumptions and a concrete failure mechanism. There is no unresolved assigned substatement. The earlier old regular primary coefficients were not reconstructed from their rounded manuscript numbers; the historical improvement comparison is explicitly at displayed precision, and the new upper and fresh regular comparisons are independently directed. Physical energy/length assignment, finite-core/pair/massive transfers, nuclear reference minima, a true ground-state cusp theorem and a new spectral lower are outside these orbital claims.

The useful disclosure is the corrected precision of the frozen energies and the nonzero rounded-column overlaps. Every safe coefficient used by the phase/binding panel remains valid. Continue by replaying the public command and incorporating the corrected displays with the unchanged safe orbital inputs in the separate track synthesis.
<!-- END ORBITALS/REPORT.md -->

## ORBITALS/DERIVATION.md

[Original document](peers/ORBITALS/DERIVATION.md)

<!-- BEGIN ORBITALS/DERIVATION.md -->
# Complete orbital and Pauli reconstruction

This verifies finite trial states of the original noninteracting point operator. The analytic argument covers the full radial integrals and every finite member of the declared regular/log family. The numerical part contracts the supplied primary coefficients; no finite-basis eigenvalue is used as a lower bound. Frozen decimal coefficients mean exact rationals throughout the replay.

## Source and dilation

The manuscript `sources/manuscript/src/atoms_01.tex`, section “Radial binding and the occupied orbital family”, defines
\[
h_U=\tau(-\Delta)-g\,U\cdot n/r,\quad \tau>0.
\]
Rotating the nonzero receiver and using \(r=(\tau/A)\rho\), \(A=g|U|>0\), gives \(h_U=(A^2/\tau)h\), \(h=-\Delta-\cos\theta/\rho\). At zero receiver the continuum infimum is zero. Only this universal point operator occurs below. The finite-core interacting, massive-action and physical-unit accounts have different inputs.

Let \(Y_{lm}\) be the complex orthonormal spherical harmonics with the usual Condon–Shortley phase. Put
\[
f_{ltp}(r)=r^l(\log r)^p e^{-r/t},\quad t\in\{1/2,1,2,4\},\quad
n_{ltp}^2=\int_0^\infty r^{2l+2}(\log r)^{2p}e^{-2r/t}\,dr.
\]
The normalized unit-scale primitive is \(b_{ltp,m}=f_{ltp}Y_{lm}/n_{ltp}\). In a signed \(m\) block, retain \(l=|m|,\ldots,L\), \(p=0\), and append four \(p=1,l=|m|+1\) seeds when enabled. This is exactly the submitted coefficient ordering. The m=0,L=16 regular/log dimensions are 68/72; the |m|=1 log dimension is 68.

The common dilation is the unitary \(D_a b(x)=a^{-3/2}b(x/a)\), \(a>0\). In particular the logarithm becomes \(\log(r/a)\); merely changing the exponential while holding \(\log r\) fixed would be a different coefficient map. The Gram stays G, kinetic scales as \(a^{-2}T\), and positive field matrix as \(a^{-1}C\). Thus \(H(a)=T/a^2-C/a\).

## Complete radial integrals and angular selection

For integer \(k\ge0\), \(\alpha>0\), define
\[
J_k^{(s)}(\alpha)=\int_0^\infty r^k(\log r)^s e^{-\alpha r}\,dr,\quad s=0,1,2.
\]
The gamma integral follows by substitution from \(\Gamma(k+1)=k!\). Differentiating in its real exponent is justified on compact exponent neighborhoods by the integrable majorants near zero and infinity. This yields
\[
J_k^{(0)}=k!\alpha^{-k-1},\quad J_k^{(1)}=J_k^{(0)}d_k,\quad
J_k^{(2)}=J_k^{(0)}(d_k^2+\pi^2/6-H_k^{(2)}),
\quad d_k=H_k-\gamma-\log\alpha.
\]
The recurrence \(\psi(k+1)=H_k-\gamma\), \(\psi_1(k+1)=\pi^2/6-H_k^{(2)}\) follows by logarithmically differentiating \(\Gamma(z+1)=z\Gamma(z)\). The same integral formulas hold for real k>-1 with gamma/polygamma; all replay operands have integer k≥0.

Azimuthal integration enforces equal signed m. Associated-Legendre recurrence and the normalization factorials give
\[
\cos\theta\,Y_{lm}=a_{lm}Y_{l+1,m}+a_{l-1,m}Y_{l-1,m},\qquad
 a_{lm}=\sqrt{((l+1)^2-m^2)/((2l+1)(2l+3))}.
\]
The recurrence is obtained from \((2l+1)xP_l^m=(l-m+1)P_{l+1}^m+(l+m)P_{l-1}^m\); substituting the normalization factors gives the displayed square root. Hence all other angular potential entries vanish. The sphere Laplacian identity \(-\Delta_{S^2}Y_{lm}=l(l+1)Y_{lm}\) gives every angular gradient term by integration by parts.

Write i=(l,t,p), j=(k,u,q), \(\alpha=t^{-1}+u^{-1}\), \(N=n_i n_j\). Suppressing the exact signed-m and spin delta factors,
\[
G_{ij}=\delta_{lk}J_{2l+2}^{(p+q)}(\alpha)/N,
\quad C_{ij}=\mathbf1_{|l-k|=1}a_{\min(l,k),m}J_{l+k+1}^{(p+q)}(\alpha)/N.
\]
For equal l, put \(\beta=1/u\). Applying the radial Laplacian to the right primitive, rather than copying the submitted double-derivative assembly, gives the replay's kinetic formula
\[
T_{ij}=\frac1N\left[
-q(2l+1)J_{2l}^{(p+q-1)}
+2\beta(l+1)J_{2l+1}^{(p+q)}
+2\beta qJ_{2l+1}^{(p+q-1)}
-\beta^2J_{2l+2}^{(p+q)}\right].
\]
Terms with zero q are omitted before evaluating their log order. Since q∈{0,1}, the extra \(-q(q-1)J_{2l}^{(p+q-2)}\) of the general formula vanishes. Unequal-l kinetic entries vanish. This expression is symmetric, although the right-acting expression does not look so. As a separately organized all-entry check, the replay expands
\[
\int_0^\infty[r^2 f_i'f_j'+l(l+1)f_if_j]dr/N,
\quad f_i'=e^{-r/t}[lr^{l-1}\log^p r+pr^{l-1}\log^{p-1}r-t^{-1}r^l\log^p r],
\]
and checks agreement of every nonzero G/T/C entry with the inherited complete integral enclosures wherever supplied. All signed coefficients and all i,j terms occur in contractions, including negative regular/log cross entries. No absolute values or diagonal truncation are used.

For p=q=0, direct simplification gives
\(G_{ij}=[2\sqrt{tu}/(t+u)]^{2l+3}\), \(T_{ij}=G_{ij}/(tu)\). These formulas supply a distinct regular-only discovery implementation. Radius moments have entries \(\delta_{lk}J_{2l+2+s}^{(p+q)}/N\), s≥0.

## Full-space membership and moments

All primitives have exponential tails, so every nonnegative radius moment exists. Near zero the worst added seed is \(r\log r\,Y_{1m}\). Its gradient is O(1+|log r|); the radial volume integral of its square converges. Its Laplacian is O(1/r)+O(|log r|), whose square also has a finite radial-volume integral. For the regular l=0 exponential the worst Laplacian is O(1/r); higher l improve the powers. More generally the p=1 seed at l≥1 has leading Laplacian \((2l+1)r^{l-2}Y_{lm}\), whose squared radial-volume power is \(r^{2l-2}\), integrable for every l≥1. Terms with the exponential derivatives are less singular.

Removing an epsilon ball produces boundary terms tending to zero (the worst radial derivative flux is O(epsilon²|log epsilon|)). Thus these are their weak derivatives, with no origin delta. The functions belong to H¹ and H² on all of R³. In Fourier language, \(\int|p|^4|\widehat\psi|^2=\|\Delta\psi\|_2^2<\infty\); this is the fourth momentum moment meant here. It is not a statement that every higher Sobolev norm exists. Coulomb expectations converge absolutely: the worst value is bounded at zero and radial measure with 1/r leaves r dr. Every finite linear combination and every finite determinant below inherits the form-domain property. This demonstrates valid trial-state membership; it does not assert density of the finite trial span or a regularity theorem for the exact ground state.

The local identity \(\Delta[r\log r\,Y_{1m}]=3Y_{1m}/r\) follows by the same radial formula. It motivates the seed. Inferring a full ground-state cusp theorem from that formal leading balance would require additional hypotheses not used here.

## One-electron witness and directed normalization

A supplied coefficient string c_i is an exact decimal rational. Set \(g=c^*Gc>0\), \(t=c^*Tc\), \(v=c^*Cc\). The exact normalized ray is \(D_a\sum c_i b_i/\sqrt g\), with Rayleigh value
\[
R(a)=(t/a^2-v/a)/g.
\]
There is no assumption that rounded coefficients have g=1 exactly. For fixed coefficients, t>0 and v>0 imply the optimum \(a_*=2t/v\), \(R_*=-v^2/(4tg)\); a stored decimal a is tested directly. The directed value at the frozen a alone supplies the variational upper. Numerical optimization is a discovery observation; the proof is form membership plus this interval-evaluated exact contraction. Improvement against earlier displayed coefficients is a comparison to those declared rounded source values; no old unpublished coefficient is reconstructed from a rounded number.

## General occupied witness, every prefix and spin multiplicity

For spin orbitals \(u_1,\ldots,u_n\), let \(S_{ij}=\langle u_i,u_j\rangle\), \(K_{ij}=\langle u_i,hu_j\rangle\). Exact signed m or spin differences force both entries to zero. Equal-label pairs retain full radial/angular coefficient contractions. If S is positive definite, the normalized antisymmetric state is
\[
\Psi=\frac{1}{\sqrt{n!\det S}}\det[u_j(x_i,\sigma_i)],\quad
\langle\Psi,\sum_i h_i\Psi\rangle=\operatorname{tr}(S^{-1}K).
\]
To derive the normalization, expand both determinants and integrate the product of one-particle overlaps: the permutation sum is n! det S. For the energy, replace one overlap by K in that expansion. The cofactor formula for the derivative of det(S+zK) at zero gives det S tr(S^-1 K), giving the stated ratio. This proof works for nonorthogonal columns; independent column normalization alone is insufficient.

Equivalently S^-1/2 orthonormalizes the occupied span, and the energy trace is invariant under any invertible change of column basis. The replay certifies positive principal minors using directed LDL pivots and computes every n=1,...,6 prefix, with a separate exact rational nonorthogonal toy control. A duplicate same-spin spatial column makes det S=0 and is refused. Only two spin labels accompany any one spatial ray. Opposite signed m states remain distinct orthogonal spatial states.

The original six labels are (0,-1),(0,+1),(0,-1 second level),(0,+1 second level),(-1,-1),(-1,+1). Hence total orbital M=-2 and Sz=0 (spin strings encode twice Sz). The additional balanced file changes only the final m to +1. The two absolute-m=1 radial functions have identical coefficients. Since G/T/C depend on m², the one-body energy is identical; exact spin/angular orthogonality preserves the full matrix. Its totals are M=0,Sz=0. Time reversal maps each occupied pair into its partner up to harmless phase; the original determinant is retained as its distinct preparation.

The safe positive c_n require each complete prefix interval to have upper endpoint ≤-c_n. These prefix energies use the six-electron file's fixed common a; they are not the separately optimized N-dependent floating discovery values. That distinction prevents a shared or mislabeled coefficient from entering phase/binding accounts. This track certifies their orbital inputs, not the independent nuclear reference calculations assigned elsewhere.

## Concrete controls and failed predecessor scope

AO01 omits the +p log^(p-1) derivative in a declared l=1,t=1 log seed, and separately drops off-diagonal Gram/kinetic contributions on the actual one-electron witness. For the unnormalized seed, the exact kinetic difference correct minus omitted is (gamma+log 2)/4-3/8, nonzero. At r=1 the true radial derivative is e^-1 and the omitted derivative is zero. The actual full witness's changed Gram/energy must also be recorded.

AO02 uses two normalized regular s exponentials with t=1 and 2 and the same spin. Their overlap is 16 sqrt(2)/27, S has off-diagonal square 512/729, and the kinetic-only normalized determinant energy is 1597/868. The independently normalized-column sum is 5/4, differing by 128/217. A repeated same-spin column, including a third claimed electron in one spatial ray with only two spins, has zero determinant. Nonorthogonal legal determinants pass only after full Gram normalization.

AO03 retains independently rebuilt regular-only matrices and floating discovery, freezes their rational witness, and submits that witness to the same directed integral contraction. The actual log witness receives its own directed check and full-cross-term replay. Floating agreement is never the certification criterion.

Inherited failed attempts remain source evidence: the decimal parser predecessor used fmpq on decimal strings; the six-electron V1 partial trace had unsupported factor dimensions; the subsequent V2 corrected that interface. The cusp-only exponential Barta attempt has a separate mathematical failure: for g(r)=-r log r/3, the local energy contains a negative log² r term near zero even after the angular 1/r cancellation. Those failures do not alter the supplied variational witness. New failures are retained in versioned attempt directories and never overwritten.
<!-- END ORBITALS/DERIVATION.md -->

## ORBITALS/DERIVATION_SUPPLEMENT.md

[Original document](peers/ORBITALS/DERIVATION_SUPPLEMENT.md)

<!-- BEGIN ORBITALS/DERIVATION_SUPPLEMENT.md -->
# Analytic and precision supplement after the first replay

This supplements the pre-execution `DERIVATION.md` without altering its sealed text. The first replay and all its predictions/code/output are retained under `attempts/A02_DIRECTED_V1`.

## Positive Gram of the whole declared finite family

For each fixed l,m, factor out r^l in a putative vanishing linear combination. The remaining expression is a finite sum of (a_beta+b_beta log r) exp(-beta r), with distinct positive rates beta=1/t. If no logarithmic seeds are present, all b_beta vanish. Divide by the slowest decaying exponential and let r tend to infinity. All faster terms tend to zero even after multiplication by log r. Hence a_beta+b_beta log r tends to zero, which forces b_beta=0 and then a_beta=0. Repeating over the remaining rates sets every coefficient to zero. Different l or signed m are orthogonal angular channels. Thus every finite regular/log basis in the declared family is linearly independent, and its full physical Gram is strictly positive definite. This applies to all L with the declared seeds, not just the numerical L=16 blocks. The finite precision replay separately certifies positive occupied Gram minors for the actual rounded coefficient columns; linear independence of the basis alone would not establish independence of arbitrary chosen columns.

## Correct interpretation of displayed last digits

The primary coefficient files consist of decimal strings, hence exact rationals in this verification. Their exact normalization and complete integral contractions produce the new directed enclosures in `attempts/A02_DIRECTED_V1/output` and overlap every relevant inherited directed enclosure. They have decimal displays

- one electron: -0.04735264960221189793807378413284;
- six electrons: -0.16329578569671925116100439108172.

The earlier prose’s “-0.047352649602211895...” is the binary64 midpoint display, rather than a sequence of certified decimal digits. Its six-electron “-0.163295785696720...” matches floating discovery and differs by approximately 1.4e-15 from the primary frozen-rational directed value. The interval evidence, variational improvement and all six safe c_n remain held. B02 and B03 receive HELD WITH CORRECTION for those displayed digits and for treating rounded columns as exactly normalized or orthogonal. No submitted scientific interval was enlarged to obtain this result.

The frozen one-electron norm is near one but not exactly one. Its stored a is near 2T/C but is an exact decimal approximation, so the exact frozen virial residual need not contain zero. The replay computes the Rayleigh quotient at that a directly. Its tiny nonzero virial residual does not enter a claim of exact stationarity. The fixed-coefficient algebraic optimum is separately enclosed.

## Meaning of the failed controls

The omitted log derivative makes the actual one-electron control energy artificially more negative (approximately -0.0515666227970171). This is an invalid gradient expectation; interpreting the change as an improvement would be an error. The exact l1,t1 control difference has the predicted nonzero sign. Discarding all off-diagonal Gram entries changes the same witness’s norm to approximately 2.54621293342542, so independently normalizing primitive contributions cannot reconstruct this source ray.

The frozen two same-spin m=0 levels are close to orthogonal, but their overlap is nonzero. Full determinant normalization is the analytic rule, regardless of how small the numerical correction is. The nonorthogonal toy makes the error macroscopically visible, while exact duplicate same-spin rays are refused.

Next step: replay the public command in a clean relocated directory, then review the corrected displayed digits alongside the unchanged safe prefix coefficients.
<!-- END ORBITALS/DERIVATION_SUPPLEMENT.md -->

## ORBITALS/HYPOTHESES.md

[Original document](peers/ORBITALS/HYPOTHESES.md)

<!-- BEGIN ORBITALS/HYPOTHESES.md -->
# Hypotheses and evidence map

B01–B03 concern the original noninteracting point-source quadratic operator in `sources/manuscript/src/atoms_01.tex`. They use the spin-two fermionic preparation, the complete radial interval (0,infinity), and all signed magnetic labels attached to the supplied states.

| Hypothesis | Role | What breaks if changed | Evidence |
|---|---|---|---|
| tau>0 and A=g|U|>0 for universal dilation; U=0 handled as free continuum | Defines h=(A²/tau)[-Delta-cos(theta)/r] | A finite-core or massive kinetic operator has different matrix elements and domain | Analytic source scaling in DERIVATION.md |
| Orthonormal complex Y_lm and two orthonormal spin labels | Fixes angular coefficients, exact selection zeros and Pauli multiplicity | Reusing a same-spin spatial ray makes the determinant vanish | Analytic recurrence, full spin/m image, AO02 |
| r^l exp(-r/t) and appended r^(|m|+1)log(r)exp(-r/t), t=1/2,1,2,4 | Defines the exact family and coefficient ordering | Changing powers, logs, angular factors or normalization changes the ray | Exact input hashes, general integral proof and all-entry replay |
| D_a is unitary; log becomes log(r/a) | Preserves Gram and gives T/a²-C/a | Changing only the exponential while holding log r fixed is a different state | Analytic dilation proof |
| Frozen decimal strings are exact rational coefficients and a | Defines a reproducible ray, without trusting floating eigenvectors as exact eigenvectors | Treating rounded norm or cross overlaps as exact can change the normalized energy | Directed complete Gram contractions |
| g=c*Gc>0, and occupied S positive definite | Makes Rayleigh/determinant normalization valid | Singular duplicate columns have no normalized Slater state | Directed LDL pivots, analytic determinant formula, duplicate controls |
| Every signed cross coefficient is retained | Specifies the actual source expectation | Dropping primitive cross terms changes norm and kinetic action; taking absolute values would also define another contraction | AO01 and complete all-entry G/H comparisons |
| Original and balanced six-state preparations are distinct | Keeps M and spin conventions explicit | Assigning M=0 to the original M=-2 state mislabels the preparation | Exact integer label sums and full matrix comparison |
| Full infinite radial integrals and H1/H2 trial membership | Gives legal all-space variational witnesses with finite fourth momentum moment | A cutoff-only computation would require extra boundary/complement work | Analytic origin/tail proof; complete gamma-log formulas |

The analytic statements apply to every finite L in the declared family. The numerical witness checks are the actual supplied L=16 m=0 and |m|=1 states, all six prefixes, the balanced file, and fresh regular comparison rays. Their scope is not an all-L convergence theorem or a ground-state regularity statement.

The safe prefix coefficients are one-sided variational uppers for the full point Hamiltonian. Combining them with a full-space lower or a nuclear reference requires those separate proofs and conventions. This track does not compute the FORM or REFERENCES assignments.

Evidence is separated as follows:

- **Analytic:** complete gamma/log and angular formulas, H1/H2 membership and fourth momentum integrability, finite-family Gram positivity, determinant normalization and trace formula, unitary dilation, balanced-preparation equality.
- **Directed host:** Arb384 complete primary contractions and all occupied-prefix Gram solves; exact rational outward endpoints. No installed research engine is executed.
- **Exact host:** Fraction source/input hashes, exact rational bounds and comparisons, integer m/spin totals, closed rational AO02 answer.
- **Floating diagnostic:** separately authored regular-only Ritz discovery and inherited log discovery. These generate/compare candidate states and carry no directed certificate by themselves.
- **Inherited evidence:** supplied raw integral enclosures, original source reports, native readback/failed-job records, earlier displayed regular energies and the failed Barta shortcut. Fresh code does not import or execute the earlier implementation.

The prior older regular witness coefficients are not reconstructed from their rounded manuscript energies. Comparisons to those historical numbers are explicitly at their displayed precision; the new ray's upper bound has its own complete directed certificate. The fresh regular comparison states have both retained floating discovery and fresh directed certificates.

No I2, I3 or R3 classification is assigned. The separately authored code and relocated local replay are the facts retained here.

Next step: replay the command in REPLAY.json and compare the exact metadata, interval fields and safe-prefix inequalities before combining these orbital inputs with the other tracks.
<!-- END ORBITALS/HYPOTHESES.md -->

## REFERENCES/REPORT.md

[Original document](peers/REFERENCES/REPORT.md)

<!-- BEGIN REFERENCES/REPORT.md -->
# REFERENCES result

One operational file audit initially failed because it matched the word
“subprocesses” in a docstring. Its failing predicate and traceback are retained
in `audits/001_false_positive.json`; the syntax-tree successor passes.
No scientific runner or result changed in that correction.

All five assigned claims held. All three controls detected the specified
changes. There were no failed scientific attempts or unexpected controls in
this track. The complete original source, each occupied prefix, every
submitted point account and both finite-core reference comparisons were
reconstructed with new code and a complete written derivation. A local
relocation replay produced seven byte-identical result files.

**Locked.** C01-C05 and AR01-AR03 are fully recorded in
`OUTCOMES.json`. The derivation is `DERIVATION.md`, including every q minimum,
all 50 phase/inventory guarantees and all 44 populated point accounts.
`HYPOTHESES.md` maps each result to its source and transfer boundary.

**Still owed.** The lead's aggregate reading and clean case replay remain
outside this track. This work does not assign external independence or an
outside-party replay classification. No assigned scientific substatement is
unresolved.

## Results against the assignment

| Claim | Result | Evidence and meaning |
|---|---|---|
| C01 | HELD | Re-enumerated all 8192 original core histories from motif incidence, matching every complete core DOS entry. Exact receiver elimination retained 49 sectors per helium and 361 per carbon, all original histories, ground multiplicities, five envelopes and eleven phases. |
| C02 | HELD | Fresh full integrals and occupied Gram cofactors certify each of the six common-dilation prefix uppers. Their own coefficients and the analytic whole-space -n/16 lower give all six strict intermediate guarantees; all 50 original phase/inventory combinations are explicit. |
| C03 | HELD | Exact minimization over every original conditional sector reproduces all 44 submitted rational point binding accounts at both couplings, with ten zero empty controls and the correct free-electron nuclear reference. |
| C04 | HELD | Both reference operations retain core self. All three exact separated minima and complete max(spectral,core-floor) lower-comparison minima were recomputed. The generic upper endpoints are exactly 5733/185, 5992/185 and 6732/185. |
| C05 | HELD | Every low-q C444 class obeys the original intrinsic gap; its exact ratio maximum is 3/20. The independently justified separated minimum and atom lower-comparison minimum give 1377/50+(27/5)*sqrt(2). |

At g=tau=1 the conservative point neutral intervals are [0.37876,0.5],
[1.51504,2], [5.87844,13.5], [10.45056,24], and [23.51376,54], in the
source order He4 cover 3, He4 cover 4, C333, C343, C444. Every other point
account and its source/reference is in
`attempts/002/output/POINT_BINDING_ALL44.json`. The whole-space electronic
cap improves exactly fourfold; the complete C333/C343 n=6 binding caps
improve by more because the older n/4 lower selected another nuclear phase.
The lower binding endpoints remain trial-supplied and the upper endpoints
remain whole-space-lower-supplied.

The six intermediate guarantees are sufficient open chi intervals, not exact
transition values. Their exact endpoints are in
`attempts/002/output/SIX_PHASE_GUARANTEES.json`. The first common-dilation
prefix expectation is approximately -0.0473466471530169, distinct from the
separately optimized one-electron witness. It certifies its own 0.04734
safe coefficient; no optimized one-electron coefficient was reused for
other inventories.

For weak finite-core carbon the exact separated minima are 1689/5,1656/5,
1536/5 at q36,q64,q144. The full finite roster yields complete binding
upper endpoints approximately 30.9533766184074,32.3311688245431,
35.1767532368147. The first two are additional contractions of the complete
finite roster and are slightly tighter than the valid submitted generic
relaxations. They are recorded separately in
`attempts/002/output/FINITE_CORE_COMPLETE.json`, not used to relabel a
weaker valid result as a failure.

For C444 the submitted sharper upper is approximately 35.1767532368147,
an improvement of 3.7032467631853 from 38.88. The intrinsic-gap maximum
attainers are q=0,18,36,72,90. The full max-bound contraction also confirms
that the finite-core floor wins for inventories 1,2,3; the spectral branch
wins for 4,5,6. The spectral inventory extension therefore carries no claim
of six strict improvements in final existing accounts. These minima are
rigorous lower-comparison minima; the interacting exact ground itself was
not computed.

## Controls and retained attempts

AR01 uses c6 for n1,...,5 and substitutes g for g squared in one account.
Each false prefix cap is refuted by its own directed expectation. The wrong
coupling changes the C444,N6,g=1/10 safe binding lower by exactly a factor
ten. AR02 flattens the C444 source gap, moving the spectral comparison
minimum to q50, and separately omits core self from the separated minimum,
missing 126/5 of the actual reference. AR03 accepts the point contract and
rejects finite-core/pair/self, ionization, massive-action and uncalibrated
eV transfers. Their full retained altered values and criteria are in
`attempts/002/output/CONTROLS.json`.

Attempt 001 passed the complete assigned claims and controls. Attempt 002
keeps that implementation and explicitly adds the full 50 phase/inventory
guarantees. It is a coverage successor, not a failure repair. Attempt 003
copies the unchanged public dependency closure into another case root and
replays there. All seven deterministic JSON outputs byte-match attempt 002;
the comparison and execution receipts are retained. All arithmetic executions
passed; the separate operational audit false positive is retained above.
Every scientific attempt has a timestamped preregistration,
runner/input hashes, concrete control criteria and a run receipt.

## Method and reproduction

The replay is newly authored host work: exact integer/Fraction source
enumeration, directed Arb integrals/radical comparisons and analytic proof.
The earlier scripts were read as definitions/reference and never imported
or executed. Missing small original public operands were recovered into
`recovered_sources/` and sealed before the first dependent calculation.
Source and copy hashes agree. No installed research engine is needed.

Run from the complete case root with Python 3.12 and the pinned dependency:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 peers/REFERENCES/scripts/replay_v2.py --output /path/to/clean/output
```

`REPLAY.json` specifies input closure, exact and interval comparisons,
deterministic hashes and the retained local relocation. The replay accepts
any clean output directory; all data paths resolve relative to the relocated
case. The recorded execution used the provided Python environment with
python-flint 0.8.0, one arithmetic process and single-thread settings.

The point, finite-core, ionization and massive/physical-unit accounts retain
their separate meanings. Existing pair/outer-filling binding lower witnesses
are inherited evidence and were not regenerated. No engine, manuscript,
Git, external service or other peer folder was changed. The next step is
the aggregate case review and public replay after every track has finished.
<!-- END REFERENCES/REPORT.md -->

## REFERENCES/DERIVATION.md

[Original document](peers/REFERENCES/DERIVATION.md)

<!-- BEGIN REFERENCES/DERIVATION.md -->
# REFERENCES derivation

The original source bounds survive reconstruction. The point-source accounts
use the complete original nuclei and their own separated reference. The
finite-core conclusions use a different Hamiltonian, keep core self in both
minima, and bound total binding. The replay supplies exact finite source
enumeration and directed integral/radical certificates; the arguments below
supply the form-domain and all-source implications.

Canonical numerical evidence is `attempts/002/output/`. The earlier complete
attempt is retained in `attempts/001/`. The dependency-closure relocation is
retained in `attempts/003_relocated/`. No original script is imported or run.

## 1. Recovering the original nuclear source

Let the isolated K4 have the six edges in the order recorded by
`recovered_sources/qa_core_CONTRACT.json`:

\[
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3).
\]

Its incidence column is -1 at its first endpoint and +1 at its second. Write
this four-by-six matrix as B. Each phase is independently in
\(\{1,i,-1,-i\}\), and \(u=\sum_{j=0}^{5}z_j\) is the INITIAL receiver.
For each retained pair edge (a,b), its current vector is \(B_a-B_b\).
The original cover-3 pair edges are the local edges 0,3,4; its triangle
vector is local \((0,1,-1,0,0,1)\). The cover-4 pair edges are 0,1,2;
its triangle vector is local \((0,0,0,1,-1,1)\). Thus the precise isolated
source is

\[
 E_c(z)=\frac{43}{4}\sum_{(a,b)\in P_c}
       |(B_a-B_b)z|^2+24|v_cz|^2.                 \tag{1}
\]

The coefficient 24 is the retained observed triangle coefficient 72 divided
by its three edges. There is no Li6 center or depth term. These vectors and
coefficients are also written explicitly in
`NUCLEAR_RECONSTRUCTION.json:core_checks`.

Every assignment of the six four-valued phases appears exactly once in the
Cartesian product in `reconstruct_cores`. The state address is
\(\sum_j \mathrm{phase}_j4^j\), the original address convention. Its
energy is evaluated at denominator four with integer squares. Histograms
are accumulated by the two integer components of u. This gives all 49
receivers in \(|u_x|+|u_y|\leq6\), \(u_x+u_y\) even. The replay checks
every histogram entry, conditional minimum, ground multiplicity and minimum
state address against the sealed original complete core DOS. In particular,
both cores have intrinsic ground 110 with 144 histories. The complete DOS
comparison, rather than only a ground comparison, also checks the original
phase and address conventions.

For each core let

\[
 e_c(u)=\min_{z:\,\sum z=u}E_c(z),\qquad
 d_c(u)=\#\{z:E_c(z)=e_c(u),\ \sum z=u\}.
\]

For carbon, all three contact edges are present (mask 7), with ordered cover
triples (3,3,3), (3,4,3), and (4,4,4). Its source is exactly

\[
 I(z_1,z_2,z_3)=\sum_{a=1}^{3}E_{c_a}(z_a)
             -\sum_{a<b}\operatorname{Re}(\overline{u_a}u_b),
 \qquad U=\sum_a u_a.                            \tag{2}
\]

At fixed receivers the contact term is constant. Therefore replacing each
core by its conditional minimum is an exact ground elimination, not a cut
to unconditionally prepared core grounds. Every other intrinsic history is
still represented in the complete count. For every U,

\[
 I(U)=\min_{u_1+u_2+u_3=U}
       \left[\sum_a e_{c_a}(u_a)-\sum_{a<b}u_a\cdot u_b\right]. \tag{3}
\]

Multiplicities of a minimizing triple multiply; multiplicities of distinct
minimizing triples add. The total number of histories attached to each U is
computed from the full core histogram masses, not their ground masses.
Consequently summing those masses gives \(4096^3=68719476736\) for each
carbon source. All \(49^3\) receiver triples are examined. They produce
361 U sectors. The change of coordinates

\[
 M=U_x+U_y,\quad T=U_x-U_y
\]

gives exactly all ordered \((M,T)\in\{-18,-16,\ldots,18\}^2\), matching
the original two-half-source convention. This proves the source elimination
covers every original phase and conditional sector.

For the electron recipient only \(q=|U|^2\) enters. Define
\(I(q)=\min_{|U|^2=q}I(U)\), keeping all attaining sectors and counts.
Both helium sources have ten q classes and each carbon has 51. The complete
conditional sector and q tables are in `NUCLEAR_RECONSTRUCTION.json`; the q
minima are also listed in the appended finite certificate below. Their
intrinsic ground energies and full ground multiplicities are

| Source | Intrinsic ground | Ground histories |
|---|---:|---:|
| He4 cover 3 | 110 | 144 |
| He4 cover 4 | 110 | 144 |
| C333 | 318 | 2916 |
| C343 | 310 | 324 |
| C444 | 282 | 4 |

The two helium intrinsic grounds include several q values: respectively
\(\{0,2,4\}\) and \(\{0,2,4,8,10,16\}\). At any sufficiently small
strictly positive point coupling the largest ground q is selected. At t=0
all original intrinsic ground sectors remain; no uniqueness at zero coupling
is claimed.

## 2. Complete point nuclear envelopes (C01)

For each q, the line is \(I(q)-tq\). It is minimal among every original line
precisely when

\[
 t\geq\max_{p<q}\frac{I(q)-I(p)}{q-p},\qquad
 t\leq\min_{p>q}\frac{I(p)-I(q)}{p-q}.          \tag{4}
\]

Intersect with t>=0. Empty or zero-length intersections supply no open phase,
although their boundary ties remain in the original source table. Applying
(4) to every row of the complete q tables gives:

| Source | Open-phase q and I | Successive transition t |
|---|---|---|
| He4 cover 3 | (4,110), (36,282) | 43/8 |
| He4 cover 4 | (16,110), (36,626) | 129/5 |
| C333 | (36,318), (324,738) | 35/24 |
| C343 | (64,310), (256,590), (324,1082) | 35/24, 123/17 |
| C444 | (144,282), (324,1770) | 124/15 |

Formula (4) proves domination against the full roster, including sectors
which are never selected for positive t. It reconstructs every one of the
eleven open phases and all six transitions. At a transition the adjacent
lines, and any collinear original rows, retain their ties.

The point separated reference is \(E_{\rm sep}=\min_q I(q)\): the ground
infimum of each free electron is zero, with the same fixed inventory on both
sides. This is an absolute intrinsic ground reference, not a thermal
free-energy or finite-core reference.

## 3. Whole-space electronic lower used by the references

Let \(\tau>0\), \(A\geq0\), a fixed unit axis e, and

\[
 h_A=\tau(-\Delta)-A(e\cdot n)/r,
 \qquad F=\frac{A}{4\tau}[2(e\cdot n)n-e].      \tag{5}
\]

Put c=e.n. Since \(\nabla c\cdot n=0\) and div n=2/r,

\[
 |2cn-e|^2=1,\quad \operatorname{div}(2cn-e)=4c/r.
\]

Thus \(|F|^2=A^2/(16\tau^2)\) and div F=Ac/(tau r). On compact smooth
functions away from the origin, integration of the real cross term gives

\[
 q_{h_A}[\psi]
 =\tau\|\nabla\psi+F\psi\|^2
      -\frac{A^2}{16\tau}\|\psi\|^2.            \tag{6}
\]

The bounded field's flux through a shrinking sphere is O(r^2), so the weak
divergence has no origin distribution. The Coulomb form is continuous on
H1: Hardy and Cauchy-Schwarz give
\(\int |\psi|^2/r\leq2\|\nabla\psi\|\|\psi\|\).
Compact smooth functions avoiding the origin are dense in H1 in three
dimensions. For example a cutoff of radius epsilon on a smooth compact
function has gradient-error square O(epsilon); then use ordinary H1 density.
The bounded F term is also continuous. Therefore (6) holds on all H1, and

\[
 h_A\geq-A^2/(16\tau).                          \tag{7}
\]

Sum the form inequality in all electron variables and spins before restricting
to the antisymmetric sector. The universal n-electron coefficient obeys
\(e_n\geq-n/16\). This argument covers every radial and angular direction.
No finite matrix complement or saturation of the nongradient F is assumed.

## 4. Independently reconstructed occupied uppers (C02)

The literal frozen input is `prior/FOUR/gen/cusp_occupancy6_witness.json`.
Each spatial seed before common dilation is

\[
 b_{l,t,p,m}(r,\Omega)
 =N_{l,t,p}^{-1}r^l(\log r)^p e^{-r/t}Y_{lm}(\Omega),
 \quad t\in\{1/2,1,2,4\},\ p\in\{0,1\}.       \tag{8}
\]

The logarithmic seeds have l>=1. Near zero, their radial and angular
derivatives have square-integrable \(r^{l-1}(1+|\log r|)\) behavior in
the three-dimensional measure. At infinity exponential decay controls all
integrals. Thus every frozen orbital belongs to the full H1 form domain.
The dilation is applied to the whole seed function, so its logarithm is the
dimensionless log(r/a), as prescribed by the frozen shape.

For \(k\geq0\) and \(\alpha>0\), let

\[
 J_k^{(p)}(\alpha)=\int_0^\infty r^k(\log r)^p e^{-\alpha r}dr.
\]

Differentiating the Mellin integral twice, justified by exponential decay and
integrable powers times logs at zero, gives

\[
\begin{aligned}
 J_k^{(0)}&=k!\alpha^{-k-1},\\
 J_k^{(1)}&=J_k^{(0)}(H_k-\gamma-\log\alpha),\\
 J_k^{(2)}&=J_k^{(0)}[(H_k-\gamma-\log\alpha)^2
                              +\pi^2/6-H_k^{(2)}].              \tag{9}
\end{aligned}
\]

Here \(N_{l,t,p}^2=J_{2l+2}^{(2p)}(2/t)\). Equal l,m seeds have Gram
\(J_{l+k+2}^{(p+s)}(1/t+1/u)/(N_iN_j)\). For the kinetic form, differentiate
each raw radial factor explicitly:

\[
 [r^l(\log r)^p e^{-r/t}]'
 =e^{-r/t}[l r^{l-1}(\log r)^p
       +p r^{l-1}(\log r)^{p-1}-t^{-1}r^l(\log r)^p].          \tag{10}
\]

Multiply both derivatives, integrate with measure r^2dr, and add
\(l(l+1)J_{l+k}^{(p+s)}/(N_iN_j)\). Equation (10) includes the log derivative
and every signed cross term. Other l values have zero kinetic/Gram entry.
For the potential, the only nonzero angular entries connect neighboring l:

\[
 \langle Y_{l+1,m},\cos\theta Y_{lm}\rangle
 =\sqrt{\frac{(l+1)^2-m^2}{(2l+1)(2l+3)}}.                    \tag{11}
\]

Multiply by \(J_{l+k+1}^{(p+s)}/(N_iN_j)\). Equations (9)-(11), with
H=T/a^2-V/a, reconstruct all occupied Gram and Hamiltonian entries without
using the earlier integral files.

The frozen coefficients are decimal strings interpreted as exact rationals.
Spin and signed m are literal labels. Different spin or signed m blocks are
exactly orthogonal. For same labels, full off-diagonal Gram and Hamiltonian
entries remain. Every occupied block is either one-dimensional or
two-dimensional. Positivity is certified by G11>0 and, for two states,
\(G_{11}G_{22}-G_{12}G_{21}>0\). Hence every prefix defines an admissible
nonzero Slater determinant with no spin multiplicity excess.

For linearly independent spin orbitals \(\phi_i\), cofactor expansion of
their normalized determinant gives

\[
 \mathcal E_n=\operatorname{tr}(G_n^{-1}H_n).                 \tag{12}
\]

In a two-state block this is exactly
\((G_{22}H_{11}+G_{11}H_{22}-G_{12}H_{21}-G_{21}H_{12})/\det G\).
The new implementation uses this cofactor formula, rather than importing an
engine solve or the submitted contracted matrices. Arb directed arithmetic
encloses each complete integral and proves each Gram determinant positive.

`OCCUPIED_PREFIXES.json` gives the six full expectation intervals. In order,
their displayed values are approximately

\[
 -0.0473466471530169,\ -0.0946932943060338,\ -0.1153452222453231,
\quad -0.1359971501846124,\ -0.1496464679406658,\ -0.1632957856967193.
\]

These are the prefixes of the common six-electron witness. The first is not
the separately optimized one-electron witness from the other track. Each
directed upper endpoint is strictly below its own conservative -c_n:

\[
 (c_1,\ldots,c_6)
 =(2367/50000,9469/100000,5767/50000,
   13599/100000,3741/25000,16329/100000).          \tag{13}
\]

By the variational principle, \(e_n\leq\mathcal E_n<-c_n\). The intervals
in this paragraph enclose witness expectations, not a lower on the exact
ground. Combining (7) and (13) gives
\(-e_n\in[c_n,n/16]\).

## 5. Six intermediate guarantees and every phase (C02)

Rotation and dilation \(r=(\tau/A)\rho\) give
\(h_A=(A^2/\tau)[-\Delta_\rho-\cos\theta/\rho]\).
For A=0 the unchanged free continuum has infimum zero, consistent with the
same final q-multiplied expression without dividing by A.
Therefore the original full nuclear/electronic ground is exactly

\[
 \min_q\{I(q)-tq\},\qquad t=\chi(-e_n),\quad \chi=g^2/\tau. \tag{14}
\]

The complete C343 intermediate phase is selected for
\(35/24<t<123/17\). Every value of the unknown full-space coefficient
inside its rigorous bounds lies in this phase whenever

\[
 \frac{35/24}{c_n}<\chi<\frac{1968}{17n}.                    \tag{15}
\]

The six exact open intervals are

| n | Lower chi | Upper chi |
|---:|---:|---:|
| 1 | 218750/7101 | 1968/17 |
| 2 | 437500/28407 | 984/17 |
| 3 | 218750/17301 | 656/17 |
| 4 | 437500/40797 | 492/17 |
| 5 | 109375/11223 | 1968/85 |
| 6 | 437500/48987 | 328/17 |

The replay checks exact endpoint multiplication and positive rational width
for each row. They are six separate sufficient intervals. No common
intersection, exact transition, or approximation \(e_n=-c_n\) is used.

More generally, for each open nuclear phase \((t_L,t_R)\), its sufficient
chi interval is \((t_L/c_n,t_R/(n/16))\), with the infinite endpoint retained.
`SIX_PHASE_GUARANTEES.json:all_fifty_phase_guarantees` records every one of
the 50 original phase/inventory combinations. All are nonempty. Retaining
the old n/4 lower with these same fresh uppers leaves exactly the six C343
intermediate guarantees empty and the other 44 nonempty. This explicitly
separates the electronic lower improvement from changes to the occupied
upper witnesses.

## 6. All original point binding accounts (C03)

The declared panel is tau=1, g=1/10 or 1, He N=1,2, and carbon N=1,...,6.
For every account

\[
 0<t\leq ng^2/16\leq3/8<35/24,
\]

and each helium first transition is still larger. Therefore every full
ground is in its original baseline positive-response phase, with
q0=4,16,36,64,144 in source order. Equations (2)-(4) justify this against all
conditional nuclear sectors, not just a baseline comparison. Thus

\[
 E_{\rm atom}=I_0-q_0\chi(-e_n),\quad
 B=E_{\rm sep}-E_{\rm atom}=q_0\chi(-e_n),
\quad q_0\chi c_n\leq B\leq q_0\chi n/16.                  \tag{16}
\]

`POINT_BINDING_ALL44.json` separately minimizes every original conditional
sector at both bounds and proves those minima equal (16). All 44 submitted
rational accounts match; all ten empty panel controls give zero. At g=1 the
neutral intervals are [0.37876,0.5], [1.51504,2], [5.87844,13.5],
[10.45056,24], and [23.51376,54]. At g=1/10 both endpoints are divided by 100.
The lower endpoint is supplied by an actual Pauli trial upper on energy;
the upper endpoint is supplied by the whole-space lower on energy.

The change n/4 to n/16 is exactly a factor four in the universal electronic
cap. The complete binding upper need not change by exactly four: recomputing
the old full minima gives old neutral g=1 caps 2,8,66,104,216, while the new
caps are 0.5,2,13.5,24,54. The old C333 and C343 n=6 lowers already selected
another nuclear phase, so their complete ratios exceed four. This is why
the old nuclear minimization cannot be replaced by q0*n/4 in those accounts.

These are total binding in the original noninteracting quadratic point model.
They do not specify ionization energy, finite-core binding, massive kinetic,
or a physical energy conversion.

The predecessor also has no maximal finite occupation by itself. Fix a smooth
angular function inside a cap where cos(theta)>=c0>0 and a radial bump on
[1,2]. Dilate that state onto [R,2R]. Its kinetic form is K/R^2 and its
attractive potential is -A*J/R with J>0, so its energy is negative for large
R. Arbitrarily many sufficiently separated annuli have disjoint supports
and zero quadratic cross terms, furnishing arbitrarily many negative
min-max directions. The Coulomb-type perturbation has essential threshold
zero; hence these are arbitrarily many negative one-body levels. Distinct
orbitals and the two spin labels allow every finite noninteracting inventory.
The 44-account panel is therefore not a prediction of a maximal physical
charge inventory; the later scalar/pair source has its own question.

## 7. Finite-core Pauli lower on its actual source

For this part alone the Hamiltonian is the original finite-core interacting
recipient, with \(C=g_cZ\geq0\), \(A=g_p\sqrt q\geq0\), rc,tau>0, and

\[
 V(x)=-(C+A\cos\theta)/\max(r,r_c),\qquad
 W(x,y)=(v_c+v_p n_x\cdot n_y)/|x-y|,
\quad v_c\geq v_p\geq0.                                    \tag{17}
\]

The full pair form is nonnegative. It is discarded only for a lower.
Multiply F in (5) by

\[
 h(r)=\begin{cases}4r/(5r_c)&r\leq r_c,\\
                     1-r_c^4/(5r^4)&r\geq r_c.\end{cases}    \tag{18}
\]

Both h and h' match at rc; h vanishes at zero, 0<=h<=1, and
\(h'+4h/r=4/\max(r,r_c)\). Its weak divergence is exactly the anisotropic
potential divided by tau, without an origin or interface distribution.
Completion of the full gradient form and \(|hF|\leq A/(4\tau)\) give
the same anisotropic lower \(-A^2/(16\tau)\). No sign of
\(C+A\cos\theta\) is assumed.

Split the same kinetic form into theta and 1-theta portions. For the scalar
part, \(-C/\max(r,r_c)\geq-C/r\). The full Coulomb spin-two spectrum
has negative levels \(-C^2/(4\theta\tau k^2)\), with multiplicity 2k^2;
separation into radial/angular equations gives these hydrogenic levels and
nonnegative continuum. Filling distinct spin states gives, for n<=6,

\[
 w_n=\min(n,2)+\max(n-2,0)/4.
\]

The scalar Pauli sum and the distinguishable anisotropic sum therefore give

\[
 E_{e,n}\geq-\frac{C^2w_n}{4\theta\tau}
              -\frac{nA^2}{16(1-\theta)\tau}.
\]

For completeness, the negative scalar spectrum used here follows directly
from the radial equation. With kinetic coefficient kappa0=theta*tau, put
\(u=rR\), energy \(-\kappa_0\eta^2\), and \(\rho=2\eta r\).
The regular H1 solution has
\(u=e^{-\rho/2}\rho^{l+1}y(\rho)\), where

\[
 \rho y''+(2l+2-\rho)y'
       +[C/(2\kappa_0\eta)-l-1]y=0.
\]

Square integrability at infinity requires the regular series to terminate
at a nonnegative integer j. Thus \(\eta=C/[2\kappa_0(j+l+1)]\), giving
principal k=j+l+1 and the displayed energies. For each k, l=0,...,k-1 and
m=-l,...,l give \(\sum_l(2l+1)=k^2\) spatial states; spin doubles this.
The regular boundary condition and termination characterize all negative
levels. The Coulomb form is relatively compact at the free threshold, so
the remaining spectrum has lower edge zero. On an antisymmetric n-body
state its one-particle occupation numbers lie between zero and one and sum
to n, hence the minimum sum fills these levels in this order. This also
justifies the Pauli comparison for correlated fermionic states, without
assuming their states are determinants.

For a,b>=0, \(\inf_{0<\theta<1}[a/\theta+b/(1-\theta)]
=(\sqrt a+\sqrt b)^2\); endpoint cases follow by limits. Consequently

\[
 E_{e,n}(q)\geq L_n(q):=
 -\frac{[C\sqrt{w_n}+(A/2)\sqrt n]^2}{4\tau}.               \tag{19}
\]

Also retain the independent core floor
\(E_{e,n}\geq-n(C+A)/r_c\), so the lower actually used is the maximum
of these two expressions. This is a statement about the quadratic kinetic
on the full fermionic form domain. Replacing it by a smaller massive kinetic
does not preserve this lower inference.

## 8. Generic complete carbon references (C04)

The submitted weak neutral panel has
\(\tau=r_c=g_c=v_c=1\), \(g_p=v_p=1/10\), Z=n=6 and w6=3. The exact
core self on the same source is

\[
 S(q)=18+q/20.
\]

The two references are independently defined by

\[
 E_{\rm sep}=\min_q[I(q)+S(q)],\quad
 E_{\rm atom}=\min_q[I(q)+S(q)+E_{e,6}(q)].                  \tag{20}
\]

No q-dependent self is cancelled before these minimizations.
The common regularized electron self, n*(vc+vp)/(2re), is identical at fixed
inventory in the coupled and separated preparations. It cancels before the
point-electron limit. The q-dependent nuclear core self is not common across
distinct minimizing states and remains in (20).

Equation (19) specializes to

\[
 L_6(q)=-27-3q/800-(9\sqrt2/20)\sqrt q.
\]

Put \(a=37/800\), \(b=9\sqrt2/20\). Since I(q)>=I0 for every original
source state, completing a square in y=sqrt(q) gives the continuous lower
relaxation

\[
 E_{\rm atom}\geq I_0-9+\inf_{q\geq0}(aq-b\sqrt q)
 =I_0-9-81/37,                                             \tag{21}
\]

at the relaxed \(q=64800/1369\). This need not be an allowed source q.
An actual baseline q0 separately supplies
\(E_{\rm sep}\leq I_0+18+q_0/20\). Subtract the atom lower from this
separated upper in this order:

\[
 B\leq27+q_0/20+81/37.
\]

This gives exactly C333 5733/185, C343 5992/185, and C444 6732/185. The
complete finite roster is also independently contracted in
`FINITE_CORE_COMPLETE.json:generic_three_carbon`: every q participates in
the exact separated minimum and in the directed minimum of
\(I(q)+S(q)+\max\{L_6(q),-6(C+A)\}\). Their separated minima are,
respectively, 1689/5 at q36, 1656/5 at q64 and 1536/5 at q144. All three
equal the submitted admissible separated uppers. This equality was computed;
it was not needed to justify the weaker generic endpoints.

The finite-roster comparison selects q36,64,144 respectively and yields
binding upper endpoints approximately 30.9533766184074, 32.3311688245431,
35.1767532368147. The first two are additional finite-roster contractions,
not replacements of a false submitted generic result. The generic bounds
are valid weaker bounds. None of these contractions computes the exact
interacting electronic ground or a new occupied upper witness.

## 9. The original C444 intrinsic gap and both minima (C05)

All 51 original C444 q classes are retained in the preceding source proof.
For every q<144 their exact table gives

\[
 \max_{q<144}\frac{144-q}{20[I(q)-282]}=3/20,
 \quad I(q)-282\geq(144-q)/3.                              \tag{22}
\]

The maximum is attained at q=0,18,36,72,90. Their intrinsic energies are,
respectively, 330,324,318,306,300. For q>=144 the same complete roster gives
I(q)>=282; equality is at q144. This reconstructs the M3 source gap from
the original source, without importing its earlier ratio as an assumption.

First consider the separated reference. Below q144,

\[
 I(q)+18+q/20\geq282+18+q/20+(144-q)/3,
\]

which decreases up to q144. Above q144, \(282+18+q/20\) increases.
An original state at q144 has I=282. Hence independently

\[
 E_{\rm sep}=282+18+144/20=1536/5.                          \tag{23}
\]

For the atom lower, put \(f(q)=37q/800-(9\sqrt2/20)\sqrt q\).
Below q144, the gap-relaxed \(282+(144-q)/3+f(q)\) is strictly decreasing:
its derivative is less than \(37/800-1/3<0\). Continuity includes q=0.
Above q144, f' is increasing and

\[
 f'(144)=(37-15\sqrt2)/800>0,
\]

because 37^2>2*15^2. Thus the full spectral lower comparison, for every
original source q, is minimized at q144. At q144 the spectral electronic
lower is above the independent core floor, so the maximum of both lowers
has this same minimum: the maximum is nowhere below the spectral
comparison and equals it at that attaining point. This proves the complete
lower-comparison minimum, not a claim that the unknown exact atom ground
must select q144.

Combining this atom lower with (23) gives

\[
 B_{444,6}\leq1377/50+(27/5)\sqrt2
 =35.1767532368147\ldots.                                  \tag{24}
\]

Its improvement from the earlier 972/25 cap is
\(567/50-(27/5)\sqrt2=3.7032467631853\ldots\).
Both minima were justified before the q-dependent self cancels in their
final difference.

For completeness, the submitted inventory extension uses
\(a_n=1/20-n/1600\), \(b_n=3\sqrt{w_nn}/20\).
Below 144 its gap-relaxed derivative is negative. Above 144,
\(a_n-b_n/24\geq a_6-b_6/24=(37-15\sqrt2)/800>0\)
because a_n decreases and b_n increases for n=1,...,6. Therefore each
spectral comparison selects q144 and gives

\[
 B_n\leq9w_n+9n/100+(9/5)\sqrt{w_nn}.                       \tag{25}
\]

The replay separately minimizes the maximum with the finite-core floor.
The floor comparison itself is also minimized at 144: below that point its
gap-relaxed derivative is
\(1/20-1/3-n/(20\sqrt q)<0\), and above it the derivative of its
I>=282 relaxation is
\(1/20-n/(20\sqrt q)\geq1/40>0\) for n<=6. Continuity includes zero.
Both spectral and core-floor comparisons therefore have their minima at
the same attaining q144; their pointwise maximum has that minimum as well.
For n=1,2,3 that floor is the winning lower at q144, giving complete binding
caps 36/5,72/5,108/5. For n=4,5,6 the spectral branch wins. This preserves
the submitted limitation: six spectral formulas do not assert six strict
improvements of the final existing accounts.

## 10. Declared controls and transfer boundaries

AR01 substitutes c6 for each of n1,...,5. Each fresh expectation is strictly
above that false energy cap, so none can certify it. The altered phase
left endpoints differ as well. Replacing g^2 by g in C444,N6,g=1/10 changes
the exact safe lower by a factor ten, and is rejected.

AR02 flattens the C444 intrinsic energies to 282 inside the atom comparison.
The complete spectral minimum then moves to q50, so the q144 claim cannot
be reconstructed from a missing intrinsic gap. Separately removing core
self from the separated reference gives 282 instead of 1536/5, a shortfall
126/5. That value is not an upper on the original separated reference and
cannot be used to upper-bound its binding. A weaker atom lower obtained by
dropping a positive self would have a different meaning; no such altered
account is mislabeled as the original minimum here.

AR03 accepts the original point source fields and explicitly refuses four
changed recipients: finite-core/pair/self; a different-inventory ionization
reference; massive kinetic; and an uncalibrated eV readout. At
tau=E0=|p|^2=1, the massive action is sqrt(3)-1<1, its quadratic recipient.
A lower for the larger quadratic kinetic therefore supplies no lower for
the smaller massive kinetic. Total-binding endpoints also do not determine
the ionization difference between two independently minimized inventories.

All controls behaved as preregistered. Their numerical certificates and
rejected contract fields are in `CONTROLS.json`. These controls check the
specified alterations and the scope of the inference; they add no physical
calibration or new atom to the source.

## 11. Arithmetic and proof boundary

Integer/Fraction evaluation covers all finite source histories and reference
coefficients. Arb balls at 512 bits cover gamma-derived log moments, normalized
Gram contractions and radical minima. Output rational endpoints are rounded
outwards to a fixed 2^-180 grid. Floating midpoint comparison only proposes a
candidate minimum; every competitor is then separated by a strictly positive
directed difference. No floating ordering is accepted as a proof.

The numerical proof covers the complete finite source, not a sampled q set.
The written form, scaling, Pauli, minimization and monotonicity arguments
extend its conclusions to the full stated electronic form domain. No
unresolved infinite-space spectral equality is used. Original pair or
outer-filling binding lowers remain inherited evidence; no pair tensor,
ion gap, geometry table, massive spectrum, physical conversion, or engine
installation was recalculated here.

The next step is the lead's aggregate reading and clean public replay of the
case after all tracks finish. No additional scientific prerequisite is left
open for C01-C05 under the hypotheses stated here.


## Appendix A. Complete finite q-minimum certificate

These are rendered directly from `NUCLEAR_RECONSTRUCTION.json`. Each row is the minimum over all original sectors at that q. Complete attaining sectors and counts remain in the JSON.

| q | He4 cover 3 I(q) | He4 cover 4 I(q) |
|---:|---:|---:|
| 0 | 110 | 110 |
| 2 | 110 | 110 |
| 4 | 110 | 110 |
| 8 | 153 | 110 |
| 10 | 153 | 110 |
| 16 | 196 | 110 |
| 18 | 196 | 368 |
| 20 | 196 | 368 |
| 26 | 239 | 368 |
| 36 | 282 | 626 |

| q | C333 I(q) | C343 I(q) | C444 I(q) |
|---:|---:|---:|---:|
| 0 | 330 | 330 | 330 |
| 2 | 330 | 330 | 330 |
| 4 | 330 | 330 | 330 |
| 8 | 328 | 328 | 328 |
| 10 | 328 | 328 | 328 |
| 16 | 326 | 326 | 326 |
| 18 | 324 | 324 | 324 |
| 20 | 324 | 324 | 324 |
| 26 | 322 | 322 | 322 |
| 32 | 363 | 320 | 320 |
| 34 | 363 | 320 | 320 |
| 36 | 318 | 318 | 318 |
| 40 | 361 | 318 | 318 |
| 50 | 357 | 314 | 314 |
| 52 | 400 | 357 | 314 |
| 58 | 398 | 355 | 312 |
| 64 | 396 | 310 | 310 |
| 68 | 394 | 351 | 308 |
| 72 | 435 | 392 | 306 |
| 74 | 435 | 392 | 306 |
| 80 | 433 | 390 | 304 |
| 82 | 433 | 347 | 304 |
| 90 | 429 | 386 | 300 |
| 98 | 470 | 427 | 556 |
| 100 | 470 | 384 | 298 |
| 104 | 468 | 382 | 296 |
| 106 | 468 | 425 | 554 |
| 116 | 464 | 421 | 550 |
| 122 | 505 | 419 | 290 |
| 128 | 503 | 460 | 804 |
| 130 | 503 | 417 | 546 |
| 136 | 501 | 458 | 802 |
| 144 | 540 | 454 | 282 |
| 146 | 497 | 454 | 798 |
| 148 | 540 | 454 | 540 |
| 160 | 536 | 450 | 794 |
| 162 | 534 | 706 | 1050 |
| 164 | 534 | 706 | 1050 |
| 170 | 532 | 489 | 532 |
| 178 | 573 | 487 | 788 |
| 180 | 528 | 700 | 1044 |
| 194 | 567 | 696 | 1040 |
| 196 | 610 | 524 | 782 |
| 200 | 608 | 522 | 780 |
| 212 | 604 | 733 | 1034 |
| 226 | 643 | 557 | 1030 |
| 234 | 639 | 768 | 1026 |
| 256 | 676 | 590 | 1278 |
| 260 | 674 | 803 | 1276 |
| 290 | 707 | 836 | 1524 |
| 324 | 738 | 1082 | 1770 |

## Appendix B. Every phase and actual inventory

Rendered from `SIX_PHASE_GUARANTEES.json`. Intervals are sufficient and open; infinity denotes no upper restriction.

| Source | q | n | Guaranteed chi interval |
|---|---:|---:|---|
| He4_3 | 4 | 1 | (0, 86) |
| He4_3 | 4 | 2 | (0, 43) |
| He4_3 | 36 | 1 | (268750/2367, infinity) |
| He4_3 | 36 | 2 | (537500/9469, infinity) |
| He4_4 | 16 | 1 | (0, 2064/5) |
| He4_4 | 16 | 2 | (0, 1032/5) |
| He4_4 | 36 | 1 | (430000/789, infinity) |
| He4_4 | 36 | 2 | (2580000/9469, infinity) |
| C12_333 | 36 | 1 | (0, 70/3) |
| C12_333 | 36 | 2 | (0, 35/3) |
| C12_333 | 36 | 3 | (0, 70/9) |
| C12_333 | 36 | 4 | (0, 35/6) |
| C12_333 | 36 | 5 | (0, 14/3) |
| C12_333 | 36 | 6 | (0, 35/9) |
| C12_333 | 324 | 1 | (218750/7101, infinity) |
| C12_333 | 324 | 2 | (437500/28407, infinity) |
| C12_333 | 324 | 3 | (218750/17301, infinity) |
| C12_333 | 324 | 4 | (437500/40797, infinity) |
| C12_333 | 324 | 5 | (109375/11223, infinity) |
| C12_333 | 324 | 6 | (437500/48987, infinity) |
| C12_343 | 64 | 1 | (0, 70/3) |
| C12_343 | 64 | 2 | (0, 35/3) |
| C12_343 | 64 | 3 | (0, 70/9) |
| C12_343 | 64 | 4 | (0, 35/6) |
| C12_343 | 64 | 5 | (0, 14/3) |
| C12_343 | 64 | 6 | (0, 35/9) |
| C12_343 | 256 | 1 | (218750/7101, 1968/17) |
| C12_343 | 256 | 2 | (437500/28407, 984/17) |
| C12_343 | 256 | 3 | (218750/17301, 656/17) |
| C12_343 | 256 | 4 | (437500/40797, 492/17) |
| C12_343 | 256 | 5 | (109375/11223, 1968/85) |
| C12_343 | 256 | 6 | (437500/48987, 328/17) |
| C12_343 | 324 | 1 | (2050000/13413, infinity) |
| C12_343 | 324 | 2 | (12300000/160973, infinity) |
| C12_343 | 324 | 3 | (6150000/98039, infinity) |
| C12_343 | 324 | 4 | (4100000/77061, infinity) |
| C12_343 | 324 | 5 | (1025000/21199, infinity) |
| C12_343 | 324 | 6 | (4100000/92531, infinity) |
| C12_444 | 144 | 1 | (0, 1984/15) |
| C12_444 | 144 | 2 | (0, 992/15) |
| C12_444 | 144 | 3 | (0, 1984/45) |
| C12_444 | 144 | 4 | (0, 496/15) |
| C12_444 | 144 | 5 | (0, 1984/75) |
| C12_444 | 144 | 6 | (0, 992/45) |
| C12_444 | 324 | 1 | (1240000/7101, infinity) |
| C12_444 | 324 | 2 | (2480000/28407, infinity) |
| C12_444 | 324 | 3 | (1240000/17301, infinity) |
| C12_444 | 324 | 4 | (2480000/40797, infinity) |
| C12_444 | 324 | 5 | (620000/11223, infinity) |
| C12_444 | 324 | 6 | (2480000/48987, infinity) |

## Appendix C. Every populated point binding account

Rendered from `POINT_BINDING_ALL44.json`; tau is one throughout. Each displayed interval has a trial-supplied lower and whole-space-supplied upper.

| Source | g | n | Binding lower | Binding upper | Earlier n/4 upper |
|---|---:|---:|---:|---:|---:|
| He4_3 | 1/10 | 1 | 2367/1250000 | 1/400 | 1/100 |
| He4_3 | 1/10 | 2 | 9469/2500000 | 1/200 | 1/50 |
| He4_4 | 1/10 | 1 | 2367/312500 | 1/100 | 1/25 |
| He4_4 | 1/10 | 2 | 9469/625000 | 1/50 | 2/25 |
| C12_333 | 1/10 | 1 | 21303/1250000 | 9/400 | 9/100 |
| C12_333 | 1/10 | 2 | 85221/2500000 | 9/200 | 9/50 |
| C12_333 | 1/10 | 3 | 51903/1250000 | 27/400 | 27/100 |
| C12_333 | 1/10 | 4 | 122391/2500000 | 9/100 | 9/25 |
| C12_333 | 1/10 | 5 | 33669/625000 | 9/80 | 9/20 |
| C12_333 | 1/10 | 6 | 146961/2500000 | 27/200 | 27/50 |
| C12_343 | 1/10 | 1 | 2367/78125 | 1/25 | 4/25 |
| C12_343 | 1/10 | 2 | 9469/156250 | 2/25 | 8/25 |
| C12_343 | 1/10 | 3 | 5767/78125 | 3/25 | 12/25 |
| C12_343 | 1/10 | 4 | 13599/156250 | 4/25 | 16/25 |
| C12_343 | 1/10 | 5 | 7482/78125 | 1/5 | 4/5 |
| C12_343 | 1/10 | 6 | 16329/156250 | 6/25 | 24/25 |
| C12_444 | 1/10 | 1 | 21303/312500 | 9/100 | 9/25 |
| C12_444 | 1/10 | 2 | 85221/625000 | 9/50 | 18/25 |
| C12_444 | 1/10 | 3 | 51903/312500 | 27/100 | 27/25 |
| C12_444 | 1/10 | 4 | 122391/625000 | 9/25 | 36/25 |
| C12_444 | 1/10 | 5 | 33669/156250 | 9/20 | 9/5 |
| C12_444 | 1/10 | 6 | 146961/625000 | 27/50 | 54/25 |
| He4_3 | 1 | 1 | 2367/12500 | 1/4 | 1 |
| He4_3 | 1 | 2 | 9469/25000 | 1/2 | 2 |
| He4_4 | 1 | 1 | 2367/3125 | 1 | 4 |
| He4_4 | 1 | 2 | 9469/6250 | 2 | 8 |
| C12_333 | 1 | 1 | 21303/12500 | 9/4 | 9 |
| C12_333 | 1 | 2 | 85221/25000 | 9/2 | 18 |
| C12_333 | 1 | 3 | 51903/12500 | 27/4 | 27 |
| C12_333 | 1 | 4 | 122391/25000 | 9 | 36 |
| C12_333 | 1 | 5 | 33669/6250 | 45/4 | 45 |
| C12_333 | 1 | 6 | 146961/25000 | 27/2 | 66 |
| C12_343 | 1 | 1 | 9468/3125 | 4 | 16 |
| C12_343 | 1 | 2 | 18938/3125 | 8 | 32 |
| C12_343 | 1 | 3 | 23068/3125 | 12 | 48 |
| C12_343 | 1 | 4 | 27198/3125 | 16 | 64 |
| C12_343 | 1 | 5 | 29928/3125 | 20 | 80 |
| C12_343 | 1 | 6 | 32658/3125 | 24 | 104 |
| C12_444 | 1 | 1 | 21303/3125 | 9 | 36 |
| C12_444 | 1 | 2 | 85221/6250 | 18 | 72 |
| C12_444 | 1 | 3 | 51903/3125 | 27 | 108 |
| C12_444 | 1 | 4 | 122391/6250 | 36 | 144 |
| C12_444 | 1 | 5 | 67338/3125 | 45 | 180 |
| C12_444 | 1 | 6 | 146961/6250 | 54 | 216 |
<!-- END REFERENCES/DERIVATION.md -->

## REFERENCES/HYPOTHESES.md

[Original document](peers/REFERENCES/HYPOTHESES.md)

<!-- BEGIN REFERENCES/HYPOTHESES.md -->
# Hypotheses and scope map

Every assigned claim held under its original hypotheses. The controls expose
changed coefficients, a missing source price or self term, and changed
recipients. They do not add a new physical assumption to the original atom.

| Claim | Required source and mathematical hypotheses | What was reconstructed | What would break this inference |
|---|---|---|---|
| C01 | Six independent C4 edge phases per isolated K4; original observed pair coefficient 43/4 and triangle coefficient 24; original INITIAL receiver; C333/C343/C444 ordered covers and all three contact edges; all intrinsic constants retained | Full core DOS, all 49/361 conditional sectors, complete q rosters, all five exact envelopes and original absolute nuclear ground references | A different cover, mask, phase/address convention, discarded core histories or intrinsic constant; a receiver not equal to the retained INITIAL sum |
| C02 | Original quadratic point operator on the full H1 form domain; tau>0; spin two; fixed n=1,...,6; exact rational frozen coefficients with their literal m/spin labels; all complete radial/log integrals and same-spin Gram cross terms | Each occupied prefix, its Gram positivity and Slater expectation; full-space -n/16 lower; all six intermediate sufficient intervals; all 50 phase/inventory guarantees | One shared coefficient for different prefixes, invalid Pauli labels, wrong normalization, omitted log derivative/cross terms, or treating a variational upper as the exact ground coefficient |
| C03 | Same noninteracting point source as C02; original separated nuclear ground plus n free electrons of ground zero; tau=1; g=1/10 or 1; He inventories 1,2 and carbon inventories 1,...,6; source energy units | Every submitted 44 populated account, ten empty controls, and both full nuclear minima at its electronic bounds; old n/4 complete uppers for comparison | Replacing g squared by g, changing q/source, dropping a nuclear sector, changing reference or units, or carrying the point account to a different Hamiltonian |
| C04 | Original finite-core scalar-plus-polarization Hamiltonian; C,A>=0; tau,rc>0; spin two; vc>=vp>=0 so the full pair law is nonnegative; quadratic kinetic; the declared weak carbon parameters; core self in both independent source minima | Complete exact separated minima, directed complete maxima of spectral/core-floor lowers, continuous generic relaxation and the three submitted rational neutral upper endpoints | Negative pair terms discarded without justification; massive instead of quadratic kinetic; cancellation of q-dependent self before minima; use of a separated lower as if it were an upper |
| C05 | C04 plus the original complete C444 intrinsic roster, I0=282 at q144 and its actual low-q gap | Exact source gap ratio over every low q; independently justified separated and lower-comparison minima; sharper complete neutral endpoint; all six spectral inventory extensions with the core floor retained | Omitting the intrinsic gap, substituting a source with another I/q roster, or confusing the lower-comparison minimizer with the unknown exact interacting atom minimizer |

The source statements above are definitions, not fitted parameters. The
recovered scientific operands are sealed in `RECOVERED_SOURCE_SEAL.json`;
every copied hash equals its original hash. Absolute original paths in that
seal are provenance only. The public runner reads its local copies and the
case-relative inputs, including after relocation.

The form identity in `DERIVATION.md` is analytic on all H1. Its n-electron
sum is obtained before antisymmetric restriction. The finite-core multiplier
has the required origin and interface behavior; it does not require
C+A*cos(theta) to remain positive. The scalar Pauli branch is a comparison
to the entire Coulomb spin spectrum, not to a finite Ritz basis. Pair
nonnegativity is used only in the electronic lower. Existing occupied pair
upper witnesses are inherited, not recomputed by this track.

The six common-dilation prefix expectations are different from the separately
optimized one-electron witness assigned to ORBITALS. In particular, the first
prefix is approximately -0.0473466471530169; this is sufficient for its
submitted safe coefficient 0.04734. No coefficient is silently replaced by
the separately optimized one-electron value.

The point envelope is exact as a function of t=(-e_n)*g^2/tau; the electronic
ground coefficient e_n remains bounded, not solved exactly. The resulting
coupling intervals are sufficient open guarantees. At t=0 the original
helium nuclear ground has additional q ties. At a transition all original
tied nuclear sectors remain in the finite source.
The noninteracting point predecessor admits arbitrarily many negative
one-body levels by disjoint attractive-cap annulus trials. Its retained
44-account panel does not predict a maximal physical charge inventory.

For finite cores, the exact separated reference is evaluated independently.
The atom quantities called minima in the numerical certificate are minima
of rigorous lower comparisons; they are not exact electronic ground
energies. The C444 proof shows the lower comparison minimizes at q144. It
does not identify the exact interacting atom's selected q without an
additional argument.

AR01 refutes each wrong shared prefix cap and the wrong g factor. AR02
retains the altered flattened-gap comparison and the self-omitted separated
value, and records why neither reconstructs the claimed reference. AR03
accepts the original point contract and rejects finite-core/pair/self,
ionization, massive-action and uncalibrated eV substitutions. Every declared
control behaved as predicted.

No physical energy/length/clock calibration, massive bank, new ionization
gap, updated common-geometry table, manuscript change, installed-engine
change, native calculation, Git operation or external-party replay is part
of this result. These boundaries are the original source distinctions; they
do not leave a substatement of C01-C05 unresolved.

The next step is aggregate case review and public replay after all tracks
finish; no scientific dependency on another track is required to execute
this REFERENCES replay.
<!-- END REFERENCES/HYPOTHESES.md -->

