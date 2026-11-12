# Peer TWO — reading-stage notes

Reading stage only. No target calculations, native submissions, or REPORT.md have been started.

## Assigned lane and working constraints

- Lane 2: exact geometric occupation weights and sharpened constant-lapse Pauli lower bound; 132 helium/carbon geometry accounts; rigid-rotor second-order molecular tail and competing Taylor terms.
- Locked inputs: 01_atoms H003004, 02_spin_memory H003005, 03/03r H003006/H003008. Do not rerun their baseline scripts. Do not fetch external large joint-density archives.
- Future work window: 1500 s; no large/multistep native submissions in final 180 s; use both native engine and pinned host environment, distinguish custody classes; precommit predictions and reachable nonsymmetry-null breaking controls.
- Only peer TWO directory is writable under the user contract. Other peers and supplied reading files are read-only.
- Ancestor AGENTS.md read: project manuscript authorship/provenance conventions, native-first calculations, concise negative-drift beginning/completion checks. Declaration read. Referenced SAM_LIVE/00_CURRENT.md and CURRENT_REVISION/README.md are absent at the ancestor root; user supplies a specific self-contained run briefing and reading bundle. No expansion into unrelated authority discovery is needed for this reading stage.

## Volume I — 01_SAM_Volume_I_FirstEdition_DRAFT_20261111.pdf

Text source: `../../reading/text/01_SAM_Volume_I_FirstEdition_DRAFT_20261111.pdf.txt` (PDF-page markers, 284 pages). Read the contents/edition guide, searched lane terminology throughout, and read the following relevant passages.

- **Ch. I §4, PDF p.5, eqs. (5)–(8):** source-only clock lapse `N(a)=sqrt(1-a)`, radial ruler `dr/sqrt(1-a)`, spherical metric `-(1-a)c²dt² + dr²/(1-a)+r²dΩ²`. Ruler declaration is an additional physical assignment. Constant-lapse spatial geometry in the target should retain this distinction.
- **Ch. I §§5–9, PDF pp.5–7:** metric agreement and the separate clock/route readings; avoid conflating source lift, floor, clock lapse, spatial metric, and optical length.
- **Ch. II §§1–3, PDF pp.12–13:** energy-to-spatial-field join needs localization, coupling, receiver, units, common reference; source-only lift and floor have separate meanings. Declared Poisson equation `Δa=-8πGρ/c²` and kernel `a(x)=(2G/c²)∫ρ(y)/|x-y|dy`.
- **Ch. II §§4–10, PDF pp.14–15:** finite source regularity; multipoles require shape, total mass fixes only monopole; full-field on-shell energy includes exterior and cross terms. Domain `D^{1,2}(R³)` with source in `L^{6/5}`. Disjoint spherical sources have cross energy `-GM₁M₂/d`; general compact shapes require actual differentiated kernel.
- **Ch. II §§11–12, PDF pp.15–16:** source-only lapse versus normalized raw-floor square root; nonlinear receiver and radial-coordinate convention matter. Endpoint lapse plus Poisson profile does not determine spatial response `γ`. A sharpened bound on a declared metric is conditional on that metric, while exact mathematical consequences remain valid.
- **Ch. II §§32–36, PDF pp.24–25:** complete energy includes field/source/interaction/counterterm; one uniform lapse multiplies full Hamiltonian on same domain; nonuniform lapse needs energy localization, support, boundary/reference, and form domain. Improvement term can change a nonuniform response while leaving integrated Hamiltonian fixed.
- **Ch. II §§39–42, PDF pp.26–27:** restored actual orbital `l=m=3`, index 6, `t=1`, coefficient 1; two-spin density `s⁶e^{-2s}(1-u²)³/(72πd³)` with integral 2; even Legendre modes L=0,2,4,6; noncompact exponential tail and derivative bounds. Orbital approximation and source polarization must remain distinct.
- **Ch. II §43, PDF pp.27–28, eqs.(8)–(11):** source-metric whitening `G=LL*`, `C=L^{-1}DL^{-*}`, Schur resolvent `r=b*(H_c+rI)^{-1}b`, `η/(1+s)≤r≤η`; curvature displacement estimate. Case 08 gives converter-radius convexity with fixed nuclear geometry; electron dilation and complete kinetic minimization are separate. Case 09 has a prepared bond well whose Gaussian carrier minimum need not minimize total interacting energy.
- **Ch. II §44, PDF p.29:** static distribution, energetic account, and time law are distinct source/receiver inputs; microscopic-memory values are retained results, not to rerun.
- **Ch. III §§34–40, PDF pp.50–51 (especially §40):** general static metric `ds²=-N²c²dt²+h_ij dx^i dx^j`; optical metric `h/N²`. Clock lapse alone cannot supply spatial metric. Relevant to the meaning of `ν` in the target.
- **Appendix A, PDF pp.276–279:** completed conditional mathematics is retained with preparation, domain, calibration, apparatus, and physical coupling stated separately. Relevant atomic/bond joins: actual common Hamiltonian, physical ruler, complete energy normalization, and moving-source/COM law.

