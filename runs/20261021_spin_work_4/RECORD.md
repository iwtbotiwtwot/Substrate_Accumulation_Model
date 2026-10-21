# Run record: spin_work_4 (staircases as one recipe; the share to seven stages; the grid artefact), 2026-10-21

**Kind:** research run, exploration (no test, no key, no claim). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; 1500 s standing window.
**Where:** ironclad `campaigns/spin_work_4_20261021/` (RUN_REPORT.md, peers ONE–FOUR, results/); history entry H002758 (commit 1f3053eb).

**Direction (Sean Brady):** "proceed as recommended, spin at 1500 s then begin FEOP run directly after".

**Outcome:** 529 returns, 520 completed, 8 controls failed as declared, one control counted against its declaration (a log trace inside a recipe fails by
engine error, so a named-check declaration cannot cover it; the new rule labelled it correctly), none undeclared; release pass. 41 staircase gains and 32
orderings certified natively, every staircase one library recipe.

**What was learned (units kT = 1, nats; four-state source, separation 1, hidden-only field):**
- **The share against total time is native to seven stages:** 0.704, 0.746, 0.729, 0.765 of the ceiling at total times 16, 20, 24, 28 with dwell-4 stages; the
  seven-stage share lies above the four-stage stationary value 0.756; finer stages beat coarser at equal total time.
- **The grid artefact.** The gain is a difference of two separately maximised works. A coarse field grid leaves the current-only policy further from its
  optimum, inflating the gain (two stages at total time 8: 0.539 on a 1/10 grid, 0.527 on 1/20, 0.527 continuous) and reversing orderings between stage counts.
  The earlier finite-dwell shares carry about 0.012 of this inflation; no ordering between stage counts stands until both policies are optimised to one
  tolerance on one family. All four peers found this independently.
- **Dwell placement:** at two stages the equal split wins; a short first stage costs less than a short last; the host optimum sits near 3.25 of 8.
- **The flag record keeps its advantage through a staircase:** at two stages the half-strength flag converts the same share of its own ceiling as the clean
  record, so its gain per net price is 25 % higher; no cycle closes, the best working share is about 4 % of the net price.

**What failed:** one submitter hang cost TWO its three- and four-stage continuous-family recipes (compiled, not executed); flag ceilings and prices are host
values; the staircase library caps at seven stages and keys maps by field only.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run spin_work_4, IRONCLAD-R31).
