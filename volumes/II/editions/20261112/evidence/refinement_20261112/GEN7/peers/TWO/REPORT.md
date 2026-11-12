# 1. Executive Delta Table

| ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict |
|---|---|---|---|---|---|
| TWO-G01 | XV.1; A05 continuation | \(E_{e,N}\ge-[C\sqrt{w_{N,\nu}}+A\nu\sqrt N/(\nu+1)]^2/(4\tau\nu^3)\). Complete geometric spectrum, spin2 and full form domain retained. | TWO_GEO_WEIGHT_V1, TWO_GEO_MID_WEIGHT_V1, TWO_GEO_PROFILE_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED finite identities | Held |
| TWO-G02 | XV.1,132 populated accounts | All 132 pointwise maxima evaluated over every original q class. Exact-weight refinement changes **0/132** final lowers relative to the already valid directional/geometric/core maximum. Against the original geometric/core lower,17 flat accounts improve;88 nonflat accounts are exactly unchanged. | TWO_GEO_FLOOR_DOMINANCE_V1: COMPLETED; full numerical panel HOST_DIRECTED_ARB | ANALYTICAL_PROOF + HOST_DIRECTED_ARB | Held |
| TWO-G03 | XV.1,ionization | Published explicit spherical-shell portfolio gives **30/132** positive ionization lowers and 102 overlaps after the upgrade. No additional opening on this fully reconstructed portfolio. Historical flat CI upper-endpoint file is absent: its exact upgraded count is bounded30–40, with 10 named candidates unresolved; do not mistake the spherical count for a full retained-CI recount. | Geometric identities above; panel is host-directed | HOST_DIRECTED_ARB; original30/132 is inherited | Partial: precise source-operand gap |
| TWO-M01 | XIV.5; XV.5–7 | \(\lvert v_C\rvert\ge6,\lvert v_O\rvert\ge8\), independent of orbital approximation. Neutral rigid singlets have zero first-order C1 mean. Exact second-order C1 coefficient is the requested \(-1/(600D^2)\) expression. Carbon monopole gives\(-27/(25D^2)\). | TWO_ROTOR_CARBON_V1, TWO_ROTOR_GENERAL_V1, TWO_ROTOR_RESOLVENT_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | Held in the explicitly added rigid-rotor model |
| TWO-M02 | XV.5 subleading terms | Full clamped rigid energy coefficient is \(K_2-S_2\), with explicit own-core and internal-pair Haar mean \(K_2\) below. Original cross-center C2 means vanish. Pair C2 can have either sign; C1 attraction alone does not fix the full D^-2 coefficient. | TWO_TAYLOR_PAIR_V1, TWO_TAYLOR_OWN_V1, TWO_TAYLOR_SIGN_CONTROL_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | New continuation |
| TWO-M04 | XV.5,full C2 comparison | \( \lvert K_2\rvert\le\sum_a[g_p\lvert U_a\rvert+v_p(n_a-1)]\mathcal R_a/3\). Equal-B sufficient full-tail attraction: C444 B<81/(85R), oxygen B<256/(115R), R=sum of radii per atom. | TWO_TAYLOR_PAIR_V1 and TWO_TAYLOR_OWN_V1 anchor the coefficient formula; uniform bound analytical | ANALYTICAL_PROOF | New sufficient full-C2 continuation |
| TWO-M03 | XV.5–7,thermal orientation | Classical independent-Haar C1 free energy is \(-\beta[\lvert v_A\rvert^2\lvert v_B\rvert^2+\lvert t_A\rvert^2+\lvert t_B\rvert^2]/(600D^2)\). Full model adds\(K_2/D^2\). | TWO_ROTOR_THERMAL_V3: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | Held |
| TWO-K01 | XV.1 / XV.6 controls | False flat centrifugal term: residual 6; wrong pair rotor gap: coefficient error−27/25; nonneutral singlet:first mean1; pair C2 sign witnesses714/625 and−1. | GEO_CONTROL_V3, ROTOR_CONTROL_V3, NEUTRALITY_CONTROL_V3, TAYLOR_SIGN_CONTROL_V1 (all prefixed TWO_): COMPLETED | NATIVE_CERTIFIED + ANALYTICAL_PROOF | All intended mathematical hypotheses break |

# 2. Self-Contained Derivations (Drop-In TeX Ready)

This is peer TWO's lane only. Locked cases H003004–H003008 are inputs at their existing I1/R2 scope; none of their base scripts was run. The general mathematical statements below are analytical proofs. Native receipts certify the displayed finite source contractions and resolvent; directed host arithmetic evaluates the new account table. No new independent CR2 level is asserted. All norms on finite coefficients are Euclidean unless a Haar/physical Gram is displayed. Energies and lengths retain the source units; no measured calibration is inserted.

**Exact geometric scalar occupation and the upgraded split.** Let
\[
 ds_g^2=\nu^{-2}dr^2+r^2d\Omega^2,\quad d\mathrm{vol}_g=\nu^{-1}r^2drd\Omega,
 \quad K_\nu=\tau\nu\|\nabla_g\cdot\|_2^2,\quad0<\nu\le1.
\]
For an N-electron state, K_nu below denotes the sum of the one-body kinetic forms. The locked A05 form/domain statement and matched directional profile are reused; the constant-nu Friedrichs form domain is the original weighted H1 closure, equivalent to flat H1 at each fixed positive nu. No origin/interface term is newly assumed. The scalar geometric Coulomb operator has all negative levels
\[
 -\frac{C^2}{4\tau\nu^3(n_r+\alpha_l+1)^2},\qquad
 \alpha_l(\alpha_l+1)=l(l+1)/\nu^2,
\]
with multiplicity\(2(2l+1)\). The radial Friedrichs realization and complete angular complement are those of the original geometry source. Define\(w_{N,\nu}\) as the sum of the N largest inverse squared denominators, including spin. Since\(\alpha_l\ge l\), the ordered geometric weights satisfy\(w_{N,\nu}\le w_N\); this follows by matching every label to its flat counterpart and applying the variational principle for the sum of the N largest weights.

For N≤6, every omitted\(l\ge3\) or\(n_r\ge3\) has denominator≥4, whereas six included s-wave slots have denominator≤3. This supplies a full-complement cutoff, not an assumed finite spectral truncation. At ν=3/4,1/2 the complete occupied weights are

| N | ν=1 | ν=3/4 | ν=1/2 |
|---:|---|---|---|
|0|0|0|0|
|1|1|1|1|
|2|2|2|2|
|3|9/4|9/4|9/4|
|4|5/2|5/2|5/2|
|5|11/4|(5777−27√137)/2048|47/18|
|6|3|(3217−27√137)/1024|49/18|

For ν=3/4 the fifth/sixth slots are l1,nr0 with denominator\((\sqrt{137}+3)/6\); for ν=1/2 they are l0,nr2. The native rational and Q(√137) contractions return exactly these sixth weights. They anchor occupation arithmetic; the analytical omitted-level argument supplies completeness.

