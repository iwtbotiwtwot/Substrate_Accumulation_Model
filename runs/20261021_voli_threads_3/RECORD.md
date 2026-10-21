# Run record: voli_threads_3 (Volume I follow-up, second of three overnight runs), 2026-10-21

**Kind:** research run, exploration (no test, no key, no claim; the manuscript was not under examination). Duck 2.3.1 / IRONCLAD-R28 / core 0.11.1.
**Where:** ironclad `campaigns/voli_threads_followup_20261020/` (RUN_REPORT.md, peers ONE–FOUR, results/); history entry H002750 (commit 602d3c2).

**Outcome:** 245 returns, 223 completed, 19 controls failed as declared, 3 undeclared failures that were check-design and input errors explained by their
authors; run label FAILED_WITH_RETAINED_OUTCOMES; release pass.

**What was learned:**
- **A reversal law explains the path-order results.** With h = z − a the (h, p) pair is a closed subsystem and every lapse segment's generator is
  conjugate to its transpose by diag(1, −1), so a path and its reverse share the bilinear h₀·h_end − p₀·p_end. From rest that is the earlier "h does not
  depend on order under a swap"; it fails for moving starts and for rearrangements that are not reversals; a radar out-and-back is self-reciprocal.
  The order gap scales with the difference in 1/N; radiated energy keeps the order where h does not. The law holds for every N, Γ and coupling, so it
  says nothing about Γ.
- **The kinetic light path has a native readout by twin profiles**: at rational points of w² + v² = 2, one profile's q is another's √q, so coordinate
  readouts of the twin are the kinetic readouts of the original. Matched clock and path give K = 1 under either reading; the kinetic excess tends to half
  the coordinate excess; a kinetic-lapse feedback at a equals a coordinate-lapse feedback at a′ = 1 − √(1 − a) byte for byte. Within profile-side readouts
  the q versus √q fork is a choice of map; only an observable tying a to the source could separate the readings (the reservoir's energy share is the
  candidate the peers name).
- **The inertia identity** (a lapse N is κ → N·κ) is now enforced by a recipe on the constructions' own retained states.

**What failed:** three undeclared failures (two check designs, one basis label); every ordered product bypasses the construction's domain check; nothing
derives Γ.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run voli_threads_3, IRONCLAD-R28).
