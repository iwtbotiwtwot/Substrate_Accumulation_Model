# Run record: spin_verify_1 (five spin results verified with everything given; the grid explanation corrected), 2026-10-21

**Kind:** verification run (no test of a volume, no key, no claim). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; 1500 s standing window.
**Where:** ironclad `campaigns/spin_verify_1_20261021/` (RUN_REPORT.md, LIVE_CAPTURE.md, peers ONE–FOUR, results/); history entry H002760. Preceded by a
false start: `campaigns/spin_reconstruct_1_20261021/` (a blind rebuild with the values sealed by hash in `runs/20261021_spin_reconstruct_1/sealed/` here;
the window opened empty and was stopped; no submissions).

**Direction (Sean Brady):** "Can we use the next run to independently reconstruct a small set of headline results rather than broaden the search again";
"this is verifiying what we learned"; on the blind staging: "we are asking the peers to verify something and not giving it to them?"; "Is the a smarter way that
is less like a test and more like a verification?"; "Restage it this way and proceed please".

**Design adopted (verification, not examination):** the peers get every value, field file and report. Checks: recomputation by separate code (two peers through
the staircase library, two with their own product chains and nothing from the library); exhaustive per-chain optimum searches, written separately by each peer;
the recorded explanation as a native ordering with its negation declared; predictions on cases never run, time-stamped in notes before computing; controls
built to break the explanation.

**Outcome:** 491 returns, 475 completed, 16 declared controls failed as declared, none undeclared, none late; release pass.

**What was verified:** the four-stage dwell-4 gain, the two-stage gain on the 1/10 and 1/20 grids with their gap, and the (2,2,4) against (2,2,2,2) ordering on
both grids all reproduce to the enclosure width (about 1e-56) across three implementations; four exhaustive searches re-derive every recorded field assignment,
so the recorded values are the true grid optima. The 1/20-grid fields behind the reversal, found non-exhaustively before, are the exhaustive optima: the
four-over-three reversal stands.

**What was corrected:** the earlier sentence that coarse grids inflate the gain by under-optimising the current-only policy holds at the first refinement for the
shapes it was read from and fails as a mechanism. At four equal dwell-2 stages the history side gains more from refinement (certified, declared in advance).
The grid error has either sign, about 1e-5 at two stages and 5e-5 at four; refinement is not monotone past 1/20 (two stages dip at 1/40 then rise at 1/80 and
1/160; four stages rise at 1/40 then fall at 1/80); the T = 8 reversal between stage counts is the two shapes pushed in opposite directions, present on 26 of 60
host grids by alignment with the optima rather than by step. The conclusion that stands: no ordering below the grid error is resolved by a grid; compare at
each policy's continuous optimum.

**Predictions:** most met (values on the 1/40 grid, their orderings, the four-stage gain on 1/20, per-policy signs); ONE's directional forecasts at four stages
on 1/40 and 1/80 and THREE's size band missed, recorded as such.

**What failed:** no undeclared failure. FOUR's scheduling left its break-attempt certificate and its own four-stage 1/20 build unfinished; two of its checks had
no power by identity and it said so. The (2,2,4)/(2,2,2,2) shapes were rebuilt on the library route only. Independence: separate code, same model, same lead.

**Method decision carried forward:** this verification form replaces the blind-rebuild form; FEOP's results are verified the same way next.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run spin_verify_1, IRONCLAD-R31).