Put\(d_c(r)=\max(r,r_c)\). For\(0<\theta<1\), split the **same** full kinetic form into θ and 1−θ. The exact geometric scalar occupation theorem gives
\[
 \theta K_\nu-\sum_iC/d_c(r_i)\ge-\frac{C^2w_{N,\nu}}{4\theta\tau\nu^3}.
\]
The locked geometric directional square, applied with τ replaced by(1−θ)τ, gives
\[
 (1-\theta)K_\nu-\sum_i A\cos\vartheta_i/d_c(r_i)
 \ge-\frac{NA^2}{4(1-\theta)\tau\nu(\nu+1)^2}.
\]
Its already verified profile is\(h=dr/[(d+1)r_c]\) inside and\(h=1-(r_c/r)^d/(d+1)\) outside, with\(d=2(\nu+1)/\nu\). The native profile receipt checks zero matching/ODE residuals at all three geometries. The positive complete Green pair form is discarded only for this lower; the original upper retains exchange and direct terms. Set\(a=C\sqrt{w_{N,\nu}}\),\(b=A\nu\sqrt N/(\nu+1)\). The exact identity
\[
 \frac{a^2}{\theta}+\frac{b^2}{1-\theta}-(a+b)^2
 =\frac{[a-(a+b)\theta]^2}{\theta(1-\theta)}
\]
proves the claimed optimized lower, with endpoint limits for a=0 or b=0. Add the independent floor\(-N(C+A)/r_c\), and the original geometric branch\(-w_{N,\nu}(C+A)^2/(4\tau\nu^3)\), by taking their pointwise maximum before either nuclear minimum.

The known A05 comparison counterexample is repaired by the new formula itself. At C1,A1/100,nu1/2,N6,tau=rc1, the new branch is
\[
 -49/9-1/7500-7\sqrt3/225,
\]
and the original geometric branch is−499849/90000. Native TWO_GEO_A05_REPAIR_V1 returns the exact positive difference
\[
 1093/10000-7\sqrt3/225
 \in(0.0554139748756349286458,0.0554139748756349286459).
\]
The old flat-weight directional branch remains a valid weaker lower and its prior comparison failure remains locked; this is a new exact-weight recipient calculation, not a replay of that case.

For N≤6 the upgraded directional branch is strictly stronger than the original geometric spectral branch whenever A>0: for N≥2,\(w_{N,\nu}\ge2>N/4\ge\nu^2N/(\nu+1)^2\); N=1 is immediate. At A=0 the spectral branches agree. A dominating core floor can still erase the strict gain. This corrects the old universal comparison without carrying its flat-weight counterexample into the new exact-weight formula.

**Why the exact-weight refinement has zero final effect on this panel.** Here\(\tau=r_c=g_c=v_c=1\),\(C=Z\in\{2,6\}\),\(1\le N\le Z\),\(A=g_p\sqrt q\ge0\),\(g_p=v_p\in\{1/10,1\}\). For x=A/C, put\(a=\sqrt{w_N}\),\(b=\nu\sqrt N/(\nu+1)\). The ratio of the flat-weight directional spectral cost to the positive core-floor cost is
\[
 \frac{C}{4\nu^3N}\frac{(a+bx)^2}{1+x}.
\]
The minimum over x≥0 of the last fraction is\(a^2\) if a≤2b, and\(4b(a-b)\) otherwise. For ν=3/4, N=1 and C≥2 give a charge-scaled minimum≥96/49. For N=2, w_N=2 gives the same bound using C/N≥1. For N≥3, replacing w_N by2 is a lower estimate and b≥3√3/7>1/√2, giving a minimum≥2. Therefore in every case the charge-scaled minimum exceeds\(4\nu^3=27/16\): the native margin is\(96/49-27/16=213/784>0\).

For ν=1/2, N=1 and C≥2 give16/9. For N≥2, use w_N≥2 and b=√N/3. The minimum over b∈[√2/3,√6/3] is at least16/9. This exceeds\(4\nu^3=1/2\), with native margin23/18. Thus even the flat-weight directional branch lies below the core floor for both nonflat geometries, for **every** A≥0. The exact geometric weight lowers the directional cost, but the same argument can use w_{N,ν}≥2 for N≥2 (and w1=1); it therefore also lies below the floor. The original geometric branch is below the new directional branch. All three-way maxima are exactly the core floor. At ν=1 the exact and flat weights agree. Hence the new exact-weight replacement changes0/132 final lower accounts relative to the previous three-way maximum, with no numerical equality tolerance used.

**Complete source minimization and the remaining upper-endpoint custody.** The locked q/I table includes all 10 helium q classes and all 51 carbon q classes (49/361 physical receiver sectors). For each account retain
\[
 S(q)=Z^2/2+g_pq/2,\quad
 G=\min_q[I(q)+S(q)],\quad
 L_N=\min_q\{I(q)+S(q)+\max(B_{\rm new},B_{\rm old},B_{\rm core})\}.
\]
The complete source table was read as an operand, without replaying its enumeration. Minima were interval-enclosed over every original row at 512-bit Arb precision. The 17 changes against the original geometric/core lower all occur at ν=1: both populated inventories of the four helium coupling/cover cohorts, and N4,5,6 in the three weak-carbon cohorts. Strong-carbon and all 88 nonflat populated accounts are unchanged.

For a fully specified available upper portfolio, the published shell formula was independently evaluated, without executing the old native adapter. Let\(\alpha=\alpha_1\),\(J_1=30(4\log2-11/4)\),\(M_\alpha=\sum_{i<j}(2R_i)^\alpha\). The disjoint normalized spherical trial with radial\(s(1-s)\) on[R,2R] obeys
\[
 \Delta U_j\le10\nu^3/R^2-(Z-j+1)J_1/R+
 \frac{g_pM_\alpha}{(2\alpha+1)R^{\alpha+1}}.
\]
Start R=2, double until this upper is negative, then multiply R by4 before the next shell. This is the original explicit formula and radius rule, freshly evaluated with outward intervals. It keeps all electrons, the same nuclear phase/reference, and the geometric Green pair bound. Define\(U_N^{\rm shell}=G+\sum_{j\le N}\Delta U_j\). The ionization interval is
\[
 [L_{N-1}-U_N^{\rm shell},\ U_{N-1}^{\rm shell}-L_N].
\]
All 132 lower/upper comparisons are valid,30 lower endpoints are positive (N1 in each of 30 cohorts), and 102 intervals contain zero. This is a complete **spherical-portfolio** calculation.

The historical geometry file additionally retained better H002309 CI/outer-shell uppers at ν=1. Neither its 714456-byte RESULTS.json (expected SHA2564b0731f60efbc7b0122d9fd0bb68c5a6ff24e185d97b324c9f801f0965fe6059) nor the 374830-byte flat predecessor (SHA256dc316d8bc657fbe400d069e7cb6d523c639c3bc0080bec0c0830d01e16a30b37) exists at the recorded local source paths. Their scripts, manifests and summaries exist. A reference hash is not an endpoint operand. We do not assign reconstructed shell uppers to that missing CI portfolio. Since only10 previous-inventory lowers that can affect a nonempty ionization account change, the original retained portfolio's upgraded count is in[30,40]; the only candidates beyond30 are He4_3/He4_4 N2 at both couplings, and C333/C343/C444 N5,N6 at g_p1/10. Restoring those ten upper endpoints is sufficient to settle it. The exact-weight change itself adds no further opening to any fixed portfolio beyond the already valid three-way bound.

