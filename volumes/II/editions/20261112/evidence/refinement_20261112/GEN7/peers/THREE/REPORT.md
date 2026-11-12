# Executive Delta Table

| ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict |
|---|---|---|---|---|---|
| THREE-S1 / TWO-O3 | VII.2, VII.4–6; VIII.8; X; App.A | All16 boundary weights equal; \(Z=16[256\cosh(4x)\cosh^4(2x)]^k\); \(h^{2k}\le\Omega_k\le h^k\); \(\mu_1=\mu_2=\Omega_k\) | THREE_STAR_K1…K4, THREE_STAR_LEDGER, THREE_HELLINGER: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | HELD |
| THREE-S1E | VII–VIII; X; App.A | At \(x=\log2/2\): \(Z_{\rm layer}=10625/8\), \(E/J=-708k/85\); full4096-state k1 enumeration, ground \(-12J\), degeneracy128; native conditional Gibbs entropy agrees with calorimetric ledger | THREE_STAR_LEDGER, THREE_PEAK: COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | HELD |
| THREE-S2 / TWO-O4 | VI–X | \(a_*\in[.20318786997997,.20318786998000]\); \(C_*\in[.04047563986824320,.04047563986824766]\); \(C(\Omega_3)=.0404751384244456948686\ldots\); fraction in \([.99998761121989,.99998761122001]\) | THREE_PEAK: COMPLETED,15 native calls | NATIVE_CERTIFIED + ANALYTICAL_PROOF | HELD; unique integer-layer optimum k3 |
| THREE-S3 / TWO-O5 | IX.10–13; X |54 signed2×2 core blocks independently rebuilt; all162 first/middle/last-history Young/Cauchy receivers overlap fresh host values; zero endpoint separations | THREE_RESIDUAL_CORE_0/1, THREE_RECEIVER_0…5: COMPLETED | NATIVE_CERTIFIED + HOST_DIRECTED_ARB + ANALYTICAL_PROOF | Negative result reproduced |
| THREE-S4 continuation | IX.9–13; X | Shared upstream-point / exact dependency linkage preserves old scalar baseline. For each37 V000_BASE histories, paid mixed-action interval admits zero additional Schur gain; perturbing that action gives a strictly positive control gain | THREE_LINKED_CERTIFICATE: COMPLETED,38 exact words | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | No resolved separation in tested linked interval relaxation; physical shared-source continuation remains open |

# Self-Contained Derivations (Drop-In TeX Ready)

Peer THREE treats H003004 (atoms), H003005 (spin-memory), H003006/H003008 (CAR/Fock/loading) as locked I1/R2 inputs. No base script, N5000/N2000 density archive, or completed VolumeIII TWO-F03 contraction was rerun. The latter remains the established signed-chain CMI interval \([3.41219962633,3.41223131098]10^{-6}\) nats. Manuscript:10 November117-page edition, SHA256 `391450c512bfda11682e5a58b6f3f8d27856cdc4381cd962432ae9d3e521a5f3`. Native certification below means arithmetic on the explicitly bound source operands, alongside the stated analytical proof; it is not outside-party verification or physical calibration.

**S1. Full-port stars and their invisible thermodynamics.** Let \(s\in\{-1,1\}^4\), \(p\in\mathcal P=\{(1,p_2,p_3,p_4):p_j=\pm1\}\), and \(h_{\ell,p}=\pm1\), \(1\le\ell\le k\). Use the original VII.2 star law
\[
H(s,h)=-J\sum_{\ell,p}h_{\ell,p}\,p\cdot s,\qquad x=\beta J>0.
\]
The eight unsigned magnitudes \(|p\cdot s|\) are4 once,2 four times,0 three times for every s. This follows by multiplying the signs in p by the boundary signs, then fixing the first ray coordinate by overall reversal. Summing every hidden spin gives
\[
Z_s=\prod_{\ell,p}2\cosh(xp\cdot s)
=Z_{\rm layer}^k,\qquad Z_{\rm layer}=2^8\cosh(4x)\cosh^4(2x).
\]
Consequently \(\pi_s=1/16\), \(Z_{\rm total}=16Z_{\rm layer}^k\). A normalized boundary reader cannot see the k-dependent factor; the absolute free energy retains it.

