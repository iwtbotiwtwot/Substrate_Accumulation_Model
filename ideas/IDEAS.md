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
- **Feedback clock definition and routed-clock prototype (2026-10-20, proposed by Claude at Sean Brady's request):** end = Σ ΔN·χ reaches the propagator by native pointer; source block scaled by N. Prototype and test matrix on ironclad branch sandbox/feedback-lapse-20261020. Decisions pending: direction of the lapse (χ = 1/N), N-scaling of the source block, release as core 0.11.1. — open