**Rigid-rotor C1 response.** Fix neutral rigid atomic preparations and rotate all of their body-frame moments together. On\(L^2(SO(3)\times SO(3),dR_AdR_B)\) with normalized Haar measure, add\(H_0=B_A L_A^2+B_B L_B^2\), B_A,B_B>0. Let\(\Omega=1\otimes1\) be the normalized product singlet. For the original coefficient
\[
 C_1=\frac1{10}[(R_Av_A)\cdot(R_Bv_B)+e\cdot(R_At_A-R_Bt_B)],
\]
Haar invariance gives\(\langle R a\rangle=0\),\(\langle(Ra)_i(Rb)_j\rangle=\delta_{ij}(a\cdot b)/3\). Consequently\(\langle C_1\rangle=0\). The three summands send Ω into mutually orthogonal left-angular-momentum sectors(1,1),(1,0),(0,1). Their squared norms are respectively
\[
 \frac{\lvert v_A\rvert^2\lvert v_B\rvert^2}{300},\quad\frac{\lvert t_A\rvert^2}{300},\quad\frac{\lvert t_B\rvert^2}{300},
\]
with exact energy gaps2(B_A+B_B),2B_A,2B_B. Arbitrary body components and v/t nonorthogonality stay inside these sectors; integrating the other rotor makes the cross terms zero. Thus
\[
 -\frac1{D^2}\langle C_1\Omega,QH_0^{-1}QC_1\Omega\rangle
 =-\frac1{600D^2}\left[
 \frac{\lvert v_A\rvert^2\lvert v_B\rvert^2}{B_A+B_B}+\frac{\lvert t_A\rvert^2}{B_A}+\frac{\lvert t_B\rvert^2}{B_B}\right].
\]
This uses the complete image of Ω for second order; there is no angular-cutoff approximation to the full rotor. Bounded C1 and the positive rotor gap justify analytic perturbation for sufficiently large D at fixed B_A,B_B. The native15-coordinate witness uses the raw Cartesian Haar Gram diag(1/9 repeated9,1/3 repeated6); its gap operator is diag(4 repeated9,2 repeated6). For vA=vB6,tA3,tB4 it returns−673/600. With only the monopole, three pair entries are18/5 in the raw basis (6/5 in normalized Cartesian coordinates), squared norm 108/25 and gap 4, giving−27/25. The independent certified complex solve encloses every15 exact resolvent component.

For any normalized correlated n-electron preparation,\(\mu=\sum_i\langle n_i\rangle\) satisfies\(|\mu|\le n\), since every n_i is a unit multiplication vector. Therefore\(|v|=|U-\mu|\ge|U|-n\). In the specified C444 sector |U|12,n6 this is6; in oxygen |U|16,n8 it is8. This argument uses no orbital approximation. At equal B=1 the oxygen monopole component is at most−256/(75D²), while carbon is at most−27/(25D²). These refer to the C1 component of the changed rotor model, not the full molecular coefficient.

The classical independent-Haar partition of C1 alone gives
\[
 -\beta^{-1}\log\langle e^{-\beta C_1/D}\rangle
 =-\frac{\beta}{600D^2}(\lvert v_A\rvert^2\lvert v_B\rvert^2+\lvert t_A\rvert^2+\lvert t_B\rvert^2)+O(D^{-3}).
\]
For the native witness β1 the exact coefficient is−1321/600. β and the B's are supplied model parameters; neither is a physical-unit calibration.

**The competing original Taylor coefficient is explicit.** Put\(\epsilon=D^{-1}\). For x=R_A+r n, c=n·e, the original common direction is exactly
\[
 n_D=\operatorname{normalize}[(1-2\epsilon rc+2\epsilon^2r^2)n-\epsilon r e].
\]
Expanding its squared norm and reciprocal square root yields
\[
 n_D=n+\epsilon a+\epsilon^2b+O(\epsilon^3),\quad
 a=r(cn-e),\quad b=r^2[(7c^2-1)n/2-3ce].
\]
At B, a reverses and b is unchanged. Averaging common rigid rotations of one atom relative to fixed e gives
\[
 \overline b=-r^2n/3,\qquad
 \overline{a_i\cdot a_j}=r_ir_j(1+c_{ij}^2)/3,
 \quad c_{ij}=n_i\cdot n_j.
\]
The full first-order mean of the original second Taylor term is therefore
\[
 K_2=\sum_{a=A,B}\left\{
 \frac{g_p}{3}\sum_{i\in a}\left\langle
 \frac{r_i^2}{\max(r_i,r_c)}U_a\cdot n_i\right\rangle
 +\frac{v_p}{3}\sum_{i<j\in a}\left\langle
 \frac{r_ir_j(1+c_{ij}^2)-(r_i^2+r_j^2)c_{ij}}
 {|x_i-x_j|}\right\rangle\right\}.
\]
These are complete correlated moments; pair expectations include exchange. Unit norm of the exact n_D keeps the regularized electron polarization self constant, so no D-dependent self term is omitted. The scalar own-core terms are D-independent. The scalar cross-center second coefficient is linear in a rotated first spatial moment and has Haar mean zero. Every polarization cross-center second term contains one unpaired vector from the independently rotated other atom, so it also has zero mean. Uniform nuclear-shell cross energy is exactly proportional to1/D. Thus no original cross-center C2 mean was dropped in this average.

For compact rigid preparations, all expansions and averaged remainders are uniform at sufficiently large D. Exponentially decaying original states can use the retained normalized localization construction and sufficiently many finite radial moments. The statement is about the effective clamped rigid model with its specified BA LA²+BB LB²; internal excitations, full moving dissociation channels and the paid localization/recoil/rotational realization are separate operands.

Accordingly the complete clamped quantum coefficient is
\[
 E(D)-E(\infty)=D^{-2}(K_2-S_2)+o(D^{-2}),\qquad
 S_2=\frac1{600}\left[
 \frac{\lvert v_A\rvert^2\lvert v_B\rvert^2}{B_A+B_B}+\frac{\lvert t_A\rvert^2}{B_A}+\frac{\lvert t_B\rvert^2}{B_B}\right].
\]
The classical coefficient is\(K_2-\beta(\lvert v_A\rvert^2\lvert v_B\rvert^2+\lvert t_A\rvert^2+\lvert t_B\rvert^2)/600\). The own-core C2 need not vanish: r2,dc2,U=(12,0,0),n=(3/5,4/5,0),gp1/10 gives native+12/25. The pair numerator is native714/625 at r2,s3,n=(3/5,4/5,0),m=(0,3/5,4/5). For parallel directions and radii2,3 it is−1. Narrow finite-energy packets around these separated configurations preserve either sign, so these are reachable controls, not null geometries. Consequently neither scalar neutrality nor vanishing vector mean alone fixes the full D^-2 coefficient or recovers a D^-6 tail.

