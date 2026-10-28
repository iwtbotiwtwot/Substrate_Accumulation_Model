# From frustrated spin to the prime work: the transition and the derivations that connect the two programs

**Attribution:** Sean Brady, originator and conceptual director. OpenAI ChatGPT and Codex (GEN3/GEN4 campaigns) and Claude Code (the October Duck runs and this report) as AI research collaborators, in the project's standing form. AI-assisted writing.
**Prepared by:** Claude (lead), at Sean Brady's request of 27 October 2026 ("a report on the transition from the frustrated-spin results to the prime work, look back through the history and produce a report with any derivations connecting the two programs").
**Register:** engineering. Every statement is traceable to a ledger entry (H-number), a campaign folder under SAM_Research_Project/GEN4, a Volume II or III chapter, or one of the two public repositories. Where this report adds its own arithmetic it says so.

---

## 0. Summary

The frustrated-spin program computed exact joint densities of states g(E, M, b) for specified signed complete Ising graphs, from N = 72 in August through N = 5000 in late September, with 10,800 cases at every size 1–1800 and a public release. The prime-event program built a seven-spin stochastic gate inside an event-created sieve and ran it, with no reference repair, to one trillion candidates on a CPU and eight trillion on three GPUs with three errors. The two programs met in the last week of September 2026, and the meeting point is a single mathematical object: **the boundary free energy of a finite Ising source with hidden spins summed out**.

That object does three jobs in sequence.

1. **Compiler.** Summing hidden spins coupled to a few boundary ports produces an effective interaction among those ports. Character (Walsh) analysis says which interactions survive; hidden fields or a pinned port are needed for any odd term. The prime gate's Hamiltonian is such a compiler: two pair modules and one four-spin "parity gadget" with fields give F(e | r₁, r₂) = C + e[−a(r₁ + r₂) + b r₁r₂], with a(β,u) = log cosh(2βu)/(2β) and b(β,t) = [4 log cosh(2βt) − log cosh(4βt)]/(2β). This is where the frustrated-spin method first enters the prime work (interaction_compiler1, 27 September).
2. **Diagnosis and design.** With one bank returning the pair terms cancel exactly, so the one-bank blocking margin is b alone. First-error replay of 126 failures found all 120 composite errors in that sector. Maximising the smaller margin, min(b, 2a − b) ≤ a with equality at b = a, fixes the triple strength in closed form, t* = ½ acosh √(C + √(C² − C)) with C = cosh(2u). That change took matched billion-candidate errors from 569 to 40 (prime_balance1).
3. **Measured transfer.** The exact N ≤ 1000 boundary responses have no odd terms (inversion symmetry; all 91,620 odd-coefficient intervals contain zero). Pinning one boundary port converts the four-body coefficient into a visible triple and a bias that a local field cancels. Fed through the compiler at the gate temperature, the N = 1000 packet response gave a one-bank leakage 8.26× below the historical gate (spin_prime_connection1, 30 September). The same report is explicit that the improvement comes from boundary-response structure, not from frustration as such: positive-fill and frustrated signed-chain sources give ratios differing by 6 × 10⁻⁷.

Every derivation in this chain is written down in the record and I re-derived the numbers: a(4) = 3.6534264659876117, b(2) = 2.9609499856382886, t* = 2.3464897298984759, the N = 1000 ratio 0.9070698726632545, the two-scale identity to zero, and the hidden_clock1 truth table to the ninth digit. What the chain does not do is also on record: it supplies no primality certificate, the integer counter and the period-writing rule are explicit digital components, and the Volume III text states that "the prime-event sources do not establish a relation to FEOP".

---

## 1. The two programs before they met

**Frustrated spin.** The exact dense frustrated-spin N = 72 replay through the SLCV21R candidate (H000253, 16 August) is the first entry; the N100 "H14F exact particle spin" grammar of 10 August (H000142) is its ancestor on the computation side. The program's object is the joint density g(E, M, b): the number of spin configurations with energy E, magnetisation M and ordered boundary assignment b on four retained ports P = (0, 1, 60, 61). Its sources are complete signed graphs built from fifteen-spin "packets" (three complete five-spin layers joined by matchings), in three families (packet, signed packet with one negative edge per layer, signed-packet chain with alternating gateway bridges), each completed with a uniform fill J₀ = ±1 on every absent pair. The solver's lever is the identity

  Σ_{i<j} s_i s_j = (M² − N)/2, hence E = E_c − (J₀/2)(M² − N), E_c = −Σ ΔJ_ij s_i s_j,

