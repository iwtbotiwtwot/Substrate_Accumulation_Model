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

## Addendum — 2026-10-24 02:40Z, per-cut decomposition (H002773; Sean Brady: "Log all three as open and do item 1")
- **Possible reduction.** The sharp change is dP/dY × ΔY cut by cut: 1379 is 3.00 × and 1371 2.00 × the ordinary per-cut profile because ΔY = 6 and 4 there; dP/dY = −4.38e-4 →
  −4.32e-4 across 1367 → 1389. New coordinates enter at zero kernel, so the census of new pairs does not move the account it arrives at. Host at Y = 1375 and 1377 (support of
  1373): 0.3349 and 0.6682 of the 1373 → 1379 step, predicted 1/3 and 2/3 before running — P(Y) is continuous and the ledger samples it. The sign of the exterior change is the
  sign of the window sum Σ_{n>Y/2} R_n(Y) under the receiver's weights; the per-cut profile is that sum split by owner (fixed across accounts; positive at 3 … 19; not a power law).
- **Failed, plainly:** the lead's guess that cut 7 carried the 1379 excess; a power-law owner profile; new events driving the small-cut rise. Record:
  `campaigns/rh_sweep_1371_1389_20261023/results/per_cut/`.

## Addendum — 2026-10-24 15:20Z, the window sum by sector and owner (H002774; Sean Brady: "proceed with your recommendation")
- **Possible reduction.** New host code enumerates every pair of the window (Y/2, Y] by sector and owner (checked against host ΔP to 1e-31 at ten intervals and the native
  per-cut values to 1e-17 at 220 cuts). At Y = 1389 the admitted window sum S = −31 179 is NEGATIVE_PP −57 331 plus BALANCED +26 222, and BALANCED is the mirror of the excluded
  RESERVED_DONOR −31 330 (92 % of it at owners ≤ 19: that is why the small owners are positive); the unrestricted sum over all sectors is +785, so the fall is the admission
  rule's choice. Owners ≥ 37 are exactly prime-pair, so their profile is 2 w_p Σ cos(π log2(q/p)) over the negative half-periods across the window: peaks at 29–31, 137, 521,
  zero above Y/√2, and a function of p/Y (it shifts an octave when Y doubles). All 96 window primes have R_n < 0. The next account was predicted from the table before
  computing: ΔP_sharp(1389 → 1391) = −8.6303e-4, host A afterwards −8.63047e-4; standing prediction for a native account −8.6305e-4.
- **Failed, plainly:** both 10 % mirror bounds (11 %, 19 %); the 137 peak against 123; both trough positions (67, 277 against 61, 245) and their depths; the expectation that
  composites have both signs (181/187 negative). Record: `campaigns/rh_sweep_1371_1389_20261023/results/window_sum/` (ironclad).

## Addendum — 2026-10-24 16:05Z, the adaptive receiver under the window table (H002775; Sean Brady: "proceed with #1")
- **Possible reduction.** A weight-free pair table (reproduces host adaptive P and frozen P at 1389 exactly; own a_p, w_p to 1e-31 at 220 cuts) shows the adaptive change is the
  same window calculus as the sharp. At unit weight the admitted window sum is +230 out of halves of ±12 600 (owners 3 … 19 +12 691 from the donor mirror, owners ≥ 23 −12 461 from
  the prime pairs). The adaptive weights (1 to 1.005) see +190 and the receiver rises; the sharp weights (1 to 4.58) weight the large owners 3.5 to 4.6 times and see −31 179,
  S_sharp = Σ_p w_p S_1(p) − Self exactly. The receivers disagree in sign because of how they weight the owners, not because they see different pairs; every coordinate's sign is
  the receiver's (all 96 window primes positive at unit weight, all negative under the sharp weights). The adaptive sum grew 61 % across the sweep (118 → 190): the sweep's
  "adaptive per-event growth" is this residual growing. The weight part W is window calculus too (1.0e-6 clean, 4.25e-7 in the host's convention). Next account predicted
  6.683e-6 before computing; host A at 1391: 6.449e-6 (695 leaves the window at the midpoint; the exact form reproduces the host to 1e-34). Standing predictions for a native
  account 1389 → 1391: sharp −8.6305e-4, adaptive +6.449e-6.
- **Failed, plainly:** the prime/composite sign expectation at unit weight (reversed); W concentrated at cuts 3 … 13 (37 %, not 80 %); the 2e-8 accuracy clause (2.3e-7).
  Record: `campaigns/rh_sweep_1371_1389_20261023/results/window_sum/` (ironclad).