Volume I has no dedicated rigid-rotor molecular derivation or exact `w_{N,ν}` account panel; those are expected in Volume II and the campaign data.

## Volume II — 02_SAM_Volume_II_Revised_Edition_20261110.pdf

Text source: `../../reading/text/02_SAM_Volume_II_Revised_Edition_20261110.pdf.txt` (117 PDF pages). Read edition scope/contents, XIII pp.73–75, XIV pp.76–79, XV pp.80–83, XVI pp.84–88, and source register pp.108–111 for the lane.

- **XIV.1–2, p.76:** actual He 4096 histories per cover, carbon `2^36`; 49 He / 361 ordered C conditional receiver sectors, 51 distinct carbon q; electron wedge space and both spin labels. Nuclear weights remain attached before trace/minimum; occupied state feeds back into nuclear selection.
- **XIV.3, p.77:** whole-space axial one-body `h_U=τ(-Δ)-g U·n/r`; published gradient-square lower `-g²|U|²/(4τ)` per electron is superseded by locked H003004 correction, not a new baseline to execute. Regular `r^l exp(-r/a)Y_lm` family, physical Gram pencils, all signed m and two spins; common dilation. Quoted display coefficients are predecessor approximations, not the corrected locked exact values.
- **XIV.4, p.77:** exact nuclear lower envelope `min_q[E_nuc(q)-t q]`; He3/4, carbon 333/343/444 phase thresholds. Manuscript calls six C343 intermediate guarantees unresolved; locked H003004 explicitly resolves them and controls this run.
- **XIV.5, pp.77–78:** Green normalization `1/(2π|x-y|)`; scalar proton +1, neutron 0, electron −1, three vector polarization channels. `S_core(q)=(g_c² Z²/v_c+g_p² q/v_p)/(2r_c)`; `V_core=-(g_c Z+g_p U·n)/max(r,r_c)`; `W=(v_c+v_p n(x)·n(y))/|x-y|`; `v_c≥v_p≥0` permits discarding positive pair energy for lower bounds. q-dependent core self stays in both original nuclear minima.
- **XIV.6–7, pp.78–79:** flat Pauli `w_N=min(N,2)+max(N-2,0)/4` for N≤6; scalar-plus-axial crude majorant `A(q)=g_c Z+g_p sqrt(q)` gives max of Coulomb Pauli lower and finite core floor. Complete filling and a numerical ionization gap are distinct claims. Original flat interacting ledger 44 populated accounts, 10 positive ionization lower intervals, 34 overlaps. Original weak C444 total-binding interval `[6.0992574809,38.88]`; later normalized six-electron shell witness improves upper.
- **XIV.8, p.79:** later 24-spin He/C/O family, oxygen 735471 Slaters; common full kinetic/recoil and source reference retained. Prepared attachment margins are not independently relaxed ion energies.
- **XV.1, p.80 — primary geometry source:** manuscript calls lapse `N` (use `ν` to avoid particle-count collision). `ds_g²=ν^{-2}dr²+r²dΩ²`, `dvol=ν^{-1}r²drdΩ`. External kinetic form `τν³|∂rψ|²+τν r^{-2}|∇Ωψ|²`. `α_l=(-1+sqrt(1+4l(l+1)/ν²))/2`. Green expansion `G_ν=(1/(2π))Σ_l[(2l+1)/(2α_l+1)] r_<^{α_l}/r_>^{α_l+1} P_l(n_x·n_y)`. Monopole and uniform-shell scalar/core self unchanged; pair/exchange higher modes change. Exactly 132 populated accounts at ν=1,3/4,1/2, original 30 positive ionization lower bounds and 102 overlaps. Radial scales `ℓ_rad=τν³/v_c`, `E_rad=v_c²/(τν³)`. Physical lapse/action/absolute radius remain assignments.
- **XV.2, pp.80–81:** full massive square root before orbital compression, six rest regimes / 792 total-binding accounts; collective recoil includes outside-span `R=Q−ΣP_α²≥0`. These are locked predecessor inputs, not a request to rerun.
- **XV.3–4, p.81:** source history acts on entire atom; incoming-state work, free continua, recoil, and nuclear gap paid once. Original oxygen source and prepared orbital bank are different records.
- **XV.5, p.82 — primary molecular source:** two-center unit direction `n_D=(r_B n_A+r_A n_B)/|r_B n_A+r_A n_B|`; cores at ±De/2. Core cross `(g_c² Z_AZ_B/v_c+g_p² U_A·U_B/v_p)/D`. D derivative changes own-core potential and internal electron pair field at same leading order as cross attraction. Admissible trials retain correlation/exchange, support localization and complete dissociation reference.
- **XV.6, p.82 — leading molecular coefficient:** carbon `C₁(e)=(6−n_A)(6−n_B)+v_A·v_B/10+e·(t_A−t_B)/10`, with `v=U−μ`, `μ=Σ_i⟨n_i⟩`, `t=T U−V_int`. Carbon phase condition `λr_c>923/2500`, all 91 charge/free allocations and fragment momenta; oxygen replaces 6 by 8, condition `λr_c>2/15`, 153 allocations. Claimed classical sign-optimized neutral C₁ bounds −18/5 (C) / −32/5 (O) differ from free rotational-singlet first-order mean; rotor kinetic gap must be paid for the target extension.
- **XV.7, pp.82–83:** positive-stiffness Gaussian feedback field, complete source/counterterm square and formation payment; no uncharged orientation control.
- **XV.8, p.83:** full-Fock virtual packet normalized pointwise; all source-controlled Weyl and derivative/kinetic costs retained; previous positive full-motion variational gains have their own actual packet and reference. Do not conflate with rotor asymptotics.
- **XVI.1–4, pp.84–85:** energy-difference enclosure requires compatible lower/upper full references; common physical unit chart `E_unit=2α²m_ec²`, `L_unit=ℏc/(2αm_ec²)`, `T_unit=ℏ/E_unit` does not itself select a source/radius/coupling. C12 source q144 U=(12,0) is explicitly retained in isotope transfer.
- **XVI.5–13, pp.85–88:** scalar-current held-He failure and current-response/tomography/perturbation sources belong to other lanes. Respect same source and energy-zero convention when joining outputs.
- **Source register, pp.108–109:** [9] H002295 `GEN4/volii_electronic_source1/REPORT.md`; [10] H002300 `GEN4/volii_radial_occupancy1/REPORT.md`; [11–13] H002305 `GEN4/volii_pair_source1/{DERIVATION,REPORT,ATOMIC_DERIVATION}.md`; [14] H002309 `GEN4/volii_outer_filling1/REPORT.md`; [17] H002311 `GEN4/volii_lapse_field1/DERIVATION.md`; [18] H002317 `GEN4/volii_action_kinetic1/REPORT.md`; [23] `GEN4/volii_molecular_source1/DERIVATION.md`; [24] H002348 `GEN4/volii_moving_reference1/REPORT.md`; [25] H002351 `GEN4/volii_o16_moving1/REPORT.md`; [27–28] H002475 `GEN4/samland_molecular_motion1/{REPORT,DERIVATION}.md`.

