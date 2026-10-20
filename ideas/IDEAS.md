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