Give each boundary spin unit heatbath attempts, and each hidden spin any fixed positive attempt rate. A boundary flip keeps all hidden coordinates. For neighboring s,t write p(h)=\(\pi(h\mid s)\), q(h)=\(\pi(h\mid t)\). Detailed balance and equal boundary partitions yield
\[
A_{ts}=\sum_h p(h)\frac{q(h)}{p(h)+q(h)}=\frac{\Omega_k}{2},
\qquad \Omega_k=2\sum_h\frac{p(h)q(h)}{p(h)+q(h)}.
\]
Boundary sign/permutation symmetries permute the signed star rays, so every boundary edge has this same multiplier. The reference thermal boundary generator has edge rate1/2. This establishes an instantaneous projected-generator statement, not equality of microscopic semigroups.

Let \(\mathfrak h=\sum_h\sqrt{p(h)q(h)}\). Arithmetic–geometric mean gives \(\Omega_k\le\mathfrak h\). Cauchy applied to \(\sqrt{2pq/(p+q)}\sqrt{(p+q)/2}\) gives \(\mathfrak h^2\le\Omega_k\). Independent layers tensorize the affinity. For one flipped port the average hidden field has magnitudes3 twice and1 six times; the complete conditional normalizer remains the original layer partition. Hence
\[
\mathfrak h=h(x)^k,\quad
h(x)=\frac{\cosh^2(3x)\cosh^6(x)}{\cosh(4x)\cosh^4(2x)},\quad
h^{2k}\le\Omega_k\le h^k.
\]
At x>0 neighboring conditional laws differ (a star coupling to the flipped port changes its odds), so strict Cauchy for probability vectors gives0<h<1. Also0<\(\Omega_k\)<1 for k>0. At x=0 or k=0, \(\Omega=1\); this degenerate branch has no claimed positive variance.

For \(f=s_0\), define \(A=-L\ge0\) in \(L^2(\pi)\), \(\mu_j=\langle f,A^jf\rangle_\pi\), \(\|f\|_\pi=1\). Only the observed-site complement \(I-P_0\) acts on f. Its orthogonal-projector identity gives
\[
\mu_1=2\mathbb E_\pi r_0=\Omega_k,\quad
\mu_2=\|(I-P_0)f\|_\pi^2=\mu_1,\quad
\operatorname{Var}_\nu(\Lambda)=\Omega_k(1-\Omega_k)>0.
\]
Thus the clock-invariant dispersion is \(\operatorname{Var}(\Lambda)/(\mathbb E\Lambda)^2=1/\Omega_k-1\). The locked reversible spectral/binary-law result makes every positive two-wait defect positive. The independent-bit projected semigroup has zero binary CMI. Equal equilibrium and a common instantaneous multiplier therefore do not identify the microscopic history.

At x=\(\log2/2\), every microscopic weight is exactly \(2^{-H/(2J)}\). An independent enumeration visits all16×256=4096 configurations. A separate Bernoulli generating-polynomial calculation uses plus probabilities16/17 once,4/5 three times,1/2 three times,1/5 once, then convolves k complete layers. Native source words multiply every spin factor before contracting the actual logistic port rate \(1/(1+2^F)\). They return the identical \(\mu_1,\mu_2\) rational values listed below.

| k | Exact \(\Omega_k\) | Decimal display |
|---:|---|---:|
| 1 | `105093049/193109800` | 0.5442139601408111 |
| 2 | `57007098595961645770832669/174163499373856136885000000` | 0.3273194372007378 |
| 3 | `41212760287527553529502111787205140357025020124861/201665913641943433960679556770064141175925000000000` | 0.2043615579016519 |
| 4 | `163824947828855352639526705333591096776735269038715878672975677355227760075384438681/1257316995841854988125588297472053408861346054456982771998526231125743625000000000000` | 0.1302972507097655 |