A sharp first-moment bound makes this comparison quantitative without evaluating every pair. Put u=(r-s)^2≥0, v=2rs(1-c)≥0, so d²=u+v and
\[
 N_2=rs(1+c^2)-(r^2+s^2)c=-cu+(1-c)v/2.
\]
Since c∈[-1,1],
\[
 d^2-N_2=(1+c)(u+v/2)\ge0,\qquad
 d^2+N_2=(1-c)u+(3-c)v/2\ge0.
\]
Therefore |N2|≤d² and the pair term has absolute value≤v_p d/3≤v_p(r+s)/3. The existing native positive/negative pair witnesses anchor the same exact numerator; the uniform inequality and the corollary here are ANALYTICAL_PROOF. With the scalar radial sum \(\mathcal R_a=\sum_i\langle r_i\rangle\), the full mean obeys
\[
 \lvert K_2\rvert\le\frac13\sum_{a=A,B}[g_p\lvert U_a\rvert+v_p(n_a-1)]\mathcal R_a.
\]
The own-core estimate uses r²/max(r,rc)≤r. This also establishes the needed integrability with only finite first radial moments and removes an apparent pair-coincidence singularity.

For identical C444 neutral preparations, g_p=v_p1/10 and equal scalar radial sums \(\mathcal R_A=\mathcal R_B=R\), this gives |K2|≤17R/15, whereas S2≥27/(25B) at equal B. Hence
\[
 0<B<81/(85R)
\]
is sufficient for a negative **full** clamped D^-2 coefficient, including the original Taylor terms. If R=6 times the mean electron radius, this is B<27/(170 mean_radius). For identical oxygen preparations the corresponding sufficient condition is B<256/(115R), or B<32/(115 mean_radius) when R=8 mean_radius. These are source-unit sufficient conditions at fixed B followed by large D, not calibrated molecular predictions. They do not require t to vanish; t only increases S2.

One useful conditional continuation follows: at equal B, let\(A_2=\lvert v_A\rvert^2\lvert v_B\rvert^2/2+\lvert t_A\rvert^2+\lvert t_B\rvert^2>0\). If the finite K2 is positive, B<A2/(600K2) is sufficient for negative full coefficient; if K2≤0 every B>0 qualifies. This concerns sufficiently large D at each fixed B, not a uniform interchange of B→0 and D→∞. Actual body-frame moments and a calibrated rotational action are still needed to assign the carbon/oxygen full coefficient.

**Source hashes and norms.** Normalized physical electronic states use the original geometric L² measure; Haar measure has total mass1; L² eigenvalues are l(l+1). The finite Cartesian witness Gram is stated explicitly above. Exact source files and SHA256 identities are:

| Source | SHA256 |
|---|---|
| Volume II controlling PDF | `391450c512bfda11682e5a58b6f3f8d27856cdc4381cd962432ae9d3e521a5f3` |
| H003004 complete q/I operand | `6e58aab8aeecef64f3ae38f6baf445dcec631f2d3af2b0de963b04537d569339` |
| Original geometry derivation | `9a96f02787876de36eba1be3f2828b0963bb8ae9921ac9ae8bb92aef0fcb73d8` |
| Original geometry adapter (read only) | `62b649edb2b4fe7336691caf64d98d455ee609cdf662c70598a8523952c09908` |
| Original geometry completion manifest | `22929e334b84063817427081bdc5c8f88ca46b6537be4162c834ec925c6acd50` |
| Original molecular direction/energy law | `6cdbcd4ae88f183ca405bcad7d6600a06aaaf8c6efd2a4ceaa90ab8aa07132a7` |
| Full signed molecular C1 proof | `4e60a39bb635b8b65e1a647619b17996a253f8f44c2caa64f089a712d2bdb27e` |
| Original FOUR-M01 submission/scope | `4ce636042050f64988a7379b4df1f6c72ad61bc6d030b65f3e864eaee9a7012d` |
| New predictions | `273fb40fff5700d9f262b60d289c5c8d5586ae0f21caeafb3f0b1de169cecd85` |
| New panel implementation | `055bea6821a59698193e9327994fd7a38a727242d0742fc48137d74469f469f3` |

**All 132 account endpoints.** Each interval below is rounded outward from the 512-bit rational endpoint box to9 decimal places. G is the exact separated source+core minimum. L is the upgraded complete lower; U_s is the freshly evaluated spherical upper; I_s is its ionization lower endpoint enclosure. These are not substituted for the missing historical flat CI uppers.

