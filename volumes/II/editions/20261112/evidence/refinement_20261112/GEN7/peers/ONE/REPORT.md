# 1. Executive Delta Table

| ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict |
|---|---|---|---|---|---|
| ONE-T1 | X; XI.13; XVI.11; XVIII | General symmetric kernel ranks18 on phase9,21 on source11; nullities18,15; an actual source600 repair detects the exhibited null | ONE7_RANK_CONTROLS, ONE7_EXACT_NULLS: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT | Verified |
| ONE-T2 | XVI.11 | Minimal real8 span,64 readings; det159888004924897312074400606300736408680062026647775541663050843745240813611778048000; exact inverse; error≤1325.485758855ε | ONE7_REAL8, ONE7_DETERMINANTS: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Verified |
| ONE-T3 | XVI.11 | Minimal complex6 span,66 readings; det−14456300689839224704350855805402087668238263310630460660892537375259550051405731882598400; exact inverse; error≤2253.867579928ε | ONE7_COMPLEX6, ONE7_DETERMINANTS: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Verified |
| ONE-A | XII.11; App.A–B | Minimax0.0464409230216487…; unchanged input under that map0.0400557228243080…; known-input optimum0.0396929079249281…; mixed-output trace distance≥8/225 | ONE7_ARRIVAL, ONE7_PAIR_SECTORS: COMPLETED | NATIVE_CERTIFIED + HOST_DIRECTED_ARB + ANALYTICAL_PROOF | Bounds verified; attainment conditional on stated full-flavor alignment |
| ONE-R | XVI.13 | Lnew≥Lold−18δ for0≤δ≤10/3; old margin≥11191/20250−23294δ/675; uniform-mode old margin≥11191/20250+5Δ/4 for−1/2≤Δ≤1/2 | ONE7_ROBUSTNESS: COMPLETED | NATIVE_CERTIFIED + ANALYTICAL_PROOF | Verified; interval of Δ is part of the claim |
| ONE-D | XI.16; XVI.13 | New cloud-dressed one-hop density-square upper16.44780324393715…; kernel error coefficient34.44780324393715…; sufficient δ<0.0465272835531455… | ONE7_DRESSED_DENSITY, ONE7_ROBUSTNESS: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | New continuation for a common bounded static perturbation; dynamic remainder explicit |
| ONE-F | XI.17; XII.16 | Explicit lattice matter/Fock localization below; inf ess Hλ(P)≥min{Lproper,minQ Eλ(Q)+1}. On42,33 the resulting whole-band essential gap is≥116/125=0.928 | ONE7_FIBER_KINEMATICS: COMPLETED (finite support/sector constants only) | ANALYTICAL_PROOF; native finite anchors | Source-specific analytical continuation; no spectral promotion of321 |

# 2. Self-Contained Derivations (Drop-In TeX Ready)

## Source, norm and evidence conventions

The controlling117-page10November2026 manuscript has SHA256 `391450c512bfda11682e5a58b6f3f8d27856cdc4381cd962432ae9d3e521a5f3`. H003004/H003005/H003006/H003008 are locked I1/R2 inputs; none of their base scripts was run. The Hamiltonian is the declared fixed-six-fermion, four-flavor CAR/scalar-Fock law on Z³×Q3, with τ=1,tc=1/1000,g²=35, common normally ordered vacuum zero and no compensating density counterterm. Operator norms below are Euclidean spectral norms in the normalized eight-dimensional Walsh chart. Trace distance means one half of the trace norm. Source columns used in tomography are deliberately unnormalized; their full common Gram is retained.

New code reads literal exterior-source columns, fixed historical source-transform coefficients, and locked one-hop source/image operands. It newly applies every Walsh density, contracts full physical images, computes determinants/inverses, and contracts the new one-hop density observable. It never executes an inherited scientific script. The mathematical source files and exact SHA256 list are printed at the end of this section. New host calculations are labelled separately from completed native arithmetic. Source600 is the physical source frame; neither1795 density-image rows nor a small trial factor is substituted for the50176-dimensional fixed-weight CAR parent.

## General symmetric static-kernel tomography

Let χq(x)=(−1)^popcount(q&x), and let ρq=Σx χq(x)ρx denote the unnormalized Walsh density. The net static energy matrix on a source F is

\[
 K_B=-\frac18\sum_{q,r=0}^7 B_{qr}F^*\rho_q\rho_rF,
 \qquad B=B^{\mathsf T}\in\mathbb R^{8\times8}.
\]

In a Fourier exterior word, ρq replaces one occupied flavor mode k by k xor q, with the annihilation and creation signs, and removes a term if its destination is already occupied. This is the newly implemented action. For literal source columns X, form Dq=ρqX on the union of all physical image words. Then Mqr=Dq*Dr is the full product, including images outside the source. There is no step (X*ρqX)(X*ρrX). Density operators commute on the full physical parent; consequently Mqr=Mrq and the real unnormalized source matrices are symmetric.

Order the36 unknowns by q≤r. For real source columns define

\[
 C_{(i,j),(q,r)}=(2-\delta_{qr})(M_{qr})_{ij},\quad i\le j.
\]

On phase9 its rank is18; on source11 it is21. Exact selected minors have determinants respectively

\[
 -80978196699832320000000000000000,
 \qquad4197909716919307468800000000000000000.
\]

