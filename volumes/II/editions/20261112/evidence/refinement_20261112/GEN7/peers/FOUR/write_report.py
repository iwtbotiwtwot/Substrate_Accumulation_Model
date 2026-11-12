from pathlib import Path
from fractions import Fraction as F
import json,hashlib,collections
H=Path(__file__).resolve().parent;O=H/'results'
load=lambda n:json.loads((O/n).read_text())
dp=load('C12_DP.json');rf=load('REFERENCES.json');gc=load('GRAMMAR_CHART.json');nc=load('NATIVE_CHECKS.json');ni=load('NATIVE_INDEX.json');rice=load('RICE_ARB.json');manifest=load('SOURCE_MANIFEST.json');wa=load('WAVE_RAW.json')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
q=json.loads(Path(next(p for p in manifest if 'INDUCED_INPUT' in p)).read_text())['data']['operator']
f=lambda x:f'{float(F(x)):.14g}'
def cells(xs):return ' | '.join(str(x)for x in xs)
text=r'''# 1. Executive Delta Table

Peer FOUR independently reconstructed the remaining lane claims from original small operands. The controlling117page Volume II edition has SHA256`391450c512bfda11682e5a58b6f3f8d27856cdc4381cd962432ae9d3e521a5f3`. H003004,H003005,H003006/H003008 are locked I1/R2 inputs; their base scripts and external N5000/N2000 archives were not rerun. Predictions and nonzero controls were written before mathematical execution in PRECOMMIT.md. Fresh host code does not import or execute earlier scientific runners. Native arithmetic, host exact enumeration, directed integration and analytical arguments retain their own provenance.

| ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict |
|---|---|---|---|---|---|
| FOUR-DP / ONE-O2 | XII.8; V; XIX |30paths/18states; rank10; minimum variation225002149/139250907; reduction7.327440840635%; work−264142984/139250907; min gross66534041/557003628; min storage124789553/61889292 | FOUR_DP_GRAM_V1 COMPLETED; FOUR_DP_BROKEN_V1 COMPLETED; FOUR_REACHABLE_CONTROL_V1 expected FAILED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Reconstructed |
| FOUR-ROLE / ONE-O2 | XII.8; XIX |Mean rolewise optimum3476627797/2228014512; information value13711843/247557168; exactly3 actions, fibers6,12,6 | FOUR_DP_GRAM_V1 COMPLETED, complete24role source orbit | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Reconstructed; apparatus unpriced |
| FOUR-REF / ONE-O4 | IV–V; XIII; XVI |176 affine-annihilating contrasts=61h1+68h2+47plaquettes; all528 frozen value contractions match; curvature8Z²h²/[A(A²−h²)] | FOUR_REFERENCE_BANK_V1 COMPLETED; FOUR_REFERENCE_BROKEN_V1 COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Reconstructed on253rows |
| FOUR-E1 / ONE-E1 | V.14–15 |Original anchor rank3; coefficients(5.3915946214…,−5.3915946214…,1.9890253020…) interpolate exactly | FOUR_ANCHOR_SOLVE_V1 COMPLETED / CERTIFIED_SOLVE | NATIVE_CERTIFIED + HOST_EXACT_RAT | Literal all-weighting impossibility rejected |
| FOUR-CHART / ONE-O5 | XI.9–10; XVI.3 |θq=p−δ/ε; p strictly decreases1→1/4, q6→0; six rational chart points | FOUR_HE3_CHART_V1, FOUR_HE3_POINTWISE_V2, FOUR_HE3_BROKEN_V1 COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Intrinsic preparation chart reconstructed |
| FOUR-GRAMMAR / ONE-O6 | I–III; XIX |120formal triples,107norms,13double fibers; (1,6,8)/(2,4,9) share sum15,norm101 | FOUR_GRAMMAR_FIBERS_V1 COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Sum+norm codec fails; norm+product injective on stated dictionary |
| FOUR-R01 | XII.7; XVII; XVIII.6–7 |||d||²=1266.24722856428927038757…; <d,ωd>=3535/4; dictionary rank2 | FOUR_WAVE_REBUILD_V1, FOUR_DICTIONARY_V1 COMPLETED / CERTIFIED_FULL_RANK | NATIVE_CERTIFIED + ANALYTICAL_PROOF | Actual full continuum receiver reconstructed |
| FOUR-R02 | XVIII.6–8 |M0=M1=0; M2²≤10864751071/40; IR norm<.054037; original band≥382.19596; sharper band>382.443; originalPe<.01315, sharperPe<.01312 | FOUR_WAVE_MOMENTS_V1, FOUR_THERMAL_METHOD_V1 COMPLETED; method executions PASSED; FOUR_WAVE_BROKEN_V1 COMPLETED | NATIVE_CERTIFIED + HOST_EXACT_RAT + ANALYTICAL_PROOF | Reconstructed and sharpened conditionally |
| FOUR-C01 | XII.7; XVIII.8 |Depth1/48 gives.005154454667189959… instead of1/192; log48/47 corrects isolated transfer | FOUR_CONTACT_TRANSFER_V1 COMPLETED (5operations, including GEN5_LOG_QUADRATIC_FORM) | NATIVE_CERTIFIED + ANALYTICAL_PROOF | Exact isolated mismatch confirmed |
| FOUR-C02 | XII.7; XVIII.8 |Var(N_T)=cT+b exactly forT≥4 in unit-radius centered held law; c∈[.18892416368715884176181444213,.18892416368715884176181444214], b∈[.06022430801813990085076003477,.06022430801813990085076003478]; VarN16∈[3.08301092701268136903979110891,3.08301092701268136903979110893] | FOUR_RICE_SCHUR_V1 COMPLETED; FOUR_RICE_BROKEN_V1 COMPLETED | NATIVE_CERTIFIED Schur algebra + HOST_DIRECTED_ARB integral + ANALYTICAL_PROOF | Prior diagnostic upgraded to directed enclosure; held law only |

The reconstructed mathematical tests suggest strong contact with their stated source concepts. The malformed source/reference/transfer and sum+norm propositions are falsified by their explicit controls below. These statements do not assign a calibrated nuclear force, physical clock, optical apparatus or endogenous count moment.

# 2. Self-Contained Derivations (Drop-In TeX Ready)

## Source identity and norms

The source norm for count paths is the complete original quadratic form, including offdiagonal terms. Field norms are normal one-photon Hilbert norms, and `<d,ωd>` is their free-energy form at I*=1. Scalar source histories are prescribed controls, with full continuum field and self/counterterm account. Euclidean matrix rank statements refer to specified finite coordinate maps, never Fock truncations. Exact rational/decimal input strings retain their frozen mathematical values. In particular anchor surface/C columns are the original stored rational feature values.

The controlling PDF was hashed directly in this window and matches the stated391450c5… edition. The raw small source operands used in the reconstruction, with SHA256, are:

'''
for p,s in manifest.items():
 if 'PRECOMMIT'not in p and 'reconstruct.py'not in p:text+=f'- `{p}`: `{s}`.\n'
