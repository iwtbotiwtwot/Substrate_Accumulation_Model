from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
R=Path(__file__).resolve().parents[1];D=json.loads((R/'gen/PANEL.json').read_text())
NR=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/native_returns')
keys=sorted(p.stem for p in NR.glob('TWO_*.json'))
receipts=[]
for k in keys:
 x=json.loads((NR/(k+'.json')).read_text());assert x['status']=='COMPLETED'
 p=Path(x['receipt']);h=hashlib.sha256(p.read_bytes()).hexdigest();assert h==x['receipt_sha256']
 v=x['returned'];val=v.get('matrix',v.get('result',{}).get('output',{}))
 if k=='TWO_ROTOR_RESOLVENT_V1':
  out=v['result']['output'];ent=out['matrix']['entries'];expect=[Q(9,10)if i in[0,4,8]else Q(0)for i in range(9)]+[Q(0),Q(0),Q(3,20),Q(0),Q(0),Q(-1,5)]
  for row,e in zip(ent,expect):
   z=row[0];assert Q(z['re']['lower'])<=e<=Q(z['re']['upper']) and Q(z['im']['lower'])==Q(z['im']['upper'])==0
  val='15/15 exact rational solution components enclosed; gaps4,2,2'
 receipts.append({'key':k,'status':x['status'],'receipt_sha256':h,'record_sha256':v.get('record_sha256',v.get('result_ref')),'value':val,'receipt_path':str(p)})
(R/'gen/NATIVE_ALL_READBACK.json').write_text(json.dumps(receipts,indent=2)+'\n')
root=Path('/home/lilhelper/SAM_Research_Overflow')
src={
 'Volume II controlling PDF':R.parent.parent/'reading/02_SAM_Volume_II_Revised_Edition_20261110.pdf',
 'H003004 complete q/I operand':Path(D['source_path']),
 'Original geometry derivation':root/'SAM_Research_Project/GEN4/volii_lapse_field1/DERIVATION.md',
 'Original geometry adapter (read only)':root/'SAM_Research_Project/GEN4/volii_lapse_field1/native_route/adapter.py',
 'Original geometry completion manifest':root/'SAM_Research_Project/GEN4/volii_lapse_field1/MANIFEST.json',
 'Original molecular direction/energy law':root/'SAM_Research_Project/GEN4/volii_molecular_source1/DERIVATION.md',
 'Full signed molecular C1 proof':root/'SAM_Research_Project/GEN4/volii_moving_reference1/PROOF.md',
 'Original FOUR-M01 submission/scope':root/'ironclad/campaigns/volii_improvement_review_20261111/peers/FOUR/gen/MOLECULAR_TAIL_WORKING_UPDATED.md',
 'New predictions':R/'PRECOMMIT.md','New panel implementation':R/'gen/panel.py',
}
manifest={name:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for name,p in src.items()}
(R/'gen/SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')
def short(k):return k.replace('TWO_','')
def iv(b,digits=9):
 scale=10**digits;l=Q(b['lower']);u=Q(b['upper']);li=l.numerator*scale//l.denominator;ui=-((-u.numerator*scale)//u.denominator)
 def fmt(v):
  neg='-'if v<0 else'';v=abs(v);return f'{neg}{v//scale}.{v%scale:0{digits}d}'
 return '['+fmt(li)+','+fmt(ui)+']'