Independent null vectors,18 and15 respectively, annihilate every row of the complete design. New exact native word products verify those zero matrices, split into≤33-row pieces to respect the64-row contract. Thus the minor lower and kernel upper meet. The perturbation B15=1,B04=−1/6, with symmetric partners, vanishes on all source11 measurements. Its6-scaled response on the additional actual source600 direction labelled `source600_0,0,5,2`, paired with originalphase0, is144; the unscaled response is24 before the−1/8 energy factor. This verifies that the chosen breaking control is reachable and not a symmetry null.

The18 raw source vectors are the nine original phase columns, source600_ground_u, source600_pair_t1_d1, and seven actual source600 Fourier-pair columns labelled

\[
 (0,0,1,2),(0,0,2,1),(0,0,2,4),(0,0,4,1),
 (0,0,4,2),(0,0,4,4),(0,0,5,2).
\]

Their literal exterior coefficients are the sealed raw-source operand; all density products were rebuilt from those coefficients. Fixed18×8 real and18×6 Gaussian-integer transformations, reproduced below, produce X8 and X6. No binding target or measured coupling is used in this verification or in selecting those already fixed designs.

For real8 use the36 upper-triangular matrix entries. For complex6 use the six diagonal real entries, followed by Re and Im of each upper off-diagonal entry in lexicographic order. Define C with the same factor2−δqr, extracting the corresponding real or imaginary component. The exact determinants are the two integers in the executive table. Native exact LU residuals P C−LU=0 and native products of signed U diagonals certify those determinants; separate native exact C Cinv=I and certified36×36 solves certify both inverses. All1296 entries per inverse were checked against their exact rational values. A complete exact specification, independent of decimal display, is

\[
 (C^{-1})_{ij}=\frac{(-1)^{i+j}\det C_{\widehat j,\widehat i}}{\det C}.
\]

Here C is fully defined by the literal source action, the transformations below and the prescribed observable order. The reconstructed rational inverse arrays have canonical JSON SHA256 `6d34c2f7129191f2c5eee281b3bfb532fa8aa4afc5f1a2a29de314594fc7c8f6` (real) and `9381ffc85aa07b582a4c53fc3c86a7f3dc0304c1d12f161642d7f1249ccd6368` (complex), using compact separators and strings. These hashes identify the exact arrays used by the native inverse identities, not an assertion inferred from a matching numerical condition number.

Suppose each normalized scalar energy reading has absolute error≤ε, with source Gram G, kinetic subtraction and absolute common zero independently known. A diagonal unnormalized entry has error≤Gii ε. Polarization gives off-diagonal real or imaginary entry error≤(Gii+Gjj)ε/2: e.g. Re Hij=[Q(xi+xj)−Q(xi−xj)]/4, and Im Hij=−[Q(xi+i xj)−Q(xi−i xj)]/4. The normalization factors are the actual source norms, not2 by assumption. Set w to these weights and β=|Cinv|w. Since b=−8Cinv y,

\[
 |\delta b_a|\le8\beta_a\epsilon,
 \quad \|\delta B\|\le\|\delta B\|_\infty
 \le8\max_q\sum_r\beta_{\min(q,r),\max(q,r)}\epsilon.
\]

The exact rational expression on the right evaluates to1325.4857588545583370… for real8 and2253.8675799276463117… for complex6, giving the outward displayed constants. Exact rational comparisons also verify that both displayed rounded constants are upper bounds. The first design requires8+2·28=64 readings; the second6+4·15=66. Seven real directions have at most28 symmetric energy entries and five complex directions at most25 Hermitian real entries, so8 and6 are minimal **span dimensions**. No minimum physical preparation count is inferred. The complex option requires calibrated relative phases. Fixed-N energy differences alone omit the absolute uniform coefficient.

## Separated arrival: three optimization questions

In the normalized phase9 basis, use Ps and Pa on pairs(0,5),(1,4),(2,6),(3,8), with Pe on edge7. These arrival projectors use unit source directions, separately from the unnormalized tomography columns. Reconstructing the separated pair central operators100C2+C3 and their four exact Lagrange projectors gives pair Grams

\[
 G_{42}^{pair}=\frac3{10}\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
 G_{33}^{pair}=\frac16\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\quad
 G_{321}^{pair}=\frac1{15}\begin{pmatrix}8&-2\\-2&8\end{pmatrix},
 \quad G_{411}^{pair}=0.
\]

Thus G42=3Ps/5+Pe,G33=Pa/3,G321=2Ps/5+2Pa/3. Their sum and the contact sum are exactly I9. Contact multiplies the non-edge42,33,321 factors by47/45,17/15,14/15. Under the original full-flavor canonical orbital alignment, identity on every complete flavor factor gives cross Gram

\[
 C=c_sP_s+c_aP_a+P_e,
 \quad c_s=\tfrac35\sqrt{47/45}+\tfrac25\sqrt{14/15},
 \quad c_a=\tfrac13\sqrt{17/15}+\tfrac23\sqrt{14/15}.
\]

For a unit antisymmetric pair vector, every flavor-preserving coherent unitary has overlap at most ca by sector Cauchy. Since ca<cs<1, the common alignment attains the lower bound on every source direction, proving minimax norm distance√(2−2ca)=0.04644092302164874715…. For unchanged14336 the (Ps,Pa,Pe) weights are(2/9,2/3,1/9), so the error under this common map is√[2−2(2cs/9+2ca/3+1/9)]=0.04005572282430802073….

