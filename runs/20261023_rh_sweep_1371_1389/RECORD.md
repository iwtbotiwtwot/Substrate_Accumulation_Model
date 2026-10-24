# Run record — rh_sweep_1371_1389 (seven accounts 1371 → 1389 for both receivers, natively, by the two-cut form)

- **Date (UTC):** 2026-10-23, 14:53Z (predictions) → 15:19Z (chain start, after the archive job) → 2026-10-24 00:47Z (chain end, unattended) → 01:00Z (triage).
- **Directed by:** Sean Brady ("Lets compress, archive, remove from T500 then start the sweep with a close eye on disk space…"). **Executed with:** Claude Code (RH
  DomainSession experiment; no Duck window).
- **Where it ran:** ironclad `campaigns/rh_sweep_1371_1389_20261023`, history entry `H002772`; native stores `native/forms_<Y0>_<Y1>` and `native/adaptive_<Y0>_<Y1>` for
  the seven transitions (session stores archived to Google Drive and removed; `docs/session_archives/ARCHIVE_LEDGER.jsonl`); T500 only.
- **Installed version:** Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; temporary changes: none (scripts 3.1 / 2.1 differ from 3 / 2 in label lines only).
- **What ran:** predictions first (nine laws across the seven accounts, `prior/LEAD_PREDICTIONS.md`); per account the previous account's certified cut-1 forms reused as
  cut-0 with provenance (the segment a new prime enters recomputed), the cut-1 forms certified natively in 12 segments, both combiners with the chain identity P(Y0) =
  previous P(Y1) checked natively, the adaptive frozen receiver and weight-change account, two host implementations at 130 digits, a ledger row, then the session stores
  compressed, uploaded, verified and removed. 9.47 h, 44,066 native calls, fourteen PASSes.
- **What it showed** (engineering labels):
  - **Possible follow-up.** Fourteen zero chain identities: the ledger is seamless from 4096/3 to 1389. Sharp falls and adaptive rises at all seven accounts; the frozen
    receiver carries 92.9–95.3 % of each rise. Sharp P −2.2256774 → −2.2334977; adaptive P −0.43487417 → −0.43482064.
  - **Possible reduction.** The sharp change is a near-constant per account (−8.66e-4 ± 0.6 % at six of seven accounts, prime or composite, 302–539 admitted events;
    1379 = 7·197 alone 3.0×; the adaptive rise shows the same pattern): the growth variable is the account, not the admitted event. Open: why 1379.
  - **Possible reduction.** The sharp storage identity release/crossing = 1 + ℓ̄/m held to six decimals at all seven steps and survived its sign change: Δℓ turned positive
    at 1383 → 1385 with release and crossing going negative together, as declared by rh_transition_4 from peer ONE's scan. The sharp storage side witnesses only sign(Δℓ).
  - **Possible follow-up.** The adaptive receiver's storage is a different law: ratio 11.66 → 10.56 against 12.06 as its Δm term (−4e-9 … −1.2e-8) grows; its Δℓ has not flipped.
  - **Possible follow-up.** Two populations: primes admit 0.54 of the new pairs, composites 0.86–0.96. The per-cut rising set is exactly {3, 5, 7, 11, 13, 17, 19} at every
    account (plus 967 at 1373 and 971 at 1381); θ* stays in 0.014–0.021 without monotone drift.
  - Both 130-digit host implementations inside every native enclosure at every account (266 of 266 rows); the relabel step passed at all seven accounts.
- **What failed, plainly:** five prediction clauses — sharp growth per admitted event at four accounts (wrong variable), composite admitted fraction at 1387 (0.957 vs 0.95),
  adaptive storage ratio within 1 % at all seven (3.4–12.5 % below), θ* "drifts upward" (two falls), time at all seven (79–87 min vs 75; 9.47 h vs 9). GitHub refused two
  per-file manifests (268 MB, 65 MB); they live beside their archives on Drive with pointers in git. Independence: none in §8's sense.
- **What it changes or opens in the volumes:** Volume III Chapter IX run-results: the sweep result; the per-account constancy of the sharp change; the storage identity's
  tested sign change; the adaptive receiver's separate storage law.
- **Ideas logged:** `ideas/IDEAS.md` "2026-10-24 — from rh_sweep_1371_1389".
- **Concluded by:** `scripts/conclude.sh` (hash in the commit).
