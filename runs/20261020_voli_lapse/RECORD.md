# Run record: voli_lapse (the two clock readings on the new constructions), 2026-10-20

**Kind:** research run on the installed Duck 2.3.0 / core 0.11.0 (no claim; no verdict on any volume).
**Where:** ironclad `campaigns/voli_lapse_20261020/` (RUN_REPORT.md, LIVE_CAPTURE.md, peers' records, results/); history entry H002745; run folder
`runs/duck/voli_lapse` (out of git, manifest committed).

**Direction and correction (Sean Brady):** "Run the Volume I follow-up with the new constructions." The lead framed the target as an examination of the
manuscript's lapse against Gravity Probe A with pre-registered pass/fail rows. Sean Brady retired that framing during the window: "We are done binding
these runs to manuscript/volume, again we are not 'testing' volume I we are trying to learn and this is not the way." and "That is the material we should
be following up on, not 'finding manuscript material to test'." Standing rule from here: targets are open questions on the material the runs themselves
produce; peers generate; all outcomes triaged; no exam, no external key.

**Outcome:** 148 returns, 142 COMPLETED, 4 REFUSED_AS_DECLARED, 1 FAILED_AS_DECLARED, 1 COMPLETED_AGAINST_DECLARATION (a declared singular-solve control
that the engine reports as completed-unresolved); finalization FAILED_WITH_RETAINED_OUTCOMES by that one declaration mismatch; no computation broke.

**What was learned (readings of the constructions, engineering register):**
- On a declared profile the coordinate reading's ratio minus one equals (a_e − a_r)/q_e exactly, and the kinetic reading's first-order coefficient is
  1/(2q_e) with second-order remainder 3a²/8. In a two-clock geometry the coefficients per Δa are 0.5000000004 and 1.0000000005.
- The time chart (reservoir) and the static chart (profile) carry the same q and the same a = tanh² within 10⁻⁴⁷ in both readings; the two reservoir lapses
  satisfy N_kin² = N_coord and are identical across clock species; an authored recipe separates them.
- The floor A₀ = 1/(12π) named in the text was bracketed natively; a profile shifted by it has kinetic coefficient 1/(2(1 − A₀)) = 0.513623; rescaling the
  map moves the excess from the redshift ratio into the light-path delay.
- A map-independent ratio of light-path excess to redshift: 1 for the coordinate reading, tending to 2 for the kinetic reading; second-order dependence
  on which radius the map uses.
- **Defect in core 0.11.0, found by two peers independently:** the feedback `lapse_source` option records the lapse but does not change any dynamics,
  because the history step carrying it has zero events and is never executed. Listed for the next release.

**Openings the peers named:** a feedback whose history step runs with nonzero events; a native √q route in the reservoir; an exact chart meeting with
algebraic rapidity; a profile taking a declared γ in the light index; whether the floor belongs in the light path; controls that report breaks by sign
rather than declared FAILED.

**State at close of session:** the next campaign, `explore_voli_threads_20261020` (exploration from Sean Brady's pasted material produced by the earlier
runs; no test, no key), is staged, prepared and committed but NOT deployed, at Sean Brady's direction to stop for the night.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run voli_lapse, IRONCLAD-R27).