Here \(\cosh x=3/(2\sqrt2)\), \(\cosh3x=9/(4\sqrt2)\), \(\cosh2x=5/4\), \(\cosh4x=17/8\), so \(h=59049/85000\), natively checked from their squared rational factors. Direct enumeration and the native partition product both give \(Z_s=10625/8\), \(Z=21250\) at k1. The source energy minimum is−12J with128 configurations, consistent with16 boundary rows and eight zero-field hidden configurations per row.

Differentiating the full partition at fixed J gives the complete calorimetric account
\[
E=-kJ[4\tanh(4x)+8\tanh(2x)],\quad
\beta^2\operatorname{Var}(H)
=k[(4x)^2\operatorname{sech}^2(4x)+4(2x)^2\operatorname{sech}^2(2x)].
\]
The heat capacity in units of \(k_B\) is the last expression. At the rational point, \(E/J=-708k/85\). For k1 the conditional hidden entropy is exactly
\[
S(h\mid s)=\log(10625/8)-(354/85)\log2;
\qquad S(s,h)=4\log2+kS(h\mid s).
\]
Native GEN5_ENTROPY on all256 conditional probabilities overlaps the independent GEN5 logarithmic ledger. Relative to uncoupled hidden spins, \(\Delta F=-k\beta^{-1}\log[\cosh4x\cosh^4 2x]\); it survives boundary normalization. These are source-unit thermodynamic statements. No SI temperature, physical attempt rate, calorimeter implementation, or reusable preparation/reset payment is assigned.

**S2. The sharp short-time coefficient and all integer layers.** Reuse the locked H003005/QUADRATURE rare-cell theorem, without replaying its proof or code:
\[
I(t,s)=\frac{ts}{4}[b\log(b/a^2)-b+a^2]+O(ts(t+s)),\quad b=\alpha a.
\]
At observed attempt1, \(0<a\le1\) and
\[
C(a)=\tfrac14a(-\log a-1+a),\quad
4C'(a)=-\log a-2+2a=:g(a),\quad
4C''(a)=2-a^{-1}.
\]
Since g decreases on(0,1/2), increases on(1/2,1), tends to+infinity at0, has \(g(1/2)=\log2-1<0\), and \(g(1)=0\), it has one interior zero \(a_*\in(0,1/2)\). C increases up to that zero and decreases thereafter to C(1)=0; C(0+)=0. This is its unique maximum. At the root, \(-\log a_*=2(1-a_*)\), so \(C_*=a_*(1-a_*)/4\). The two precommitted rational endpoints have natively positive signed g values, yielding the executive interval. The proof uses monotonicity of g, not false global concavity of C.

Native logarithmic evaluations give
\[
(C(\Omega_1),C(\Omega_2),C(\Omega_3),C(\Omega_4))
=(.02076540344020355,\ .03634376231953460,\ .04047513842444569,\ .03805442433528087)
\]
as rounded displays. For every k≥5, \(0<\Omega_k\le h^k\le h^5<a_*\). C increases on that interval; native evaluation proves
\[
C(\Omega_3)-C(h^5)>0.00070507061498.
\]
Native positive differences also separate k3 from k1,k2,k4; k0 has C(1)=0. Therefore k3 is the unique integer optimum in this fixed eight-star dictionary. Its fraction of the universal maximum is99.9987611… percent. This is an asymptotic coefficient optimum: it supplies no finite-lag optimum, minimum hidden-spin theorem outside the dictionary, or remainder constant uniform as a→0.