For a unitary chosen for that one known input, sector Cauchy instead gives maximal overlap Σλ√(wsep,λ wc,λ), with wsep=(11/45,2/9,8/15),wc=(169/675,34/135,112/225). The full-flavor factorization permits that alignment:42/33 have one weight line, and the retained normalized321 flavor factor is common; one may rotate the42 orbital vector without enforcing every other phase input. Its distance is0.03969290792492810896…. The two squared errors differ strictly by0.0000289339914409698435484…; they are not interchangeable optima. Attainment retains the stated complete flavor alignment, rather than following from central weights alone.

A deterministic channel with flavor-trivial ancillary systems preserves the central sector probabilities. Measuring them cannot increase trace distance, so the contact target and any such output have distance at least

\[
 \tfrac12\sum_\lambda|w_{c,\lambda}-w_{sep,\lambda}|=8/225.
\]

This mixed-output statement has a different norm and domain from coherent vector distance. A flavor-carrying ancilla changes the allowed resources. Both coherent errors exceed0.001, so deterministic arrival is not already paid by the earlier small compiler allowance. The15/17 instrument and its failure record remain a separate conditional route.

Native squared-distance enclosures additionally imply the following outward decimal norm intervals. Each decimal endpoint was checked by an exact rational square comparison against the native lower/upper endpoint; no untracked decimal rounding enters these bounds.

| Quantity | Certified enclosing norm interval |
|---|---|
| sym | [0.0273824066891853, 0.0273824066891854] |
| minimax | [0.0464409230216487, 0.0464409230216488] |
| fixed | [0.0400557228243080, 0.0400557228243081] |
| known | [0.0396929079249281, 0.0396929079249282] |

## Branch-aware and signed uniform robustness

For a fragment of n particles, Pauli4 gives Σxρx²≤16⌊n/4⌋+(n mod4)². Summing over cells cannot increase this convex concentration maximum. For proper six-particle size partitions,5+1 has cap18,4+2 cap20, all others≤18. The locked common lower lines at the benchmark are

\[
 E_1\ge-12,\ E_2\ge-48,\ E_3\ge-108,
 \ E_4\ge-188,\ E_5\ge-692/3.
\]

The5+1 sum is−728/3;4+2 is higher by20/3. Every other size type is at least−216. For a common static perturbation of normδ the4+2 lower stays above Lold−18δ exactly throughδ≤10/3. Thus

\[
 L_{new}\ge L_{old}-18\delta,\quad
 m_{old\ target,new}\ge\frac{11191}{20250}-\frac{23294}{675}\delta,
 \quad0\le\delta\le10/3.
\]

The target contribution is its actual11144δ/675, and the sufficient tolerance isδ<11191/698820. Atδ=10/3+1/100 the4+2 line is below the asserted5+1 envelope by1/50: the displayed interval cannot be dropped.

For Bnew=35G+Δ11ᵀ/8, the interaction shift is−ΔΣR NR²/8. The full all-cell fragment comparison gives, for−1/2≤Δ≤1/2, the preceding En lines shifted by−n²Δ/8. Split-cell slack remains positive: the N5 split slack80/3 can lose at most5/4, and N4 slack68 at most3/4. Smaller fragments retain their positive same-cell concentration advantage. Enumerating every one of the ten proper size types at both endpoints proves5+1 remains lowest throughout. Hence

\[
 L_{new}\ge-728/3-26\Delta/8,\quad
 U_{old,new}=U_{old}-36\Delta/8,\quad
 m_{old,new}\ge11191/20250+5\Delta/4.
\]

Positivity is sufficient forΔ>−22382/50625 within that declared interval. Unlike an affine constituent rest reference, this mode changes the6-versus5+1 comparison by−10Δ/8; treating it as a cancelling baseline loses a nonzero term.

## New cloud-dressed one-hop calibration recipient

Use the locked H003006 isometry Jλα=(Jλ−αλKJλ)Cλ, Cλ=(I+αλ²Vλ)^−1/2, Vλ=Jλ*K²Jλ, with α42=α33=1/56,α321=1/40. Define the **new** observable D2=ΣR,xρR,x². Parity kills its target/one-hop cross term. Its exact compression is

\[
 J_{\lambda\alpha}^*D_2J_{\lambda\alpha}
 =C_\lambda(s_\lambda I+\alpha_\lambda^2W_\lambda)C_\lambda,
 \quad W_\lambda=J_\lambda^*K D_2KJ_\lambda,
 \quad s=(20,18,14).
\]

For the retained signed involutions S,T and the **actual** coherent overlaps r42=e^(−2332g²/11025),r=e^(−17g²/225), the new internal moments are

\[
 W_{42,int}/(4\tau^2)=220I+36r_{42}S,\quad
 W_{33,int}/(4\tau^2)=168I,\quad
 W_{321,int}/(4\tau^2)=144I+28r^2S-4rT.
\]

These are obtained by summing every locked physical one-hop image with its new weight Σxρm,x², retaining each signed pair of source paths and multiplying by the overlap of their original source clouds. The−4rT term would be lost by replacing the density square with the old bare-profile mean. Native full weighted image products agree with all exponent-class sums. Cell escape contributes tc²(24sλ+72)I, since its five-central/one-remote density square is sλ−2ρx+2 and there are six outward directions per particle.

With the already verified exponential ceilings r42<1/1000,r<1/10, the exact W uppers are110018069/125000,84000063/125000,72340051/125000. Use the locked V lowers13998009/250000,12000009/250000,11980009/250000. The positive congruence gives the uniform sector bound

\[
 S_\lambda=\frac{s_\lambda+\alpha_\lambda^2W_{\lambda,+}}
 {1+\alpha_\lambda^2V_{\lambda,-}}.
\]

They are19.92490702818282…,17.93969844791798…,13.94407489806138…. For unchanged source weights(169/675,34/135,112/225), their weighted sum is