## Volume III — 03_SAM_Volume_III_20261111_refined.pdf

Text source: `../../reading/text/03_SAM_Volume_III_20261111_refined.pdf.txt` (192 PDF pages). Read contents/source boundary, searched lane terminology throughout, and read IV pp.31–32, XIV–XV pp.84–90, XXVIII/revision map pp.155–159, Part 2 VI–VIII pp.170–173.

- **Source boundary p.6; XV.8 p.90; XXVIII.6 p.156:** prior refinement native service OOM, completed receipts and analytical results remain distinct from missing native outcomes; an admission size is no resource guarantee. Use bounded minors/structural reductions within this run's stricter 64² exact-rational guardrail.
- **IV.11, p.31, eq.(IV.4):** already-completed TWO-F03 signed-chain N5000 at β=1/5000, 668 negative pairs / 166 paths / 3000 free sites. `I_chain∈[3.41219962633,3.41223131098]×10^{-6}` nats at lag1/3. Locked cross-volume input; do not recompute it or download DOS archive. Printed extraction says “mnats”; briefing's nats is the run's controlling convention.
- **IV.12–13, p.32:** moment/resolvent refinement reuses source without repeat integrations; missing μ5,μ6 operands remain unbuilt. Not a target for lane TWO.
- **XIV.1–4, pp.84–85:** exact rational, symbolic log and certified interval are distinct return types. Scalar inputs are exact integer/rational/decimal strings, not binary floats. Cancellation precedes approximation; arithmetic precision does not reduce source uncertainty. Full noncommuting operator order and support retained.
- **XIV.5–6, p.86:** retained operand identity includes source, mathematical value, provenance and dependency closure. Reuse only when the actual input and implementation match; publishing an operand differs from executing a result.
- **XV.1–4, pp.87–88:** recipes have executable assumptions and checked outputs; admission, equality, and interval containment provide different evidence. New compiled execution still needed for a requested native calculation. A source-radius plateau cannot be cured with arithmetic precision.
- **XV.8, p.90:** exact linear-algebra memory costs can exceed admission envelope; analytical structure or bounded minors can avoid redundant elimination. Do not invent native results for jobs without returns.
- **XXVIII.1–6, pp.155–156:** handoff tuple `(source/preparation, state law/metric, operator, clock, receiver, dependencies)`; equal matrix sizes or recurring integers do not supply a physical identification. Source-specific mathematical objects stay useful with exact scope preserved.
- **Revision map, pp.157–159:** III's opportunity IDs are a separate namespace from Volume II's similarly named records; TWO-F03 is already complete. Historical missing-native/operational entries are not independent scientific findings.
- **Part 2 VI–VII, pp.170–172:** historical Duck protocol, task/dependency references, complete receipts, controls by returned status (`COMPLETED` plus `INVERTIBILITY_UNRESOLVED`, not necessarily failure). Current user window/guardrails supersede historical 900-s defaults. Do not repair the engine during the run.
- **Part 2 VIII, p.173:** whole-source paid He3 and retained cross-volume exact operands remain established inputs; calibration and species/source-map assignments retained explicitly.