so a dense complete graph is handled through its sparse correction and the collective M (Volume III Chapters IV–V; spin_joint_install1). The GEN4 pod campaign of 24–26 September (fourteen Blackwell workers, H001709–H001777) took it from N = 72 benchmarks to N2000, N3000, N4000 and N5000 (1,530,259,992 nonzero records at N5000), then the RAM-retention pilot (H002005) and the continuous N1–1800 campaign (10,800 cases, 118,387,509,614 support entries, public release H002064, repository `iwtbotiwtwot/frustrated-spin`, 86,809 files). The Volume II home is Part II, Chapters VI–X; the Volume III home is Chapters IV–VI.

**The prime work before spin.** Prime work in the record predates the spin scale-up: the Mersenne (MP) program of 4–22 August (H000011 onward: prime ruler, SLC Mersenne farm, M1279 and M607 exact closures, proof-carrying farm) and the RH program's prime-indexed ledgers. These are arithmetic programs; they did not use a spin source. The prime-event program is different in kind, and it is the one the spin results fed.

---

## 2. The transition, day by day

| Date (2026) | Entry | Step | What it carried from spin |
|---|---|---|---|
| 27 Sep | H001796 | prime_clock1: prime-indexed tick schedules on a six-state Al27 clock; prime order vs reversal changes survival 0.2691 → 0.2734 at equal gap multiset | Volume I clock; no spin yet |
| 27 Sep | H001802 | prime_surface1: prime/composite circulation periods on one corrugated sphere; lcm returns; 5/7 geometry | Volume I geometry; supplies the cadence later used as gate exposure |
| 27 Sep | H001794, H001801 | GEN4 discovery on N2000 boundary states; four-hidden-spin parity gadget with pure four-spin effective interaction | **Frustrated spin:** thermal boundary readouts at β·N = ½, 1, 2 and the first hidden-spin gadget |
| 27 Sep | H001804, H001805 | Unequal-copy ratios; exact two-scale identity q₂ⱼ = p₂ⱼ − 4pⱼ | Character calculus on boundary free energy |
| 27 Sep | (interaction_compiler1) | Selective compiler: subgroup selection, copy counts, local modules, the odd triple via fields; source `mixed_1` (six hidden spins) | The compiler is the bridge object |
| 27 Sep | H001806 | hidden_clock1: `mixed_1` driven by externally supplied recurrence periods under Volume I exposure √(1 − A); first truth table and the one-bank cancellation | Spin gate meets Volume I clock |
| 27 Sep | H001807 | prime_feedback1: periods become event-created; the sieve induction; 60 primes to 281; composite channels never return at primes | First prime-event run with a spin gate |
| 27 Sep | H001808–H001810 | Source scale 2 and three readings; 100 million; one billion on a pod (1/64 exact) | |
| 27 Sep | H001811 | Seed mechanism: 126 first errors transfer with the draw triple; all 120 composite errors in the one-bank sector; a = 3.6534, b = 2.9609 reconstructed from the 128-state tables | The algebra explains the data |
| 27 Sep | H001812–H001814 | Balanced source a = b: 569 → 40 errors, 47/64 exact; fresh 13/16 | Closed-form design from the compiler |
| 27 Sep | H001830, H001844, H001848 | Manuscript; public release `iwtbotiwtwot/prime-event` v0.1.0/0.1.1; MIT / CC BY split matched to frustrated-spin's; Zenodo 23002148 | Licensing copied from the spin repository |
| 27 Sep | H001836, H001838 | Prime-event channels transferred to the RH signed ledger; weighted prime estimate (Abel transfer) | Prime events → RH |
| 29 Sep | H002013 | spin_prime_dataset1: 6,000 spin cases N1–1000, 91,620 boundary records, 183,272 interaction coefficients joined to the two gates in one SQLite database; Walsh translation recovers the compiler's a, b | **The explicit join** |
| 30 Sep | H002014 | spin_prime_connection1: pinning a port makes the triple; N1000 ratio 0.9071; 8.26× lower one-bank leakage; energy/entropy decomposition of the pinned field | **The measured transfer** |
| 30 Sep | H002015, H002016 | Wider dynamics map (five coupled layers); Volume II memory kernel on the gate; prime_duck1 17× error reduction at Γ = 64 by kinetics and timing | Volume II projection method |
| 30 Sep | H002029 | MP event bridge: prime-event gate features do not improve Mersenne candidate ranking (falsified) | |
| 30 Sep | H002050 | Technical companion report on both programs | |
| 1 Oct | H002093–H002097 | Harvey's identity for prime-event history reconstruction (55,662,472 events) | Prime events → FEOP side |
| 3 Oct | H002255, H002257 | Native activity clocks on the gate; exact three-term clock correction | Volume I clock method |
| 3 Oct | H002208 | Standing instruction: after every request, review the latest frustrated-spin work for contributions | Sean's rule that keeps the two programs in contact |
| 3 Oct | (prime-event repo) | u5 local trajectory stopped at 1,039,515,000,000 decisions, 0 errors; three-GPU run stopped at 8 × 10¹² with 3 false emissions | |

