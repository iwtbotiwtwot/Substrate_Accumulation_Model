# Ideas (status: open / adopted / dropped; only Sean Brady changes a status)

The ironclad repository keeps its own `sandbox/IDEAS.md` for instrument ideas. This file holds ideas that bear on the volumes.

## 2026-10-19 — Map the manuscript's accumulation a to the chart's q (proposed by Claude; from ironclad run peer_restore_next) — open

The GEN6 charts certify Ξ density ∝ 1/q and c_eff = c₀q. Volume I's teeth law is (1−a)^(−k) with γ = 2k and Cassini needing
k = 0.50001. With 1−a = q the chart gives k = 1 (γ = 2); with 1−a = q² it gives k = 1/2 (γ = 1). The identification a(q) is a
computation, not a convention: the manuscript's a and the source clock's A_los against q on one construction. Recommended next.

## 2026-10-19 — The ruler reads a path mean of 1/q (from CLOCK's teeth-per-tick method) — open

Teeth per elapsed tick is ν₀ on every clock; teeth per internal tick is ν₀⟨1/q⟩ over the path. Chapter IV's delay would then
be the path average of 1/q, not an endpoint value.

## 2026-10-19 — Tick from source and road, ledger from the interface (JOINT, PROPAGATION) — open

Clock rate depends on E_s/η and the delay only; the energy split depends on εg²Wp². A statement for Chapters IV–V.

## 2026-10-19 — Accumulation depth as an additive rapidity (RULER) — open

Compositions of depth obey the tanh addition law; Ξ ∝ cosh² composes as γ² of a rapidity sum. A presentation for Chapter II.

## 2026-10-19 — A resting-clock comparison across two depths decides γ (from run aq_identification; all four peers) — open

The charts' light quantities fit two readings of the lapse: √q (giving a = 1 − q, γ = 1/(1 − a), PPN γ = 1) and q (γ = 0).
Two resting clocks at different depths exchanging teeth give a received ratio √(q_e/q_r) under the first and q_e/q_r under the
second. No construction has compared resting clocks; the unused `reception` construction is the candidate. Recommended next.

## 2026-10-19 — Status note on "Map the manuscript's a to q": the identification a = 1 − q is now the peers' converged reading (three of four), with the lapse fork open; the earlier worry about k = 1 versus k = ½ dissolves because γ runs as 1/(1 − a) with PPN value exactly 1 — status unchanged (open) pending Sean's word.

## 2026-10-19 — Recommended model per role (lead's recommendation after the comparison) — open

Peers: Opus by default (matched Fable on every instrument number in aq_identification); Fable for a run the owner wants the
strongest minds on; mechanical peers and conversions: Sonnet; watchers: shell loops. Making this a field of the Duck 2.0
method document is a permanent change and awaits "Allow permanent changes".

## 2026-10-19 — Status note on the resting-clock decider: run `resting_clock` (H002733) could not decide; both ratios are exact rows of every exchange; every certified rate runs at q. The decider now needs two constructions (below). Status unchanged (open) pending Sean's word.

## 2026-10-19 — A static, spatially varying accumulation profile Λ(x) with two positions (all four peers of resting_clock) — open

The reservoir is homogeneous (J = V = 0, no position); the returning field has one source; reception binds one state against a
clockless reference. A reservoir with a source term J(x), two positions, and a light path whose delay integrates 1/c_eff along it
would make redshift and Shapiro delay two readings of one q(x). A new construction in the vendored library: permanent change.

## 2026-10-19 — Derive the local metric clock instead of supplying the lapse (RULER, PROPAGATION, JOINT) — open

`common_action.py` marks `local_metric_clock` OPEN and names "redshift-to-Ξ density" among its unknowns; feedback forces the lapse
to 1. Candidate: the kinetic-metric phase rate e^(Λ/2)ψ̇ = 2E₀√q against the coordinate phase rate 2E₀q, as a pre-registered test
that fails one way or the other. Permanent change.

## 2026-10-20 — Full-observable-distribution control as a method note for Volume II's spin-memory chapter (from the abandoned Codex run spin_memory; lead's triage) — open