\[
 \overline S_\alpha=16.44780324393715\ldots,
 \quad c_\alpha=18+\overline S_\alpha=34.44780324393715\ldots.
\]

Let Mα=2139952734887423053027468631/1335165038749772953286830250 be the locked sufficient benchmark margin. For the common full Hamiltonian perturbation Hnew=Hold−ΣRρRᵀΔBρR, with ||ΔB||≤δ, the original cloud-dressed trial is fixed and

\[
 m_{\alpha,new}\ge M_\alpha-c_\alpha\delta,
 \quad0\le\delta\le10/3.
\]

This is a bounded instantaneous density perturbation of the full Fock law; it is semibounded at fixed particle number and changes the net static kernel to35G+ΔB. It does not require replacing the old trial by bare densities. Sufficientδ is0.0465272835531455…. Combining the reconstructed tomography constants gives sufficient normalized reading errorsε<0.0000351020622004667… real, orε<0.0000206433084035217… complex, before preparation/Gram/kinetic errors.

A different harmonic receiver with the same calibrated net static kernel may change its clouds and hopping response. Static data alone cannot bound that dynamic change. If its actual transported trial supplies an additional full energy-form errorη, the valid statement is Mα−cαδ−η. The conditionη=0 holds for the explicit bounded instantaneous perturbation just stated; it is not silently assigned to a changed inertia/vertex law. This is the physical/calibration boundary of this continuation.

Uniform mode also detects the one-hop cell component. Let pcell,λ=36tc²αλ²⟨Cλ²⟩ in a normalized sector input. Then the actual compression of ΣR NR² is36−10pcell,λ. The same V lower gives weighted pcell≤1.65456182334269×10^−8. Therefore the new positive-Δ margin slope is at least(5/4)(1−1.65456182334269×10^−8); for negativeΔ the safe old slope5/4 remains valid. The pure one-cell value36 cannot be copied exactly to the dressed trial.

## Explicit Bloch fibers and lattice Fock localization

This paragraph supplies a source-specific analytical step for the **declared benchmark lattice law**, rather than importing a continuum Nelson theorem. Let Γa translate all matter and field cell coordinates by a∈Z³. It commutes with H and global flavor. Since N=6>0, its action on finite matter configurations is free. Choose one representative of each matter-translation orbit, translate field coordinates with that representative, and Fourier transform the orbit coordinate. This defines a fixed fiber Hilbert space and

\[
 H=\int_{\mathbb T^3}^{\oplus}H(P)\,\frac{dP}{(2\pi)^3},
 \quad H_\lambda(P)=H(P)|_\lambda,\quad E_\lambda(P)=\inf\sigma H_\lambda(P).
\]

No photon cutoff defines these fibers. Because1≤ω≤7, bounded fixed-N hopping and the density vertex give a common domain D(Nb) and form domain D(Nb^1/2). Young's inequality gives H(P)≥Nb/2−CN,g uniformly in P. Flavor localization commutes with the central sector projector.

Only external matter hopping depends on P. Its off-diagonal row/column sum is≤6Ntc=36tc; thus comparison of its twisted forms gives bandwidth≤12Ntc=72tc. Continuity of Eλ can be seen without relying on a discontinuous orbit representative: multiplication by exp(i h·Rcm), Rcm=N^−1ΣiRi, maps momentum P to P+h, commutes with the density vertex/free field and twists each external matter hop by exp(±ihj/N). It is permutation invariant. On a local momentum chart the conjugated difference tends to zero in norm. Hence Eλ is continuous, and eλ=minQ Eλ(Q) exists.

Here are the cutoffs and the required error order. Take a smooth χM(Nb) equal to1 below M and0 above2M. The vertex changes Nb by one, so on D(H)

\[
 \|[H,\chi_M(N_b)]\|\le C_{N,g}M^{-1/2},\qquad
 \|(1-\chi_M)\psi\|^2\le C_E/M
\]

for normalized energy-bounded Weyl sequences. The first bound follows from the1/M discrete derivative times the creation/annihilation factor√(2M+1); the fixed-N density vector is uniformly bounded. This justifies taking M→∞ at the end, rather than declaring the field finite.

For fixed M, form a smooth translation-invariant partition of unity of the matter configurations into: a single cluster with relative diameter≤CNR, and every proper set partitionπ of the six particles with distinct clusters separated by≥R and each cluster diameter≤CNR. Such a finite cover is obtained by graph components at successive geometric distance scales; among N scales one has no component merger. Products of smooth distance cutoffs, divided by the square root of their positive sum of squares, give bounded finite overlap and hop differences O(1/R). Include all particle relabellings, or equivalently use the antisymmetric cluster tensor maps with their factorial normalization. This preserves full fermionic antisymmetry and covers every flavor allocation.

On a branchπ, define field functions ja(y) equal to1 at the matter cells of cluster a, supported within distance R/3 of that cluster, and with disjoint supports for different clusters. Let j∞=(1−Σa ja²)^1/2. Choose cosine/sine transition profiles so both ja and j∞ are Lipschitz with constant C/R. They depend on the cell coordinate and are identity on all eight Q3 modes. The one-particle map

\[
 j:\mathfrak h\longrightarrow\bigoplus_{a\in\pi}\mathfrak h\oplus\mathfrak h_\infty,
 \quad f\mapsto(j_af)_a\oplus j_\infty f
\]