Two things stand out in the dates. Almost the whole bridge was built on 27 September, in one day, in a chain of eleven campaigns each authorised by Sean Brady after the previous result. And the explicit spin-to-prime join (the dataset and the connection experiment) came two days later, after the prime results already existed: the spin program's exact responses were brought in to explain and improve a gate that had been designed by the compiler method the spin program made available.

---

## 3. The derivations, in order

Notation. Spins take values ±1. β is the dimensionless inverse temperature. For the gate, e is the output spin, r₁, r₂ the two bank inputs (+1 when a bank returns). "Record" means the number appears in the cited campaign; "checked" means I recomputed it for this report.

### 3.1 Boundary free energy as the common interface

For a source with boundary spins s and hidden spins summed out, the boundary free energy is a character expansion

  F(s; β) = Σ_S c_S(β) ∏_{i∈S} s_i,

and when each hidden spin a couples only through a local field W_a·s + h_a the sum is explicit:

  F(s) = −(1/β) Σ_a log[2 cosh β(W_a·s + h_a)].

A 16-state Walsh transform over the four boundary ports recovers the c_S (spin_prime_dataset1 DESIGN; H002013 "Walsh translation recovers the compiler's pair/triple source coefficients"). This is the same object the frustrated-spin program calls its boundary thermal readout: the N2000–N5000 milestones retain certified log Z, free energy, moments and boundary Walsh coefficients at β = 1/N and 4/N (spin_prime_progress1 §5). The dataset's representation is dimensionless, β·c_S, so a gate at β = 1 and a graph at β = 4/1000 are compared on one scale.

Global spin reversal of a zero-field source sends every odd character to minus itself, so odd coefficients vanish. The dataset confirms this on the whole corpus: all 6,000 cases have zero fields and all 91,620 odd-degree coefficient intervals contain zero (H002013). This single fact shapes the rest of the bridge: a prime gate needs an odd term, and a zero-field spin graph cannot give one unless its symmetry is broken.

### 3.2 Character selection: how a compiler chooses an interaction

interaction_compiler1/DERIVATION.md, 27 September, Codex under Sean Brady's direction.

- **Subgroup projection.** Multiplying independent copies of a source over a sign-flip subgroup G of F₂⁴ keeps exactly the characters in G^⊥, which is closed under symmetric difference. So retaining pairs {1,2} and {3,4} forces the four-body term; retaining {1,2} and {1,3} forces {2,3}. All 67 subgroups were enumerated; no single subgroup isolates a non-closed support.
- **Copy counts.** A unit star (one hidden spin coupled to all four ports, strength 1) has only the constant, six pairs and the full parity: c_pair = −log cosh(4β)/(8β), c_four = [4 log cosh(2β) − log cosh(4β)]/(8β), both nonzero for every β. Taking w_p nonnegative copies of the eight sign representatives multiplies c_A by T_A = Σ_p w_p χ_A(p); Fourier inversion gives w = (N + a χ_A)/8, so an isolated single character needs N ≥ |a| ≥ 4 copies and two characters need 8. Searching 6,560 copy vectors found exact supports a subgroup cannot (table: support {15} in 4 copies, {3,12} in 8, {3,12,15} in 2).
- **Local modules.** A hidden spin coupled only to ports i, j gives z = 2 cosh β(s_i + s_j) and F = C − [log cosh(2β)/(2β)] s_i s_j, one pair term and nothing else. Independent modules add free energies, so compositions create no cross terms. This is what makes the gate's a and b separately tunable.
- **The odd term.** Four hidden spins with fields h = 1 and coupling rows p ∈ {±1}³ of product +1 have local fields 1 + p·s; the conditional partition functions are 16 cosh(4β) and 16 cosh(2β)⁴ in the two parity sectors, so F = C + g(β) s₁s₂s₃ with g = [4 log cosh(2β) − log cosh(4β)]/(2β) > 0. This is the four-spin parity gadget of H001801 with one port fixed at +1, realised as hidden fields. The record is explicit that "a zero-field globally spin-reversal-symmetric source cannot produce an odd boundary term."