Matching only one visible port manufactures spurious hidden memory; matching the whole present visible distribution (16
ports) is necessary, shown exactly on a decoupled null source (exact rank 1). A tool the chapter could use once SAM's own
frustrated-spin source is the operand; that transfer needs a source-derived three-time tensor and controlled Hamiltonians.

## 2026-10-20 — from feop_bound_c02 (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Depth-uniform two-sided bracket** for the fixed-z count: S_g ∈ X∏d_p(k) ± envelope for any k ≤ g, uniform in g, L, A; write the
  derivation and check the superset step and the k-class count pointwise natively. (BOUND) — open
- **Ultrametric tree formula** 1 − D(L) = (1/(p+1)) Σ_j max(0, p^(−σ_j) − p^(−2L)) for any even-valuation tuple; proof or break with a
  verifier separate from the emitter. (LOCAL) — open
- **Sparse-digit families** (base-p⁴ binary digits): bounded density with polynomial diameter; run through the Legendre count and
  the two-sided bracket (TARGET item 2). (LOCAL, REVIEW) — open
- **True remainder size**: observed max |E| grows roughly like T, not (1+T)^π(z); certify a full-period worst case as a receipt.
  (CRT) — open
- **Restate C02** as fixed-z Legendre plus depth truncation, then ask what is left of C01/C02; the FEOP question proper begins when z
  grows with X. (REVIEW) — open
- **Literature**: get Halberstam–Richert (Selberg Λ², level of distribution) into the retrieval index before any write-up. — open

## 2026-10-20 — from feop_bound_c02_rerun (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Exact Selberg remainder in C02's frame**: replace the coarse 324/576 constant by B_z(g) = Σ|γ_m|T^ω(m) (leading constant ≈1.44 / 3.27);
  gate the signs of γ_m natively. (BOUND) — open
- **Roster as a free parameter**: build the best-roster curve against g natively; the ≤14 roster already beats C02's and Legendre at g=16..19. (BOUND, REVIEW) — open
- **Put run 1's depth-uniform bracket and the rerun's exact remainder side by side natively**; neither recurred in the other run. (lead) — open
- **Measured interval discrepancy instead of T^ω(m)**: the observed worst case sits 3× to 50× below the cylinder count. (CRT, LOCAL, REVIEW) — open
- **Growing z with X**: the only setting where capping the Selberg support is needed and where a statement beyond the standard fixed-level sieve could sit. (CRT, BOUND) — open
- **Procedure**: peers keep host generators under peers/<NAME>/gen/ (shared scratchpad collisions); lead's live capture outside what peers read. — open

## 2026-10-20 — from feop_bound_c02_run3 (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Exact remainder polynomial** 4T³+19T²+12T+1 (z=7), 14T³+34T²+15T+1 (z=11) in place of 9|D|²T³; restate C02 with it and compare at equal X
  with the two-sided Legendre count using the measured remainder. (CRT, BOUND) — open
- **Form of the measured joint discrepancy**: not additive across primes (refuted), not linear in T; candidates ∏(1+D_p) − 1 or k·max D_p,
  tested exactly at 3–4 primes. (CRT) — open
- **Minimal diameter of tuples with the nested per-prime structure**: is max_p p^(2(g−1)) a lower bound? exhaustive search at small g. (REVIEW, LOCAL) — open
- **Frontier correction made exact in a native recipe**: D_g(L) − D_g(∞) = g/((p+1)p^(2L)) for L ≥ g. (LOCAL) — open
- **Design point D5 (program)**: let a task declare an expected FAILED so negative-control recipes do not relabel the run. — open, Sean Brady's decision

## 2026-10-20 — from feop_sidebyside (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Run 1's depth-uniform bracket**: now with native receipts for its two steps on small cases and located hypotheses; next is coverage
  past the 64-row word limit (fibered layout or authored recipe) so p = 11 and k ≥ 2 get receipts. — open
