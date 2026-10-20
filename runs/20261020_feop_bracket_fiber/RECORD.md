# Run record: feop_bracket_fiber (the recipe route past the 64-row word limit), 2026-10-20

**Kind:** engineering research run (executed identities; no scientific claim; BOUND_C02 stays CANDIDATE).
**Where:** ironclad `campaigns/feop_bracket_fiber_20261020/` (TARGET.md, PREREGISTRATION.json, LIVE_CAPTURE.md, RUN_REPORT.md, peers' records,
results/RESULT_LEDGER.json, results/RUN_SHA256_MANIFEST.json); history entry H002742; run folder `runs/duck/feop_bracket_fiber` (1.4 GB,
out of git, manifest committed).
**Program:** installed Duck 2.0.1 / IRONCLAD-R23, no program change.

**Direction (Sean Brady):** offered an engine release to raise the native word's 64x64 matrix limit or the untried fibering route:
"Try the recipe route for the matrix limit first."

**Outcome:** finalization FAILED_WITH_RETAINED_OUTCOMES: 298 returns, 281 COMPLETED, 17 FAILED, eight of them declared controls, six
first attempts against word-grammar rules, three peer input errors recovered in-run. None mathematical.

**Reading (engineering register):**
- The route works. Splitting a residue system into blocks of at most 64 rows, one word per few blocks, and summing the block partials by
  reference gave native receipts for the bracket's two steps at p = 3, 5, 7 and 11 for k = 2, at k = 3 and 4 for small p, at k = 6 for p = 2,
  and for p = 11 up to 1.77 million residues, within one window. Two peers fibered the same cases with separate generators and agree exactly.
  Every control in fibered form breaks. All four pre-registered expectations met and exceeded.
- The matrix limit is not the obstruction. Cost grows with the number of residues p^(2k): p = 11 at k = 3 needs about 2,800 words, at k = 4
  about 330,000, and the bracket rows at k = 24 would need about 4·10^11 words at p = 2. No matrix limit, raised to any value, reaches them
  by enumeration. The engine release would buy convenience, not reach.
- Three findings on what a fibered receipt needs: a partition check with coverage and first-moment residuals (a cell count is fooled by a
  block-boundary error); the density rows alone cannot certify the steps (a tuple with zero density residuals fails both steps pointwise);
  the authored recipe gate does not bind blocks to a tuple and passed a non-partition, so it is a summing device, not yet a certificate.
- The route to k = 24, if any: a receipt per cylinder level (a transfer operator of size about g × p², O(k) numbers per case) instead of
  enumeration. Logged as the open idea that replaces the engine release.

**Independence:** none (all Claude-authored).

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_bracket_fiber, IRONCLAD-R23).