for p in [Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4/volii_boundary_process1/PROOF.md'),Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4/volii_contact_formfactor1/adapter.py'),Path('/home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/sources/registered/GEN4/volii_quantum_wave1/DERIVATION.md')]:
 text+=f'- `{p}`: `{sha(p)}`.\n'
text+=r'''
The local source operator is
\[
Q=\begin{pmatrix}756&104&40&0\\104&2100&0&0\\40&0&756&40\\0&0&40&756\end{pmatrix}.
\]
It is the original H002423 input. In original pair-port coordinates z=a+4b,
\[
B_{a+4b,c+4d}=\frac{Q_{ac}Q_{bd}+\delta_{bd}Q_{ac}+\delta_{ac}Q_{bd}+\delta_{ad}\delta_{bc}}{573049},
\qquad573049=(1+Q_{00})^2.
\]
Simultaneously permute both role indices by each π∈S4 and set `Bbar=(1/24)sum Pπ^T B Pπ`. Native ordered words construct Q⊗Q, the two induced terms, exchange, all24conjugations and the complete18state Gram from these operands.

## C12 path graph, all objectives and role policy

Let s=(a,b,c,d) count H1,H2,H3,He3 templates. The initial state is(6,0,0,0), target(0,0,2,2), with the original single-cell recipe. The only actions are
\[
A:s\mapsto(a-1,b+1,c,d),\quad
B:s\mapsto(a,b-1,c+1,d),\quad
C:s\mapsto(a-2,b,c,d+1).
\]
Retain nonnegative counts, b+c≤2,d≤2. Each action increments neutron count `b+2c+d` by1, so this is an acyclic graph with six actions in every complete word. Set
\[
u(s)=(a,b,c,2d)/6,\quad v(s)_{a+4b}=u(s)_a u(s)_b,
\quad K_{st}=v(s)^T\bar Bv(t),\quad E_s=K_{ss}.
\]
The18reachable states are:
'''
text+='\n`'+', '.join('('+','.join(map(str,s))+')'for s in dp['states'])+'`.\n'
text+=r'''
The native K equals the independently constructed exact host matrix entry by entry (324checks), and native exact rank is10. The rank counts source features retained on this finite graph. It does not replace the full physical phase/wave state.

For edge s→t define
\[
q_{st}=K_{ss}+K_{tt}-2K_{st},\quad w_{st}=E_t-E_s.
\]
The Bellman recurrence `V(target)=0`, `V(s)=min_{s→t}(q_st+V(t))` is exact by backward induction on neutron count: every path has one first edge and a shorter suffix, and every minimizing edge/suffix concatenation is admitted. Independent complete path recursion gives30words and the same optimum. Signed work telescopes to E_target−E_seed for every word. Gross work is `sum max(w,0)`; ideal initial capital is `max(0,max(E_s−E_seed))`; with zero capital storage is `E_seed−min E_s`. These are distinct functionals.

| Quantity | Exact result | Decimal display |
|---|---|---|
'''
can=next(r for r in dp['paths']if r['word']=='ABABCC');rev=next(r for r in dp['paths']if r['word']=='CCABAB')
for n,x in [('Canonical ABABCC variation',can['variation']),('Reverse CCABAB variation',rev['variation']),('Minimum variation',dp['min_variation']),('Signed endpoint work',can['work']),('Minimum gross positive work',dp['min_gross']),('Minimum storage',dp['min_storage']),('Mean rolewise optimal variation',dp['rolewise_mean']),('Value of role information',dp['value_of_information'])]:text+='| '+cells([n,x,f(x)])+' |\n'
text+=r'''
The reduction is exactly `(971170543−900008596)/971170543=71161947/971170543`, or7.327440840635…%. The earlier working derivation also quoted345446941/185422932 as the literal canonical contact baseline. The original C12 row places that number in reference_energy_profiles.current, whereas its literal field is971170543/557003628. The fresh calculation and the prior complete DP JSON both agree with the latter and with the target1.74356232918. This is a prose/reference-field correction, not a changed source or numerical result.

All30mean-reference paths require zero ideal reversible initial capital. The four distinct nondominated(variation,gross,storage) tuples are:

| Representative word | Variation | Gross positive work | Storage |
|---|---|---|---|
'''
seen=set()
for i in dp['pareto_indices']:
 r=dp['paths'][i];key=tuple(r[k]for k in ['variation','gross','storage'])
 if key not in seen:text+='| '+cells([r['word'],*key])+' |\n';seen.add(key)
