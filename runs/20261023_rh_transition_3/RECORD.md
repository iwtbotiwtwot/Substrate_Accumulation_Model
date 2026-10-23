# Run record — rh_transition_3 (the adaptive receiver at 4096/3 → 1367, natively on T500 and the Google Cloud replica)

- **Date (UTC):** 2026-10-23, 01:14Z (predictions) → 03:47Z (both native PASS).
- **Directed by:** Sean Brady ("Should we run the adaptive receiver natively on the cloud?" — "proceed as recommended please"). **Executed with:** Claude Code (RH
  DomainSession experiment; no Duck window yet).
- **Where it ran:** ironclad `campaigns/rh_transition_3_20261023`, history entry `H002770`; native stores `native/adaptive1` (T500) and `cloud_adaptive1` (cloud).
- **Installed version:** Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2; temporary changes: none.
- **What ran:** predictions first; two host implementations generalised to a receiver (pair census with forward Abel group energies; cut telescope), each at both cuts for
  both receivers and at Y1 with the receiver frozen; a native adaptive combiner over the exterior ledger's certified mask forms computing the adaptive weights natively
  (2 × 218 logarithms), the price at both cuts, the frozen-receiver price, the weight-change account, the exact adaptive telescope, the closure, the published target.
- **What it showed** (engineering labels):
  - **Possible follow-up.** Both published receivers reproduced natively from the rules; adaptive P(Y₀) = −0.4348853154523694 against −0.434885315452.
  - **Possible follow-up.** The adaptive price rises (+2.715e-6) and the rise is structural: +2.494e-6 with the receiver frozen; the weight-change account is 8 %.
  - **Possible reduction.** The sign of the exterior change is a weighting fact: the admitted energy rises at the five smallest cuts and falls at 154 of 212; uniform-like
    weights read a rise, growing weights read a fall three hundred times larger. "Declare the receiver's weights before reading the sign."
  - **Needs inspection (host-only).** The adaptive Fchi release (+1.375e-5) covers the crossing rise and the whole price rise; nothing unpaid by that chart; native queued.
- **What failed, plainly:** four of five testable predictions failed (recorded in prior/LEAD_PREDICTIONS.md); three native attempts stopped on the lead's own checks
  (a = 0 exactly at cut 1367 at both cuts; a basis length) before the PASS; the 60-digit host cannot sit inside 1e-116 enclosures (agreement to 8e-60; 130-digit rerun
  in progress). Independence: none in §8's sense.
- **What it changes or opens in the volumes:** Volume III Chapter IX run-results: the adaptive receiver's native result and the weighting lesson; the lesson is carried
  into the Volume I chart extraction (IX's two rulers, X's two geometries, XI's count-equals-energy weights, VIII's unweighted containers).
- **Ideas logged:** `ideas/IDEAS.md` "2026-10-23 — from rh_transition_3".
- **Concluded by:** `scripts/conclude.sh` (hash in the commit).