is an isometry. Its bosonic second quantization, followed by the canonical Fock tensor identification, is the geometric localization map. Crucially [ω,ja]=0 exactly, because ω acts only inside each cell. At every occupied matter cell exactly one ja=1 and the others vanish; the vertex therefore intertwines exactly into that cluster's field copy. Matter hops change j by O(1/R). On Nb≤2M, telescoping each tensor product gives a bound C M/R for the Fock-map difference. Bounded hopping then gives, for the combined branch map JR,M,

\[
 \|J_{R,M}H-H^{ext}J_{R,M}\|_{N_b\le2M}
 \le C_Nt_c(1+M)/R.
\]

The partition-of-unity hopping error has the same order. This estimate suffices; no unproved uniform-in-M compactness is used.

On a proper matter partition, Hext is the sum of the actual fragment Hamiltonians, each with its own full field, plus a nonnegative free-field factor. The locked all-cell/all-flavor proper lower applies to every allocation, hence this channel is≥Lproper. On the single matter-cluster branch with at least one external field quantum, Fourier transformation of the free copy gives

\[
 H_\lambda^{ext}(P)=\bigoplus_{m\ge1}\int^{\oplus}
 \left[H_\lambda(P-\sum_{j=1}^mk_j)+\sum_{j=1}^m\omega_{\ell_j}\right]d\mathbf k,
 \quad\omega_\ell\in\{1,3,5,7\},
\]

so this channel is≥eλ+1. If the matter is in the single bounded cluster and the external field copy is vacuum, all remaining relative coordinates lie in a finite lattice set and Nb≤2M. This branch is finite rank in a fixed momentum fiber: finite internal cube/flavor multiplicity and finitely many boson occupations remain. Its action on a weakly null Weyl sequence tends to zero.

Apply these statements to a Weyl sequence at a finite essential spectral point. First take its sequence index→∞ at fixed M,R to remove the finite-rank branch, then R→∞ to remove the hopping/localization defect, finally M→∞ to remove the number cutoff. The common domain and displayed commutator bounds justify each step. This gives

\[
 \boxed{\inf\sigma_{ess}H_\lambda(P)\ge
 \min\{L_{proper},\min_QE_\lambda(Q)+1\}.}
\]

The proof uses the finite-range density vertex, the absence of intercell boson propagation, the optical gap and fixed finite fermion number. Changing those hypotheses requires new commutator/cluster estimates. Møller's massive continuum analysis is a methodological comparison for geometric Fock localization, not the theorem used to cover this lattice CAR operator: [Møller2004](https://web.ma.utexas.edu/mp_arc/c/04/04-258.pdf).

The translated one-hop trial has a unique six-particle cluster center. Its norm and Hamiltonian pullbacks between different center translates vanish: translating all six particles to a new cell requires at least six cell hops, while the polar one-hop norm uses at most two and the energy uses at most three. The coherent clouds do not change matter support. Thus the Bloch sum has the original Gram and the same sector energy upper at every P. A native seven-count path certificate gives0 for the three-hop endpoint and720 for six hops, retaining the first reachable translation rather than assuming translation never occurs.

The locked sector uppers give Lproper−U42>31.6161863519252 and Lproper−U33>16.1415545876072. For every P, Eλ(P)≤Uλ and Eλ(P)−eλ≤72tc=9/125. The threshold inequality consequently yields

\[
 \inf\sigma_{ess}H_\lambda(P)-E_\lambda(P)
 \ge\min\{L_{proper}-U_\lambda,1-72t_c\}
 \ge116/125\quad(\lambda=42,33).
\]

Their bottoms are therefore isolated finite-multiplicity fiber eigenvalues, including their finite flavor factors. This is a spectral existence/gap statement in the declared law, not a prepared released eigenstate, capture amplitude, lifetime or electromagnetic nuclear prediction. The321 sufficient upper remains20.8492111445889… above the common proper lower; no321 band is inferred from the weighted source margin. The free-boson channel is indispensable: remote optical quanta provide the competing eλ+1 channel even where proper matter breakup is much higher.


## Exact design transformations and source custody

The following rows give the fixed transforms in the18-column order specified above; each row is one raw-source coefficient row. Entries containing i are Gaussian integers, with i²=−1. Thus X8=Xraw T8 and X6=Xraw T6 are specified exactly.

real8:

```text
0 0 -1 1 0 -1 -1 0
1 1 -1 1 -1 -1 0 0
1 1 0 0 -1 0 -1 0
0 1 1 1 0 1 0 1
1 -1 -1 1 1 0 0 1
1 0 0 -1 -1 0 0 1
1 1 1 0 0 0 -1 -1
-1 1 1 0 -1 -1 0 0
1 0 1 0 1 1 0 1
-1 -1 0 1 0 0 0 0
0 1 1 1 0 -1 1 -1
1 -1 1 0 -1 0 1 1
1 0 1 1 1 -1 -1 1
-1 1 -1 -1 -1 -1 0 1
0 1 0 -1 1 -1 -1 1
0 0 -1 0 1 -1 0 1
-1 1 1 1 1 0 1 0
0 -1 1 0 1 1 1 -1
```

complex6:

