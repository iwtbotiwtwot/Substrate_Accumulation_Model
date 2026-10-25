# The spin model with the light isotopes inside the folds (host refit, 2026-10-25)

Sean Brady, 2026-10-25: "If we are able to include lighter isotopes in the spin/tensor model they should be." Host refit of the recorded BULK_NORMALIZED_SPIN
model (GEN4/duck_binding_open1, H002485; inputs and recorded predictions from ~/Downloads/isotope_residuals_253_20261017, source receipts to the archive) with the
thirteen light and anchor rows moved from transfer cohorts into the training folds. Exact rational least squares (Fraction normal equations), no new data, no
new features. Prediction written before running: light error under 3 MeV, development error worse by under 0.1 MeV, anchors still several MeV off.
Directed by Sean Brady. Executed with Claude Code.

## Reproduction first

The recorded model is whole binding B_reference as target on fourteen exact source features (A, surface, C, asymmetry, pairing, rule_depth,
rule_displacement_density, rule_displacement_curvature, current/literal cohesive energy per A, spin current/literal contact mean per A, current/literal relative
history per A), no constant term, folds 0–4. Reproduced exactly: full-fit and out-of-fold predictions differ from the recorded ones by 0.0 on all 253 rows;
development OOF 2.071766, light transfer 6.675659, anchors 37.608104 as recorded.

## Extensions (RMSE, MeV)

| Form | development OOF (208) | light (10) | anchors H1, H2, He3 (3) | historical 32 (never trained) |
|---|---:|---:|---:|---:|
| recorded (light and anchors as transfer only) | 2.071766 | 6.675659 (transfer) | 37.608104 (transfer) | 1.464112 |
| A: light + anchors inside the five folds (221 rows; new rows round-robin by Z, N) | 2.169658 | **2.082644** (OOF) | 10.402581 (OOF) | 1.813235 |
| B: leave-one-out over the 13 light/anchor rows (208 + other 12) | — | 2.1405 | 9.5244 | — |
| C: light inside the folds, anchors held (218 rows) | 2.124790 | 3.137422 (OOF) | 13.770539 (held) | 1.687821 |

Per-row out-of-fold errors in form A (MeV, prediction minus reference; transfer error before in brackets): H1 −9.41 (+26.50), H2 −13.70 (−55.88), He3 +6.95
(−20.45), He4 −3.92 (−16.64), Li6 +1.00 (−3.07), Li7 −0.24 (−10.54), Be9 +1.08 (−2.21), B10 +1.92 (−0.05), B11 +0.81 (−1.68), C12 −1.48 (−1.79), C13 −2.19
(−4.69), N14 −3.04 (−2.48), N15 −2.28 (−3.03).

## Reading

All three predicted clauses held (light 2.08 < 3; development +0.098 < 0.1; anchors 10.4 MeV). Including the light isotopes costs the heavy rows about a tenth
of an MeV out of fold and a third of an MeV on the historical rows, and brings the light rows from 6.7 to 2.1 MeV, the same level as the development rows. The
three free constituents (H1, H2, He3) cannot be carried by this linear source model at any weighting: 7 to 14 MeV off either way. He4 is 4 MeV off. The model
from Li6 upward is now one model.

The tensor channel (B5T's path features) is still absent for Z < 8: B5T's paths are built from the B4 native feature file, which covers Z ≥ 8 only and is not
in the local git objects (bulk). Extending the tensor to the light chains needs the B4 native features generated for Z < 8 by the SLC route and the frozen B5T
assignment applied to the new chains; that is the next step and is a construction change to B5T.

Script: `refit.py` beside this file (reproduction, A, B, C). Output: `LIGHT_REFIT.json`.
