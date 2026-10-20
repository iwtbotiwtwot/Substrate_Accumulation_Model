# Run record: feop_bound_c02_run3 (third replicate, on the installed Duck 2.0.1), 2026-10-20

**Kind:** research run, replication and regression check of the installed version (no scientific claim; BOUND_C02 stays CANDIDATE).
**Where:** ironclad `campaigns/feop_bound_c02_20261020/run3/` (RUN3_RUN_REPORT.md with the three-run comparison, PREREGISTRATION.json
amendment 4, peers' NOTES/REPORT/tasks/gen, results/RESULT_LEDGER.json, results/RUN_SHA256_MANIFEST.json) and
`campaigns/feop_bound_c02_20261020/RUN3_LIVE_CAPTURE.md`; history entry H002740; run folder `runs/duck/feop_bound_c02_run3` (169 MB,
out of git, manifest committed); branch `feop-run3`.
**Program:** installed Duck 2.0.1 / IRONCLAD-R23, no temporary change. Worktree of main with the records of runs 1 and 2 removed;
handle references removed from the peers' guides (documented deviation: handles do not exist on 2.0.1).

**Direction (Sean Brady):** "We should do the exact same run as 2 and 3 with the reverted version 2.0.1 to make sure it doesn't
outperform the temp changes. Thoughts?" then "go". Framed, with Sean Brady's agreement, as a regression check of the installed
version and a third replicate for the recurrence table, not as a performance comparison (run-to-run spread exceeds any code effect).

**Outcome:** finalization FAILED_WITH_RETAINED_OUTCOMES: 61 returns, 60 COMPLETED, 1 FAILED, the FAILED being BOUND's negative
control recipe that was declared in advance to fail and did. The lifecycle label cannot distinguish an intended failure from a defect
(design point D5, for Sean Brady). Nothing in the run is a defect.

**Regression answer:** the installed 2.0.1 ran the whole peer recipe: peer-authored submissions, cross-controller references with
causality recorded, three authored recipes admitted, compiled and executed with every check passed, exact sign combines, retrievals.
No peer asked for the handle. The temporary change bought nothing this campaign needed.

**Three-run comparison (engineering register):**
- Forced by the seeds (3 of 3): the closed local theory; C02 as the fixed-z Selberg sieve whose full roster is Legendre, with the
  main-term gap 0.3496 vs 0.2879 at z=7.
- Recurred (2 of 3): the exact Selberg remainder, about 1.44 against C02's 324 at z=7, reproduced to four digits by a different peer
  on a different version, and its crossover against Legendre near g=19 (z=7) / 24 (z=11); interval identities; constructive
  smaller-diameter tuples (two constructions, both a constant factor only).
- Single-run: run 1's depth-uniform two-sided bracket and ultrametric tree formula; run 2's roster curve.
- Negative result from run 3: CRT's additive-discrepancy idea refuted on 22 of 22 exact rows.

**Irregularities:** BOUND paused five minutes before the close and resumed after finalization (same peer-harness pattern as run 2);
three peers again first used offset 1 for 0 and caught it; no scratchpad collisions this time; no external literature in the index.

**Independence:** none (all Claude-authored). Runs independent in their peers, not in seeds or lead.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_bound_c02_run3, IRONCLAD-R23).