```text
1+(1)i 0+(1)i 1+(1)i 1+(-1)i 0+(-1)i 0+(0)i
0+(0)i -1+(0)i 0+(1)i 0+(0)i 0+(-1)i 0+(-1)i
1+(-1)i 1+(1)i 1+(1)i -1+(-1)i 1+(-1)i -1+(-1)i
-1+(0)i 1+(1)i 0+(1)i 0+(1)i 1+(-1)i -1+(-1)i
0+(1)i -1+(1)i 0+(-1)i 1+(1)i 1+(-1)i -1+(0)i
0+(-1)i 0+(1)i 0+(-1)i 0+(1)i 1+(-1)i 1+(0)i
-1+(1)i 1+(0)i -1+(-1)i 0+(1)i 1+(-1)i 1+(0)i
0+(1)i 1+(0)i 0+(1)i 1+(1)i 1+(1)i 0+(0)i
-1+(-1)i 0+(-1)i 1+(1)i 1+(1)i 0+(-1)i -1+(1)i
1+(1)i 0+(0)i 0+(-1)i -1+(1)i -1+(1)i -1+(0)i
-1+(0)i 0+(0)i 1+(-1)i 1+(0)i 1+(0)i -1+(-1)i
-1+(0)i 1+(1)i 0+(-1)i 0+(0)i 1+(-1)i -1+(0)i
0+(1)i -1+(0)i 0+(1)i -1+(1)i -1+(-1)i -1+(1)i
-1+(1)i 0+(-1)i -1+(-1)i 0+(0)i 1+(0)i 1+(-1)i
0+(0)i -1+(0)i 1+(-1)i -1+(0)i -1+(0)i 0+(-1)i
0+(0)i -1+(-1)i 0+(0)i -1+(1)i 1+(1)i -1+(1)i
1+(0)i 0+(0)i 1+(0)i 0+(0)i 0+(1)i 1+(1)i
1+(1)i 1+(0)i -1+(0)i 1+(0)i -1+(1)i 0+(0)i
```

The raw exterior coefficient operand is authoritative for signs and source ordering. Independent reconstruction acts in ascending Fourier-mode order within each of the four flavor masks, with flavor order proton-up,proton-down,neutron-up,neutron-down. This convention fixes every annihilation/creation sign. The complete inverse specification is the cofactor expression above with these transforms and this operand; saved inverse arrays were also checked entry by entry.

Source SHA256 custody (paths shortened only by the declared roots):

| Source | SHA256 |
|---|---|
| /home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/peers/THREE/gen/ANISOTROPIC_REPAIR_OPERANDS.json | `653b7546e23bc2f4760c260bd91a2e0b830e8b83e52db0ea78cd6618df77cb96` |
| /home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/peers/THREE/gen/ANISOTROPIC_SOURCE8_OPTIMIZED.json | `7e9822018f9afdf097035201b0b2574da095da2a885ed0d99a41f6e16b56fd32` |
| /home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/peers/THREE/gen/ANISOTROPIC_SOURCE6_COMPLEX_V2.json | `277ed366c920059bdec40f5719f85bbf207925e7fdaa971387e5129e1c4dfc87` |
| /home/lilhelper/SAM_Research_Overflow/GEN7/vol_ii_refine_1111901/duck_run_20261112T043202Z/peers/ONE/work/reconstruct.py | `4a15a7dc98a3a45b8a80f835c254d32ece9a8d3bdd81475a7c5bf4748acee65d` |
| /home/lilhelper/SAM_Research_Overflow/GEN7/vol_ii_refine_1111901/duck_run_20261112T043202Z/peers/ONE/PRECOMMIT.md | `d075043831e42235caba26aab16ca0c365d8fad46c7d3435aac828b2d748d121` |
| /home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6/PHYSICAL_IMAGES.json | `eab597013f2869b4e6241ce58a3fef4a284b8d8dc4ad588ec9d416d2bf2c69d4` |
| /home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6/MOMENTS.json | `929ec03c604ddb80d03995e6de17deabfe33a6f18a2240229e06ebb705f72482` |
| /home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6/BOUNDS.json | `27e6c26776bb095e673bcf8cca30c23a9e994dff18f21b5244a1e232bb0fcdf8` |
| /home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/sources/receiving_action/peers/ONE/gen/SPATIAL_FLAVOR_DISCOVERY.json | `cf25c8cdf6870c4b8aacf9013e8d5f51ee381cff1ae96191a53beb3302dc2272` |
| /home/lilhelper/SAM_Research_Overflow/GEN7/vol_ii_refine_1111901/duck_run_20261112T043202Z/peers/ONE/PRECOMMIT_PAIR.md | `0cb2c00da0c295a7138a038d145878c7563bc6d746cef4b07921b0ee2f17fe8b` |

For complete reconstruction without any ancillary file, the18 raw columns are given next as sparse sums in the four-mask exterior basis. Each item `c:(a,b,c,d)` means that integer coefficient times the unit exterior word with those decimal bit masks; absent words have zero coefficient. Mask bit k denotes the occupied Fourier mode k. This is the complete nonzero raw source data, not a compressed density operator.