- **Hybrid envelope**: min over k of the bracket upper and the truncated exact-remainder Selberg upper, paired with the sharpened lower. (COMPARE, BRACKET) — open
- **Step (b) for general even-separated tuples** (count distinct offsets mod p^(2k) instead of k), needed for the small-diameter families. (REVIEW) — open
- **A lower side that survives growing z** (inclusion–exclusion over primes instead of a union bound). (REVIEW) — open
- **Program limit**: the source-word 64×64 matrix bound is the binding constraint on native coverage; raising it is a permanent-change
  candidate for Sean Brady's decision. — open
- **Documentation**: source-word payload contract added to the authoring guide (done 2026-10-20). — adopted (documentation fix, Tier 1)

## 2026-10-20 — from feop_bracket_fiber (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Receipt per cylinder level** for the bracket's steps: a transfer operator (about g × p²) checked natively on reached levels and iterated,
  O(k) numbers per case instead of p^(2k) residues; the only visible route to k = 6..24. (FIBER, ELEVEN, REVIEW) — open
- **Bind the partition into the recipe gate**: coverage and first-moment residuals as zero checks, selectors fixed to whole single-case words,
  offsets recomputed from (p, g, k, L). (REVIEW, RECIPE) — open
- **Partition step in every summing word** (row coverage as one extra step). (REVIEW) — open
- **Cost curve**: p=7 k=3 (about 205 words) and p=11 k=2 L=4 by a two-level summing tree in a longer window. (FIBER) — open
- **Engine release for the 64×64 limit**: downgraded from a reach item to a convenience item by this run. — open, Sean Brady's decision

## 2026-10-20 — after core 0.11.0 (proposed by Claude; status open; only Sean Brady changes a status)
- **Volume I follow-up run (the one the constructions were built for):** a pre-registered peer run that puts the two readings of a declared
  profile (q_r/q_e and √(q_r/q_e)) and the reservoir's two lapses beside the manuscript's N = √(1 − a) and the retired raw-lapse control
  √(1 − A₀ − a), with the Gravity Probe A first-order coefficient as the external answer key (the closing section's table). — open
- **Derived profile:** a reservoir with a source term J(x) so that q(x) is derived rather than declared; the static_profile construction then
  becomes its reading layer. — open
- **Derived lapse carried into the field:** feedback with lapse_source derived from a reservoir readout by reference (the readout is an enclosure;
  the construction takes an exact rational, so an exact q from a declared profile is the current route). — open
- **Update the 2.0 method document's §6:** three of the seven listed defects remain outside the Duck (per-stroke trace time: core; recipe scalar
  inputs: SLC engine). — open

## 2026-10-20 — from voli_lapse (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Fix the feedback lapse (program defect, core 0.11.0):** make the history step run with nonzero events so lapse_source reaches τ and elapsed time; today it is a label. — open, next release
- **Native √q in the reservoir** (exp(−Λ/2)) so the kinetic lapse is computed, not read as sech. — open
- **Exact chart meeting:** algebraic or enclosure-valued rapidity in the profile. — open
- **Profile with a declared γ in the light index**, so the light-path row becomes a scan. — open
- **Does the floor A₀ belong in the light path?** The two readings' light-path ratio depends on it. — open
- **Controls by sign, not declared FAILED:** singular solves and ranks return "unresolved", not FAILED; the declared-control rule should accept a sign/rank report. — open
- **Next material (Sean Brady's paste):** explore from the a(q) identification, the resting-clock fork and the spin-memory results (hidden history in the
  64-state system; the four-state work advantage with preparation, measurement, erasure and reset outside the account). Campaign `explore_voli_threads_20261020` staged. — open