At β = 1 the compiled `mixed_1` source has pair coefficients −0.662501373679 each and triple +0.996411381809 (checked: log cosh(2)/2 = 0.66250, [4 log cosh 2 − log cosh 4]/2 = 0.99641).

### 3.3 The gate marginal

Volume III Chapter XXIV writes the retained Hamiltonian:

  E = −u h₁(e + r₁) − u h₂(e + r₂) − t Σ_{p∈P₊} z_p (1 + p₁e + p₂r₁ + p₃r₂),  P₊ = {+++, +−−, −+−, −−+}.

Summing the hidden spins:

  a(β,u) = log cosh(2βu)/(2β),  b(β,t) = [4 log cosh(2βt) − log cosh(4βt)]/(2β),
  F(e | r₁, r₂) = C(r₁, r₂) + e·H(r₁, r₂),  H = −a(r₁ + r₂) + b r₁r₂,
  Pr(e = −1 | r₁, r₂) = 1/(1 + e^{−2βH}).

The three input sectors have fields 2a + b (no return: accept), −b (one return), b − 2a (both return). The desired truth table needs a > 0 and 0 < b < 2a; the two composite-blocking margins are b and 2a − b. **In the one-bank sector r₁ + r₂ = 0 and the pair terms cancel; its margin is b alone, and no pair strength can change it.** This cancellation is the hinge of the whole story.

Checked against hidden_clock1's table. At source scale 1 (u = 1, t = 1): a = 0.66250, b = 0.99641; P(accept | none) = 0.990461, P(reject | one) = 0.880041, P(reject | both) = 0.658627. Doubling only the pair strength (u = 2): 0.999817, 0.880041 (unchanged, as the cancellation predicts), 0.990258. All six digits match the record. At source scale 2 (u = 4, t = 2), the production gate: a = 3.6534264659876117 (record identical), b = 2.9609499856382886 (checked 2.9609499856382895; last-digit rounding), one-bank gap 2b = 5.92190, equilibrium false output 1/(1 + e^{2b}) = 0.00267294 per reading (record 0.00267293946).

### 3.4 From a driven response to an event-created sieve

**Dynamics.** Heat-bath generator L_{yx} = Γ/(1 + e^{β(E_y − E_x)}) on the 128 states (output plus six hidden spins), columns summing to zero. Exposure per candidate is Γ d_k √(1 − A_k): d_k from the corrugated-sphere circulation of prime_surface1 (35-phase 5/7 geometry), √(1 − A) the Volume I lapse factor, A the accumulation profile (uniform ¼ or the rough cos/sin profile with the same step mean). Three confirming readings: P_acc(n | ρ) = 1ᵀ D T_n D T_n D T_n ρ, a masked contraction that keeps the state between readings and between candidates. It is not the cube of an equilibrium probability (Volume III XXIV; prime_fidelity1).

**The sieve** (prime_feedback1 DESIGN, 27 September). Start at n = 2 with no channels. An accepted n installs a channel of period n with first return at 2n; channels alternate between two banks by creation order; a bank input is the OR of its returning channels; the ideal rule accepts iff neither bank returns. Induction: if the accepted set below n is exactly the primes below n, a prime n has no returning channel and a composite n = mp has p's channel returning. No prime table, trial division or modular test enters the rule; an independent sieve only scores afterward.

**Two structural lemmas** the record proves and uses. (i) A channel born at a composite returns only at multiples mp with m ≥ 2, which are composite; so no erroneous channel can directly suppress a prime (zero prime return signals in all 384 trajectories of prime_feedback1). (ii) An erroneous event changes the creation-order parity and hence the bank assignment of every later channel; the traced chain of seed 1000053 (extra event at 312,596,611 → prime 483,920,363 enters the other bank → at 967,840,726 = 2 × 483,920,363 the two returns share a bank in one history and split in the other → opposite decisions) shows the effect travelling through digital memory, not divisibility (prime_seed_mechanism1).

### 3.5 Diagnosis and the balance derivation

Seed mechanism (H001811): of 126 first errors, 120 were composite emissions and every one had exactly one returning bank; swapping the three random draws moved the error 126/126 times, swapping the incoming state never did. One missed prime (3,510,937) was resolved to a third draw 0.99966476186306341 falling in a rejecting-state interval 3.77 × 10⁻¹¹ wide. The algebra of 3.3 says why the one-bank sector is weak.