No dedicated exact geometric `w_{N,ν}` or rigid-molecular-rotor derivation was found in Volume III; its bearing is custody, exact operations and non-duplication.

## Data files — read after the volumes

Reading begins below in the requested order. Full file content remains available at `../../reading/` for reopening during the work window.

### 00a_NATIVE_ENGINE.md — fully read (118 lines)

- Duck 2.3.5/core0.11.3 IRONCLAD-R32; native service starts only at window open. No engine submissions during reading.
- Wrapper auto-populates controller, target and source_binding; `submit` acceptance is not computation; `returns` then `show KEY` to read completed value. Underlying native receipt JSON needed for hashes.
- Run binding: kind GEN7_DUCK, campaign 20261112T043202Z, law_namespace SAM_land, target SHA256 `821ae35dfa3c40c1cec69487ee426ac1215d6859cce16a64c48c8d477c0a3721`.
- Single-operation tasks or `gen6_job` source-hashed programs; exact source and dependency pointer wire examples are in file. Preserve failures/superseded keys; controls declare expected returned status/reason.
- Engine root/pinned host Python: `/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z`, `.venv/bin/python`. All normal task-specific guardrails from briefing take precedence over generic installed maxima.

### 00b_CAPABILITY_MENU.md — fully read (413 lines, 21 groups / 254 operations)