- **Feedback clock definition and routed-clock prototype (2026-10-20, proposed by Claude at Sean Brady's request):** end = Σ ΔN·χ reaches the propagator by native pointer; source block scaled by N. Prototype and test matrix on ironclad branch sandbox/feedback-lapse-20261020. Decisions taken by Sean Brady 2026-10-20: χ = 1/N, N scales the source block; installed as core 0.11.1 / Duck 2.3.1 (H002746). — adopted

## 2026-10-20 — from explore_voli_threads_2 (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Per-event derived lapse with a path-ordered propagator** (feedback history N_i per event, field state carried between events, domain check kept): the 0.11.1 clock collapses a history to its end; order matters on receipts. — open, construction candidate
- **A construction that derives Γ (field inertia)** from the source or the profile: in the present constructions a lapse is exactly κ → N·κ, so the q vs √q fork is a free choice of inertia per tick until Γ is derived. — open
- **Kinetic-reading light path** (c₀·√q beside c₀·q) in static_profile, or a derivation of the c₀·q convention. — open
- **Inertia identity as an enforced recipe** (entry-by-entry check). — open
- **History policy at separation ≈ 2**, where the decision-bit information peaks; does the achieved gain follow the ceiling? — open
- **Field-strength control per branch** (dwell alone cannot reach the j = 0 information). — open
- **Reset stroke and repeated cycles with the register reused**; the register ledger on the 64-state source once a control Hamiltonian is declared. — open
- **Matched-present test on the order-dependent field state** (same present ticks, different field memory). — open

## 2026-10-20 — from spin_work_1 (proposed by Claude peers; status open; only Sean Brady changes a status)
- **Finite-dwell staircase** with a hidden-spin field: how much of the 0.79 share of the hidden information survives finite time; compare the two schedules (visible then hidden vs both together). — open
- **Price the record at the staircase optimum** natively at separations 1/2, 1, 2, 4; reuse the j = 1 record over repeated cycles against a per-cycle cost. — open
- **Dwell plus hidden field at separation 1/4**: is the short-separation dwell gain the finite-dwell part of the hidden-field route? — open
- **The hidden-field stroke on one hidden port of the 64-state source** (a concrete control Hamiltonian); the visible-field staircase there needs only stationary weights of declared generators. — open
- **A source with more than two earlier values**, to test whether a coarse record keeps the gain. — open
- **Is a field on an unobserved spin an admissible control?** (the hidden-field family's premise.) — open
- **Recipes with interval_contains checks enforcing the gain signs**, so the separation trend becomes a checked result. — open
- **Benchmark families**: any future history-vs-current-only comparison must give both the same control family (strength, stages, hidden field); the earlier 0.00023 did not. — open (method)

## 2026-10-20 — Sean Brady: "Why am I thinking of the RH program reading these results?" (idea, logged at his word "just log it")
The spin results have an RH shape: an ordered past entering a present quantity through a kernel (reciprocal history ↔ hidden-history memory; path-order dependence of the field ↔ the ordered switching ledger); the staircase share of the ceiling (0.45, 0.65, 0.79 → 1 in the quasistatic limit) as a nested recurrence with a complete remainder, the FEOP form; the same sign-bracketing instrument; novelty dissolved in both by widening the comparison family (Selberg sieve; benchmark family); the 64 wall (matrix limit; 64-state control Hamiltonian). Concrete check proposed by Claude: write the staircase gain as a function of stage count with its remainder to I(i;h|j) and test whether the remainder has the FEOP recurrence structure. Low confidence it connects; cheap to find out. — open; **run 2026-10-21 (rh_crossover_1, H002751):** the remainder does have the exact-recurrence-plus-remainder form on both sides (double/simple roots by hard/soft start, p⁻² on the diagonal), but the ratios come from quadrature order on the spin and field sides and from the residue tree on the RH side; the peers call the match a coincidence until one construction makes the level and the refinement the same object. Status unchanged: open

## 2026-10-20 — from spin_work_2 (proposed by Claude peers; status open)
- **Share of I against total time** for 2, 3, 4 free stages, both policies re-optimised at every dwell, each chain inside one recipe DAG. — open
- **Records chosen for correlation with the hidden part**, not completeness (64-state: port 0 carries 68 % of the ceiling at a quarter of the price); noisy or coarse records to raise ceiling/floor above 6 %. — open
- **A hidden-field stroke on one hidden port of the 64-state source**, priced against its ~5e-4 ceiling. — open
- **A repeated-cycle family** that reuses j as the next cycle's i. — open
- **Program note:** the Duck's run-wide queue bound (64 queued-or-running) should be in every briefing; a per-peer in-flight cap is the peers' discipline. — open (method)

## 2026-10-21 — from voli_threads_3 (proposed by Claude peers; status open)
- **A feedback construction with an initial field coordinate, or one lapse per event carrying the field state** with the domain check kept; the reversal recipe as its regression check. — open, construction candidate
- **A readout that fixes N·Γ separately from N** (from the reservoir's E₀ and α): the only route to deriving Γ the runs can see. — open
- **A bracketed twin in the reservoir chart** (sech²(αt′) = sech(αt)) as the observable that ties a to the source and could separate the two readings. — open
- **A kinetic light-index option in static_profile** for general rational u; a radiated-energy or phase readout telling a radar palindrome from its sorted rearrangement; how the symmetry matrix relates to the energy identity. — open

## 2026-10-21 — from rh_crossover_1 (proposed by Claude peers; status open)
- **One construction in which residue-tree levels and staircase stages are the same object**; until then the p⁻² / (refinement)⁻² match is a coincidence. — open
- **Matched end fields** (add the s·s_h direction or re-match actions per n) so the quasistatic limit is exactly I, then split I − gain(n) into mismatch and quadrature. — open
- **A kernel not of |t − s| alone** (the lapse-scaled source of core 0.11.1) as the only kind that could keep a path-order gap in the switching work. — open
- **Closed forms as recipes**: the g·4⁻ᵍ amplitude; the (l+1)/6 constants and the closed-cycle/open-ramp match across kernel degrees. — open
- **Program notes:** 64 operators per word; GEN5 entropy routes take exact probabilities only. — open (method)

## 2026-10-21 — from spin_work_3 (proposed by Claude peers; status open)
- **One recipe DAG per staircase** (generators, maps, states, contraction, witness), then the full total-time-8 set for 1–4 stages natively with the 3-vs-2 and 4-vs-3 witnesses that nesting does not decide. — open (method, first for the next spin run)
- **Free unequal dwell per stage at fixed total time** (a family that nests properly): where should the dwell go? — open
- **How each n-stage finite-dwell curve closes the gap to its stationary value**; a real optimiser through the exact maps. — open
- **A runnable protocol combining geodesic spacing with end half-steps**, priced by forward work only; a native thermodynamic-length recipe; geodesic schedules inside the history/current-only gain; whether the symmetric-1/n / asymmetric-1/n² split survives finite dwell. — open
- **The flag record**: a → 1 share in closed form as a ratio of two relative entropies; the channel (a, b) optimum per separation; the flag record on the 64-state source; a staircase driven by the flag record. — open
- **Program note (D5):** the three declared controls carried their status this run; the six undeclared failures were first attempts against an exact-zero-eigenvalue log trace. A support-only trace is the workaround; worth a line in the authoring guide. — open (method)

## 2026-10-21 — Ordered feedback clock: definition and prototype (proposed by Claude at Sean Brady's "Proceed with item 2"; status open; only Sean Brady changes a status)
One metric lapse per event (`metric_lapse` N_i), chi_i = 1/N_i and elapsed_i natively in an event-clock word, the propagator as the path-ordered product of one exponential per event acting on the full (z, p, a) state so the field is carried between events, an optional initial field coordinate a(0), the domain check kept, and per event two native certificates: the energy identity and the inertia identity G(N_i, Γ)·elapsed_i = G(1, N_i·Γ)·ΔN_i, with N_i·Γ emitted as the readout `inertia_scale`. Legacy and 0.11.1 charts byte-identical. Offline matrix on ironclad branch `sandbox/feedback-ordered-20261021` (`sandbox/feedback_ordered_20261021/FEEDBACK_ORDERED_DEFINITION.md`, `RESULTS.md`): path order reproduces the peers' hand-built gaps (kinetic z gap 1.4635e-3, coordinate 4.031e-3), the reversal invariant h_end from rest holds to 1e-47 on both readings, all certificates zero. **Γ is not derived**: the state depends on N and Γ only through N·Γ and on time through the tick count; separating them needs an observable outside the contract (reservoir η = E₀/(2α²) as a field inertia replacing κ; a radiated-energy ledger per proper time; the bracketed twin). Decisions taken by Sean Brady 2026-10-21: Γ stays declared ("Leave it declared - Allow permanent changes", "readback approved"); installed as core 0.11.2 / Duck 2.3.2 / IRONCLAD-R29 (H002753). The three Γ candidates stay open ideas. — adopted
