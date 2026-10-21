# Run record: feop_verify_1 (the transfer-operator results verified with everything given; hypotheses mapped), 2026-10-21

**Kind:** verification run (no test of a volume, no key, no claim; BOUND_C02 stays CANDIDATE). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; 1500 s standing window.
**Where:** ironclad `campaigns/feop_verify_1_20261021/` (RUN_REPORT.md, LIVE_CAPTURE.md, peers ONE–FOUR, results/); history entry H002761.

**Direction (Sean Brady):** "Proceed with the FEOP verification run in the same form" as spin_verify_1: the peers get every value, matrix, report and generator;
strength from separate code, enumeration where none has been, predictions written before computing, the derivation re-done, controls built to break the hypotheses.

**Outcome:** 346 returns, 318 completed, 28 declared controls failed as declared, none undeclared, none superseded; release pass.

**What held:**
- The two 4×4 matrices were re-derived from the lifting rule by all four peers, two of them before reading the record, and equal the recorded ones for every prime.
- Class counts were enumerated where no enumeration had been: primes 11 and 13 at depth 2, prime 5 at depth 4 (390,625 residues), prime 3 at depth 5 through the fixed
  library (the case the library defect had blocked), prime 2 at depths 7 and 8, and prime 7 at depth 3 re-enumerated with separate code. Every count matched the
  operator's prediction written beforehand, with the partition residuals zero.
- The remainder law (plateau g/(p+1) from depth g−1, last departure −(p−1)/p²) holds at primes 13, 17, 19, 23 and at g = 6, 8, 12; the spectrum relations hold at the new
  primes with the Jordan-block control failing as declared. A native map now carries the stationary form onto the four-state form, so the two readings of the run
  before are one object with a receipt.
- The joint-prime recurrence holds with 11 and 13 in the modulus; the explicit coefficient formula holds at four and five primes and at g = 2, 3, 4; direct joint
  enumerations at three new moduli, including one with mixed valuations, equal the Kronecker product; dropped-piece and early-start controls fail with the predicted
  values.

**What was mapped:** the operator fails exactly where its hypotheses are exceeded: two offsets sharing a class, a cluster dying whole, a prime not dividing Q, or a
schedule not set offset by offset by valuation. The offset-tree rule from the run before matched all ten new tuples.

**What was corrected:** the lead's definition of the zero class's children (settled p²−2p, not p−2); the additive miss is the product of dead counts at two primes only,
the inclusion–exclusion remainder at three.

**What failed:** no undeclared failure. One peer's chain driver idled for ten minutes; two gate executes went in late; two admissions were refused for reused keys. The
masks are host-enumerated throughout; gates check sums of squares with per-entry residuals in the returns. Independence: separate code and new cases; the same model.

**Next (deployed directly after, as directed):** volii_matter_1, the four-state spin prototype applied to Volume II matter and binding constructions.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_verify_1, IRONCLAD-R31).