- Most relevant: GEN3_SOURCE_OPERATOR_WORD, small GEN3_COMPLEX_{PRODUCT,ADJOINT,SOLVE,RANK,EXP}; GEN5_LOG_{QUADRATIC_FORM,TRACE,EXPRESSION}; reusable METHOD_ADMIT/COMPILE/EXECUTE. Exact operation contracts must be read before use.
- Source words contract `CURRENT_REVISION/engines/SLC/SOURCE_OPERATORS.md`; complex operations `MODULAR.md`; GEN5 `GEN5.md`; recipes `gen5/contracts/METHOD_CONTRACT.md`; full-source methods `FULL_SOURCE.md`.
- Retained inputs are source-bound operands, not host-derived native certificates. Native group breadth does not alter the run's stricter memory guardrails. GEN2_HD_PRIMITIVES standalone is blacklisted by briefing despite being listed in menu.
- Geometry PDF p.80 was also visually inspected from the PDF: confirms `τν³` radial / `τν` angular form, `α_l`, Green coefficient, unchanged monopole, and 132/30/102 counts.

### 04_REPORTvolii.md — fully read (6710 lines)

- Lines 1–~950: complete four-peer original Volume II review, all opportunities, scoped failures and native/host custody. Lane-primary FOUR-A03/M01 passages are near lines 770–900; the complete CR2 handoff begins near line 950.
- FORM full report/proof/hypotheses (roughly lines1050–1360): constant-lapse domain equivalent to flat H1 for fixed ν; geometric divergence `a[νh'+2(ν+1)h/r]cosθ`; `a=A/[2τν(ν+1)]`, `d=2(ν+1)/ν`, profile `h=dr/[(d+1)r_c]` inside and `1−(r_c/r)^d/(d+1)` outside. Matched value/derivative, O(r) origin, h≤1. Directional lower `−A²/[4τν(ν+1)²]` follows with exact h² remainder. Variable ν requires `div_g(νF)` and the νν′b term; not an allowed transfer.
- FORM A05 old comparison counterexample: ν1/2,N6,C1,A1/100,τr_c1, w=49/18. Old exact geometric branch `−499849/90000`; previous flat-weight directional branch `−6−1/7500−sqrt(2)/25`; floor `−303/50`. Scalar exact denominators `n_r+α_l+1`; α1=(sqrt33−1)/2>2 ensures only 1s,2s,3s occupied. This is an already verified correction, not new work to rerun. It explicitly identifies exact-w kinetic splitting as the continuation.
- FORM controls: constant wrong field has right norm/wrong divergence with −1/3 witness; mismatched profile produces interior residual1/r_c and normal jump−1/5; pair-negative and changed/smaller kinetic transfers fail. Controls must be chosen reachable for the new task rather than replayed as new work.
- ORBITALS reports/proofs (roughly lines1360–1610): exact frozen decimal coefficients require full Gram normalization; corrected frozen energies and safe c_n remain locked inputs. All-space regular/log integrals, signed m/spin and complete determinant trace retained. Do not recompute.
- REFERENCES report/proof begins ~1610: complete q/I roster and core self retained in both minima. Source sector elimination gives 49 He and 361 C U sectors, 10/51 q classes; all original histories retained. Carbon source triples333/343/444. Lower-comparison minima differ from interacting exact ground.
- Full FORM comparison correction was reopened at lines1290–1310; it explicitly says exact-w splitting is possible and no additional refined panel was claimed in that case.
- Complete embedded 01_atoms, 02_spin_memory and 03_car_fock_loading reports, derivations, hypothesis maps, finite tables, failures and controls were read through EOF. These are locked H003004–H003006 inputs, not work to repeat. Full q/I tables at lines~2360–2440 can serve as already verified operands in a new recipient.
- Spin portion (~2650–4400): exact signed source identity, count insertions, degree-four positive moments, Gauss/Radau, full binary reference and rare-cell law, growing-wait domain and physical-site clock all retained. Distinct scope: source law, adjacent-fit boundary clock, accepted-mass memory, global limits. Host certificates stay host evidence.
- CAR/Fock portion (~4400–6710): Li6 common full-source polar map versus unchanged14336 energy upper; all physical density images before compression, both ordered vertices, own-cloud covariance, exact cell escape; corrected LA01 nonnull control `(0,1,2)/(0,1,4)` has N0,Q−4/5, whereas initial pair `(0,1,2)/(0,2,1)` was null. N12 source/DP/full-flavor/instrument and continuum scalar loading full proofs are locked. No old loading/energy-response constants transfer automatically to changed states.
- LOADING complete proof: shell `p=(2/π)sinc²`, positive-counterterm reference, finite signed unit-mass BV ramps, residue-fiber box-square bound and unique positive schedule, normal finite-time Fock state versus nonnormal static equilibrium shift; actual incoming/control/counterterm baseline retained.

