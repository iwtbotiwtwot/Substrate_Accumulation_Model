# Run record — peer_restore_next (first Duck 2.0-shape run, one 900 s window)

- **Date (UTC):** 2026-10-19, window 22:00:48–22:15:48.
- **Directed by:** Sean Brady. **Executed with:** Claude Code (GEN6 Duck run `peer_restore_next`; peers CLOCK, RULER, PROPAGATION, JOINT).
- **Where it ran:** ironclad campaign `campaigns/peer_restore_20261019`, commit `26211ab` (report `NEXT_RUN_REPORT.md`), history entry `H002730`, run `runs/duck/peer_restore_next`; the method was then promoted as Duck 2.0.0 / IRONCLAD-R22 (`H002731`, tag `duck-2.0.0`).
- **Installed version at the run:** Duck 1.16.2 / IRONCLAD-R21 (identical code to 2.0.0). Temporary changes: none; the 900 s window was the owner's setting for this run and became the 2.0 default.
- **What ran:** four Claude-backed peers bound to G6_01–G6_04, lead outside, method authoring available; 133 returns (121 COMPLETED, 11 FAILED, 1 REFUSED), 110 peer submissions accepted, 10 methods authored.
- **What it showed** (engineering labels):
  - possible follow-up: a native division (CLOCK, via GEN3_COMPLEX_SOLVE) gives a teeth-per-tick ruler; teeth per elapsed tick = ν₀ on every clock; teeth per internal tick = ν₀⟨1/q⟩, the path mean.
  - possible reduction: the sech² and 1 − x² accumulation laws are endpoint readings of charts whose means are tanh(x)/x and artanh(x)/x (CLOCK, on JOINT's and RULER's operands).
  - possible follow-up: certified local speed c_eff = c₀q by reference across three peers' operands (PROPAGATION).
  - needs inspection: three controllers' outputs in one executed method, u² c_eff = c₀ (RULER).
  - possible reduction: tick = f(E_s/η, τ); ledger = g(εg²Wp², R, readout, c); ε and c enter the ledger as one product (JOINT, PROPAGATION).
- **What failed, plainly:** four compiles bound the wrong method reference; three executes failed in the checker on an entry-level path; two designed controls failed as designed; two identities did not hold as written; one chart refusal; one negative-time control refused. All read and acted on in the window.
- **What it changes or opens in the volumes:** Volume I, Chapter IV (delay as a path mean of 1/q), Chapter II (depth as rapidity), Chapters IV–V (tick from source and road, ledger from the interface), and the κ_s research item (the a(q) identification, `ideas/IDEAS.md`). No change to the living text yet; openings only.
- **Ideas logged:** four entries in `ideas/IDEAS.md` (2026-10-19).
- **Concluded by:** `scripts/conclude.sh`, see git log.