text+=r'''
There are eight attaining words across those four tuples. The four variation minimizers are AABCBC,AABCCB,AACBBC,AACBCB; min gross is CCABAB, and min storage is CCAABB or CCABAB.

For each of24original role assignments π, independently contract the same Q-derived Bπ and evaluate all30words. Let mπ=min_p q(p,π), and S_p={π:q(p,π)=mπ}. Exhaustive set union over all30singletons and all435pairs finds no cover of all24assignments; exactly one three-word cover exists, AABCBC,AACBCB,ACBABC. Its disjoint fibers have6,12,6assignments. Thus three actions are necessary and sufficient for exact rolewise minima; no measurement of the full permutation is required for this decision. Averaging mπ gives3476627797/2228014512, and subtracting from the optimum chosen before role information gives13711843/247557168=0.05538859210087587…. The record for this particular uniform policy has entropy H(1/4,1/2,1/4)=3log2/2≈1.039720770839918nats, independently enclosed by native FOUR_ROLE_ENTROPY_V1; no minimum-entropy claim over every alternative optimal policy is made. The numerical advantage is a quadratic source-cost advantage. Sensing, feedback, field changes, failed contacts, work-store coherence, clock and reset are not priced. No physical formation-energy saving is inferred.

## All176 matched-reference contrasts and anchor interpolation

On the literal253row roster define X_i=(1,Z_i,N_i). A signed row w with wX=0 obeys
\[
w(e+\alpha1+\beta Z+\gamma N)=we.
\]
Conversely, invariance under all three independent affine shifts implies each coefficient vanishes by varying one shift at a time. Hence the complete invariant space is the left kernel of X. Historical `(Au−m_atom)c²` and neutral atomic `(Zm_H+Nm_n−m_atom)c²` targets differ by an affine function of(Z,N) on matched masses/scales, so their contrasts agree. This does not change either raw target convention or its RMSE.

Enumerate only actual roster endpoints. At fixed Z, weights(1,−2,1) at N−h,N,N+h give61stencils for h1 and68for h2. Four corners(Z,N),(Z+2,N),(Z,N+2),(Z+2,N+2) with weights(1,−1,−1,1) give47plaquettes. Each of176rows annihilates all three columns exactly. Native multiplication also reproduces all528original frozen reference/spin/tensor contractions (1056entrycontainment checks including nuisances). Missing tensor entries were set to zero only outside the stencil support; every stencil has its three comparison columns available in the frozen source. No synthetic isotope was added.

For f_Z(N)=(N−Z)²/(N+Z), write `f=A−4Z+4Z²/A`. The first two terms are affine and cancel; therefore
\[
f_Z(N+h)-2f_Z(N)+f_Z(N-h)
=4Z^2\left(\frac1{A+h}-\frac2A+\frac1{A-h}\right)
=\frac{8Z^2h^2}{A(A^2-h^2)}.
\]
This requires positive admitted denominators and A>h. It is the curvature of the ledger shape, not the complete binding law.

The complete stencil availability is listed compactly below; each N list gives all center values for the fixed-Z second difference or all lower-left N values for the plaquette at that Z. Counts can be recovered directly by expanding these lists.

| Kind | Z | All N |
|---|---:|---|
'''
by=collections.defaultdict(list)
for c in rf['contrasts']:
 co=c['coords'][1]if c['kind'].startswith('N')else c['coords'][0];by[(c['kind'],co[0])].append(co[1])