Balance (prime_balance1 DERIVATION.md): at fixed a > 0, min(b, 2a − b) ≤ a with equality iff b = a. At β = 1 with pair strength u = 4, a = ½ log cosh 8. Set C = cosh 8, z = cosh(2t)²; since cosh(4t) = 2z − 1, b(t) = a becomes

  z² = C(2z − 1),  z = C + √(C² − C),  t* = ½ acosh √(C + √(C² − C)) = 2.3464897298984759.

Checked: t* = 2.346489729898476, b(t*) − a(4) = 0.0. The other root is below 1 and is not a cosh². The criterion was fixed before any successor trajectory was run. At general β the equaliser is t(β) = acosh √(C(β) + √(C(β)² − C(β)))/(2β) with C(β) = cosh 8β, so a fixed t balances at one temperature only; this is the explicit distinction from the all-temperature constructions of 3.7.

Result: one-bank three-reading false emission 1.91 × 10⁻⁸ → 3.04 × 10⁻¹⁰ (÷63), both-bank 4.74 × 10⁻¹² → 3.01 × 10⁻¹⁰ (×64); matched 64 seeds × 2 profiles through 10⁹: errors 569 → 40, exact trajectories 1/64 → 47/64, fresh 13/16 (prime-event repository headline table). The later u = 5 balance, t = 2.8465622403941495, a = b = 4.653426410750604 (checked to all digits), dropped the worst blocked-input emission to 8.06 × 10⁻¹³ and ran a trillion decisions with no error.

### 3.6 The measured transfer: pinning a port

spin_prime_connection1 (H002014). The exact N ≤ 1000 four-port responses have only even characters. Fix one boundary spin p; the four-body coefficient becomes a visible triple and the pair joining output to the pinned port becomes an output bias:

  βF(e, r₁, r₂ | p) = input-only terms + e(d + u r₁ + v r₂ + w r₁r₂).

A local output field βh = −d cancels the bias at the chosen temperature, leaving e[−a₁r₁ − a₂r₂ + b r₁r₂], the gate's form. For the N = 1000 positive-fill packet at β = 4/1000 (pin vertex 0 to −1, output vertex 1, inputs 60 and 61): d = u = v = −1.907980462097066, w = +1.730671594798363, so b/a = w/|u| = 0.9070698726632545 (checked exactly). Transferring that ratio into `mixed_1` at β = 1 with the mean pair coefficient held at 3.6534264659876117 compiles a new 128-state gate whose worst one-bank false emission is 2.31833 × 10⁻⁹, 8.26× below the historical gate's 1.91437 × 10⁻⁸ (N = 62 and N = 300 interpolate at 5.10 × 10⁻⁹ and 2.61 × 10⁻⁹); the balanced gate at 3.04 × 10⁻¹⁰ remains better. The unadjusted pinned gate (bias kept) suppresses one-bank emission to 7 × 10⁻¹⁹ but misses primes at 2.67 × 10⁻⁶, which is the record's demonstration that all four bank sectors must be optimised, not the weakest static margin alone.

**Entropy enters the gate.** The pinned field decomposes as (β/2)ΔF = (β/2)Δ⟨E⟩ − ½ΔS; for the no-return packet field 3.6386520569 = 4.0074318192 − 0.3687797623. Ground energies alone would miss the entropy part. This is the one place where the frustrated-spin program's thermal machinery (certified thermal readouts, degeneracies) is strictly needed by the prime work.

**What the transfer shows and does not show.** The search covered 11,268 source/temperature pairs and 4,326,912 candidate evaluations, with 96 Arb-certified truth tables; six gates got finite-rate evaluation; no closed-loop prime stream was run with them. Positive-fill packet and frustrated signed-chain ratios at N = 1000 differ by 5.95 × 10⁻⁷. The record's conclusion, repeated in Volume III: boundary-response structure is the useful input; frustration itself is not identified as the cause.

### 3.7 The all-temperature construction (unequal copies and two scales)

two_scale_ratios1 (H001805), the exact identity the search found: with p_J = −log cosh(4βJ)/(8β) and q_J = [4 log cosh(2βJ) − log cosh(4βJ)]/(8β),

  q_{2J} = p_{2J} − 4p_J  for every β > 0, J > 0

