# Release record: core 0.11.0 / Duck 2.3.0 / IRONCLAD-R27, the Volume I pair (PERMANENT), 2026-10-20

**Kind:** program release (engineering; constructions added, no scientific claim; no reading of the clock fork chosen).
**Where:** ironclad `docs/CORE_0_11_PLAN.md` (readback), `docs/DUCK_2.3_ROLLBACK_CHECK.json`, `docs/DUCK_2.3_FREEZE.json`, history entry
H002744, tag `duck-2.3.0`, tests `tests/test_core_0_11.py`, fixtures `qualification/fixtures/static_profile` and `metric_clock`.

**Direction (Sean Brady):** "Allow permanent changes, do the five Duck-layer defects as one release followed by the volume i pair readback
approved." The pair, named by all four peers of the resting-clock run (2026-10-19): a static, spatially varying accumulation profile with
two positions, and a derived local metric clock in place of a hand-supplied lapse.

**How the sealed core was respected:** core 0.10.2 stays byte-identical in `active_core/` (checked against the 2.0.1 freeze); core 0.11.0 is a
copy in `core_0_11_0/` with the additions; the Duck's core manifest points to it with this entry as authority.

**What was added (core 0.11.0):**
1. `static_profile`: a declared profile at two or more positions, each by a rational rapidity u with q = 1 − u², a = u², Λ = −log q computed
   natively; both two-position readings, the coordinate ratio q_r/q_e (exact) and the kinetic-metric ratio √(q_r/q_e) (native enclosure), with
   their identity; the exact first-order identity q_r/q_e − 1 = (a_e − a_r)/q_e; and the light-path delay Σ ℓ_j/(c₀ q_j) with c_eff = c₀ q
   along a piecewise path, with its excess over the flat path. It derives no profile and chooses no reading.
2. The reservoir's `local_metric_clock` readout: candidate lapses q and √q from the same native trajectory, their phase rates and the identity
   N_kin² − N_coord. The action's readout stays OPEN and points to it.
3. Feedback `lapse_source` (declared, derived_kinetic, derived_coordinate), recorded in the program's source binding; a `common_clock` block on
   a feedback is now refused with a message instead of silently dropped.
4. Duck layer: the construction wired; a declared control may also expect REFUSED (found necessary by the fixture).

**Checks:** suite OK (151); verify PASS on IRONCLAD-R27 / Duck 2.3.0 / core 0.11.0; rollback to Duck 2.2.0 verified before install. Fixtures
pre-registered before execution: static profile, every exact column as written (ratio 5/4, first-order identity 0, delay 97/15, excess 7/15;
equal-position control ratio 1); metric clock, reservoir readout present, feedback lapses recorded as declared and derived, common-clock control
refused with the message. Two first attempts recorded plainly: a readout-status rule of the adapter refused the first profile run (fixed), and
the metric-clock control's first declaration said FAILED where the engine labels a rejected packet REFUSED (fixture amended, rule extended).

**What this does not decide:** which lapse is a resting clock's proper time. Both readings now exist on receipts for a pre-registered Volume I
comparison against the manuscript's N = √(1 − a) and the raw-lapse control the closing section retires. That run is the next Volume I step.

Directed by Sean Brady. Executed with Claude Code.
