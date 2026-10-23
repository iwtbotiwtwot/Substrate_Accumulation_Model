# Run record — rh_transition_4 (the next account 1367 → 1371 for both receivers, natively; the two-cut combiner)

- **Date (UTC):** 2026-10-23, 04:15Z (predictions) → 07:36Z (chain end, unattended) → 14:30Z (read, hosts at 130 digits, triage).
- **Directed by:** Sean Brady ("word on the overnight pair, start it when storage lands"). **Executed with:** Claude Code (RH DomainSession experiment; no Duck window).
- **Where it ran:** ironclad `campaigns/rh_transition_4_20261023`, history entry `H002771`; native stores `native/forms_1367_1371` (66 segment sessions + sharp combiner),
  `native/adaptive_1367_1371`, `native/two_cut_regression_input`; T500 only (the cloud replica stayed stopped).
- **Installed version:** Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; temporary changes: none.
- **What ran:** predictions first (six, in `prior/LEAD_PREDICTIONS.md`); the receiver-independent mask forms of 1367 → 1371 certified natively in 66 rotating sessions
  (version-3 sharded script, transition-general, 4550 shared primitives by exact value); the sharp combiner with the chain identity P(Y0) = rh_transition_3's P(Y1) checked
  natively; the adaptive combiner (version 2) with the same identity, the frozen-receiver price and the weight-change account; two host implementations with a receiver
  argument at 60 and 130 digits; the two-cut combiner (one process per cut, a ledger process after) regressed against the exterior ledger of 4096/3 → 1367.
- **What it showed** (engineering labels):
  - **Possible follow-up.** Three native PASSes; both chain identities zero enclosures, so the ledger runs 4096/3 → 1367 → 1371 without a seam. Sharp ΔP = −1.752e-3 (2.4×
    the previous step, admitted-H carries it); adaptive ΔP = +8.43e-6 (3.1×, 93.8 % with the receiver frozen). Both signs persist and both changes grow.
  - **Possible follow-up.** The per-cut profile keeps its shape (rises at cuts 3 … 19, +7.09e-4; falls at 211; uniform cumulative never negative); θ* moved 0.0110 → 0.0138.
  - **Possible reduction.** At the sharp receiver the storage release covers the crossing rise by the exact factor 1 + (ℓ0 + ℓ1)/(2m) = 1.7623 at both steps (Δm = 0 there;
    Fchi = (m + ℓ)²/m, Pchi = ℓ²/m). "The release covers the crossing" is equivalent to "ℓ decreases"; the two signs flip together; the storage question reduces to the sign
    of Δℓ and the size of m. Declared, unchecked: where the release turns negative in peer ONE's scan (1383 → 1385) the crossing term turns negative too.
  - **Possible follow-up.** The two-cut combiner reproduces the single combiner's 14 headline endpoints identically; it is the form for a sweep (cut forms reusable, ledger cheap).
  - Both 130-digit host implementations inside every native enclosure (sharp 9/9 and 11/11, adaptive 16/16 and 17/17; worst 8.6e-121); A and B agree to 4e-129.
- **What failed, plainly:** two of six predictions failed in one clause each (482 new admitted events, not 250–350; adaptive rise 8.4e-6, not 1e-6 … 6e-6); the lead
  predicted persistence at the previous step's scale. The scripts' source-binding parent text carries a stale rh_transition_1 wording (the transition field is correct).
  The forms session store is 128 GB on disk (out of git, SHA manifest in results/); compression awaits Sean Brady's word. Independence: none in §8's sense.
- **What it changes or opens in the volumes:** Volume III Chapter IX run-results: the second account, the growth of both changes, and the release/crossing identity
  (the storage coverage at the sharp receiver is the chart's algebra, which narrows what the storage side can witness).
- **Ideas logged:** `ideas/IDEAS.md` "2026-10-23 — from rh_transition_4".
- **Concluded by:** `scripts/conclude.sh` (hash in the commit).