**S3. Original-source reconstruction of the joint residual block.** The source remains the complete original physical Gibbs system, \(A=C+B\), where C sums all20 core heatbath complements and \(0\le C\le20I\); B retains every background flip. Inner products are Gibbs \(L^2(\pi)\), resolvent is \((A+\xi)^{-1}\), and mean attempted-site count is N/\(\xi\). Retain
\[
b_5=(d,e,u_d,u_e,w_d),\quad
G_5=\langle b_5,b_5\rangle,\quad D_5=\langle b_5,Ab_5\rangle,
\quad c=G_5^{-1}D_5[:,4].
\]
Let \(\lambda=W_{de}/W_{dd}\), \(r_1=w_e-\lambda w_d\), \(r_2=Aw_d-b_5c\), and \(R=(r_1,r_2)\). Fresh solves reconstruct c and the source-core polynomial coefficients from the retained basic Grams, p/q coefficients and action identities. They are compared with the original residual-output cache only after reconstruction. With \(\phi=(d,e,Cd,Ce,C^2d,C^2e,C^3d)\), write \(U=\phi V\) for the seven-feature core map. Native products evaluate \(V^TE_{\rm edge}V\) separately for every54 preparation, retaining the mixed entry and all coefficient intervals. None is inferred from a million-state re-integration; the completed edge integrals are the source operands.

For a fully explicit coefficient reconstruction, let \(B_0=V_0^{-1}D_s\) be the original two-coordinate port projection, \(p_d,p_e,q_d,q_e\) the original two-component source coefficients. In the feature order above,
\[
v_1=(q_e-\lambda q_d,\ -p_e+\lambda p_d,\ -\lambda,1,0)^T,
\quad v_2=(0,0,q_{d0},q_{d1},-p_{d0},-p_{d1},1)^T-Mc,
\]
where the first two groups in v1 each have two entries and
\[
M=\begin{pmatrix}
1&0&-(B_0)_{00}&-(B_0)_{01}&q_{d0}\\
0&1&-(B_0)_{10}&-(B_0)_{11}&q_{d1}\\
0&0&1&0&-p_{d0}\\0&0&0&1&-p_{d1}\\
0&0&0&0&1\\0&0&0&0&0\\0&0&0&0&0
\end{pmatrix},\qquad V=(v_1,v_2).
\]
At V000_BASE, fresh native contractions are enclosed by the outward display
\[
\begin{pmatrix}
[10.4132006,10.4132021]&[-0.0000069,0.0000144]\\
[-0.0000069,0.0000144]&[9.7484518,9.7487630]
\end{pmatrix}.
\]
The two computed off-diagonal enclosures overlap and both contain the common true signed mixed entry. Neither interval is replaced by its midpoint as a scientific value.

The exact full residual Gram is
\[
G_R=\begin{pmatrix}\delta W&j\\j&\beta_r\end{pmatrix},\quad
\delta W=W_{ee}-W_{de}^2/W_{dd},\quad
j=J_{21}-\lambda J_{11},\quad
\beta_r=F_{11}-k^TG_5^{-1}k,\quad k=D_5[:,4].
\]
Self-adjointness and the retained source action give the stronger linked coupling identity
\[
H=\langle b_5,AR\rangle
=\begin{pmatrix}0&0\\0&0\\0&0\\\delta W&j\\j&\beta_r\end{pmatrix}.
\]
In particular the tiny nonzero interval midpoints in the first three entries of the older h column are enclosure effects, not additional exact couplings.

For the conservative full matrix reconstruction, write \(R=U+V_{\rm rem}\) and \(\|v_i\|_\pi^2\le\delta_i^2\). For every real or complex coefficient z,
\[
\|V_{\rm rem}z\|_\pi^2\le2\sum_i\delta_i^2|z_i|^2.
\]
Let \(M_+\) be the signed auxiliary core contraction, enlarged by symmetric row-radius uncertainty and the full physical-field transfer \(80E_0\operatorname{diag}(R_1^2,R_2^2)\), with \(E_0=(\beta/N)/(\pi/4)^2\) and \(R_i\) the actual analytic coefficient amplitude. The factor80 follows from the original40 transfer and \((\sum|z_i|R_i)^2\le2\sum|z_i|^2R_i^2\). Young and C≤20I then yield
\[
D_R\preceq J_+=(1+\eta)M_+
+40(1+\eta^{-1})\operatorname{diag}(\delta_1^2,\delta_2^2)
+2\operatorname{diag}(b_1,b_2),\qquad\eta>0.
\]
The background terms bound every physical background flip. Here \(\delta_2,b_2\) are the retained complete r2 payments; \(\delta_1\) uses \(B h_e-\lambda B h_d\), its auxiliary norm and its full strip transfer. The explicit conservative derivative used for r1 is
\[
L_1=960+320|\lambda|+4|p_{e0}-\lambda p_{d0}|
+12|p_{e1}-\lambda p_{d1}|+(5\beta+4)(12+4|\lambda|),
\quad b_1=2(N-20)(\beta/N)^2L_1^2.
\]
This is a full-source upper cap; it is not an evaluation of exact physical \(D_{12}\).

