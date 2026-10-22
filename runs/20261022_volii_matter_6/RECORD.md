# Run record: volii_matter_6 (the switched share on a second and a third field family under four fixed conventions), 2026-10-22

**Kind:** research run, exploration in the verification form (Volume II is material, not a statement under test; the lead's predictions were written before any
second-family computation and a host addendum after, both given to the peers; no key, no claim). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; staircase library
revision 3 and front library revision 2; 1500 s standing window at 12 GiB; sixty-task ceiling.
**Where:** ironclad `campaigns/volii_matter_6_20261022/` (RUN_REPORT.md, LIVE_CAPTURE.md, prior/LEAD_PREDICTIONS.md, peers ONE–FOUR, results/); history entry
H002767; ironclad commit 71103284.

**Direction (Sean Brady):** "run the switched share please. For the proposed check, keep the record preparation, switching account and information denominator
consistent, optimize both policies for total work, and test the switched N=1/2 versus N=1/4 ordering on the second field family." The four constraints were written
as rules of the run: records prepared on the unlapsed source; the switching account is the native lapse ledger with the lapse list (1, N, N, 1) for every N; the
information denominator is the unlapsed record's ceiling for every N; every chain at its field-plus-lapse optimum. Every peer reports no departure.

**Outcome:** 207 returns, 184 completed, 22 declared controls failed as declared, one builder fault superseded, none undeclared or late; the completion record
followed the close by three seconds.

**What was learned (Volume II Chapter XV, the recipients of a lapse; every convention declared):**
- **The switched share at lapse 1/4 is above the share at lapse 1/2 on three field families**, with the common denominator making the ordering a plain difference of
  totals: gaps of +3.0e-5 on G80, +2.2e-5 on G160 and +2.4e-5 at the continuous optimum, each witnessed with its negation failing as declared. The gaps agree to
  9e-6, and that spread is also the size of the gap's own drift between families, so the ordering is resolved by a factor of two to three, not more.
- **The switched curve on the second family rises as the lapse falls with diminishing increments**, witnessed: large steps from lapse 1 to 3/4 and 3/4 to 1/2, a step
  ten times smaller from 1/2 to 1/4.
- **The totals are stable across families to seven parts in a million, and the lapse term is not.** At lapse 1/4 the lapse term is positive on G80, negative on G160
  and positive again at the continuous optimum. Which ledger carries the ordering reverses between the two grids while the ordering's sign does not, and the sign
  flip sits on two chains whose field works move the opposite way. This is the volii_matter_5 mechanism seen chain by chain.
- **The exit-switch identity holds on every family** with its controls, replicated on separate controllers.
- **A witness's label follows the width of its operand, not the form or size of the ordering.** The plain difference certifies; the cross product with the ceiling
  inherits the ceiling's width and comes back budget-limited; the same row certifies at a looser tolerance. Under the common denominator the plain difference is the
  right witness.
- All seven of the lead's predictions held; one clause held at lapse 1/4 only between the two grids.

**What failed:** one undeclared first attempt (a builder fault), superseded. Two peers handed back before the finalization marker at their harness's demand, with
all their tasks returned. The continuous optima are host statements; the receipts certify values at the rounded points and, for one chain, local maximality.
Independence: none.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run volii_matter_6, IRONCLAD-R31).