| ν | Source | gp | N | G | L | U_s | I_s |
|---|---|---|---:|---|---|---|---|
| 1 | He4_3 | 1/10 | 1 | 112 | [111.000000000,111.000000000] | [111.986834583,111.986834584] | [0.013165416,0.013165417] |
| 1 | He4_3 | 1/10 | 2 | 112 | [109.956078643,109.956078644] | [111.975944114,111.975944115] | [-0.975944115,-0.975944114] |
| 1 | He4_3 | 1 | 1 | 112 | [111.000000000,111.000000000] | [111.986834583,111.986834584] | [0.013165416,0.013165417] |
| 1 | He4_3 | 1 | 2 | 112 | [109.335786437,109.335786438] | [111.980631614,111.980631615] | [-0.980631615,-0.980631614] |
| 1 | He4_4 | 1/10 | 1 | 112 | [111.000000000,111.000000000] | [111.986834583,111.986834584] | [0.013165416,0.013165417] |
| 1 | He4_4 | 1/10 | 2 | 112 | [109.956078643,109.956078644] | [111.975944114,111.975944115] | [-0.975944115,-0.975944114] |
| 1 | He4_4 | 1 | 1 | 112 | [111.000000000,111.000000000] | [111.986834583,111.986834584] | [0.013165416,0.013165417] |
| 1 | He4_4 | 1 | 2 | 112 | [109.335786437,109.335786438] | [111.980631614,111.980631615] | [-0.980631615,-0.980631614] |
| 1 | C12_333 | 1/10 | 1 | 1689/5 | [331.199999999,331.200000001] | [337.408507499,337.408507500] | [0.391492500,0.391492501] |
| 1 | C12_333 | 1/10 | 2 | 1689/5 | [324.599999999,324.600000001] | [337.236842394,337.236842395] | [-6.036842395,-6.036842394] |
| 1 | C12_333 | 1/10 | 3 | 1689/5 | [317.999999999,318.000000001] | [337.197255467,337.197255468] | [-12.597255468,-12.597255467] |
| 1 | C12_333 | 1/10 | 4 | 1689/5 | [312.363950105,312.363950106] | [337.189552157,337.189552158] | [-19.189552158,-19.189552157] |
| 1 | C12_333 | 1/10 | 5 | 1689/5 | [309.600210680,309.600210681] | [337.188259752,337.188259753] | [-24.824309647,-24.824309646] |
| 1 | C12_333 | 1/10 | 6 | 1689/5 | [306.846623381,306.846623382] | [337.188100323,337.188100324] | [-27.587889644,-27.587889643] |
| 1 | C12_333 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.608507499,347.608507500] | [0.391492500,0.391492501] |
| 1 | C12_333 | 1 | 2 | 348 | [330.000000000,330.000000000] | [347.446217394,347.446217395] | [-6.688858082,-6.688858081] |
| 1 | C12_333 | 1 | 3 | 348 | [318.000000000,318.000000000] | [347.409560155,347.409560156] | [-17.409560156,-17.409560155] |
| 1 | C12_333 | 1 | 4 | 348 | [306.000000000,306.000000000] | [347.402625887,347.402625888] | [-29.402625888,-29.402625887] |
| 1 | C12_333 | 1 | 5 | 348 | [294.000000000,294.000000000] | [347.401528032,347.401528033] | [-41.401528033,-41.401528032] |
| 1 | C12_333 | 1 | 6 | 348 | [282.000000000,282.000000000] | [347.401417384,347.401417385] | [-53.401417385,-53.401417384] |
| 1 | C12_343 | 1/10 | 1 | 1656/5 | [324.399999999,324.400000001] | [330.808507499,330.808507500] | [0.391492500,0.391492501] |
| 1 | C12_343 | 1/10 | 2 | 1656/5 | [317.599999999,317.600000001] | [330.636842394,330.636842395] | [-6.236842395,-6.236842394] |
| 1 | C12_343 | 1/10 | 3 | 1656/5 | [310.799999999,310.800000001] | [330.597255467,330.597255468] | [-12.997255468,-12.997255467] |
| 1 | C12_343 | 1/10 | 4 | 1656/5 | [304.745266807,304.745266808] | [330.589552157,330.589552158] | [-19.789552158,-19.789552157] |
| 1 | C12_343 | 1/10 | 5 | 1656/5 | [301.800280907,301.800280908] | [330.588259752,330.588259753] | [-25.842992945,-25.842992944] |
| 1 | C12_343 | 1/10 | 6 | 1656/5 | [298.868831175,298.868831176] | [330.588100323,330.588100324] | [-28.787819417,-28.787819416] |
| 1 | C12_343 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.608507499,347.608507500] | [0.391492500,0.391492501] |
| 1 | C12_343 | 1 | 2 | 348 | [330.000000000,330.000000000] | [347.446217394,347.446217395] | [-6.688858082,-6.688858081] |
| 1 | C12_343 | 1 | 3 | 348 | [317.786796564,317.786796565] | [347.409560155,347.409560156] | [-17.409560156,-17.409560155] |
| 1 | C12_343 | 1 | 4 | 348 | [304.000000000,304.000000000] | [347.402625887,347.402625888] | [-29.615829324,-29.615829323] |
| 1 | C12_343 | 1 | 5 | 348 | [290.000000000,290.000000000] | [347.401528032,347.401528033] | [-43.401528033,-43.401528032] |
| 1 | C12_343 | 1 | 6 | 348 | [276.000000000,276.000000000] | [347.401417384,347.401417385] | [-57.401417385,-57.401417384] |
| 1 | C12_444 | 1/10 | 1 | 1536/5 | [299.999999999,300.000000001] | [306.808507499,306.808507500] | [0.391492500,0.391492501] |
| 1 | C12_444 | 1/10 | 2 | 1536/5 | [292.799999999,292.800000001] | [306.636842394,306.636842395] | [-6.636842395,-6.636842394] |
| 1 | C12_444 | 1/10 | 3 | 1536/5 | [285.599999999,285.600000001] | [306.597255467,306.597255468] | [-13.797255468,-13.797255467] |
| 1 | C12_444 | 1/10 | 4 | 1536/5 | [278.647900211,278.647900212] | [306.589552157,306.589552158] | [-20.989552158,-20.989552157] |
| 1 | C12_444 | 1/10 | 5 | 1536/5 | [275.325421361,275.325421362] | [306.588259752,306.588259753] | [-27.940359541,-27.940359540] |
| 1 | C12_444 | 1/10 | 6 | 1536/5 | [272.023246763,272.023246764] | [306.588100323,306.588100324] | [-31.262678963,-31.262678962] |
| 1 | C12_444 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.608507499,347.608507500] | [0.391492500,0.391492501] |
| 1 | C12_444 | 1 | 2 | 348 | [330.000000000,330.000000000] | [347.446217394,347.446217395] | [-6.688858082,-6.688858081] |
| 1 | C12_444 | 1 | 3 | 348 | [316.539501058,316.539501059] | [347.409560155,347.409560156] | [-17.409560156,-17.409560155] |
| 1 | C12_444 | 1 | 4 | 348 | [300.000000000,300.000000000] | [347.402625887,347.402625888] | [-30.863124830,-30.863124829] |
| 1 | C12_444 | 1 | 5 | 348 | [282.000000000,282.000000000] | [347.401528032,347.401528033] | [-47.401528033,-47.401528032] |
| 1 | C12_444 | 1 | 6 | 348 | [264.000000000,264.000000000] | [347.401417384,347.401417385] | [-65.401417385,-65.401417384] |
| 3/4 | He4_3 | 1/10 | 1 | 112 | [109.958578643,109.958578644] | [111.924841041,111.924841042] | [0.075158958,0.075158959] |
| 3/4 | He4_3 | 1/10 | 2 | 112 | [107.799999999,107.800000001] | [111.899552698,111.899552699] | [-1.940974055,-1.940974054] |
| 3/4 | He4_3 | 1 | 1 | 112 | [109.585786437,109.585786438] | [111.924841041,111.924841042] | [0.075158958,0.075158959] |
| 3/4 | He4_3 | 1 | 2 | 112 | [106.000000000,106.000000000] | [111.904826869,111.904826870] | [-2.319040432,-2.319040431] |
| 3/4 | He4_4 | 1/10 | 1 | 112 | [109.958578643,109.958578644] | [111.924841041,111.924841042] | [0.075158958,0.075158959] |
| 3/4 | He4_4 | 1/10 | 2 | 112 | [107.799999999,107.800000001] | [111.899552698,111.899552699] | [-1.940974055,-1.940974054] |
| 3/4 | He4_4 | 1 | 1 | 112 | [109.585786437,109.585786438] | [111.924841041,111.924841042] | [0.075158958,0.075158959] |
| 3/4 | He4_4 | 1 | 2 | 112 | [106.000000000,106.000000000] | [111.904826869,111.904826870] | [-2.319040432,-2.319040431] |
| 3/4 | C12_333 | 1/10 | 1 | 1689/5 | [331.199999999,331.200000001] | [336.821702498,336.821702499] | [0.978297501,0.978297502] |
| 3/4 | C12_333 | 1/10 | 2 | 1689/5 | [324.599999999,324.600000001] | [336.465253963,336.465253964] | [-5.265253964,-5.265253963] |
| 3/4 | C12_333 | 1/10 | 3 | 1689/5 | [317.999999999,318.000000001] | [336.384998349,336.384998350] | [-11.784998350,-11.784998349] |
| 3/4 | C12_333 | 1/10 | 4 | 1689/5 | [311.399999999,311.400000001] | [336.369457513,336.369457514] | [-18.369457514,-18.369457513] |
| 3/4 | C12_333 | 1/10 | 5 | 1689/5 | [304.799999999,304.800000001] | [336.366847626,336.366847627] | [-24.966847627,-24.966847626] |
| 3/4 | C12_333 | 1/10 | 6 | 1689/5 | [298.199999999,298.200000001] | [336.366523028,336.366523029] | [-31.566523029,-31.566523028] |
| 3/4 | C12_333 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.021702498,347.021702499] | [0.978297501,0.978297502] |
| 3/4 | C12_333 | 1 | 2 | 348 | [330.000000000,330.000000000] | [346.675802305,346.675802306] | [-5.918442993,-5.918442992] |
| 3/4 | C12_333 | 1 | 3 | 348 | [318.000000000,318.000000000] | [346.598536688,346.598536689] | [-16.598536689,-16.598536688] |
| 3/4 | C12_333 | 1 | 4 | 348 | [306.000000000,306.000000000] | [346.583755158,346.583755159] | [-28.583755159,-28.583755158] |
| 3/4 | C12_333 | 1 | 5 | 348 | [294.000000000,294.000000000] | [346.581335493,346.581335494] | [-40.581335494,-40.581335493] |
| 3/4 | C12_333 | 1 | 6 | 348 | [282.000000000,282.000000000] | [346.581058464,346.581058465] | [-52.581058465,-52.581058464] |
| 3/4 | C12_343 | 1/10 | 1 | 1656/5 | [324.399999999,324.400000001] | [330.221702498,330.221702499] | [0.978297501,0.978297502] |
| 3/4 | C12_343 | 1/10 | 2 | 1656/5 | [317.599999999,317.600000001] | [329.865253963,329.865253964] | [-5.465253964,-5.465253963] |
| 3/4 | C12_343 | 1/10 | 3 | 1656/5 | [310.799999999,310.800000001] | [329.784998349,329.784998350] | [-12.184998350,-12.184998349] |
| 3/4 | C12_343 | 1/10 | 4 | 1656/5 | [303.999999999,304.000000001] | [329.769457513,329.769457514] | [-18.969457514,-18.969457513] |
| 3/4 | C12_343 | 1/10 | 5 | 1656/5 | [297.199999999,297.200000001] | [329.766847626,329.766847627] | [-25.766847627,-25.766847626] |
| 3/4 | C12_343 | 1/10 | 6 | 1656/5 | [290.399999999,290.400000001] | [329.766523028,329.766523029] | [-32.566523029,-32.566523028] |
| 3/4 | C12_343 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.021702498,347.021702499] | [0.978297501,0.978297502] |
| 3/4 | C12_343 | 1 | 2 | 348 | [330.000000000,330.000000000] | [346.675802305,346.675802306] | [-5.918442993,-5.918442992] |
| 3/4 | C12_343 | 1 | 3 | 348 | [317.786796564,317.786796565] | [346.598536688,346.598536689] | [-16.598536689,-16.598536688] |
| 3/4 | C12_343 | 1 | 4 | 348 | [304.000000000,304.000000000] | [346.583755158,346.583755159] | [-28.796958595,-28.796958594] |
| 3/4 | C12_343 | 1 | 5 | 348 | [290.000000000,290.000000000] | [346.581335493,346.581335494] | [-42.581335494,-42.581335493] |
| 3/4 | C12_343 | 1 | 6 | 348 | [276.000000000,276.000000000] | [346.581058464,346.581058465] | [-56.581058465,-56.581058464] |
| 3/4 | C12_444 | 1/10 | 1 | 1536/5 | [299.999999999,300.000000001] | [306.221702498,306.221702499] | [0.978297501,0.978297502] |
| 3/4 | C12_444 | 1/10 | 2 | 1536/5 | [292.799999999,292.800000001] | [305.865253963,305.865253964] | [-5.865253964,-5.865253963] |
| 3/4 | C12_444 | 1/10 | 3 | 1536/5 | [285.599999999,285.600000001] | [305.784998349,305.784998350] | [-12.984998350,-12.984998349] |
| 3/4 | C12_444 | 1/10 | 4 | 1536/5 | [278.399999999,278.400000001] | [305.769457513,305.769457514] | [-20.169457514,-20.169457513] |
| 3/4 | C12_444 | 1/10 | 5 | 1536/5 | [271.199999999,271.200000001] | [305.766847626,305.766847627] | [-27.366847627,-27.366847626] |
| 3/4 | C12_444 | 1/10 | 6 | 1536/5 | [263.999999999,264.000000001] | [305.766523028,305.766523029] | [-34.566523029,-34.566523028] |
| 3/4 | C12_444 | 1 | 1 | 348 | [340.757359312,340.757359313] | [347.021702498,347.021702499] | [0.978297501,0.978297502] |
| 3/4 | C12_444 | 1 | 2 | 348 | [330.000000000,330.000000000] | [346.675802305,346.675802306] | [-5.918442993,-5.918442992] |
| 3/4 | C12_444 | 1 | 3 | 348 | [316.539501058,316.539501059] | [346.598536688,346.598536689] | [-16.598536689,-16.598536688] |
| 3/4 | C12_444 | 1 | 4 | 348 | [300.000000000,300.000000000] | [346.583755158,346.583755159] | [-30.044254101,-30.044254100] |
| 3/4 | C12_444 | 1 | 5 | 348 | [282.000000000,282.000000000] | [346.581335493,346.581335494] | [-46.581335494,-46.581335493] |
| 3/4 | C12_444 | 1 | 6 | 348 | [264.000000000,264.000000000] | [346.581058464,346.581058465] | [-64.581058465,-64.581058464] |
| 1/2 | He4_3 | 1/10 | 1 | 112 | [109.958578643,109.958578644] | [111.634838332,111.634838333] | [0.365161667,0.365161668] |
| 1/2 | He4_3 | 1/10 | 2 | 112 | [107.799999999,107.800000001] | [111.570082141,111.570082142] | [-1.611503498,-1.611503497] |
| 1/2 | He4_3 | 1 | 1 | 112 | [109.585786437,109.585786438] | [111.634838332,111.634838333] | [0.365161667,0.365161668] |
| 1/2 | He4_3 | 1 | 2 | 112 | [106.000000000,106.000000000] | [111.573864543,111.573864544] | [-1.988078106,-1.988078105] |
| 1/2 | He4_4 | 1/10 | 1 | 112 | [109.958578643,109.958578644] | [111.634838332,111.634838333] | [0.365161667,0.365161668] |
| 1/2 | He4_4 | 1/10 | 2 | 112 | [107.799999999,107.800000001] | [111.570082141,111.570082142] | [-1.611503498,-1.611503497] |
| 1/2 | He4_4 | 1 | 1 | 112 | [109.585786437,109.585786438] | [111.634838332,111.634838333] | [0.365161667,0.365161668] |
| 1/2 | He4_4 | 1 | 2 | 112 | [106.000000000,106.000000000] | [111.573864543,111.573864544] | [-1.988078106,-1.988078105] |
| 1/2 | C12_333 | 1/10 | 1 | 1689/5 | [331.199999999,331.200000001] | [336.079514998,336.079514999] | [1.720485001,1.720485002] |
| 1/2 | C12_333 | 1/10 | 2 | 1689/5 | [324.599999999,324.600000001] | [335.675927973,335.675927974] | [-4.475927974,-4.475927973] |
| 1/2 | C12_333 | 1/10 | 3 | 1689/5 | [317.999999999,318.000000001] | [335.592549954,335.592549955] | [-10.992549955,-10.992549954] |
| 1/2 | C12_333 | 1/10 | 4 | 1689/5 | [311.399999999,311.400000001] | [335.576770835,335.576770836] | [-17.576770836,-17.576770835] |
| 1/2 | C12_333 | 1/10 | 5 | 1689/5 | [304.799999999,304.800000001] | [335.574135309,335.574135310] | [-24.174135310,-24.174135309] |
| 1/2 | C12_333 | 1/10 | 6 | 1689/5 | [298.199999999,298.200000001] | [335.573806423,335.573806424] | [-30.773806424,-30.773806423] |
| 1/2 | C12_333 | 1 | 1 | 348 | [340.757359312,340.757359313] | [346.279514998,346.279514999] | [1.720485001,1.720485002] |
| 1/2 | C12_333 | 1 | 2 | 348 | [330.000000000,330.000000000] | [345.879710375,345.879710376] | [-5.122351063,-5.122351062] |
| 1/2 | C12_333 | 1 | 3 | 348 | [318.000000000,318.000000000] | [345.797313230,345.797313231] | [-15.797313231,-15.797313230] |
| 1/2 | C12_333 | 1 | 4 | 348 | [306.000000000,306.000000000] | [345.781779659,345.781779660] | [-27.781779660,-27.781779659] |
| 1/2 | C12_333 | 1 | 5 | 348 | [294.000000000,294.000000000] | [345.779205523,345.779205524] | [-39.779205524,-39.779205523] |
| 1/2 | C12_333 | 1 | 6 | 348 | [282.000000000,282.000000000] | [345.778891984,345.778891985] | [-51.778891985,-51.778891984] |
| 1/2 | C12_343 | 1/10 | 1 | 1656/5 | [324.399999999,324.400000001] | [329.479514998,329.479514999] | [1.720485001,1.720485002] |
| 1/2 | C12_343 | 1/10 | 2 | 1656/5 | [317.599999999,317.600000001] | [329.075927973,329.075927974] | [-4.675927974,-4.675927973] |
| 1/2 | C12_343 | 1/10 | 3 | 1656/5 | [310.799999999,310.800000001] | [328.992549954,328.992549955] | [-11.392549955,-11.392549954] |
| 1/2 | C12_343 | 1/10 | 4 | 1656/5 | [303.999999999,304.000000001] | [328.976770835,328.976770836] | [-18.176770836,-18.176770835] |
| 1/2 | C12_343 | 1/10 | 5 | 1656/5 | [297.199999999,297.200000001] | [328.974135309,328.974135310] | [-24.974135310,-24.974135309] |
| 1/2 | C12_343 | 1/10 | 6 | 1656/5 | [290.399999999,290.400000001] | [328.973806423,328.973806424] | [-31.773806424,-31.773806423] |
| 1/2 | C12_343 | 1 | 1 | 348 | [340.757359312,340.757359313] | [346.279514998,346.279514999] | [1.720485001,1.720485002] |
| 1/2 | C12_343 | 1 | 2 | 348 | [330.000000000,330.000000000] | [345.879710375,345.879710376] | [-5.122351063,-5.122351062] |
| 1/2 | C12_343 | 1 | 3 | 348 | [317.786796564,317.786796565] | [345.797313230,345.797313231] | [-15.797313231,-15.797313230] |
| 1/2 | C12_343 | 1 | 4 | 348 | [304.000000000,304.000000000] | [345.781779659,345.781779660] | [-27.994983096,-27.994983095] |
| 1/2 | C12_343 | 1 | 5 | 348 | [290.000000000,290.000000000] | [345.779205523,345.779205524] | [-41.779205524,-41.779205523] |
| 1/2 | C12_343 | 1 | 6 | 348 | [276.000000000,276.000000000] | [345.778891984,345.778891985] | [-55.778891985,-55.778891984] |
| 1/2 | C12_444 | 1/10 | 1 | 1536/5 | [299.999999999,300.000000001] | [305.479514998,305.479514999] | [1.720485001,1.720485002] |
| 1/2 | C12_444 | 1/10 | 2 | 1536/5 | [292.799999999,292.800000001] | [305.075927973,305.075927974] | [-5.075927974,-5.075927973] |
| 1/2 | C12_444 | 1/10 | 3 | 1536/5 | [285.599999999,285.600000001] | [304.992549954,304.992549955] | [-12.192549955,-12.192549954] |
| 1/2 | C12_444 | 1/10 | 4 | 1536/5 | [278.399999999,278.400000001] | [304.976770835,304.976770836] | [-19.376770836,-19.376770835] |
| 1/2 | C12_444 | 1/10 | 5 | 1536/5 | [271.199999999,271.200000001] | [304.974135309,304.974135310] | [-26.574135310,-26.574135309] |
| 1/2 | C12_444 | 1/10 | 6 | 1536/5 | [263.999999999,264.000000001] | [304.973806423,304.973806424] | [-33.773806424,-33.773806423] |
| 1/2 | C12_444 | 1 | 1 | 348 | [340.757359312,340.757359313] | [346.279514998,346.279514999] | [1.720485001,1.720485002] |
| 1/2 | C12_444 | 1 | 2 | 348 | [330.000000000,330.000000000] | [345.879710375,345.879710376] | [-5.122351063,-5.122351062] |
| 1/2 | C12_444 | 1 | 3 | 348 | [316.539501058,316.539501059] | [345.797313230,345.797313231] | [-15.797313231,-15.797313230] |
| 1/2 | C12_444 | 1 | 4 | 348 | [300.000000000,300.000000000] | [345.781779659,345.781779660] | [-29.242278602,-29.242278601] |
| 1/2 | C12_444 | 1 | 5 | 348 | [282.000000000,282.000000000] | [345.779205523,345.779205524] | [-45.779205524,-45.779205523] |
| 1/2 | C12_444 | 1 | 6 | 348 | [264.000000000,264.000000000] | [345.778891984,345.778891985] | [-63.778891985,-63.778891984] |

