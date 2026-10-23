# Volume I, Chapters VII–XII: chart extraction (what we have, what we don't, and the low-lying fruit for ironclad)

Sean Brady, 2026-10-23: "the later chapters use a lot of 'identities' that are honestly blanks filled as best as I could. The distance and redshift work has
evolved significantly while the later chapters simply have not received the same attention. Lets do the extraction to see what we already have, what we don't,
and rank the low lying fruit." Lead's reading of the living text (volumes/I/SAM_Volume_I.md lines 27235–34581, the 19 October 2026 expanded edition) against the
three ledger forms the run program now uses: the Volume II staircase (gain = field + lapse + switching, every switch once, the total optimised), the RH transition
ledger (price = accounts each once; a one-use identity checked in integers; a storage question across one transition; a frozen-chart identity separating the
receiver's own motion), and the verification form (predictions first, separate code, every failure kept). Companion document, not the living text; nothing in the
volume is moved or deleted by it. Engineering register. Directed by Sean Brady. Executed with Claude Code.

## How each chapter's statements are sorted

Every numbered statement in these chapters falls into one of three bins, and the chapters themselves mostly say which:

- **(A) Exact algebra given declared premises.** Safe to carry; a run can certify it, and certifying it teaches us only whether our transcription is right.
- **(B) Selected identifications.** A number from the count grammar matched to a known value after the value was known. The chapters say so in each case.
  These are the "blanks filled": they are not wrong, they are unexplained, and a run cannot explain them; only a construction that produces them from a
  declared measure can.
- **(C) Missing laws.** A dynamical, boundary or measure law the chapter names as absent. No run is possible until one is written down; a run can only test a
  candidate.

The runs we know how to do well act on (A) when (A) has the shape of a ledger with a storage question, and on (C) when a candidate law is small enough to declare.
They do nothing for (B).

## Chapter VII — horizon thermodynamics and the finite-entry ledger (pages 181–189)

**Declared quantities.** A(r) = r_s/r, F = 1 − A; surface gravity κ = c²/(2r_s); T_H = ħκ/(2πck_B); entry count N = A_H/(4ℓ_P²) = 4πGM²/(ħc); S_H = k_B N;
the integer-N sequence M_N ∝ √N; the finite emission ΔE_j = Mc²(1 − √(1 − j/N)); the ratio c*(q) = ΔE/(k_B T_H) = 2/(1 + √(1 − q)) with its Catalan expansion
Σ C_j q^j/4^j and the remainder bound q^{m+1}/(1 − q); the step temperature T_step = ΔE_j/(j k_B); detailed balance Γ_em/Γ_abs = e^{−j}; the backreaction
exponent −ε/(k_B T_H) + aε²; the truncated geometric occupation p_n = q^n/Z_K with total-variation distance q^{K+1} from the infinite law; binomial transmission
with ⟨m⟩ = η⟨n⟩, Var(m) = η(1 − η)⟨n⟩ + η²Var(n); the Si29 Hessian pair (G not proportional to H_A; H_A indefinite at the second reference); the access-channel
contraction; the three-step account 4 → 3 → 2 → 1 with emitted energies (2 − √3, √3 − √2, √2 − 1)E* summing to exactly one.

**Bin (A), exact:** everything above given the three bridges (metric adapter, Hawking conversion, quarter-area rule). The finite first law is a telescoping sum, the
Catalan series and its bound are exact, the TV distance is exact, the worked count experiment ((8,4,2,1)/15 → (85,27,7,1)/120, Fano 359/330) is exact.
**Bin (B):** the quarter-area premise and "k_B per entry" (the chapter is explicit that g_N = e^N is not an integer degeneracy).
**Bin (C):** the emission clock (absolute rate), the boundary response R(ω) (shared with Chapter XI), the energy join ε_Q = ħω_phys, the formation floor N_floor, the
species sum, the boundary density operator. The chapter lists these as "the missing physical joins".

**Weights assumed without saying so in the equations:** shell weights ∝ e^{S/k_B} and matched matrix elements in the detailed-balance ratio; equal treatment of the
one-jump and three-jump paths in the energy account (the chapter does say their dynamics differ).

**What a ledger would need, and what we already have.** The finite-entry sequence IS a staircase in the Volume II sense: ordered stages N → N − 1, each paying an exact
amount, the total telescoping, with a stop rule (the floor). Its "field" term is the energy (order-independent: one jump of three entries equals three jumps of one),
and its order-sensitive term is the step temperature (T_step differs between the paths while the total does not), which is the matter engine's lapse question in
another coat. The chapter's two entropy balances are storage questions in our exact form: with variable-temperature reservoirs the released entropy k_B(N_i − N_f)
cancels the horizon's loss exactly (eq. 41, a telescoping identity); with one fixed bath the balance ΔE/T_b − j k_B is of either sign and is zero exactly when
T_b = T_step (eq. 42). The depletion-feedback unit test (subtracting three copies of the first gap emits 3(2 − √3)E* ≠ E*) and the floor at N = 2 (allowed total
(2 − √2)E*) are declared-fail controls ready made.

## Chapter VIII — cosmic inventory and the Hubble cascade (pages 190–198)

**Declared quantities.** ĥ = 2, d̂ = 3; R = ĥ²d̂ = 12, Θ = ĥd̂² = 18, L = R² + Θ = 162, S = ĥ^d̂ = 8, M_count = (7/8)R² = 126, V = d̂³ = 27; A_0 = 1/(Rπ) = 1/(12π);
χ = (8/3)A_0 = 2/(9π); Ω_m = RA_0 = 1/π; Ω_b = 2A_0(1 − χ); Ω_c = Ω_m − Ω_b; Ω_Λ,ledger = 1 − Ω_m; η = (7/4)A_0^6; Ω_m,eff = RA_0 − 2A_0(χ + d̂χ²); the thermal
conversion n_γ = (2ζ(3)/π²)(k_B T_0/ħc)³, K = ρ_crit,100/(m_p n_γ), ω_b = η/K, h² = ω_b/Ω_b, H_0 ≈ 67.2504; d log H_0/d log A_0 = (5 + χ/(1 − χ))/2 ≈ 2.53806;
the nine-candidate set η = wA_0^p; the covariance examples; the flat ΛCDM age and z_acc.

**Bin (A):** the whole arithmetic chain and every sensitivity derivative; the container partition R² = Θ + M_count = 18 + 126 (each of the 144 units in exactly one
account: a one-use identity in integers, trivially true here).
**Bin (B):** Ω_m = 1/π as a density; the allocation (1 − χ); the exponent 6 and weight 7/4 in η; the clean/effective choice. The chapter says the expressions "were
selected within a discrete grammar after relevant target values were known" and that χ, containing π, "cannot be the ratio of two unweighted finite integer
cardinalities".
**Bin (C):** the measure that excludes exactly χ; "six independent stages with the same attenuation" that would make the exponent structural; the dynamical
interpretation of the complement (an equation of state).

**What a ledger would need.** The chapter's own prospective protocol (freeze the grammar, compute an untouched observable, report the whole residual vector) is the
verification form we now use, written in 2026 before we used it. Beyond that, the only run-shaped object is the hypothetical six-stage attenuation: a staircase of
six identical stages with retention A_0 per stage. Under a clock-type recipient such a product is order-blind by construction (the inertia identity), so the
question a run could ask is whether a lapse-type term exists for these stages at all, and nothing in the chapter supplies one. Thin.

## Chapter IX — thermal history, recombination and the microwave sky (pages 199–207)

**Declared quantities.** The seven-entry packet; A_s = η√R, n_s = 1 − χ/2, τ_rei = 2A_0; E²(a) = Ω_r a^{−4} + Ω_m a^{−3} + Ω_Λ,bg with Ω_Λ,bg = 1 − Ω_m − Ω_r;
Ω_r = Ω_γ(1 + 0.2271 N_eff); R_b = 3Ω_b a/(4Ω_γ); c_s = c/√(3(1 + R_b)); r_s, D_M, θ*, ℓ_A; the Peebles equation (10)–(11) with case-B rates and the C factor;
the matter-temperature equation; τ_γ(a), the visibility g_η = −(dτ/dη)e^{−τ}, ∫g dη = 1 − e^{−τ(η_i)}; the drag depth τ_d with r_d = r_s(a_d); the native receipt
CR001c@19 (z* = 1073.063, z_d = 1055.812, r_s = 143.299, D_M = 13532.742, 100θ* = 1.0589, ℓ_A = 296.683, r_d = 144.806 Mpc) against the distance-packet ruler
147.769 Mpc; the full-shape receipts CR037B/C; the corrected peak comparator (220, 535, 812) against (220.0, 537.5, 810.8); the analytic diagnostics: δr_s =
F(a*)δa* + ∫F(δ ln c_s − δ ln H), δ ln c_s = −(1/2)(R_b/(1 + R_b))δ ln R_b, the toy medium with τ = 4/3 at the visibility maximum, the blackbody heating
compatibility Ṫ/T = −H + Q/(4ρ) = −H + S/(3n), the two-residual covariance 2/(1 ± ρ), the Richardson test, δη* = −δg′/g″.

**Bin (A):** all the analytic diagnostics (standard, correct, exact in their premises) and the Friedmann/visibility bookkeeping.
**Bin (B):** the three perturbation selectors (the chapter: "seven amplitude selectors were examined"); the packet's proximity to the Planck posterior.
**Bin (C):** a converged recombination calculation (the atomic physics is inherited, the execution record was not supplied), one drag ruler, a governing
perturbation law.

**What a ledger would need, and what we already have.** Two things in this chapter are ledgers in our sense already. The visibility function is a one-use
distribution: every photon last-scatters at exactly one epoch, ∫g = 1 − e^{−τ_i}, and the chapter's insistence on publishing the whole g rather than its peak is
the same discipline as our per-cut vectors against a summed price. And the two rulers (photon decoupling weighted by n_e, baryon drag weighted by n_e/R_b) are two
receivers of one ionisation history, which is exactly tonight's RH lesson: the sign and size of a change can belong to the weighting, so declare the receiver
before reading the number. The 2% gap between 144.806 and 147.769 is a receiver question, not yet a physics question, and the chapter's four-calculation design
(native and reference recombination at each of two backgrounds) is a verification-form run waiting to be executed. Our own receipt CR001c@19 is the regression; the
toy medium (τ = 4/3) and the two change-of-variable checks are its unit tests.

## Chapter X — many-source accumulation and galaxy halos (pages 208–216)

**Declared quantities.** A_lift = Σ 2GM_i/(c²|x − x_i|); A_circ = 2V_c²/c² = −R∂_R A_lift; the spherical identity A_circ = 2GM(<r)/(c²r) (exterior shells lift but do
not pull); X = V_h²/V_bar², f_supp = X/(1 + X); X_∞ = (R − ĥ)Ω_m = 10/π, f_∞ = 10/(π + 10) = 0.76094; the SPARC receipts (median outer support fraction 0.760699 on
175 galaxies and 3,391 points; RMS 40.95 → 3.63 km/s with the clustered profile; binned median 3.12; mass-ratio medians 0.9983 and 0.99928 on 173 galaxies;
scatter 0.38 dex; permutation p = 1/1001 twice); SE of the median ≈ 0.0362 dex → 0.0152 in f; the median-inversion identity med(X_∞/X_i) = X_∞/med(X_i); the
exponential disk M_d(<R) and V_d² = 4πGΣ_0 R_d y²[I_0K_0 − I_1K_1] with q_d ≠ 1; ∂X/∂ϒ_d = −V_obs²D/B²; the positivity filter (1/4πGr²) d(rXV_bar²)/dr ≥ 0; the
local law M_h ∝ r^{1+q−p}; the worked profile X = X_∞ r/(r + b), ρ_h = 3X_∞M_b b/(4π(r + b)⁴), r_1/2 = b/(2^{1/3} − 1); the Hankel representation; the RAR
comparator with X ∼ √(g†/g_bar).

**Bin (A):** the spherical identity, the median-inversion identity (which shows the mass-placement medians of CR032/CR033 restate the support median and are not an
independent test of 173 masses: the chapter says so), the disk formulas, the positivity filter, the asymptotic incompatibility (a finite X_∞ gives a Keplerian
fall; an indefinitely flat curve with finite baryons needs X ∝ r).
**Bin (B):** X_∞ = 10/π ("proposed after the empirical plateau had been measured").
**Bin (C):** the radial organisation law. The chapter: "the radial dynamical law remains the decisive missing ingredient."

**What a ledger would need.** The chapter's "inference ledger" (velocities → residual → density → constituents → formation, each arrow adding assumptions) is a
transfer ledger with nothing yet to transfer; every computable statement is either standard disk mechanics or a filter on a law nobody has written. The one
structural lesson that does carry is, again, receiver dependence: the same photometric mass gives a different "support" under a spherical receiver and a disk
receiver (q_d ≠ 1), and the outer radius of observation weights the population. This is the chapter Sean Brady named as out of place, and the extraction agrees:
it is empirical phenomenology awaiting a transport law, and the SPARC comparison belongs to established-reference testing, which we are not doing. No ironclad run
until a candidate law exists.

## Chapter XI — carrier radiation and ringdown (pages 217–225)

**Declared quantities.** R² = 144 = 8Θ, L = 162 = 9Θ, M_count = 126 = 7Θ, S = 8 = d̂^{d̂−1} − 1, V = 27; ω̂_R = Θd̂/R² = 3/8; γ̂ = R/(L − V) = 12/135 = 4/45; Q =
ω_R/(2γ) = 135/64 = 2.109375 against the Schwarzschild ℓ = 2, n = 0 mode 0.37367168 − 0.08896232i (residuals +0.3555 %, −0.0825 %; Q ≈ 2.1002); the higher
candidate (L + ĥ)/L = 164/162; the ceiling E_GW ≤ E_C(0) ≤ E_0/8 under four reservoir premises, with the replenishment payment when premise 2 fails; the area-theorem
bound 1 − √(m_1² + m_2²)/(m_1 + m_2) → 0.2929; the catalog fractions (GW150914 0.0475 … GW200115 0.0038); the comparator flux identity ∂_t e + ∂_x j = J∂_tψ; the
QNM problem with the surface impedance ψ′/ψ = iω(R − 1)/(R + 1); the solvable surface Z_s = k_s − m_sω² − ib_sω, R_s = (iω + Z_s)/(iω − Z_s), |R_s|² and the
absorbed fraction A_s = 4b_sω²/((k_s − m_sω²)² + (1 + b_s)²ω²) ∈ [0, 1]; the pole equation iω = Z_s and the inverse design m_s = 45/4, b_s = 1, k_s =
m_s((3/8)² + (4/45)²) giving exactly 3/8 − 4i/45; the pulse energy B²π²/(2T); the template overlap 2√(γ_1γ_2)/√((γ_1 + γ_2)² + (ω_2 − ω_1)²) ≈ 0.999972
(mismatch 2.8e-5); the strain power with ∫sin⁴θ dΩ = 32π/15.

**Bin (A):** the count reductions, Q, the ceiling as a subtraction of nonnegative debits, the flux identity, the impedance algebra, the passivity bound, the pulse
and overlap integrals.
**Bin (B):** 3/8, 4/45, 1/8, 164/162 as physical frequencies and a physical energy fraction (the chapter: "the particular expression is not interchangeable with
these few neighbors" is all the control history shows; the inverse-designed oscillator "is not evidence that this oscillator is the SAM boundary").
**Bin (C):** the boundary law R(ω) (the SAME missing law as Chapter VII's), the count-to-energy map (why 18 of 144 labels carry 1/8 of the energy: a uniform
weighting assumption), the unit chart, spin, the weak-field luminosity.

**What a ledger would need, and what we already have.** The ceiling's premise set is a storage question in our exact form: E_C(0) = E_C(T) + E_GW + E_other + ΔE_store,
every debit once, nonnegative, with replenishment as the account that breaks the bound; the chapter's own words are that "the integrated source work still has to be
paid from the stated reservoir." And the QNM problem with a surface impedance is a well-posed computation whose answer constrains bin (C): the chapter proves the
half-line toy can be inverse-designed to the rationals, and asserts without computing that an exactly absorbing Schwarzschild exterior cannot make them exact.
What nobody has computed is the question in between: in the Regge–Wheeler exterior with a passive surface (|R| ≤ 1) at r_s(1 + ε), does any impedance of the
declared oscillator class place a pole at 3/8 − 4i/45, and if so at what ε and with what reflected fraction? That is a root search on a Wronskian, host arithmetic
at high precision, with the absorbing Schwarzschild mode as its regression. Its answer, either way, is a constraint on the one blank that Chapters VII and XI share.

## Chapter XII — cosmological fate and the completed boundary (pages 226–234)

**Declared quantities.** A_los(z) = (1/π)(1 − (1 + z)^{−3}), concave, limit 1/π, slope 3/π at zero; f(z) = 1 − A_los; dA/du = 3(1/π − A) with u = log(1 + z);
Ω_m* = 1/π, Ω_Λ* = (π − 1)/π; H∞ = H_0√Ω_Λ ≈ 55.525; H_fit,∞ = H_0Ω_Λ^{3/2} ≈ 0.562834H_0 ≈ 37.851; Ḋ_readout/D_readout = H − ḟ/f; the inferred rate (23) and
q_0,inferred = q_0 − 6/π; the duality ratio η_D = g_L/g_A; the Home recurrence E_{n+1} = E_n + I_n − O_n with 0 ≤ O_n ≤ E_n + I_n, the cumulative identity
E_N = E_0 + ΣI − ΣO and ΣO ≤ E_0 + ΣI, R_n ≥ R_form, N_n/N_form = (1 + E_n/M_form)²; the worked receipts (M_form = 10, E_0 = 2; (3,1) → 4; (0,3) → 1; (0,1) → 0;
cumulative output 5, floor never debited); the lossless transfer toy ρ_u ∝ a^{−3−λ}, ρ_H = a^{−3}[ρ_H0 + ρ_u0(1 − a^{−λ})], total dust unchanged; the radiative
fraction β with the exact check (1/128, 3/512, 1/1024; sum 15/1024 < 16/1024); the interacting-complement toy Q = 3ξHρ_X with a ∝ t^{2/(3ξ)}, H → 0, acceleration
for ξ < 2/3, event horizon iff ξ < 2/3; the entropy ledger s(BR) = H(p) + Σp_r s(ρ_r) and the mutual information.

**Bin (A):** every property of the road function; the recurrence's nonnegativity by induction and its cumulative identity ("ledger theorems"); the toy models' exact
solutions; q_0 − 6/π as the consequence of the uncompensated map.
**Bin (B):** A_los(∞) = Ω_m* as a physical join ("equal expectation values do not make those operations identical"); the re-indexing identity A_0 = A_H/(4πD).
**Bin (C):** the evolution law that would make 1/π an attractor (the chapter writes the toy dB/dN = λ(B* − B) and says it "does not derive it"); the exchange law Q;
the transition mechanism of the Home handoff.

**What a ledger would need, and what we already have.** The Home recurrence is our ledger form outright: receipts I_n, O_n each counted once, a frozen floor that is
never debited, and the storage inequality written as the bound on O_n. It is also the same object as Chapter VII's finite-entry staircase seen from the custody
side: VII gives the per-step payment O_n as a function of N (ΔE_j), XII gives the recurrence with inflow and the floor. Put together they are one staircase with two
accounts (energy and entropy) and a stop rule, and the question "does the release at this step cover the payment, and if not what remains unpaid" can be asked of it
exactly as it was asked of the RH transition. The transfer toys are the chapter's own demonstration that an inventory without an exchange law predicts no future; that
is a statement about bin (C) and needs no run.

## The ranking: low-lying fruit for ironclad, by what we would learn per hour

1. **The finite-entry staircase as a storage ledger (Chapters VII + XII; Duck idea run in the standard form).** Stages N → N − j with the exact payments ΔE_j; accounts:
   horizon entropy (−j k_B), reservoir or bath entropy, step temperature; the floor as stop rule; the replenishment I_n from XII's recurrence. Questions: where
   is the fixed-bath balance ΔE/T_b − j k_B positive, zero, negative across (N, j, T_b); whether the one-jump and multi-jump paths differ in any account other than
   the step temperature (the order question); whether the Catalan remainder bound is sharp at small N; whether XII's gross-emission-with-net-growth receipts can be
   driven by VII's payments with the floor respected. Controls ready made: the depletion-feedback error (3(2 − √3) ≠ 1) and the floor at N = 2. Exact rational and
   algebraic arithmetic, native-certifiable (products, square roots by SOLVE/EXP, logarithms), the staircase library's per-stage-state return reusable in shape.
   Cost: one evening. Learn: whether Volume I's own boundary staircase has the Volume II algebra (field-like total, lapse-like step temperature) or a different one.
   This is also the cleanest transfer-ledger entry between Volume I and Volume II yet seen.
2. **Reproduce the native recombination receipt in the verification form (Chapter IX).** Two separate host implementations of the hydrogen-only Peebles transport
   from the chapter's own equations (10)–(17) on the chapter's background, predictions first, both rulers, CR001c@19 as the regression (z* = 1073.063 …
   r_d = 144.806), the toy medium τ = 4/3 and the two change-of-variable checks as unit tests, Richardson refinement to a stated tolerance. Then the chapter's
   four-calculation design to locate the 2% ruler gap (receiver or construction). Cost: a day; host arithmetic (an ODE integrator is not a native operation, so
   this is a domain experiment with native witnesses on its algebraic identities). Learn: whether our own earlier receipt reproduces from the printed equations
   alone, as the RH price did, and what the two rulers measure. No external data enters until Sean Brady says so.
3. **The passive-surface quasinormal-mode question (Chapter XI, constraining the Chapter VII/XI shared blank).** Regge–Wheeler ℓ = 2 exterior, a surface at
   r_s(1 + ε) with the declared oscillator impedance, root search on the Wronskian, the absorbing Schwarzschild mode as regression; ask whether any passive surface
   puts a pole at 3/8 − 4i/45 and at what reflected fraction. Cost: one to two days; host arb. Learn: a constraint on the boundary law, which is the single blank that
   two chapters depend on. Established-reference testing (the catalog) stays out.
4. **Chapter VIII's six-stage attenuation and allocation measure.** Mathematics, not a run: what measure on the 144 containers excludes exactly 2/(9π), and whether
   six identical stages have any lapse-type account. Log as questions; no compute until a candidate measure exists.
5. **Chapter X.** No run until a radial organisation law exists. One afternoon's host question if wanted: does the RAR-type X ∼ √(g†/g_bar) pass the positivity filter
   against an exponential-disk V_bar at every radius, and where does it fail. Otherwise the chapter stays a labelled extension, which supports the placement options
   already logged (ideas, 2026-10-22).

## One lesson to carry into every chapter

Tonight's RH result (rh_transition_3, host-side) is that the sign of a change can belong to the receiver's weights, not to the transition: the admitted energy rose at
the five smallest cuts and fell at 154 of the rest, so near-uniform weights read a rise and growing weights read a fall three hundred times larger. Chapters IX
(photon ruler against drag ruler), X (spherical against disk receiver; outer-radius weighting of the population), XI (count weights assumed equal to energy weights)
and VIII (unweighted containers against a π-measure) each contain the same unstated step. The first line of any chart extracted from these chapters should be its
weights.
