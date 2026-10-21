# Release record: core 0.11.2 / Duck 2.3.2 / IRONCLAD-R29, the ordered feedback clock, 2026-10-21

**Kind:** permanent installed-version change (CLAUDE.md §13). Sean Brady: "Proceed with item 2", then "Leave it declared - Allow permanent changes", then "readback approved".
**Where:** ironclad main 3884cce (tag duck-2.3.2), history entry H002753, plan docs/CORE_0_11_2_PLAN.md, definition and offline matrix on branch
sandbox/feedback-ordered-20261021, fixture qualification/fixtures/feedback_ordered (PREREGISTRATION.json, OFFLINE_PRECHECK.json, RUN_CHECK.json), run
runs/duck/ironclad-r29-feedback-ordered.

**What changed.** The feedback construction can now take one metric lapse per event. A native event-clock word computes the elapsed field time per event
as ticks divided by the lapse and certifies that its end equals the common-action end. The propagator is the path-ordered product of one exponential per
event acting on the full state, so the field coordinate is carried between events. An optional initial field coordinate lets a chain of constructions
continue a field. Per event the construction certifies the energy identity and the inertia identity (an interval at lapse N over field time ΔN/N equals the
flat chart at inertia N·Γ over the tick count ΔN) and emits N·Γ as the readout inertia_scale. Without the new keys the legacy and 0.11.1 charts are
byte-identical. Three directories unchanged: the sealed 0.10.2, 0.11.0 and 0.11.1.

**Decision by Sean Brady (labelled):** Γ stays declared through κ. The construction makes explicit that the state depends on N and Γ only through N·Γ;
separating them needs an observable outside the contract (candidates logged as open ideas).

**Evidence.** Tests 156 OK before, 162 OK after; verify PASS at IRONCLAD-R29 / 2.3.2 / 0.11.2; offline matrix: regression byte-identical, path-order gaps
equal to the peers' hand-built products (kinetic 1.4635e-3, coordinate 4.031e-3), reversal invariant from rest equal to 1e-47, all certificates zero;
pre-registered Duck fixture COMPLETE with every relation holding (legacy and routed equal the 0.11.1 references exactly; ordered single event equals routed
exactly; two orders disjoint with equal end and equal h_end; initial field 1/5 gives source energy 8/25; three controls refused as declared). Rollback to
duck-2.3.1 verified before install. Independence: none (§8).

**What this opens for the volumes.** Paths of lapses (radar out-and-back, deeper-first vs shallower-first) are now one native construction with the domain
check kept; the reversal law recipes become regression checks; a Volume I run can carry a declared profile's lapses event by event.

Directed by Sean Brady. Executed with Claude Code.
