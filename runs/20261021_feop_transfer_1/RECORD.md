# Run record: feop_transfer_1 (the cylinder-level transfer operator), 2026-10-21

**Kind:** research run, exploration (no test, no key, no claim; BOUND_C02 stays CANDIDATE). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; 1500 s window.
**Where:** ironclad `campaigns/feop_transfer_20261021/` (RUN_REPORT.md, peers ONE–FOUR, results/); history entry H002759 (commit a1b6c0ee); RH live page appended.

**Direction (Sean Brady):** "spin at 1500 s then begin FEOP run directly after".

**Outcome:** 447 returns, 416 completed, 29 controls failed as declared, 2 first attempts superseded, none undeclared; COMPLETE; release pass. 51 gate recipes
passed natively with exact-zero checks.

**What was learned:**
- **The transfer operator exists.** For the nested family at one prime, the residues at each level fall into four classes carried to the next level by two
  exact 4×4 matrices, one at the levels where an offset splits off (set by the valuation of Q at p) and one elsewhere. Every fibered enumeration up to the fiber
  run's reach equals the iterate; the iterate to level 24 equals the local density closed form at primes up to 13 and tuple sizes up to 24, so the bracket's
  constants at k = 24 are read from a 26×26 iterate instead of p^48 cells. All four peers wrote the operator independently in the window (not independent
  verification: four instances of one model reading one framing).
- **Its spectrum is {p², 1, p⁻²}** with a Jordan block at the split step, which is the crossover run's per-level ratio and its double root on the diagonal; the
  remainder reaches g/(p+1) from depth g − 1 with last departure −(p − 1)/p².
- **Across primes the local factor is exactly multiplicative** (a Kronecker product), with the joint remainder's recurrence roots the products of p⁻² over prime
  sets and explicit coefficients, so the earlier non-additive discrepancy is a truncation effect, not a local one.
- Every hypothesis the operator needs was broken by a declared control that failed at its check.

**What failed:** two gaps in the lead's fibering library (a single-case summing word; the row count in 2-D fibering), worked around in the window and to be fixed
with controls; no new enumerated level beyond the fiber run's reach.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_transfer_1, IRONCLAD-R31).