For \(K=\xi G_5+D_5\), \(g=G_5[:,0]\), \(v=H^TK^{-1}g\), the seven-coordinate lower is
\[
L_{7,+}=g^TK^{-1}g+v^T[\xi G_R+J_+-H^TK^{-1}H]^{-1}v.
\]
Fresh host directed arithmetic and324 native solve/product nodes cover all162 comparisons (indices0,18,36 for54 preparations). Every native value overlaps the fresh host enclosure; none separates above its completed scalar receiver. For V000_BASE the rounded normalized differences at indices0,18,36 are respectively−1.54×10^{-24},−1.03314×10^{-7},−2.98678×10^{-8}. They describe this overpaid cap and do not erase the option of retaining the original scalar lower.

**S4. Link the scalar baseline and variational increment.** A new source-linked test avoids the baseline inflation of the preceding joint Young cap. Preserve the completed scalar \(C_{22}\) exactly at the same source reference. The signed core mixed entry receives its entrywise physical transfer. A valid absolute mixed-action error is
\[
\varepsilon_{12}\le40R_1R_2E_0
+\sqrt{20\delta_2^2 I_{11,+}}+\sqrt{20\delta_1^2 I_{22,+}}
+20\sqrt{\delta_1^2\delta_2^2}+\sqrt{b_1b_2}.
\]
This follows from Cauchy for each core/remainder pair and each background pair, keeping both remainder columns. At V000_BASE the full mixed-action enclosure is conservatively contained in[−0.00476,0.00476]; its core midpoint is only3.76957×10^{-6}. The separate d11 cap is \((\sqrt{I_{11,+}}+\sqrt{20\delta_1^2})^2+b_1\). The old scalar cap is9.757902951928404… .

For a symmetric completion C, put
\[
S=\xi G_R+C-H^TK^{-1}H,\quad
q=v_1-S_{12}v_2/S_{22}.
\]
Schur elimination gives the exact additional gain over the retained r2 receiver:
\[
\Delta L=\frac{q^2}{S_{11}-S_{12}^2/S_{22}}\ge0.
\]
This is the linked variational-increment identity: the old value is the same dependent source expression on both sides. Subtracting two independently rounded receiver intervals would lose that linkage.

The test fixes one rational point in the *upstream* G4,D4,W,J11,J21,F11 intervals, then reconstructs G5,D5,c,lambda,GR and H by exact rational operations. All history-independent primitives are common. For each history, the critical mixed completion is
\[
C_{12}^{\rm crit}=H_1^TK^{-1}H_2-\xi(G_R)_{12}
+S_{22}\frac{v_1}{v_2}.
\]
It makes q=0. For every37 V000_BASE histories this critical value lies inside the above paid mixed-action interval, and the exact Schur leading minor/determinant remain positive. A separate exact audit checks64 primitive/derived entry containments, positive G7 and all37 residual caps and K7 matrices; the smallest K7 LDL pivot exceeds0.5063. The critical values range from−0.000892975820706 to−0.000010412731066. Native exact source words verify both full7 and retained6 solve residuals are zero and their value difference is exactly zero, for each of the37 witnesses. Changing C12 by1/1000 on history18 gives a positive gain, so the zero-gain test is reachable and not a symmetry null.