# 3. Controls, Obstructions & Superseded Attempts

PRECOMMIT.md was written before any scientific script or native task, and the Taylor extension was added before its contractions. All mathematical breaking controls are reachable: l1 is a legal nonzero angular channel; the carbon pair image has nonzero norm 108/25; charges+1,+1 are an explicitly changed allocation; separated electron radii2,3 and open neighborhoods give nonzero pair terms.

- **Geometry:** falsely taking α1=1 at ν1/2 misses the centrifugal coefficient by8−2=6. The control receipt returns6. Exact selected s-state weights cannot detect this alone, so the nonzero l1 control is retained separately.
- **Rotor gap:** replacing the pair gap 4 by the single-rotor gap 2 changes−27/25 to−54/25. The native wrong-minus-true witness is−27/25.
- **Neutrality:** dropping neutral allocation gives the scalar first mean1 for charges+1,+1. Haar averaging does not eliminate a scalar charge product.
- **Original C2:** dropping own-core response misses+12/25 in the stated physical witness. Dropping the a_i·a_j term misses\(r_ir_j(1+c_{ij}^2)/3\). The positive714/625 and negative−1 pair numerators refute a universal sign shortcut. The full-tail conclusion retains K2 rather than replacing it by zero.
- **Caller-contract corrections:** three V1 control submissions were rejected because `expected_reason` is permitted only with expected FAILED/REFUSED, while these controls expect COMPLETED nonzero witnesses. Three V2 attempts were rejected because `supersedes` cannot name an unadmitted task; the thermal V2 attempt was rejected because `supersedes` cannot name a completed task. Corrected V3 submissions use expected_status COMPLETED without those invalid fields. These are7 unadmitted requests, with submitted JSONs retained, not mathematical failures.
- **Thermal operand correction:** TWO_ROTOR_THERMAL_V1 completed an incorrect precomputed variance input 673/150, yielding−673/300. It is scientifically superseded by the full-image contraction TWO_ROTOR_THERMAL_V3, which returns−1321/600. The exact correction is+1/24. Quantum rotor receipts and the general thermal formula are unchanged. No completed erroneous operand is erased or counted as independent evidence.
- **Host failures:** panel attempt001 had the Python typo `else6`; attempt002 compared Arb directly with Fraction. Their scripts are retained. A rational endpoint audit then exposed extra outward rounding when subtracting Arb objects versus separately rounded endpoint boxes. The final runner constructs ionization endpoint differences directly over exact rationals from the displayed lower/upper boxes; the original Arb version and failed audit remain. All 132 interval-containment/count checks pass without changing the source or count criterion. The corrected runner uses Arb source evaluation and exact rational endpoint differences for the same full132-account specification. No acceptance criterion, source table, or baseline upper was changed to obtain a count.
- **Physical/model boundary:** the geometry lower assumes the original quadratic kinetic and constant ν; it does not transfer to the smaller massive square-root kinetic or variable lapse. Rotor BA,BB and thermal β are explicitly added/supplied. The full C2 moments, internal excitations, moving-fragment reference, recoil, physical vertex/unit calibration and apparatus resources remain named inputs rather than being supplied by C1 averaging.

