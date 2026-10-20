# Test record: feedback clock definition and offline nonzero-history test, 2026-10-20

**Kind:** engineering test in the sandbox lane (EXPLORATORY; no claim; the installed core 0.11.0 is unchanged).
**Where:** ironclad branch `sandbox/feedback-lapse-20261020`, folder `sandbox/feedback_lapse_20261020/` (FEEDBACK_LAPSE_DEFINITION.md, PROTOTYPE_feedback.diff,
RESULTS.md, offline_execute.py, params_*.json, out/ with SHA manifest).

**Direction (Sean Brady):** after withdrawing a rollback of the Volume I pair: "I need a precise definition connecting lapse, event count, elapsed time and
the feedback evolution time. A nonzero-history test demonstrating the intended effect of changing lapse. Simply replacing zero events with one is not
enough: the propagator uses a separately supplied time. Side-by-side regression checks against 0.10.2 for unchanged feedback and reservoir inputs."

**Definition (proposed, conventions labelled):** N = dτ/dt the source's metric lapse; ΔN source events per interval; χ = coordinate time per event
(1/N when derived); elapsed_i = ΔN_i·χ_i; event times t_k cumulative; end = t_last + ΔN_f·χ_f; the feedback propagator is exp(G·end) with end taken by
native pointer from the coefficient word, the source block of G scaled by N, the field block unscaled. Two conventions for Sean Brady's decision: the
direction of the lapse (χ = 1/N vs N) and whether N scales the source block.

**Test (sandbox prototype, executed natively offline through the core's own adapter):** at the same end time 1/2, N = 1, 4/5 and 16/25 give pairwise
disjoint states (exact enclosures of width 4e-48, differences of order 1e-2); N = 1 routed through a one-event and a three-interval history reproduces the
sealed 0.10.2 result exactly; the uncoupled source at N = 4/5 equals 0.10.2 at time N·end exactly (cos 2/5, −sin 2/5); the energy identity residual is
exactly zero in every case; five malformed inputs are refused at compile time.

**Regression (unchanged inputs):** feedback seed 0.10.2 vs 0.11.0: 16/16 readouts and 18/18 DAG steps identical. Reservoir αt = 1/4: 14/14 shared readouts
and 18/18 shared steps identical; 0.11.0 adds four steps and the local_metric_clock readout. Prototype on the legacy chart: 18/18 steps identical, 15/16
readouts identical (the contract text differs; a one-line choice).

**Not done:** no release. A 0.11.1 needs Sean Brady's decision on the two conventions and "Allow permanent changes".

Directed by Sean Brady. Executed with Claude Code.