text=r'''# 1. Executive Delta Table

| ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict |
|---|---|---|---|---|---|
| TWO-G01 | XV.1; A05 continuation | \(E_{e,N}\ge-[C\sqrt{w_{N,\nu}}+A\nu\sqrt N/(\nu+1)]^2/(4\tau\nu^3)\). Complete geometric spectrum, spin2 and full form domain retained. | TWO_GEO_WEIGHT_V1, TWO_GEO_MID_WEIGHT_V1, TWO_GEO_PROFILE_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED finite identities | Held |
| TWO-G02 | XV.1,132 populated accounts | All132 pointwise maxima evaluated over every original q class. Exact-weight refinement changes **0/132** final lowers relative to the already valid directional/geometric/core maximum. Against the original geometric/core lower,17 flat accounts improve;88 nonflat accounts are exactly unchanged. | TWO_GEO_FLOOR_DOMINANCE_V1: COMPLETED; full numerical panel HOST_DIRECTED_ARB | ANALYTICAL_PROOF + HOST_DIRECTED_ARB | Held |
| TWO-G03 | XV.1,ionization | Published explicit spherical-shell portfolio gives **30/132** positive ionization lowers and102 overlaps after the upgrade. No additional opening on this fully reconstructed portfolio. Historical flat CI upper-endpoint file is absent: its exact upgraded count is bounded30–40, with10 named candidates unresolved; do not mistake the spherical count for a full retained-CI recount. | Geometric identities above; panel is host-directed | HOST_DIRECTED_ARB; original30/132 is inherited | Partial: precise source-operand gap |
| TWO-M01 | XIV.5; XV.5–7 | \(|v_C|\ge6,|v_O|\ge8\), independent of orbital approximation. Neutral rigid singlets have zero first-order C1 mean. Exact second-order C1 coefficient is the requested \(-1/(600D^2)\) expression. Carbon monopole gives\(-27/(25D^2)\). | TWO_ROTOR_CARBON_V1, TWO_ROTOR_GENERAL_V1, TWO_ROTOR_RESOLVENT_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | Held in the explicitly added rigid-rotor model |
| TWO-M02 | XV.5 subleading terms | Full clamped rigid energy coefficient is \(K_2-S_2\), with explicit own-core and internal-pair Haar mean \(K_2\) below. Original cross-center C2 means vanish. Pair C2 can have either sign; C1 attraction alone does not fix the full D^-2 coefficient. | TWO_TAYLOR_PAIR_V1, TWO_TAYLOR_OWN_V1, TWO_TAYLOR_SIGN_CONTROL_V1: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | New continuation |
| TWO-M04 | XV.5,full C2 comparison | \( |K_2|\le\sum_a[g_p|U_a|+v_p(n_a-1)]\mathcal R_a/3\). Equal-B sufficient full-tail attraction: C444 B<81/(85R), oxygen B<256/(115R), R=sum of radii per atom. | TWO_TAYLOR_PAIR_V1 and TWO_TAYLOR_OWN_V1 anchor the coefficient formula; uniform bound analytical | ANALYTICAL_PROOF | New sufficient full-C2 continuation |
| TWO-M03 | XV.5–7,thermal orientation | Classical independent-Haar C1 free energy is \(-\beta[|v_A|^2|v_B|^2+|t_A|^2+|t_B|^2]/(600D^2)\). Full model adds\(K_2/D^2\). | TWO_ROTOR_THERMAL_V3: COMPLETED | ANALYTICAL_PROOF + NATIVE_CERTIFIED | Held |
| TWO-K01 | XV.1 / XV.6 controls | False flat centrifugal term: residual6; wrong pair rotor gap: coefficient error−27/25; nonneutral singlet:first mean1; pair C2 sign witnesses714/625 and−1. | GEO_CONTROL_V3, ROTOR_CONTROL_V3, NEUTRALITY_CONTROL_V3, TAYLOR_SIGN_CONTROL_V1 (all prefixed TWO_): COMPLETED | NATIVE_CERTIFIED + ANALYTICAL_PROOF | All intended mathematical hypotheses break |

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

Put\(d_c(r)=\max(r,r_c)\). For\(0<\theta<1\), split the **same** full kinetic form into θ and1−θ. The exact geometric scalar occupation theorem gives
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

**Complete source minimization and the remaining upper-endpoint custody.** The locked q/I table includes all10 helium q classes and all51 carbon q classes (49/361 physical receiver sectors). For each account retain
\[
 S(q)=Z^2/2+g_pq/2,\quad
 G=\min_q[I(q)+S(q)],\quad
 L_N=\min_q\{I(q)+S(q)+\max(B_{\rm new},B_{\rm old},B_{\rm core})\}.
\]
The complete source table was read as an operand, without replaying its enumeration. Minima were interval-enclosed over every original row at512-bit Arb precision. The 17 changes against the original geometric/core lower all occur at ν=1: both populated inventories of the four helium coupling/cover cohorts, and N4,5,6 in the three weak-carbon cohorts. Strong-carbon and all88 nonflat populated accounts are unchanged.

For a fully specified available upper portfolio, the published shell formula was independently evaluated, without executing the old native adapter. Let\(\alpha=\alpha_1\),\(J_1=30(4\log2-11/4)\),\(M_\alpha=\sum_{i<j}(2R_i)^\alpha\). The disjoint normalized spherical trial with radial\(s(1-s)\) on[R,2R] obeys
\[
 \Delta U_j\le10\nu^3/R^2-(Z-j+1)J_1/R+
 \frac{g_pM_\alpha}{(2\alpha+1)R^{\alpha+1}}.
\]
Start R=2, double until this upper is negative, then multiply R by4 before the next shell. This is the original explicit formula and radius rule, freshly evaluated with outward intervals. It keeps all electrons, the same nuclear phase/reference, and the geometric Green pair bound. Define\(U_N^{\rm shell}=G+\sum_{j\le N}\Delta U_j\). The ionization interval is
\[
 [L_{N-1}-U_N^{\rm shell},\ U_{N-1}^{\rm shell}-L_N].
\]
All132 lower/upper comparisons are valid,30 lower endpoints are positive (N1 in each of30 cohorts), and102 intervals contain zero. This is a complete **spherical-portfolio** calculation.

The historical geometry file additionally retained better H002309 CI/outer-shell uppers at ν=1. Neither its714456-byte RESULTS.json (expected SHA2564b0731f60efbc7b0122d9fd0bb68c5a6ff24e185d97b324c9f801f0965fe6059) nor the374830-byte flat predecessor (SHA256dc316d8bc657fbe400d069e7cb6d523c639c3bc0080bec0c0830d01e16a30b37) exists at the recorded local source paths. Their scripts, manifests and summaries exist. A reference hash is not an endpoint operand. We do not assign reconstructed shell uppers to that missing CI portfolio. Since only10 previous-inventory lowers that can affect a nonempty ionization account change, the original retained portfolio's upgraded count is in[30,40]; the only candidates beyond30 are He4_3/He4_4 N2 at both couplings, and C333/C343/C444 N5,N6 at g_p1/10. Restoring those ten upper endpoints is sufficient to settle it. The exact-weight change itself adds no further opening to any fixed portfolio beyond the already valid three-way bound.

**Rigid-rotor C1 response.** Fix neutral rigid atomic preparations and rotate all of their body-frame moments together. On\(L^2(SO(3)\times SO(3),dR_AdR_B)\) with normalized Haar measure, add\(H_0=B_A L_A^2+B_B L_B^2\), B_A,B_B>0. Let\(\Omega=1\otimes1\) be the normalized product singlet. For the original coefficient
\[
 C_1=\frac1{10}[(R_Av_A)\cdot(R_Bv_B)+e\cdot(R_At_A-R_Bt_B)],
\]
Haar invariance gives\(\langle R a\rangle=0\),\(\langle(Ra)_i(Rb)_j\rangle=\delta_{ij}(a\cdot b)/3\). Consequently\(\langle C_1\rangle=0\). The three summands send Ω into mutually orthogonal left-angular-momentum sectors(1,1),(1,0),(0,1). Their squared norms are respectively
\[
 \frac{|v_A|^2|v_B|^2}{300},\quad\frac{|t_A|^2}{300},\quad\frac{|t_B|^2}{300},
\]
with exact energy gaps2(B_A+B_B),2B_A,2B_B. Arbitrary body components and v/t nonorthogonality stay inside these sectors; integrating the other rotor makes the cross terms zero. Thus
\[
 -\frac1{D^2}\langle C_1\Omega,QH_0^{-1}QC_1\Omega\rangle
 =-\frac1{600D^2}\left[
 \frac{|v_A|^2|v_B|^2}{B_A+B_B}+\frac{|t_A|^2}{B_A}+\frac{|t_B|^2}{B_B}\right].
\]
This uses the complete image of Ω for second order; there is no angular-cutoff approximation to the full rotor. Bounded C1 and the positive rotor gap justify analytic perturbation for sufficiently large D at fixed B_A,B_B. The native15-coordinate witness uses the raw Cartesian Haar Gram diag(1/9 repeated9,1/3 repeated6); its gap operator is diag(4 repeated9,2 repeated6). For vA=vB6,tA3,tB4 it returns−673/600. With only the monopole, three pair entries are18/5 in the raw basis (6/5 in normalized Cartesian coordinates), squared norm108/25 and gap4, giving−27/25. The independent certified complex solve encloses every15 exact resolvent component.

For any normalized correlated n-electron preparation,\(\mu=\sum_i\langle n_i\rangle\) satisfies\(|\mu|\le n\), since every n_i is a unit multiplication vector. Therefore\(|v|=|U-\mu|\ge|U|-n\). In the specified C444 sector |U|12,n6 this is6; in oxygen |U|16,n8 it is8. This argument uses no orbital approximation. At equal B=1 the oxygen monopole component is at most−256/(75D²), while carbon is at most−27/(25D²). These refer to the C1 component of the changed rotor model, not the full molecular coefficient.

The classical independent-Haar partition of C1 alone gives
\[
 -\beta^{-1}\log\langle e^{-\beta C_1/D}\rangle
 =-\frac{\beta}{600D^2}(|v_A|^2|v_B|^2+|t_A|^2+|t_B|^2)+O(D^{-3}).
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
 \frac{|v_A|^2|v_B|^2}{B_A+B_B}+\frac{|t_A|^2}{B_A}+\frac{|t_B|^2}{B_B}\right].
\]
The classical coefficient is\(K_2-\beta(|v_A|^2|v_B|^2+|t_A|^2+|t_B|^2)/600\). The own-core C2 need not vanish: r2,dc2,U=(12,0,0),n=(3/5,4/5,0),gp1/10 gives native+12/25. The pair numerator is native714/625 at r2,s3,n=(3/5,4/5,0),m=(0,3/5,4/5). For parallel directions and radii2,3 it is−1. Narrow finite-energy packets around these separated configurations preserve either sign, so these are reachable controls, not null geometries. Consequently neither scalar neutrality nor vanishing vector mean alone fixes the full D^-2 coefficient or recovers a D^-6 tail.

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
 |K_2|\le\frac13\sum_{a=A,B}[g_p|U_a|+v_p(n_a-1)]\mathcal R_a.
\]
The own-core estimate uses r²/max(r,rc)≤r. This also establishes the needed integrability with only finite first radial moments and removes an apparent pair-coincidence singularity.

For identical C444 neutral preparations, g_p=v_p1/10 and equal scalar radial sums \(\mathcal R_A=\mathcal R_B=R\), this gives |K2|≤17R/15, whereas S2≥27/(25B) at equal B. Hence
\[
 0<B<81/(85R)
\]
is sufficient for a negative **full** clamped D^-2 coefficient, including the original Taylor terms. If R=6 times the mean electron radius, this is B<27/(170 mean_radius). For identical oxygen preparations the corresponding sufficient condition is B<256/(115R), or B<32/(115 mean_radius) when R=8 mean_radius. These are source-unit sufficient conditions at fixed B followed by large D, not calibrated molecular predictions. They do not require t to vanish; t only increases S2.

One useful conditional continuation follows: at equal B, let\(A_2=|v_A|^2|v_B|^2/2+|t_A|^2+|t_B|^2>0\). If the finite K2 is positive, B<A2/(600K2) is sufficient for negative full coefficient; if K2≤0 every B>0 qualifies. This concerns sufficiently large D at each fixed B, not a uniform interchange of B→0 and D→∞. Actual body-frame moments and a calibrated rotational action are still needed to assign the carbon/oxygen full coefficient.

**Source hashes and norms.** Normalized physical electronic states use the original geometric L² measure; Haar measure has total mass1; L² eigenvalues are l(l+1). The finite Cartesian witness Gram is stated explicitly above. Exact source files and SHA256 identities are:

| Source | SHA256 |
|---|---|
'''
for name,z in manifest.items():text+=f'| {name} | `{z["sha256"]}` |\n'
text+='\n**All132 account endpoints.** Each interval below is rounded outward from the512-bit rational endpoint box to9 decimal places. G is the exact separated source+core minimum. L is the upgraded complete lower; U_s is the freshly evaluated spherical upper; I_s is its ionization lower endpoint enclosure. These are not substituted for the missing historical flat CI uppers.\n\n| ν | Source | gp | N | G | L | U_s | I_s |\n|---|---|---|---:|---|---|---|---|\n'
for r in D['rows']:text+=f"| {r['nu']} | {r['source']} | {r['g']} | {r['N']} | {r['separated']} | {iv(r['upgraded_joint_lower'])} | {iv(r['spherical_upper'])} | {iv(r['fresh_spherical_ionization_lower'])} |\n"
text+=r'''
# 3. Controls, Obstructions & Superseded Attempts

PRECOMMIT.md was written before any scientific script or native task, and the Taylor extension was added before its contractions. All mathematical breaking controls are reachable: l1 is a legal nonzero angular channel; the carbon pair image has nonzero norm108/25; charges+1,+1 are an explicitly changed allocation; separated electron radii2,3 and open neighborhoods give nonzero pair terms.

- **Geometry:** falsely taking α1=1 at ν1/2 misses the centrifugal coefficient by8−2=6. The control receipt returns6. Exact selected s-state weights cannot detect this alone, so the nonzero l1 control is retained separately.
- **Rotor gap:** replacing the pair gap4 by the single-rotor gap2 changes−27/25 to−54/25. The native wrong-minus-true witness is−27/25.
- **Neutrality:** dropping neutral allocation gives the scalar first mean1 for charges+1,+1. Haar averaging does not eliminate a scalar charge product.
- **Original C2:** dropping own-core response misses+12/25 in the stated physical witness. Dropping the a_i·a_j term misses\(r_ir_j(1+c_{ij}^2)/3\). The positive714/625 and negative−1 pair numerators refute a universal sign shortcut. The full-tail conclusion retains K2 rather than replacing it by zero.
- **Caller-contract corrections:** three V1 control submissions were rejected because `expected_reason` is permitted only with expected FAILED/REFUSED, while these controls expect COMPLETED nonzero witnesses. Three V2 attempts were rejected because `supersedes` cannot name an unadmitted task; the thermal V2 attempt was rejected because `supersedes` cannot name a completed task. Corrected V3 submissions use expected_status COMPLETED without those invalid fields. These are7 unadmitted requests, with submitted JSONs retained, not mathematical failures.
- **Thermal operand correction:** TWO_ROTOR_THERMAL_V1 completed an incorrect precomputed variance input673/150, yielding−673/300. It is scientifically superseded by the full-image contraction TWO_ROTOR_THERMAL_V3, which returns−1321/600. The exact correction is+1/24. Quantum rotor receipts and the general thermal formula are unchanged. No completed erroneous operand is erased or counted as independent evidence.
- **Host failures:** panel attempt001 had the Python typo `else6`; attempt002 compared Arb directly with Fraction. Their scripts are retained. A rational endpoint audit then exposed extra outward rounding when subtracting Arb objects versus separately rounded endpoint boxes. The final runner constructs ionization endpoint differences directly over exact rationals from the displayed lower/upper boxes; the original Arb version and failed audit remain. All132 interval-containment/count checks pass without changing the source or count criterion. The corrected runner uses Arb source evaluation and exact rational endpoint differences for the same full132-account specification. No acceptance criterion, source table, or baseline upper was changed to obtain a count.
- **Physical/model boundary:** the geometry lower assumes the original quadratic kinetic and constant ν; it does not transfer to the smaller massive square-root kinetic or variable lapse. Rotor BA,BB and thermal β are explicitly added/supplied. The full C2 moments, internal excitations, moving-fragment reference, recoil, physical vertex/unit calibration and apparatus resources remain named inputs rather than being supplied by C1 averaging.

# 4. Exceptions-Only Custody Diff

'''
text+=f'Native completed tasks:{len(receipts)}; scientifically current completed tasks:{len(receipts)-1}; completed caller-operand superseded tasks:1 (TWO_ROTOR_THERMAL_V1). All completed receipt files were read, their SHA256 verified, exact source-word outputs checked and all15 resolvent components checked by rational containment. No admitted native task is missing its return. Unadmitted requests:7 as listed above. Every matrix has at most15 rows/columns; no large-matrix rank/solve was submitted.\n\n'
text+='**Source operand exception:** original geometry RESULTS.json and flat H002309 RESULTS.json are absent locally at their documented paths and were not recovered in the bounded local searches. Their expected byte counts/hashes are stated in section2. This prevents the original retained-CI ionization recount; it does not prevent the full132 lower table, the zero incremental exact-weight theorem, or the complete spherical-portfolio30/132 calculation. There is no `MISSING_RECEIPT` among this run\'s admitted native tasks.\n\n'
text+='Only this peer folder was written. Locked H003004–H003008 scripts, large N5000/N2000 archives and completed Volume III TWO-F03 were not replayed. Sources and new host scripts are hash-bound above; native task JSONs and readbacks remain under tasks/ and gen/. Peak workload was one bounded host process with OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and ctx.threads=1. No manuscript, engine, external app, Git history or other peer folder was modified.\n\n'
text+='| Native key | Status | Receipt SHA256 |\n|---|---|---|\n'
for e in receipts:text+=f"| {e['key']} | COMPLETED{'; superseded operand' if e['key']=='TWO_ROTOR_THERMAL_V1' else ''} | `{e['receipt_sha256']}` |\n"
text+='\nThe bounded frustrated-spin transfer review uses the prescribed locked spin material: preserve the full physical metric, mixed terms and uncertainty links; no new numerical atomic or rotor operand follows from those spin summaries. No additional relevant undisclosed result was identified. NEGATIVE DRIFT CHECK — COMPLETION: CLEAR.\n'
import re
text=re.sub(r'\b(All|all|and|with|its|the|at|of|from|over|plus|in|gives|input|residual|norm|gap|coefficient|count)(?=[0-9])',r'\1 ',text)
text=text.replace('ν=1the','ν=1 the').replace('at512','at 512').replace('B_A,B_B>0','B_A,B_B>0')
for v in ['v_A','v_B','t_A','t_B','v_C','v_O','K_2','U_a']:
 text=text.replace('|'+v+'|',r'\lvert '+v+r'\rvert')
(R/'REPORT.md').write_text(text)
print('REPORT written',len(text),'characters;',len(receipts),'completed native receipts')