for (kind,z),nn in sorted(by.items()):text+='| '+cells([kind,z,','.join(map(str,nn))])+' |\n'
text+=r'''
There is no unit Z/N plaquette. The13light/anchor endpoints contain no fixed-Z three-point stencil. The retained statistical mass uncertainties and shared folds are correlated inputs; absolute weighted uncertainty sums are not confidence intervals. These full-fit contrasts are descriptive and do not create a new held-chain score. For variational intervals, signed w uses lower endpoints on positive weights and upper endpoints on negative weights for its lower bound, reversing for the upper; subtracting two trial uppers is insufficient.

The actual anchor matrix and target vector are
\[
M=\begin{pmatrix}
1&1&0\\
2&24803141437/15625000000&0\\
3&520020955763/250000000000&1386722548701/1000000000000
\end{pmatrix},\qquad
b=(0,2224566269/10^9,1929510337/250000000)^T.
\]
Its determinant is−8940004137598226376663/15625000000000000000000≠0. Native certified solve encloses the exact rational solution
\[
(a,b_s,c)=\left(
\frac{278070783625}{51574868504},
-\frac{278070783625}{51574868504},
\frac{35563788859572595628875}{17880008275196452753326}
\right).
\]
Direct rational multiplication gives zero residual. Thus the literal statement “cannot carry H1,H2,He3 at any weighting” is false on the original frozen features. This interpolation says nothing about bulk/held accuracy or a physical mechanism; the observed tradeoff of the tested fits remains its own comparison.

## He3 scale-free response chart and finite grammar fibers

Use the locked full192source reduction to its actual four-pole factor; the reduction is an inherited input, not a replacement physical parent. Let r=τ/δ≥0, `a_k=(1+4kr)^−1`, k0…3, `S_j=sum a_k^j`. The normalized intrinsic factor is a/sqrt(S2), and its rank-one incidence projector is P=11^T/4. Define
\[
\theta=\tau/\epsilon=rS_1/4,\quad d=\delta/\epsilon=S_1/4,
\quad p=\langle P\rangle=S_1^2/(4S_2),
\quad q=4\sum_{k=0}^3 k a_k^2/S_2.
\]
The factor equation `(4θ diag(k)−P)a=−d a` holds coefficientwise. Also `S1−S2=4r sum k a_k²`, whence
\[
\theta q=\frac{S_1(S_1-S_2)}{4S_2}=p-d.
\]
No extra energy gain is added: this is the original formation-cost identity divided by ε. Six rational r values0,1/100,1/10,1,10,100 were checked independently. The first native check aggregates their residuals; the additional24×6block certificate FOUR_HE3_POINTWISE_V2 retains every point's residual in a separate block, all zero. Each individual exact host residual is zero as well. These factor checks do not rerun or replace the locked full192spectral theorem.

Since `(r a_k)'=a_k²`, θ'=S2/4>0. For r>0,
\[
\frac{p'}p=\frac2r\left(\frac{S_2}{S_1}-\frac{S_3}{S_2}\right)<0
\]
by strict Cauchy–Schwarz, because the positive a_k are unequal. For q, differentiate its probability weights a_k²/S2: q'/4 is the covariance of k with `−8k/(1+4kr)`, which is strictly negative. Thus θ parametrizes the curve one-to-one; p decreases1→1/4, q decreases6→0. Expansion gives `1−p=20θ²+O(θ³)` and `p−1/4=11/(192θ)+O(θ^−2)`. Inverse calibration is well conditioned only on interior compact ranges. An actual measurement must identify P/detuning and prepare this intrinsic factor or pay joint-field backreaction; no joint-ground susceptibility, absolute scale or physical τ follows from the chart alone.

For the source alphabet P={1,2,3,4,6,8,9,12}, complete unordered triples with repetition number C(10,3)=120. Enumerating their integer squared norms yields107classes; all13nonsingleton fibers contain two members. Native full Gram differences verify the13equal-norm diagonal identities. These formal candidates are not identified with the manuscript's differently selected120tested three-body rows by cardinality.

| Squared norm | First triple | Second triple |
|---:|---|---|
'''
for n,pair in sorted(gc['collision_fibers'].items(),key=lambda t:int(t[0])):text+='| '+cells([n,tuple(pair[0]),tuple(pair[1])])+' |\n'
text+=r'''
The fiber at101 has equal first moment15: (1,6,8) and(2,4,9). It directly rejects sum+norm injectivity. Norm+product yields120distinct signatures on this dictionary, but neither code determines typed identity, admission, stability or label reveal, and no universal triple reconstruction is asserted.

## Actual O16 coherent history receiver and thermal band

Start with four owned K4 cores, each original C4 address32. In each core its six digits give `(x_k,y_k)`, hence Gray signs `S_k=x_k+y_k`, `T_k=x_k−y_k`, and current `u=(sumS+sumT,sumS−sumT)/2`. All48signs and8currents are retained. At j/8,j0…96, HELD leaves them fixed; FORWARD flips0…47 twice, REVERSE flips47…0 twice. Each history begins/ends at u=(4,0)^4. There are97endpoint-inclusive frames.

The original equal-radius components are
\[
G_{\rm edge}=(2I_4+J_4)\otimes I_2,\quad
G_{\rm outer}=J_4\otimes I_2/10,\quad\tau_r=I_*=1.
\]
Native QUANTUM_WAVE_HISTORY receives all these increments and the whole shell spectrum; its returned `full_continuum=true`, `cutoff_used=false`. Only the scalar nuclear-history phase is set to zero in this classical-alternative discrimination calculation. The physical current/field work and all counterterms are unchanged. Full quantum-superposition nuclear phases remain separate required operands and are not inferred from overlap magnitudes.

For normal outgoing amplitudes fF,fR define d=fF−fR. Full number/energy Gram contractions give
\[
\|d\|^2\in[1266.24722856428927038757097294,
1266.24722856428927038757097296],\qquad
\langle d,\omega d\rangle=3535/4.
\]
The energy equality was independently reconstructed over rational numbers as `(1/2)sum_ij Δu_i^T G Δu_j (1−|t_i−t_j|/2)+=3535/4`, using all97difference events. Native interval arithmetic contains3535/4 and pays all overlap-rounding radii. Field work is26111/40and25727/40, and the complete ledger residuals contain zero. All48new contact means agree at observation16; equal means have not removed d.

For a supplied matched phase reference, let h=d/||d|| and `X_h=(a(h)+a†(h))/2`. Coherent quadrature variance is1/4 and the two means differ by||d||. The midpoint decision has `Pe=Φ(−||d||)≤(1/2)exp(−||d||²/2)`. A mode with calibrated signal power transmission η replaces squared separation by η||d||²; detector noise and physical collection are additional specified data.

Let Δu_j be the full F−R event differences. Exact8×97native multiplication yields
\[
M_0=\sum_j\Delta u_j=0,\qquad M_1=\sum_jt_j\Delta u_j=0.
\]
For `z(ω)=sum Δu_j e^{iωt_j}`, Taylor's integral remainder gives
\[
\|z(\omega)\|_G\le\frac{\omega^2}{2}\sum_jt_j^2\|\Delta u_j\|_G.
\]
Set M=sum t_j²||Δu_j||G. Cauchy–Schwarz over all original97nodes gives the exact cap
\[
M^2\le(\sum_jt_j^2)(\sum_jt_j^2\Delta u_j^TG\Delta u_j)
=10864751071/40.
\]
The original shell measure is `p_τ(ω)=2τ sinc²(τω)/π`, and its amplitude denominator is sqrt(2I*ω). Thus
\[
N_{[0,\omega_0]}\le\frac{M^2\omega_0^4}{16\pi}<0.054037
\quad(\omega_0=1/100).
\]
The squared norm, not its square root, is bounded here. Energy positivity gives `N_(1,∞)≤<d,ωd>=883.75`; hence the original conservative band≥382.19596 holds. Using the full directed number Gram strengthens this to
\[
N_{[.01,1]}>1266.24722856428927038757-883.75-.054037
>382.443.
\]
For post-collection covariance bounded as a positive operator by `C(ω)=coth(βω/2)` and calibrated η, the matched Gaussian filter is proportional to C^−1d. Its squared effective separation is
\[
Q=\eta\langle d,C^{-1}d\rangle
\ge\eta\tanh(.01\beta/2)N_{[.01,1]}.
\]
At β200,η1/40, a reusable native recipe was admitted, compiled and executed at256bits. Its two executions PASSED, using exp([[0,1],[1,0]]) and a1×1solve for tanh1, followed by native products/exponentials. The original band gives Q>7.27695523914758 and Pe<.013146171<.01315. The sharpened band gives Q>7.28165884465476 and Pe<.013115290<.01312. These are conditional receiver guarantees in the original source units; mean efficiency/noise is insufficient to establish the assumed operator inequalities. Physical temperature/frequency scales, collection, mode shaping, phase locking, apparatus energy and reset remain unassigned.

For a fixed coherent dictionary f1,…,fM, a common displacement leaves differences d_j=f_j−f1. Their normal Gram has rank r≤M−1. Choose an orthonormal basis of their span and extend its isometry to a passive one-photon unitary. The orthogonal coherent factor is then common to all hypotheses and can be discarded without losing their statistical distinction. Native B*NB and B*EB with `B=[[-1,-1],[1,0],[0,1]]` give actual HELD/FORWARD/REVERSE rank2; its determinant is enclosed strictly above1837116.41394784. Binary F/R requires one matched mode. Two modes here means two complete amplitude directions with infinite Fock spaces, not two frequencies or a finite-dimensional quantum state. Nuclear/Weyl phases must accompany any coherently controlled source superposition.

## Isolated marked crossing versus finite hazard

Freeze the actual full-field acceptance a at an isolated transverse eligible Gray crossing. In the original column convention
\[
A=\begin{pmatrix}-a&1-a\\a&-(1-a)\end{pmatrix},\qquad A^2=-A.
\]
The exponential series therefore sums exactly to
\[
e^{\lambda A}=I+(1-e^{-\lambda})A.
\]
One consumed timestamp with one uniform48label attempt has transfer `I+A/48`. Equality requires `1−exp(−λ)=1/48`, namely λ=log48/47. A shrinking window with integral|ξ'|δε(ξ)dt→1 and prefactor1/48 has depthλ1/48, giving a different transfer. Native ordinary logarithmic quadratic form and modular negative logarithm independently enclose the same calibrated positive depth0.02105340919783234224322305298… . At the reachable full-gap value a1/4 (βΔH=log3), native exponentials yield
\[
(I+A/48)_{21}=1/192=0.00520833333333333333\ldots,
\qquad(e^{A/48})_{21}=0.00515445466718995918563\ldots.
\]
Their separation exceeds0.00005387866614337. This is a local mismatch between two stated domains. It does not retract the separately constructed weak boundary process or establish a global thin-layer limit. Coupled freezing error, postjump eligibility and ordering of coincident/repeated surfaces need their actual account. A weighted crossing sumΣb_k and accepted Bernoulli count have different conditional second moments, differing byΣb_k(1−b_k) when those prescribed trials are conditionally independent; they cannot be identified from their mean alone.

## Rice diagonal and directed held crossing variance

The original low-field scalar process is a Brownian convolution with hτ(s)=s on[0,2τ],4τ−s on[2τ,4τ],zero elsewhere. At τ1 its variance kernel has denominator integral h1²=16/3. Direct piecewise integration gives integral h1(s)h1(s+h)ds=16/3−2h²+h³/2 on[0,2] and(4−h)³/6 on[2,4]. Dividing by16/3 independently reconstructs the actual normalized covariance:
\[
r(h)=\begin{cases}1-3h^2/8+3|h|^3/32,&|h|\le2,\\(4-|h|)^3/32,&2\le|h|\le4,\\0,&|h|\ge4.\end{cases}
\]
Thus the derivative is continuous with Brownian regularity, λ2=−r''(0)=3/4, and the level-zero mean crossing rate is ν=sqrt3/(2π). For r(h)=1−ah²+b|h|³+O(h⁴), conditional on X0=Xh=u, the derivative mean is `(-r'u/(1+r),r'u/(1+r))=O(h)`, and the conditional covariance is
\[
S=\begin{pmatrix}2a-r'^2/(1-r^2)&-r''-rr'^2/(1-r^2)\\-r''-rr'^2/(1-r^2)&2a-r'^2/(1-r^2)\end{pmatrix}
=2bh\begin{pmatrix}2&-1\\-1&2\end{pmatrix}+O(h^2).
\]
Exact native Schur contractions at six nonzero rational lags verify the full covariance divided by h, including every inverse/cross term. Its limiting correlation is−1/2. For centered normal velocities with variance s and correlationρ,
\[
E|V_1V_2|=\frac{2s}{\pi}(\sqrt{1-\rho^2}+\rho\arcsin\rho).
\]
Since the joint position density at(u,u) is asymptotic to `exp(−u²/2)/(2πsqrt(2a)h)`, the Rice pair density has finite nonzero diagonal
\[
R_u(0+)=\frac{b}{2\pi\sqrt{2a}}
\left(\frac{4\sqrt3}{\pi}+\frac23\right)e^{-u^2/2}
=\left(\frac3{8\pi^2}+\frac{\sqrt3}{48\pi}\right)\frac{e^{-u^2/2}}{\tau^2}.
\]
The moving-triangle representation gives a C1 modification, with derivative a finite Brownian-increment combination. Its one-time Gaussian density is uniformly bounded. To exclude a level tangency, restrict to sample paths whose derivative modulus on mesh h is at most ε. A tangent zero forces a mesh value into an interval of width2εh about u; the union bound over O(T/h)grid points costs at most a constant times Tε. Uniform continuity makes the restriction hold eventually, and ε→0 excludes tangencies. Consequently zeros are isolated and finite on each compact interval. For pairs separated by a fixed δ>0, coarea and the nondegenerate joint Gaussian position law give the two-time Rice integral. Let δ decrease to zero: the pair counts increase monotonically to N_T(N_T−1), while the explicitly finite diagonal limit bounds the integral. This establishes a finite held second moment. A finite set of nonparallel source directions uses its actual joint covariance; distinct levels in one coordinate have exponentially suppressed small-lag joint density. No squared surface delta or Poisson assumption is used.

For u0, pair density R(h)=ν² for h≥4 exactly, so the stationary factorial-moment identity gives, for T≥4,
\[
\operatorname{Var}N_T=T\nu+2\int_0^4(T-h)[R(h)-\nu^2]dh=cT+b_0,
\quad c=\nu+2J,\quad b_0=-2K,
\]
where `J=∫_0^4(R−ν²)`, `K=∫_0^4 h(R−ν²)`. The affine relation is exact in this held law, not merely a large-T fit.

To avoid catastrophic cancellation, on0≤h≤2 factor `1−r²=h²D`, `Sdiag=hs`, `Soff=hc`, with
\[
D=-3(h-4)(3h^3-12h^2+64)/1024,
\]
\[
s=\frac{3(3h^3-24h^2+84h-128)}{4(h-4)(3h^3-12h^2+64)},\quad
c_h=\frac{3(9h^4-84h^3+288h^2-480h+512)}{32(h-4)(3h^3-12h^2+64)}.
\]
Then `R(h)=s[√(1−ρ²)+ρasinρ]/(π²√D)`, ρ=c_h/s, is nonsingular at zero. On2…4 use the exact cubic-tail covariance and its derivatives. Fresh192bit Acb integration splits0,1,2,3,4, checks the analytic square-root branches, and checks the real enclosure ofρ lies strictly inside(−1,1) whenever analytic evaluation is requested. Every integral includes its directed error; no infinite-tail approximation is present because the pair excess vanishes past4. The resulting outward decimal enclosures are:
\[
c\in[0.18892416368715884176181444213,
0.18892416368715884176181444214],
\]
\[
b_0\in[0.06022430801813990085076003477,
0.06022430801813990085076003478],
\]
\[
\operatorname{Var}N_{16}\in[3.08301092701268136903979110891,
3.08301092701268136903979110893].
\]
Exact rational endpoint balls (widths below1e−50) are retained in RICE_ARB.json. Radius scaling gives `VarN_T=c T/τ+b0` forT≥4τ at u0. This supplies no physical-seconds map.

The endogenous/Palm count remains a separate question. The retained L2density estimate alone would require `E_Q Z_T^4<∞` to conclude `E_P N_T²≤(E_Q density²)^(1/2)(E_Q Z_T^4)^(1/2)`. A held second moment and almost-sure nonexplosion do not supply this fourth moment. That exact missing input is preserved; no broader process theorem is claimed here.

# 3. Controls, Obstructions & Superseded Attempts

| Control | Precommitted failed check | Observed exact witness / native return |
|---|---|---|
| Diagonal-only C12 B |Canonical full source variation reproduction |Bad−full variation5454347/557003628≠0. FOUR_DP_BROKEN_V1 completes with nonzero action Gram; FOUR_REACHABLE_CONTROL_V1 deliberately requires rank0 and returns FAILED as predicted. It is a mathematical control, not an implementation failure. |
| Wrong reference center weight−1 |Affine nuisance annihilation |First actual stencil O16/O17/O18 returns(1,8,9) against(1,Z,N); native FOUR_REFERENCE_BROKEN_V1. Correct stencil curvature16/153 and reference contrast390229/100000. |
| Sum+norm triple signature |Injective source codec |Native norms agree101; exact sums15 for(1,6,8)/(2,4,9), while products48/72 differ. |
| He3 q replaced by0 at r1 |Formation identity |Native FOUR_HE3_BROKEN_V1 returns exact−5727442/52966485 and rank1, matching the independently calculated normalized quadratic residual. This is not a symmetry null. |
| Omit one actual F−R event |Zeroth Fourier cancellation |Removed event j1; native FOUR_WAVE_BROKEN_V1 has a nonzero M0 vector. Full event moments were not altered to restore cancellation. |
| Hazard depth1/48 |Marked isolated transfer equality |Native(2,1)entry.00515445466718995918563… excludes1/192; correctedlog48/47contains1/192. |
| Delete actual covariance cubic term |Actual Schur covariance / Rice diagonal |At h1/64 malformed local r=1−3h²/8 yields native S/h=[[-144,144],[144,−144]]/65533. The negative diagonal is an explicit invalid local replacement, not an admitted alternative global Gaussian law. It cannot supply the actual positive Rice limit. |

The first directed Rice runner stopped before emitting an integral because python-flint0.8.0 `acb.asin` has no `analytic` keyword. `rice_arb_failed_v1.py` and the failure explanation are retained. The successor checks the asin branch domain explicitly and forwards the analytic flag to sqrt; unchanged formulas/tolerances then complete. A diagnostic readback initially encountered a compact large-return pointer; its successor reads and hashes the underlying5,137,595byte reference receipt. A final source/IR readback initially used system Python, which lacks flint; the pinned .venv successor checks the unchanged source recipe, both literal baselines, endpoint work and directed IR upper. No native mathematical task was repeated or superseded for those readback corrections.

The canonical-account wording in the earlier source-path derivation copied the current-profile number into the literal-profile sentence. The actual original row and complete old DP JSON use the correct literal value, also independently reconstructed here. Both reference fields remain preserved. No prior manuscript or frozen artifact was edited.

# 4. Exceptions-Only Custody Diff

'''
complete=sum(v['status']=='COMPLETED'for v in ni.values());failed=sum(v['status']=='FAILED'for v in ni.values())
text+=f'{complete} completed native submissions; {failed} deliberate expected FAILED control. No unexpected native task failure, superseded native key, MISSING_RECEIPT or unadmitted task. V2 is an additional pointwise chart certificate; its completed V1 remains valid and retained. Programs include the five-operation contact comparison, five-operation dictionary contraction, and method ADMIT/COMPILE/EXECUTE with two successful six-operation executions. Host enumerations and the directed Rice integral are not relabelled native. All returned values, not admission acknowledgements, were read. All{nc["checks"]}readback checks passed.\n\n'
text+='| Native key | Status | Receipt SHA256 |\n|---|---|---|\n'
for k,v in ni.items():text+='| '+cells([k,v['status'],v['receipt_sha256']])+' |\n'
text+='\nLocal custody hashes (supporting artifacts are retained in the peer folder; their scientific content is summarized above because only REPORT.md is handed back):\n\n'
for p in [H/'PRECOMMIT.md',H/'reconstruct.py',H/'followups.py',H/'rice_arb.py',H/'rice_arb_failed_v1.py',H/'thermal_method.py',H/'final_checks.py',O/'C12_DP.json',O/'REFERENCES.json',O/'GRAMMAR_CHART.json',O/'WAVE_RAW.json',O/'RICE_ARB.json',O/'TRIANGLE_ENERGY_EXACT.json',O/'FINAL_SOURCE_CHECKS.json',O/'NATIVE_CHECKS.json',O/'NATIVE_INDEX.json']:
 text+=f'- `{p.name}`: `{sha(p)}`.\n'
text+='\nNo external publication, base-script replay, bulk archive download, physical unit fit, cross-peer edit or engine change was made. The remaining physical/calibration and endogenous-moment gaps are stated at their owning equations above.\n'
(H/'REPORT.md').write_text(text)
print('Wrote REPORT.md',len(text),'characters')
