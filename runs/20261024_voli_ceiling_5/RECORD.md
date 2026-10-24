# Run record — voli_ceiling_5 (Duck idea run: is the exponent the number of accumulation directions?)

- **Date (UTC):** 2026-10-24, window 21:12:33Z–21:37:33Z (1500 s).
- **Directed by:** Sean Brady ("Proceed with your recommended run, lets do the standard 1500 minutes this run." — read by the lead as the standing 1500-second window and recorded so
  before the run). **Executed with:** Claude Code (lead outside; peers ONE–FOUR, Opus, no roles).
- **Where it ran:** ironclad campaign `campaigns/voli_ceiling_5_20261024/`, commit `bf37c5a3`, history entry `H002781`, run `runs/duck/voli_ceiling_5` (bulk outside git; hashes in
  `RESULTS_MANIFEST.json`). Preregistered before preparation (52 files and the index hash); the lead's two candidate pictures sympy-checked before hashing.
- **Installed version:** Duck 2.3.5 / IRONCLAD-R32 / core 0.11.3 (H002779). No change to the machine; recipes consuming the constructions' readouts were the hands.
- **What ran:** the parent question "can the exponent be the number of accumulation directions rather than a declared number?" with two candidate pictures written by the lead:
  (A) the volume-measure action (one cyclic field with kinetic metric e^{ΣΛ_i}, three accumulations with the reservoir stiffness; symmetric solution the installed reservoir with
  α_tot = √3 α, per-direction scale factor q^{1/3}) and (B) three independent one-log reservoirs; eight openings. 165 returns, 143 COMPLETED, 17 FAILED_AS_DECLARED, 3 FAILED_SUPERSEDED,
  2 FAILED_AGAINST_DECLARATION (two first-revision controls that hit engine errors before their declared check; both superseded), 0 late, 1 rejected; runtime label
  FAILED_WITH_RETAINED_OUTCOMES, resource release PASS. No external data.
- **What it showed** (engineering labels; tags possible follow-up / possible reduction / no clear lead yet / needs inspection):
  - **Possible reduction.** The lapse d = 3 needs exists natively: a = exp(−Λ/3) from the installed reservoir's own Λ gives a³ = q and matches the d = 1 line of sight at s = Λ̂/3 to the
    approximant error; the installed coordinate and kinetic lapses are the d = 1 and d = 2 members of the family a_d = q^{1/d}.
  - **Possible reduction.** Pictures (A) and (B) agree on everything the line of sight reads (q_tot = (1 + z)^{−3} in both) and differ only in a clock (H_A² = (4α²/3)(1 − (1 + z)^{−3})
    against H_B² = 4α²(1 − (1 + z)^{−1})) and an energy (E₀ against 3E₀); (B)'s volume drawn share is 3u² − 3u⁴ + u⁶ in (A)'s; with n charges each spanning k directions the z chart
    reads nk, the clock reads k, the energy reads n.
  - **Possible reduction (the derivation ledger of A).** The exponent is the number of accumulations under one charge only when their stiffnesses are equal: d = η_dir/η_tot =
    α_tot²/α_dir²; with unequal stiffnesses each direction has its own exponent, a_i = q^{p_i}, p_i ∝ 1/η_i (witnessed natively). The declared count becomes a declared isotropy of
    stiffness. Still declared: the photon rule, the floor, the weight.
  - **Possible reduction.** Shear (Λ_i = Λ_tot/3 + c_it, Σc_i = 0) leaves everything the volume law reads unchanged and carries its own conserved energy E_total = E₀ + (η/2)Σc_i²;
    declaring the total E₀ forces isotropy, declaring the total instead makes shear a slower clock and a multiplicative ceiling. Per-direction lines of sight and the energy ledger
    see it; the shear mark is the arithmetic-over-geometric mean excess (2/3)(cosh δ − 1)a₀.
  - **Possible reduction / possible follow-up.** The additive floor belongs to the volume (it does not factor over directions; a per-direction floor changes c₁ by 1/(1 + f + f²)) and
    is produced by a declared unaccumulated channel E_χ: q_obs = (E_χ + E₀q)/(E_χ + E₀), q_f = 15/22 at E_χ = 15/7, with the weight w = E₀/(E_χ + E₀) an energy ratio — the first
    language in which the weight has a dynamical name. A one-dimensional law for the observed accumulation exists: Λ_obs″ = 2(Q − q_f)(Q² + q_fQ − 2q_f)/((1 − q_f)Q²).
  - **Needs inspection.** Two first-revision engine errors and their against-declaration controls; a rejected `supersedes` on a control; two wrong row labels; the lead's framing
    table listed three q^{1/3} values typed rather than computed (off in the fourth digit; nothing built on them).
- **What failed, plainly:** nothing derives the count, the photon rule, the floor or the weight; the two first-revision controls witnessed nothing; the lead's table slip.
- **What it changes or opens in the volumes:** Volume I: a second addendum to §7 of the drafted ceiling section and a received-results subsection "the exponent as the number of
  directions (voli_ceiling_5)"; change-log lines. Targets register: result notes on T-02 (floor as a declared channel; does not factor over directions), T-03 (the weight as an energy
  ratio E₀/(E_χ + E₀)) and T-10 (the exponent as a stiffness ratio; the clock as the readout that counts directions). Nothing moved or removed.
- **Ideas logged:** `ideas/IDEAS.md` "2026-10-24 — from voli_ceiling_5" (seven, open).
- **Concluded by:** `scripts/conclude.sh` on 2026-10-24 (hash in the commit).