These are37 *alternative mixed completions*, one per history, at a common upstream point. They are not one physical source cancelling all histories simultaneously. Thus this explicit linked interval relaxation does not certify an individual strict endpoint separation, even after preserving the scalar baseline. The actual physical source has one shared mixed action; recovering its tighter dependency/covariance information, or directly paying that mixed action, could change the result. No universal physical no-gain theorem is asserted. A shared-source multi-history guarantee beyond this relaxation remains open.

**Source custody and provenance.** New finite enumeration, symbolic/rational reconstruction and Arb calculations are host work. Native certification applies to the completed words/products/solves/logs/entropy read back here. The original integrated source operands are authenticated before use; no inherited scalar output is called a new physical mixed measurement.

- `PREDICTIONS.md` SHA256 `51f3d2c3e3267fda1cbd723055493800d80e0aa2142e10a0729fd05042ebb35c`.
- `build_star.py` SHA256 `3a18d10b1887bedea52f7ebf8e5a5750a7f6c8d1d832ce8be60b1b9f3b50a160`.
- `star_host.json` SHA256 `d87681208d192a84b668b10728f641b6e8428ccba09eff8c559931ee2924cb1c`.
- `build_peak.py` SHA256 `1d6a6d65d7ef4d80e012c63476b14461fab79a423a3cfefa59dd24e727429c78`.
- `residual_host.json` SHA256 `197e7b371a5802b62e5de1473eab7277f4b2fc23d3b51713c4a46779e6b67c42`.
- `linked_point.json` SHA256 `101156e385924dc3f03bfb37acc52e0a9c733e18d20b6c11fda454d380493194`.

The retained raw source root is `SAM_Research_Project/GEN4/spin_source_moments_gcp1_20261017/cloud_runs/spin-source-moments-20261017-054112/extracted/results/science/profiles/`; the basic matrices come from `spin_difference_fifth1/native1/`, higher moments from `spin_upper_source1_20261014/{pilot3,native1}/`, and Gibbs source definitions from `spin_conditional_variance1/sources/original/`. Exact original/copy paths and hashes for every54 profile are carried in `residual_host.json` and each native job's sources list. Those directories were read only.

# Controls, Obstructions & Superseded Attempts

1. **Reachable star omission:** deleting only the++++ ray gives conditional partitions625/2 at s=(−,−,−,−) and2125/4 at s=(−,−,−,+), with exact difference−875/4. This was checked before locking the control, and certified by THREE_STAR_LEDGER. No symmetry-null fixture was used. THREE_CONTROL_STAR_V4 reaches that native output and fails its deliberately false zero-defect check with engine outcome FAILED_AS_DECLARED. V3 reached the same mathematical failure but its reason string did not match the engine substring contract; that declaration mismatch is retained.
2. **Probability support:** THREE_CONTROL_ENTROPY_V2 intentionally supplies probabilities(−1/2,3/2), with expected FAILED status and the exact engine-reason substring. The original ENTROPY request reached the same domain rejection but was FAILED_AGAINST_DECLARATION because its descriptive reason was not an engine-error substring; it remains in custody. It returns FAILED with “Probabilities must be exact nonnegative values summing to one.” This guards against interpreting signed source coefficients as statistical weights.
3. **False concavity shortcut:** THREE_PEAK returns \(C''(3/4)=1/6>0\); global concavity is false although the unique-maximum proof holds.
4. **Reachable residual control:** at the linked history18 point, changing only C12 by1/1000 produces full7-minus6 gain in[561461163/10^20,561461164/10^20], strictly positive; native solve residuals remain exactly zero. Zero innovation is therefore tied to the allowed completion, not a structural symmetry or rounding null.
5. **Reachable core-coefficient control:** adding1 only to the d coefficient of the actual V000_BASE r2 core vector changes the original quadratic contraction by the native rational interval[402384528779/549755813888,402726553379/549755813888], contained in[0.7319,0.7326]. THREE_CORE_CONTROL_V3 retains five completed product outputs and fails the deliberately false zero-defect check. Two preceding unadmitted wrappers are retained: CORE_CONTROL used expected_reason with COMPLETED, which the engine forbids; V2 used expected_failed_check outside its METHOD_EXECUTE-specific contract. V3 changes only declaration/check syntax.
6. **Retained caller-contract corrections:** THREE_CONTROL_STAR first failed before mathematical execution because its readout used unsupported status CONTROL. V2's formal supersedes field was rejected: the engine permits supersedes only for undeclared failed first attempts, not declared controls. V3 preserves the same−875/4 source witness and false equality check with DERIVED_NATIVE readout status, without the forbidden supersedes field. Final readback exposed the separate reason-substring contract on both STAR_V3 and the original ENTROPY control; STAR_V4 and ENTROPY_V2 correct only that declaration, and both return FAILED_AS_DECLARED. The two FAILED_AGAINST_DECLARATION records are not counted as successful declared controls. Neither earlier failure/rejection is counted as a successful hypothesis test. Minor read-only/audit corrections also remain: a system-Python diagnostic lacked python-flint; the pinned .venv succeeded; an early audit needed the direct-native return shape and Python's integer-string digit allowance. No source, prediction or mathematical acceptance criterion changed.
7. The missing physical D12 is distinct from a core auxiliary contraction; setting them equal would remove the explicit0.00476-scale payment. Additional action norm \(\|Ar_2\|^2\), full minimal invariant closure, SI units, preparation/readout/controller/reset costs and finite-time coefficient remainder constants are not supplied by this work.

