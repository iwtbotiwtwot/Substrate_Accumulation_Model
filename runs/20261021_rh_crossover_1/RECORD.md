# Run record: rh_crossover_1 (RH beside the latest Volume I and spin work; third of three overnight runs), 2026-10-21

**Kind:** research run, exploration (no test, no key, no claim; BOUND_C02 stays CANDIDATE). Duck 2.3.1 / IRONCLAD-R28 / core 0.11.1.
**Where:** ironclad `campaigns/rh_crossover_20261020/` (RUN_REPORT.md, peers ONE–FOUR, results/); history entry H002751 (commit ed9f018); RH live page updated.

**Direction (Sean Brady):** "Why am I thinking of the RH program reading these results?" then "for kicks lets do a Duck run on RH with the latest work in vol i
and spin." The lead's RH-shape idea (logged earlier tonight) was the material beside the FEOP, Volume I and spin run reports.

**Outcome:** 315 returns, 308 completed, 2 controls failed as declared, 5 undeclared failures that were word-limit, check-design and operand-type errors
explained by their authors; run label FAILED_WITH_RETAINED_OUTCOMES; release pass.

**What was learned:**
- **The staircase remainder has the FEOP shape**: the quasistatic spin staircase's remainder is an Euler–Maclaurin series with coefficients from the end
  states only and geometric modes 1/2, 1/4, 1/16, 1/64 in the level index; a hard record gives a double root and a soft start a simple root with constant
  equal to half the Jeffreys divergence; the field-side staircase through the reciprocal-history operation has remainder exactly 1/(6n²).
- **The FEOP remainder level by level**: the local factor's remainder is exactly p⁻² per level from depth g − 1, with a double root on the diagonal g = L;
  the Selberg constants c₇ and c₁₁ are limits of one ω level's mass, settling as g·4⁻ᵍ then g·9⁻ᵍ.
- **Reciprocal history keeps no path-order gap in the switching work** for a kernel of |t − s|: time reversal preserves the pairwise differences; order
  lives in the end field. This is the field-side reading of the reversal law found in the Volume I run.
- **The crossover, as the peers state it**: the same hard/soft ↔ double/simple root split on both sides, but the ratios come from quadrature order on one
  side and the residue tree on the other; a coincidence until one construction makes the p-adic level and the stage refinement the same object.
- **Correction to the earlier spin reading**: with actions held fixed the quasistatic limit is 1.069 × I, so "share of I" depends on the family.

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run rh_crossover_1, IRONCLAD-R28).