(checked to zero at two (J, β) pairs). The copy vector [4, −1, 0, −1] over scales J and 2J gives P = 4[4p_J − p_{2J}] and Q = −4q_{2J} = P, so the four-body-to-pair ratio is exactly 1 at every temperature, with 24 hidden spins; a rational ratio n/d costs 20d + 4|n| copies. The result F = C + P s₁s₂[1 + s₃s₄] is a parity-conditioned pair interaction. This is the machinery the record names as the alternative route to the gate's odd term ("requires an explicit source mapping, including the fixed port or hidden fields that allow the odd term"); it was not substituted into the production gate, whose balance is fixed-temperature.

### 3.8 The first-error bound and the census survival

Volume III Chapter XXIV states a finite theorem. If the accepted history is exactly the primes and fresh draw triples are independent conditional on the past, with c bounding blocked-input emission and d bounding no-bank suppression over all phases and incoming states, then disjoint decomposition by the first error gives

  Pr(an error through N) ≤ [N − 1 − π(N)] c + π(N) d.

The exact three-reading probability of the encoded sampler is V₃(s)/L³ with L = 2⁵³ and V_{k+1}(s) = Σ_{j: e(j) = −1} W_{sj} V_k(j), W the integer grid counts of each stored CDF row.

My arithmetic with the recorded c, d at N = 10⁹ (π = 50,847,534): baseline (c = 1.914 × 10⁻⁸, d = 3.62 × 10⁻⁹) bound ≥ 1, no information; balanced (3.044 × 10⁻¹⁰, 9.060 × 10⁻¹⁰) gives survival ≥ 0.665 against the observed 47/64 = 0.734 and the census envelope [0.717107, 0.717210] of Chapter XXV; u = 5 (8.06 × 10⁻¹³, 2.25 × 10⁻¹²) gives survival ≥ 0.9991, consistent with the trillion-decision run. The census itself (50,847,534 no-return, 129,835,417 bank-0-only, 77,222,775 bank-1-only, 742,094,273 both-bank decisions) explains the cost of balancing: the both-bank sector is the largest and carries 0.224 of the balanced hazard 0.332.

### 3.9 Memory and clocks: the Volume I and II methods applied to the gate

- **Memory kernel** (prime_sam_dynamics1, Connection B). Let C retain output probabilities and R lift to conditional Gibbs hidden states; with p = Rq + r, q̇ = Aq + CQr, ṙ = Bq + Dr, K(t) = CQ e^{Dt} B. All four bank sectors have nonzero kernels; output-flip hazards within one output sector range from 7.9 × 10⁻¹⁶ to nearly 1, so the output bit alone is not lumpable. A both-return → no-return switch at Γ = 8 gives acceptance 0.3069 full against 0.5814 for the two-state projection. This is the Volume II projection framework (executed first on a 24-hidden-spin module) transferred to the actual gate.
- **Activity clocks** (H002255). With λ_b the total flip rate and κ_b the output flip rate, τ_all = ∫λ, τ_out = ∫κ; in output-activity time the output has the exact two-state quotient C_e Q^out = H C_e with H = [[−1, 1], [1, −1]] for every bank and preparation, yet the stopping coordinates carry the hidden memory: two preparations with identical acceptance mass 0.999999999094 have conditional Laplace values 0.99999986 and 0.22523 at z = 1.
- **Clock-weighted correction** (H002257). For the eight-coordinate reduction (output plus hidden bits 5, 6), G_full − G₈ = Δ₀ + Δ₁ + Δ₂ exactly (preparation replacement, first-reading reset, second-reading reset); the plain endpoint discrepancy is 6 × 10⁻²⁰ while the clock-weighted one is 0.7748, so an event-accurate reduction can hide a large clock response.
- **Clock-dependent boundary free energy** (Connection C). Under the departure-state law Q' = Q diag(ν) the stationary occupancy is π'_s ∝ exp[−β(E_s + β⁻¹ log ν_s)]: a clock term inside the effective potential, which after hidden summation shifts the gate's bias by up to 0.0164 and the triple by 0.0080. "The new spin→gate mapping, thermal energy/entropy decomposition, and this clock occupancy correction now meet at a common boundary free-energy representation."

### 3.10 The other inlet: Volume I geometry and prime timing

