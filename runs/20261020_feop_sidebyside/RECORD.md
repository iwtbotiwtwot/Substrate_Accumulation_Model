# Run record: feop_sidebyside (run 1's bracket beside runs 2/3's exact remainder, both made native), 2026-10-20

**Kind:** research run (ideas and executed identities; no scientific claim; BOUND_C02 stays CANDIDATE).
**Where:** ironclad `campaigns/feop_sidebyside_20261020/` (TARGET.md, PREREGISTRATION.json with four written expectations, LIVE_CAPTURE.md,
RUN_REPORT.md, peers/*/{NOTES,REPORT}.md, tasks and generators, results/RESULT_LEDGER.json, results/RUN_SHA256_MANIFEST.json); history
entry H002741; run folder `runs/duck/feop_sidebyside` (328 MB, out of git, manifest committed).
**Program:** installed Duck 2.0.1 / IRONCLAD-R23. No program change was needed; Sean Brady's "temporary change approved" was not consumed.

**Direction (Sean Brady):** after asking which FEOP run was most promising, and being told run 1's bracket was the most promising lead and
runs 2/3's exact remainder the most reliable result: "Run the side by side natively, temporary change approved."

**Outcome:** finalization FAILED_WITH_RETAINED_OUTCOMES: 210 returns, 198 COMPLETED, 12 FAILED, every one a first attempt that broke the
source-word payload contract (a field the operation does not take; a required field left out; an input name; a 64-row limit) and was
resubmitted and completed. None is a mathematical failure. The guide now documents the contract. 177 of 201 peer tasks took their inputs
by reference to retained results; 97 exact sign receipts; 22 authored-recipe executes.

**Reading (engineering register), the four pre-registered expectations all met:**
1. The bracket's two host-side steps hold natively, pointwise, on every nested case two peers could test, and break only off-hypothesis.
   The hypotheses are now explicit: nested offsets, p dividing Q, k ≤ g, k ≤ L. A flat even-separated tuple breaks step (b), so nesting is
   needed, not even separation alone. Native coverage stops at small p and k because of the word operation's 64-row matrix limit; the
   bracket rows at larger p and k still rest on the argument, backed by small-case receipts. Promoted from "host-side" to "verified where
   the program allows"; not a proof.
2. Every sign in the exact Selberg remainder is gated natively (693 checks) and reproduced by an independent construction up to g = 64.
3. At equal X and z the bracket upper is the tightest upper bound from g = 2 at both z. It is nontrivial from g = 4 (z=7) / 5 (z=11),
   against 12/13 for the exact-remainder Selberg bound, 17/18 for C02's coarse bound and 17/23 for Legendre, with sign receipts on every
   crossover. Its lower side turns positive at g = 7/9.
4. The measured extreme counts over all starts lie inside the bracket wherever a full-period scan exists.

**New:** a sharpened step narrowing the two-sided width by 20–25 %; a truncated exact-remainder Selberg bound, nontrivial from g = 4, that
beats the bracket only at small g. The enumeration question (tuples fitting in the window) is untouched by all three bounds.

**Independence:** none (all Claude-authored). Within-run agreement between separately written generators is not independent verification.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_sidebyside, IRONCLAD-R23).