# Exceptions-Only Custody Diff

Final readback:16 completed submissions,493 mathematical nodes in those completed submissions, three FAILED_AS_DECLARED controls, one failed wrapper, two FAILED_AGAINST_DECLARATION reason-string mismatches, and three unadmitted caller-contract corrections. Three failed mathematical-check programs additionally retain seven completed arithmetic-prefix outputs (two star words, five core-control products); they are not counted as completed programs. No MISSING_RECEIPT, in-flight or uncollected admission remains. All54 core matrices,162 receivers and37 exact linked equalities were read and checked; all611 bound source-hash occurrences still match. Arithmetic and receipt counts describe custody, not an external-verification level. No accepted/unread task is treated as a result. Locked baseline claims and their I1/R2 status are reused without new proof/replay; external archives are untouched. No manuscript, engine, Git history, external account or other peer folder is changed.


| Native key | Final status / control outcome | Receipt SHA256 |
|---|---|---|
| THREE_CONTROL_ENTROPY | FAILED / FAILED_AGAINST_DECLARATION | `eafb5853fedd9438b0f3606a5093e1e14698dcee1ac161b8a8b5d13c872545f2` |
| THREE_CONTROL_ENTROPY_V2 | FAILED / FAILED_AS_DECLARED | `d8d1aeaae09fb361c01657d021d8e5c386fa85225b167da85651c2e5ad47628d` |
| THREE_CONTROL_STAR | FAILED / FAILED_AGAINST_DECLARATION | `b3ed960333e56099e1cdede38530da2b20fe921545e63a571b9c19181f9772f1` |
| THREE_CONTROL_STAR_V3 | FAILED / FAILED_AGAINST_DECLARATION | `f7dd81659f19ad56e9513750c09c79cde51d50ae54163b34a09b4ed4287bfa39` |
| THREE_CONTROL_STAR_V4 | FAILED / FAILED_AS_DECLARED | `65a0fa778c1470177929f15b897d9e6490f9a4bb368c88bbc5b8b9db81488e94` |
| THREE_CORE_CONTROL_V3 | FAILED / FAILED_AS_DECLARED | `3761c5b25690c8a378abaf440fc913e2679cf418d74a858b41e7095c4779ab5c` |
| THREE_HELLINGER | COMPLETED | `9779456b650e8ccac73a5812b9328d0df76523cbcf0fbebd5cf138d9eeaf4386` |
| THREE_LINKED_CERTIFICATE | COMPLETED | `adfe497e5b4ea39b03061b062488dddf6e5fd184ce22fba6ce10678178b22a7b` |
| THREE_PEAK | COMPLETED | `08dee335acf0fb138fe1fc5d8879f3371a518fb381f422d11f07c4a01de3cd39` |
| THREE_RECEIVER_0 | COMPLETED | `f4f39674e8e45412e1c5d546e95c449a5ee18df3341a7507d07223562794673e` |
| THREE_RECEIVER_1 | COMPLETED | `f13881989be9ebc5a159696f81a3d028671bd8b4aba4de6a772ef3a625773191` |
| THREE_RECEIVER_2 | COMPLETED | `77d456e25330b5a30ba0927b58021444579815e6e0384e4a1de710de23acd92f` |
| THREE_RECEIVER_3 | COMPLETED | `327c4683807d57860f0f641f741006179c92df097366b3e85f4599d790397448` |
| THREE_RECEIVER_4 | COMPLETED | `059717615caed6520ec718f5ed5e3ed9d217fb9fc6f8530eae7fb723e9a79c71` |
| THREE_RECEIVER_5 | COMPLETED | `b521754f0ef42f6d025b749250b23175408892426347e00d7bec0c2d58c34c56` |
| THREE_RESIDUAL_CORE_0 | COMPLETED | `7a0e5dbc115a0d0acf4740c2e4e6d49f7a8c0bb268dc6a459940d5d0068e14fc` |
| THREE_RESIDUAL_CORE_1 | COMPLETED | `008bbb8ec1e9f3f03b8c7a8a6ec8acfeef761793cdf295e279bcfec7cbd75fec` |
| THREE_STAR_K1 | COMPLETED | `7140eb4b62d68dc526a10c524be671f3f0d0453a6df0a6373d1362eb75495933` |
| THREE_STAR_K2 | COMPLETED | `e0fbce779358a885b7a42f1136823ed3f856e03cc5033ef40c909f0bf2e9855b` |
| THREE_STAR_K3 | COMPLETED | `d1232dde3d05c6f949f00806dec1f278c9bdf5a2ca542667cb018af2830c490e` |
| THREE_STAR_K4 | COMPLETED | `b9035ae88050ff6ce186cc9169d5a9c6f3b73cd60d6650521edeb7570a7a2a52` |
| THREE_STAR_LEDGER | COMPLETED | `87bd0423da9ede2892ee086299e822aeb5880c504f81e73ec39c5ff6afa771c7` |

