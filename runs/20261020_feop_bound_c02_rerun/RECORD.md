# Run record: feop_bound_c02_rerun (blind replication of the FEOP BOUND_C02 peer run), 2026-10-20

**Kind:** research run, replication (no scientific claim; BOUND_C02 stays CANDIDATE).
**Where:** ironclad `campaigns/feop_bound_c02_20261020/rerun/` (RERUN_RUN_REPORT.md with the comparison, PREREGISTRATION.json
amendment 3, peers/*/{NOTES,REPORT}.md and tasks, results/RESULT_LEDGER.json, results/RUN_SHA256_MANIFEST.json) and
`campaigns/feop_bound_c02_20261020/RERUN_LIVE_CAPTURE.md` (lead's live capture, kept outside the worktree); history entry H002739;
run folder `runs/duck/feop_bound_c02_rerun` (177 MB, out of git, manifest committed); branch `feop-rerun` (88c1df4 + 98aa0d4).
**Program:** Duck 2.1.1 / IRONCLAD-R25 installed temporarily in a worktree for this run only (Sean Brady: "Exact replication on
2.1.1, temporary change approved, readback approved"); ironclad main stayed on Duck 2.0.1 / IRONCLAD-R23; the worktree was removed
at conclusion.

**Direction (Sean Brady):** "can we rerun the FEOP without the data it gained from this run? … can we run the exact same FEOP and
compare?"

**Blinding:** worktree at the pre-run commit, so no record of run 1 existed on disk; same target, openings, briefing (plus two
approved guide fixes), task shapes, prior folder and research index by hash; four fresh Opus peers; lead outside the window; the
lead's live capture written outside the worktree. (Run 1's capture had been written inside the campaign folder the peers read; no
peer record refers to it, but the exposure is recorded.)

**Outcome:** COMPLETE, 61 returns, 61 COMPLETED, 0 FAILED (run 1: 74). Comparison, engineering register:
- **Recurred:** the closed local theory (closed form, pointwise mask identity, controls, C02's tail); C02 as the fixed-z Selberg
  sieve whose full divisor roster is Legendre (three independent constructions); crossovers by exact sign; authored recipes.
- **Did not recur:** run 1's second tier: tree formula, sparse-digit tuple families, native Legendre identity on intervals, and the
  depth-uniform two-sided bracket that was run 1's headline.
- **New:** the exact Selberg remainder (leading constant about 1.44 vs C02's 324 at z=7; 3.27 vs 576 at z=11) makes the C02-frame
  bound nontrivial from g=12 instead of 17, and makes Λ² sharper than the Legendre envelope through g=19 (z=7) / g=25 (z=11). This
  corrects run 1's reading "C02 is weaker than the elementary count" to "weaker only with the coarse constant". The Selberg roster is
  a free parameter; an intermediate roster beats both at g = 16..19.
- **Reading:** the seeds force the first tier; the second tier is trajectory. Run 1 replaced the frame, the rerun sharpened it from
  inside. Neither second tier is established by the recipe; each has one run behind it.

**Irregularities:** CRT stopped submitting eight minutes early on a misread notice; peers' shared scratchpad caused generator
overwrites (no submitted task affected); no external literature in the index (unchanged); peers' "actual" sides mostly host-computed.

**Independence:** none (all Claude-authored). The two runs are independent in their peers, not in seeds or lead.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_bound_c02_rerun, IRONCLAD-R25 in worktree).