### 05_REPORT.md — fully read (175 lines)

- Cross-volume RH follow-up on TWO odd-phase remainder, not a new atom/rotor input. Nonuniform screen uses actual odd index `A_j=4q_j^{3/2}`; signed contraction before absolute values improves finite paid bounds2.53–4.16×. Energy kernel G and complex bilinear remainder R are distinct; tiny energy residual does not itself bound signed core. Host Arb192 certificates, exact residual/terminal payments, and failed arb.inv API attempt retained.
- Relevant methodological transfer only: preserve operator/source metric, signed cross terms and terminal contributions; call host work by its actual custody class. No RH work is authorized by lane TWO.

### 06_FULL_RESEARCH_HANDOFF.md — fully read by exact shared-content confirmation (5787 lines)

- This last file is byte-for-byte the entire suffix of 04_REPORTvolii.md beginning at line924, already read in full above. Exact full-byte comparison returned true for `04_bytes[106019:]==06_bytes`; no content is omitted or changed. It has 342922 bytes and SHA256 `3aad8ee8d76f2ee5ead2aa705cb4c99cedd033a3b3392d6b90db1d125e107622`.
- Reopened its beginning through FORM/ORBITALS to refresh the lane-primary geometry correction last, then confirmed the complete identity rather than repeatedly consuming the same 5787 lines. It contains all three locked case reports and all verifier reports/proofs/hypothesis maps, with the public 03r recovery notice. Case counts: atoms 13 claims / 9 controls / 19 files; spin 11 / 9 / 22; CAR/Fock/loading 12 / 11 / 24. All reached I1/R2; final manifest director approval remains unset in the preserved historical text.
- Fresh lane memory: exact geometric scalar denominators and spin degeneracies; matched geometric directional field and full form domain; pointwise maximum of legal branches/floor; source-core-self minima and same-inventory references; rotor C1 component differs from the full molecular D^-2 coefficient; physical calibration stays separate from arithmetic certification.

## Reading-stage completion

- All eight requested files are accounted for: three volumes read for the assigned target with precise locations above; five data files' entire contents read (06's complete identity with the already-read 04 suffix confirmed).
- Reading only: no target calculations, native submissions, baseline replays, external archive reads, REPORT.md, engine changes, or writes outside peer TWO.
- The bounded spin transfer review is supplied by the prescribed III/04/06 passages: preserve complete Gibbs metrics, linked residuals and clock/preparation hypotheses. No additional lane TWO mathematical result is claimed during reading.
- Next action is to wait for the user's explicit work-window opening. Before execution, read exact native operation contracts and locate the raw 132-account geometry/source operands named by the retained sources; do not rerun locked baseline scripts.