Retained completed control-prefix output `THREE_CONTROL_STAR_V3/000_false_uniformity.output.json` SHA256 `a170ffde2b79e29217281d273b33aef8f231da9cb519654324e453b1db9fbc29`.

Retained completed control-prefix output `THREE_CONTROL_STAR_V4/000_false_uniformity.output.json` SHA256 `fbf2972d6211cc05e419580e622a65002a8a97bc4338f22ac98befed5c70a0ff`.

Retained completed control-prefix output `THREE_CORE_CONTROL_V3/004_defect.output.json` SHA256 `58dee8252233b6699838616c9d5e9fea52399ca4a035b1d02ad1f3607f15c14f`.

Full readback/audit SHA256 `737dde9d78fbed57fcc92a46051f9023a1f937ed2a0fe14a58310ea775fae2e2`; linked containment/positivity audit SHA256 `8634bf4be2ac349ef6e9b24d10492b878286b9ae15009e42dbed27c626e917ce`. THREE_CONTROL_STAR is a wrapper failure. STAR_V3 and original ENTROPY are declaration-string mismatches; the mathematical failures are retained separately from corrected declared outcomes. STAR_V2, CORE_CONTROL and CORE_CONTROL_V2 are unadmitted and have no mathematical receipts. No missing or in-flight native outcome remains. Last research admission was05:03:03.78UTC, before the final180-second cutoff; the closing interval is reserved for readback, proof wording and report assembly.