| Column | Label | Nonzero coefficient:mask terms |
|---:|---|---|
| 0 | originalphase0 | `1:(3,2,3,1); 1:(5,2,5,1); -1:(9,2,9,1); 1:(17,2,17,1); -1:(33,2,33,1); -1:(65,2,65,1); -3:(129,2,129,1)` |
| 1 | originalphase1 | `1:(3,16,3,1); 1:(5,16,5,1); -1:(9,16,9,1); 1:(17,16,17,1); -1:(33,16,33,1); -1:(65,16,65,1); -3:(129,16,129,1)` |
| 2 | originalphase2 | `1:(3,4,3,1); 1:(5,4,5,1); -1:(9,4,9,1); 1:(17,4,17,1); -1:(33,4,33,1); -1:(65,4,65,1); -3:(129,4,129,1)` |
| 3 | originalphase3 | `1:(3,8,3,1); 1:(5,8,5,1); -1:(9,8,9,1); 1:(17,8,17,1); -1:(33,8,33,1); -1:(65,8,65,1); -3:(129,8,129,1)` |
| 4 | originalphase4 | `1:(3,1,3,16); 1:(5,1,5,16); -1:(9,1,9,16); 1:(17,1,17,16); -1:(33,1,33,16); -1:(65,1,65,16); -3:(129,1,129,16)` |
| 5 | originalphase5 | `1:(3,1,3,2); 1:(5,1,5,2); -1:(9,1,9,2); 1:(17,1,17,2); -1:(33,1,33,2); -1:(65,1,65,2); -3:(129,1,129,2)` |
| 6 | originalphase6 | `1:(3,1,3,4); 1:(5,1,5,4); -1:(9,1,9,4); 1:(17,1,17,4); -1:(33,1,33,4); -1:(65,1,65,4); -3:(129,1,129,4)` |
| 7 | originalphase7 | `-2:(3,1,3,1); 2:(5,1,5,1); -2:(33,1,33,1); 2:(65,1,65,1)` |
| 8 | originalphase8 | `1:(3,1,3,8); 1:(5,1,5,8); -1:(9,1,9,8); 1:(17,1,17,8); -1:(33,1,33,8); -1:(65,1,65,8); -3:(129,1,129,8)` |
| 9 | source600_ground_u | `1:(3,1,3,1); 1:(5,1,5,1); -1:(9,1,9,1); 1:(17,1,17,1); -1:(33,1,33,1); -1:(65,1,65,1); -3:(129,1,129,1)` |
| 10 | source600_pair_t1_d1 | `-1:(5,1,9,1); 1:(9,1,5,1); -1:(17,1,33,1); 1:(33,1,17,1); -1:(65,1,129,1); 1:(129,1,65,1)` |
| 11 | source600_0,0,1,2 | `-1:(5,1,9,1); -1:(9,1,5,1); 1:(17,1,33,1); 1:(33,1,17,1); -1:(65,1,129,1); -1:(129,1,65,1)` |
| 12 | source600_0,0,2,1 | `-1:(3,1,9,1); -1:(9,1,3,1); 1:(17,1,65,1); -1:(33,1,129,1); 1:(65,1,17,1); -1:(129,1,33,1)` |
| 13 | source600_0,0,2,4 | `1:(3,1,9,1); 1:(9,1,3,1); -1:(17,1,65,1); -1:(33,1,129,1); -1:(65,1,17,1); -1:(129,1,33,1)` |
| 14 | source600_0,0,4,1 | `-1:(3,1,33,1); 1:(5,1,65,1); -1:(9,1,129,1); -1:(33,1,3,1); 1:(65,1,5,1); -1:(129,1,9,1)` |
| 15 | source600_0,0,4,2 | `1:(3,1,33,1); -1:(5,1,65,1); -1:(9,1,129,1); 1:(33,1,3,1); -1:(65,1,5,1); -1:(129,1,9,1)` |
| 16 | source600_0,0,4,4 | `-1:(3,1,33,1); -1:(5,1,65,1); -1:(9,1,129,1); 1:(33,1,3,1); 1:(65,1,5,1); 1:(129,1,9,1)` |
| 17 | source600_0,0,5,2 | `1:(3,1,17,1); -1:(5,1,129,1); -1:(9,1,65,1); 1:(17,1,3,1); -1:(65,1,9,1); -1:(129,1,5,1)` |

# 3. Controls, Obstructions & Superseded Attempts

Predictions and failing-control expectations were committed before execution in the SHA-bound PRECOMMIT.md; the independent central-projector control was additionally committed in PRECOMMIT_PAIR.md. These are testable changes to the hypotheses, rather than relabellings of a null symmetry.

| Control or obstruction | Exact witness / expected result | Completed native readback and disposition |
|---|---|---|
| Invisible source11 kernel, then reachable repair | 6(B15=1,B04=−1/6) gives zero on all old columns, but new physical source-pair response144 | ONE7_RANK_CONTROLS plus ONE7_EXACT_NULLS; old invisibility and new nonzero both observed |
| Prematurely compressing density | Full ρ4² minus compressed square has raw source diagonal90; source norm15 gives normalized error6. Edge7 gives128/16=8 | ONE7_RANK_CONTROLS; rejected shortcut, positive omitted-image contribution |
| Too few independent real directions | Duplicating one real8 source direction makes the36-entry design singular | ONE7_SINGULAR_CONTROL_V3 overall COMPLETED; inner INVERTIBILITY_UNRESOLVED, as required by engine contract |
| Treating 5+1 as sole branch beyond its crossing | δ=10/3+1/100 makes the competing4+2 envelope lower by1/50 | ONE7_ROBUSTNESS; δ≤10/3 is retained |
| Uniform shift cancels between target and breakup | Sum of cell particle squares is36 for target,26 for5+1, giving nonzero margin shift5Δ/4 | ONE7_ROBUSTNESS and ONE7_DRESSED_DENSITY; cancellation rejected |
| Deleting C3 in the pair central polynomial | A full-parent basis direction has P411 diagonal1/6; the selected pair source has P411=0 and would be an unreachable control | ONE7_PAIR_SECTORS; full-parent witness used, selected pair null explicitly avoided |
| Conflating common-map error and known-input optimum | Squared-distance difference0.0000289339914409698435484…>0 | ONE7_ARRIVAL; optimization domains kept explicit |
| Assuming no intercell translate is reachable at any order | Three-hop endpoint vanishes, six-hop endpoint720 | ONE7_FIBER_KINEMATICS; finite order used, no all-orders claim |
| Promoting all flavor sectors from a weighted margin | The sufficient321 upper is20.8492111445889… above common breakup lower | ONE7_FIBER_KINEMATICS; only42 and33 receive the displayed isolated-band conclusion |