# 4. Exceptions-Only Custody Diff

Native completed tasks:16; scientifically current completed tasks:15; completed caller-operand superseded tasks:1 (TWO_ROTOR_THERMAL_V1). All completed receipt files were read, their SHA256 verified, exact source-word outputs checked and all 15 resolvent components checked by rational containment. No admitted native task is missing its return. Unadmitted requests:7 as listed above. Every matrix has at most15 rows/columns; no large-matrix rank/solve was submitted.

**Source operand exception:** original geometry RESULTS.json and flat H002309 RESULTS.json are absent locally at their documented paths and were not recovered in the bounded local searches. Their expected byte counts/hashes are stated in section2. This prevents the original retained-CI ionization recount; it does not prevent the full132 lower table, the zero incremental exact-weight theorem, or the complete spherical-portfolio30/132 calculation. There is no `MISSING_RECEIPT` among this run's admitted native tasks.

Only this peer folder was written. Locked H003004–H003008 scripts, large N5000/N2000 archives and completed Volume III TWO-F03 were not replayed. Sources and new host scripts are hash-bound above; native task JSONs and readbacks remain under tasks/ and gen/. Peak workload was one bounded host process with OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and ctx.threads=1. No manuscript, engine, external app, Git history or other peer folder was modified.

| Native key | Status | Receipt SHA256 |
|---|---|---|
| TWO_GEO_A05_REPAIR_V1 | COMPLETED | `a28e2b27ae1bc9fbf19dfb5af5e508db46cf786e16b6877c02f1a45fa474caa1` |
| TWO_GEO_CONTROL_V3 | COMPLETED | `4c0b008fead4586703156873ca87b841ff2c2964ece7c1bd1c895c1c36a9880c` |
| TWO_GEO_FLOOR_DOMINANCE_V1 | COMPLETED | `48d725eca9ac3db1bb3664800dc794ca91d6a7884ad27963ec5ae24cd5f1e5c3` |
| TWO_GEO_MID_WEIGHT_V1 | COMPLETED | `c883e532b5b30ea021a8aa3e38a066d2a7484210bd805308ae739109c21fde9b` |
| TWO_GEO_PROFILE_V1 | COMPLETED | `70d4fe32f0b2f730fc29e39b5ecc1186e683aa03efed4cbaf5caf288f82ca3b2` |
| TWO_GEO_WEIGHT_V1 | COMPLETED | `eca32663b27ad7b0edeaff08a72d0f2dc2fe56c27ef12051a295fa370af5572b` |
| TWO_NEUTRALITY_CONTROL_V3 | COMPLETED | `187cb2145db832a634db99ef0b51c7ece3b0c2f70963ab982a7a607f9df0be3b` |
| TWO_ROTOR_CARBON_V1 | COMPLETED | `23b4aaec9df9cf64f0c5dd0c4fd7d123cfdf064b98496a17450590b8f24f43c4` |
| TWO_ROTOR_CONTROL_V3 | COMPLETED | `5382bb6de85b82461009ddffd44371efe2f126e7b041079dc1d82d1e91f8e8a7` |
| TWO_ROTOR_GENERAL_V1 | COMPLETED | `4eed704091dce73f8a755c2132129114111a7fb71b9c509ae261984a13314048` |
| TWO_ROTOR_RESOLVENT_V1 | COMPLETED | `c9f2b9aedf02ad8ad34bb24129772a2312360553b98c426a84e8b5f3c984d8f4` |
| TWO_ROTOR_THERMAL_V1 | COMPLETED; superseded operand | `1a4e5893d78e9de13595a2ca03e98d6717817d67a86685aba0fee6d2eaef1759` |
| TWO_ROTOR_THERMAL_V3 | COMPLETED | `c062628736049fda8ea581e3853dca09dc686483c39ea62fb5a19f8534795a5e` |
| TWO_TAYLOR_OWN_V1 | COMPLETED | `a930b0d0b37fe2b7b452a98ca30c24e127afa4eb0ffbd57c4dfc54b50225901a` |
| TWO_TAYLOR_PAIR_V1 | COMPLETED | `0bb3ba73e587d7d50a9a953c370fa76f9ae4e98bf9875c293bacb0f20adb0d9f` |
| TWO_TAYLOR_SIGN_CONTROL_V1 | COMPLETED | `f995659006113f2ea4e79534039ea96b1f9bc4a152646634af4f7d3860183422` |

The bounded frustrated-spin transfer review uses the prescribed locked spin material: preserve the full physical metric, mixed terms and uncertainty links; no new numerical atomic or rotor operand follows from those spin summaries. No additional relevant undisclosed result was identified. NEGATIVE DRIFT CHECK — COMPLETION: CLEAR.