The cadence the gate runs on is not arbitrary. prime_surface1 put prime and composite circulation periods on one corrugated sphere r(θ, φ) = 1 + [sin²θ cos 2φ + sin³θ cos 3φ/3]/20 with equal area and mean cadence; the joint configuration returns after lcm(p, q), the 5/7 pair gives 35 ticks with 1.94% interval spread, and prime-indexed sampling moves the mean through the residues it visits (1.010069 against 1 for 12/16's 48 ticks). prime_clock1 showed that prime-ordered and reversed gap schedules with the same multiset change a six-state clock's survival (0.2691 vs 0.2734). These are the Volume I ingredients (surface, lapse √(1 − A), order sensitivity) that the gate inherits as exposure; the record is explicit that they supply timing, not a prime selector.

---

## 4. Verification status, derivation by derivation

| Derivation | Where | Native or exact receipt | Independent check | Re-derived here |
|---|---|---|---|---|
| Character selection, copy minima | interaction_compiler1 | 6,560 copy vectors enumerated; 67 subgroups | Codex-written checker | coefficient values at β = 1 |
| Gate marginal a, b; sector fields | hidden_clock1, Vol III XXIV | 128-state tables, 7,208 checks | Padé/spectral replays | truth table to 9 digits; a, b to 16 digits |
| Sieve induction; no prime return | prime_feedback1 | 384 trajectories, 435,370 checks | trial-division scorer | — (elementary) |
| One-bank weakness | prime_seed_mechanism1 | 1.15 × 10⁹ decisions replayed; 126 swaps | 2,349 checks | — |
| Balance t* | prime_balance1 | source built by bisection; 1,080 checks | matched 64 seeds, fresh 16 | t* and u = 5 values exact |
| Pinned-port transfer | spin_prime_connection1 | 96 Arb truth tables; 1,752 checks | Padé 4.7 × 10⁻¹⁵ | b/a ratio exact |
| Two-scale identity | two_scale_ratios1 | Arb256 finalists; 930 checks | algebraic proof in record | residual 0 |
| First-error bound | Vol III XXIV (V3PE10) | exact V₃/L³ counting | — | survival bounds 0.665 / 0.9991 |
| Memory kernel, clocks | prime_sam_dynamics1, H002255/57 | 320-bit native products; 29,712 scalars | Taylor/Poisson series | — |

Independence, plainly: every derivation was written by ChatGPT or Codex under Sean Brady's direction and checked by separately written code of the same provenance; the public repositories' one-command replays (prime-event seed 1000063 to 10⁹ exact; frustrated-spin N2000 packet/+1 reproduction) are the artefacts an outside reader can run. My re-derivations above are a third pass by a different instrument on the closed forms only, not on the trajectories.

---

## 5. What the transition produced downstream

- **Prime events → RH.** The event-created channels were attached to the RH signed ledger (H001836: at 65,536, 699 balanced triples form 55 pairs and the full coefficient drops 0.2209 → 0.0401; about 98% of the remaining cost sits in the shared prime-event feature) and a payment-aware Abel transfer gave an all-scale inequality with factor ζ ≤ 1/log 11 (H001838). These are transfers of the prime-event object into the arithmetic program, not of spin.
- **Prime events → Mersenne.** The one attempt to use gate features for MP candidate ranking was falsified (H002029: test mean rank 2.857 gate vs 2.286 arithmetic).
- **Prime events → Harvey.** Harvey's generating-function identity was used for exact history reconstruction of the prime-event stream (prime_harvey1–4, 1 October); this is the entry point of the FEOP program reported separately.
- **Spin → RH and FEOP (October).** The spin program's later staircase work (spin_work, spin_verify, 20–21 October) and the FEOP local operator were put side by side in rh_crossover_1: both show a recurrence-plus-remainder with a double root at a boundary and a simple root beyond. The peers called the p⁻² against refinement⁻² match a coincidence until one construction unifies them; Sean's clarification of 22 October asks that such links be recorded as a transfer ledger, not a claimed unity.
- **Spin → Volume II matter.** The compiler, memory-kernel and residual-direction methods became Volume II Part II (Chapters VI–X) and fed the October volii_matter and volii_gate runs. Chapter XXIV's closing paragraph names the method transfer and refuses the numerical one: "assigning its numerical constants to Prime Event would change the source."

---

## 6. What the connection is not

The record is careful on five points and this report repeats them.

1. The gate does not certify primality. Its exact trajectories are observed outcomes of a stochastic model; the first-error theorem bounds the probability of a first error, not behaviour after one.
2. The integer counter, the period-writing rule and the alternating-bank assignment are explicit digital components. The spin source decides; it does not create the arithmetic.
3. Frustration is not shown to matter. The measured improvement came from boundary-response structure, and an unfrustrated packet gives the same ratio as the frustrated chain to 6 × 10⁻⁷.
4. Prime-gap statistics were not tested in any spin-to-prime campaign.
5. Volume III states that the prime-event sources establish no relation to FEOP. The two prime programs share Harvey's identity as a tool and a lineage of people and instruments, not a theorem.

---

## 7. Where the material lives

- Volume III: Chapters IV–VI (N5000, N2000, joint state spaces), XXIV (Prime Events from Ising Sources), XXV (Prime Event Computation), XXVI (continuation and clocks); typeset sources `volumes/III/src/book_20261025/{n5000_chapter,n2000_chapter,exact_01,prime_event_01,prime_main,prime_continuation}.tex`.
- Volume II: Part II, Chapters VI–X (spin), with the later matter chapters receiving the methods.
- Public: `github.com/iwtbotiwtwot/frustrated-spin` (86,809 files; N1–1800 release 8.34 GB; milestones N2000–N5000 on Drive; Zenodo 10.5281/zenodo.22989862) and `github.com/iwtbotiwtwot/prime-event` (232 files; 288 trajectories; replay to 10⁹; Zenodo 10.5281/zenodo.23002148). Both MIT software / CC BY 4.0 data.
- Private campaigns: `SAM_Research_Project/GEN4/` folders interaction_compiler1, hidden_boundary_wildfowl1, unequal_copy_ratios1, two_scale_ratios1, hidden_clock1, prime_surface1, prime_clock1, prime_feedback1, prime_fidelity1, prime_distance1, prime_pod1, prime_seed_mechanism1, prime_balance1, spin_prime_dataset1, spin_prime_connection1, prime_sam_dynamics1, prime_duck1, spin_prime_progress1, prime_native_clock1, prime_clock_memory1, and the frustrated_spin_* and spin_* folders; bulk data on the T500 and Google Drive.
- The public SAMA repository holds nothing of either program after 29 August; both belong to the SAMA backlog recorded this morning.

---

## 8. Recommendations

1. **Close the open half of the transfer.** The pinned-port gates were evaluated conditionally, never in matched closed-loop runs against the balanced gate. One matched 64-seed run of the N = 1000 gate would make the spin-to-prime connection a measured end-to-end result rather than a conditional one (Volume III names this as the first of two assignments).
2. **Write the bridge as one derivation note** for outside readers: 3.1–3.6 above with the checked numbers, about four pages, since it is the cleanest self-contained piece of mathematics the two programs share and both public repositories already carry the data it needs.
3. **Record the lineage honestly in the volumes.** Chapter XXIV already credits the compiler, balance and leakage derivations to Codex under Sean Brady's direction; the author line should follow his decision of 27 October.
4. **Keep the standing review** (H002208) but point it at the spin engine's October results, which have moved to reciprocal history, so the prime work is told when something it can use appears.
5. **Do not restate the FEOP link.** The record's negative is correct and should stay until a construction connects a spin staircase level to a p-adic level.

---

## Sources

Ledger (ironclad SAM_HISTORY/entries): H000142, H000253, H001563, H001709–H001713, H001727, H001730, H001766, H001777, H001791, H001794, H001796, H001801, H001802, H001804–H001812, H001814, H001822, H001826, H001830, H001836, H001838, H001844, H001848, H001979, H002005, H002013–H002016, H002028–H002031, H002037, H002050, H002063, H002064, H002091, H002093–H002097, H002148, H002161, H002208, H002219, H002255, H002257.
GEN4 (SAM_Research_Project): interaction_compiler1/DERIVATION.md; hidden_clock1/REPORT.md; two_scale_ratios1/DERIVATION.md; prime_feedback1/{DESIGN,REPORT}.md; prime_balance1/DERIVATION.md; prime_seed_mechanism1/REPORT.md; spin_prime_dataset1/DESIGN.md; spin_prime_connection1/REPORT.md; prime_sam_dynamics1/REPORT.md; spin_prime_progress1/REPORT.md; prime_surface1/REPORT.md; prime_clock1/REPORT.md.
Volumes (Substrate_Accumulation_Model, branch volumes-from-source-20261025): III/src/book_20261025/prime_event_01.tex, prime_main.tex, prime_continuation.tex, n5000_chapter.tex, n2000_chapter.tex, exact_01.tex; II/src/spin_00–spin_04.tex.
Public: github.com/iwtbotiwtwot/frustrated-spin (README, commit 8b0b506); github.com/iwtbotiwtwot/prime-event (README, commit eab9da0).
Live pages: SAM_LIVE/04_PRIME_GRAMMAR_CURRENT.md (H002257).