The initial rank task's rational null products returned enclosing intervals at zero. This establishes containment, not an exact-zero certificate by itself; ONE7_EXACT_NULLS supersedes that part with exact source-word integer products. Native rank and inverse calculations stayed at36×36 or below. Full density contractions used1795 physical rows but at most8 source columns; no large dense parent solve or rank was submitted.

Admission corrections: ONE7_SINGULAR_CONTROL was rejected before admission because expected_reason was supplied with expected_status=COMPLETED. ONE7_SINGULAR_CONTROL_V2 was rejected because supersedes named an unreturned admission rejection. V3 removed those invalid metadata fields, completed, and gave the intended inner singularity status. There was no admitted failed scientific task. A missing numpy import stopped a host successor generator before its final null-task file was written; the dedicated additional_native.py generated that file and it subsequently completed. The audit helper initially assumed status CERTIFIED instead of CERTIFIED_SOLVE and a mapping instead of a row-list solution; its corrected version checked all entries. A diagnostic read of a None-valued unused sector matrix and a plain python executable lookup also failed before producing scientific output; python3/the pinned .venv executable and explicit sector filtering resolved them. None changes a source hash or an already sealed input.

Calibration scope is substantive. The error bound for reconstructed B assumes known source Grams, common energy zero and the subtracted kinetic term; the complex scheme also assumes controlled relative phases. Source11 still has15 invisible directions. The one-hop continuation treats a common bounded instantaneous density perturbation of the full law. Altering receiver frequencies, vertices or hopping while only matching completed static B requires the explicit extra form-error allowance η derived above. The reported static tomography alone cannot set η=0. The arrival attainment assumes access to the stated full-flavor orbital alignment; central Gram information certifies its obstruction but does not construct a physical control apparatus. Fiber eigenvalues prove spectral existence in the declared lattice law; preparation, release and capture remain separate physical questions.

# 4. Exceptions-Only Custody Diff

There are11 completed native submissions containing127 completed native operations, with13713 exact rational/interval-entry readback checks in the local custody audit. Every key below has an on-disk completed receipt and every recorded program trace was read. The native-reported receipt SHA256 is printed; results/NATIVE_AUDIT.json separately records the native receipt hash and the SHA256 of the full on-disk return. The analytical localization proof is labelled ANALYTICAL_PROOF: its infinite-dimensional assertion is not relabelled as a native finite-matrix certificate.

| Native key | Status | Operations | Receipt SHA256 |
|---|---|---:|---|
| ONE7_ARRIVAL | COMPLETED | 8 | `e7b7491a290559487a8262303ee2083bedf905d6b29f9e884125ff7af76d5364` |
| ONE7_COMPLEX6 | COMPLETED | 39 | `47b9cdcc47edc829a6e2db895f0429b0485b9b2227be0cde847df94b0991e0e8` |
| ONE7_DETERMINANTS | COMPLETED | 4 | `dc6bca80fd4f3a3a756ef0725920e24f7fddb2a3c4774303165e204be0d1e32f` |
| ONE7_DRESSED_DENSITY | COMPLETED | 14 | `eeb755ad95f46cead5a0fea82e233a8793361949819a357e64212831b44f1b51` |
| ONE7_EXACT_NULLS | COMPLETED | 4 | `74bacddb6d5ae5a843663fc387a858d7fcd9129407772f3883d9dec965e1733b` |
| ONE7_FIBER_KINEMATICS | COMPLETED | 4 | `6968c414f139b219a70ee078f4b203580e6511734695d68e7955d1c65886e56a` |
| ONE7_PAIR_SECTORS | COMPLETED | 5 | `6024a633e08e245a94315e63f4b12718789ecc003e6c7c81826d6141a274b651` |
| ONE7_RANK_CONTROLS | COMPLETED | 6 | `401d56feed74ed01c7682bb8fb4b7271e64dad4fb081722c19618ea577a2d5a1` |
| ONE7_REAL8 | COMPLETED | 39 | `a0d30f4c0189158ab5537c36d8d4b4353e51e10820180d19afbc1e61df704d7c` |
| ONE7_ROBUSTNESS | COMPLETED | 3 | `854402368e5700131f16fbeb1d3ef7bdc2d1ae4e314d4f22002a4aae09e16bd7` |
| ONE7_SINGULAR_CONTROL_V3 | COMPLETED | 1 | `a12f95c71186115c1fd45cd2bae65d1c9fc04da409b3349b15206e7be5de0d4d` |

MISSING_RECEIPT:0. Unadmitted schema corrections:2 (the singular-control attempts described above); neither is counted among the11. Superseded mathematical evidence: interval-only zero checks in ONE7_RANK_CONTROLS are replaced by ONE7_EXACT_NULLS. No baseline replay, external joint archive, N=5000 contraction, GEN2_HD_PRIMITIVES standalone call, or dense rational solve above64×64 was run. Scientific host commands were pinned and single-threaded. All tasks were admitted before the final180-second readback/assembly reserve. Completion drift check: the initial claims were reconstructed, the uniform-shift interval was retained, and the new dynamic calibration remainder was kept explicit. No locked baseline was reopened. The written report carries every asserted result and qualification; ancillary work files are supporting custody, not additional delivered conclusions.
