# Run record: volii_matter_2 (the matter engine on the Volume I clock under both lapse recipients, the lapse ledger native), 2026-10-22

**Kind:** research run, exploration (Volume II is material, not a statement under test; no key, no claim). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; staircase
library revision 2; 1500 s standing window.
**Where:** ironclad `campaigns/volii_matter_2_20261022/` (RUN_REPORT.md, LIVE_CAPTURE.md, peers ONE–FOUR, results/); history entry H002763; the library revision
at ironclad d027c39d (`campaigns/recipe_library/staircase/README.md`, section "Revision 2").

**Direction (Sean Brady):** "Build the staircase recipe that returns each stage's state and proceed."

**The instrument built first:** the staircase recipe now returns every stage state, takes per-stage dwells (the ordered clock's elapsed intervals need no lattice)
and per-stage lapses, and under the energy recipient carries the lapse-switching ledger natively (lapse work per policy, lapse gain, total gain, sign witness on
the total). Offline it reproduces the legacy gain to every digit and the lapse term that could only be computed on the host the night before.

**Outcome:** 586 returns, 575 completed, 11 declared controls failed as declared, none undeclared or against declaration; release pass.

**What was learned (every lapse, tick scale and field family a declared convention):**
- **Under the clock recipient the lapse order is invisible, certified.** The two orders of the ordered clock give the same gain to every digit, and an identity
  recipe on the gain and every interior state passes with its control failing as declared: the inertia identity, now inside the matter engine.
- **Under the energy recipient the order matters and the lapse term is native.** Order 1 (lapse 4/5 then 3/5) wins once the lapse is paid, on both field families
  tried; the order differences are witnessed on one family.
- **The lapse term at gain-optimal fields depends on the field family by a factor of four** while the field gains agree to two parts in a million. The field gain sits
  at a flat optimum; the lapse ledger reads the stage states, which differ between near-equal optima. So the total of field and lapse work has to be the quantity
  optimised, not the field gain alone. Optimising the total moves the fields; whether it raises the total is unresolved between families.
- **At fixed fields the lapse ledger has the prototype's identities:** an order gap of about half the field gap with the same sign; the lapse work changes sign under
  path reversal; equal consecutive stages merge to every digit; frozen states pay nothing (zero check passed, moving-state controls failed as declared). Host
  reading: the entry switch cancels between the two policies because the current-only record is the sum of the history records.
- **The energy recipient's share of its own ceiling rises as the lapse falls**, 0.527, 0.557, 0.579, 0.599 at lapse 1, 3/4, 1/2, 1/4, with every gain and ceiling
  native and the first pair ordered by disjoint cross products without division. The earlier 0.603 was grid inflation.
- **The mixed recipient at a = 1/2 folds into an energy-recipient spec** (the square-root clock becomes a dwell factor): declared, not yet tested natively.

**What failed:** no undeclared failure. Every peer front-loaded its maps and lost witnesses and controls to the serial controller lanes; finalization took eighteen
minutes draining the tail. Lesson recorded: about forty tasks per peer per window, chain steps ahead of new maps. Independence: none.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run volii_matter_2, IRONCLAD-R31).
