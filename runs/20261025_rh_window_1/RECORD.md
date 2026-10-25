# Run record — rh_window_1 (Duck run in the verification form: the window calculus of the RH price)

- **Date (UTC):** 2026-10-25, window 21:06:37Z–21:31:37Z (1500 s); COMPLETE 21:31:39Z (no drain cutoff needed).
- **Directed by:** Sean Brady ("Put #2 on the top of the vol ii ideas list and go #1"). **Executed with:** Claude Code (lead outside; peers ONE–FOUR, Opus, no roles).
- **Where it ran:** ironclad campaign `campaigns/rh_window_1_20261025/`, commit `d315bbae`, history entry `H002784`, run `runs/duck/rh_window_1` (bulk outside git; hashes in
  `RESULTS_MANIFEST.json`; three peer census outputs over 5 MB kept out of git, listed in `results/BULK_KEPT_OUT_OF_GIT.md`). Preregistered before preparation (56 files).
  Verification form: the 24 October window-table work given (host, never shown to peers), the lead's host code and receiver results given, the lead's predictions written and
  hashed before its own host check, the peers' predictions in NOTES.md before computing, separate code, native certificates.
- **Installed version:** Duck 2.3.5 / IRONCLAD-R32 / core 0.11.3. No change to the machine.
- **What ran:** 22 openings (standing host numbers admitted by exact value; the ratio 379/67 and its native log); 120 peer tasks: 94 COMPLETED, 24 controls FAILED as declared,
  3 undeclared FAILED superseded (SUPPORT_UNRESOLVED on mixed-scale log-trace diagonals). 146 returns, 0 late, 0 failed_returns. Operations: 75 log traces, 28 products, 24
  admits, 8 logs, 4 exponentials, 3 log evaluations. No external data.
- **What it showed** (engineering labels; tags possible follow-up / possible reduction / no clear lead yet / needs inspection):
  - **Possible reduction.** Six separately written censuses reproduce the window table at Y = 1389 (S_sharp to 25–30 digits; the sectors, halves, counts; the exact linear form);
    THREE's full price reproduces P_sharp and P_adaptive at 1389 to 1e-40 and the standing changes 1389 → 1391 to 1e-32 of host A; every standing number witnessed natively with
    a failing control.
  - **Possible reduction.** Every census sign decision is exact integer arithmetic: (m, n) negative iff 2^{4j+1}m² < n² < 2^{4j+3}m²; never unresolvable for odd m, n. The pair
    (67, 379) is POSITIVE_PP (379² < 32·67² by 7) — the lead's opening text had the sign wrong; all four peers caught it. 833 pairs certified by exact integers; 12–15 by native
    log enclosures; the nearest boundary pair at Y ≤ 3930 is (2617, 3701). GEN3_COMPLEX_LOG returns −log.
  - **Possible reduction.** The owner profile above the pure prime-pair threshold is O_p = 2 w_p Σ_q min(cos(π log₂(q/p)), 0)·#{h odd squarefree coprime, Y/2q < h ≤ Y/q},
    matching the censuses to 1e-12 at every Y tried (1389 to 7860); a smooth law (2Y/ln Y)·Φ(p/Y) with no fit puts the peaks at p/Y = 0.380, 0.0955, 0.0240, where every
    census sits at every Y to 60 000. The sweep's "fixed owner profile" was a 1.6 % change in Y.
  - **No clear lead yet.** The unit-weight residual = mirror half (≈ Y²) − prime-pair half (≈ Y²/log Y); local descriptions (1/ln Y, (ln Y)^1.7) hold a few octaves and fail
    beyond; the lead's and three peers' growth ranges FAILED.
  - **Possible follow-up (the one new far-Y statement, with its caveats).** The admitted sharp window sum is negative to Y = 57 000 and positive at 60 000 and 62 880 in TWO's and
    FOUR's separate float codes and the lead's third vectorized census (−46 308 / +267 731 / +560 641 without Self); the sharp weights saturate near 4.660 and the weighted
    prime-pair/mirror ratio falls about 0.30 per unit ln Y through 1. Window sum only — dC/dY not computed; float at a crossing of two 5e7 halves; the rules applied literally far
    outside the original support. Whether the fixed constants (donor bound 1024, the original support) are meant to reach that far is Sean Brady's decision.
  - **Settled as exploration.** 1379 and 1387 differ only by ΔY = 6 and the least factor.
  - **Needs inspection.** An authoring rule: GEN5_LOG_TRACE diagonals must not mix scales (scale rows to their tolerances; ≤ 64 rows — a 350-row trace held a lane 178 s).
- **Volumes:** Volume III Chapter XX received the result at source (`volumes/III/src/book_20261025/body09.tex`, rebuilt to 154 pages on branch `volumes-from-source-20261025`).
- **Next, by the peers' reading:** the overnight sweep 1391 → 1429 tests the ledger account by account (ONE's S values written first; linear ΔP_sharp −8.64644e-4 → −8.30167e-4);
  the far-Y sign needs a census with dC/dY at 3e4–6e4 at higher precision, and the owner's decision on the rules' reach.
- **Independence (CLAUDE.md §8):** none; six Claude-written codes agree. Nothing is a claim; no statement about RH, a complete-price constant or a bound.

Directed by Sean Brady. Executed with Claude Code.
