# Run record: spin_work_3 (share of the ceiling against total time; trapezoid staircase; noisy record), 2026-10-21

**Kind:** research run, exploration (no test, no key, no claim). Duck 2.3.1 / IRONCLAD-R28 / core 0.11.1, no program change.
**Where:** ironclad `campaigns/spin_work_3_20261021/` (RUN_REPORT.md, peers ONE–FOUR, results/); history entry H002752 (commit 6a19b88).

**Direction (Sean Brady):** "Please proceed with item 1", the lead's morning recommendation: the spin question both earlier spin runs asked for
independently, share of the information ceiling against total time for 2, 3 and 4 free stages with both policies re-optimised at every dwell.

**Outcome:** 465 returns, 456 completed, 3 controls failed as declared, 6 undeclared failures (log traces on matrices with an exact zero eigenvalue, fixed
in the window); run label FAILED_WITH_RETAINED_OUTCOMES; release pass. Two native receipts spot-checked by the lead match the peer reports.

**What was learned (units kT = 1, nats; I(i;h|j) = 0.0226357 on the declared four-state source):**
- **More stages never lose at equal total time when both policies are free.** Hidden-only, native with positivity witnesses: 0.380 / 0.539 / 0.601 of I
  at total time 4 / 8 / 12 for 1 / 2 / 3 stages; four stages about 0.704 at 16 (host sum over native states). Visible plus hidden at total time 4:
  0.417 → 0.454, the ordering witnessed with its negated control failing as declared. spin_work_2's crossover in favour of the single stroke belonged to
  the fixed halved-field family. Nesting guarantees 2 ≥ 1 and 4 ≥ 2 at equal dwell; 3 vs 2 is a host reading. Every finite-time value lies below its
  stationary share (0.437 / 0.607 / 0.699 / 0.756): the finite-dwell curve approaches from below.
- **The trapezoid staircase removes the 1/n mode exactly**, leaving b/n² with b = (Var₀ − Var₁)/12; the midpoint leaves −b/2; Simpson falls as n⁻⁴;
  T_2n = (T_n + M_n)/2 exactly. Equal-thermodynamic-length spacing lowers the forward dissipation (witnessed) but raises the asymmetric part. Neither
  trapezoid nor midpoint is a protocol an engine can run.
- **A noisy record raises the share under the net price** B = H(ĩ|j) − H(ĩ|i): a 1/20 flip at separation 1 and three flips at separation 2 beat the clean
  record natively; an asymmetric flag on the rare visible-down class reaches about 0.076 against 0.060 clean. Under the floor price noise only hurts.
  Still about 8 % of the net price; no cycle closes on this source. The record should carry the rare informative class, as the 64-state port-0 reading said.

**What failed:** depth set by the shared queue again (four-stage gain, the total-time-8 chains, the τ = 4 and a → 1 ledgers never admitted); no peer wrote
the one-recipe-per-staircase DAG the briefing asked for; field optima are host grid optima certified only at the declared rationals; matched end fields and
the 64-state source untouched.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run spin_work_3, IRONCLAD-R28).
