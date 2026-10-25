# B5T against the 253-contract models on the same isotopes (host check, 2026-10-25)

Sean Brady: "If BST used the exact some roster as the tensor model which one would be better?" Host computation on recorded predictions only; no fit, no new
data. Inputs: B5T per-isotope predictions (archive git object `SAM_REVIEW/campaigns/SLCV21R_FULL_INTERSECTION_STARBREAKER_BINDING_PROGRAM_V1/phase_h/phase_h1/release/B5T_PREDICTIONS.csv`,
2,375 rows, H000258), B4's roster (`SLC/18_SAM_NATIVE_QC/SLCV12_BINDING_RESIDUAL_LEARNING_B4_V1/release/BINDING_B4_PREDICTIONS.csv`), and the 17 October residual
tables in ~/Downloads (`isotope_residuals_240_tensor_20261017/data.json`, BULK_INTENSIVE_TENSOR; `isotope_residuals_253_20261017/data.json`, BULK_NORMALIZED_SPIN;
source receipts name `GEN4/duck_binding_open1/candidates/...`, H002485). Script: `compare.py` beside this file. Directed by Sean Brady. Executed with Claude Code.

## Facts

- B5T's roster (B4's, August) has 2,375 isotopes with minimum Z = 8. No isotope with Z < 8 was ever in it, so no tensor path exists for H, He, Li, Be, B, C or N.
- The 253-row contract's 240 featured rows are exactly 240 B5T isotopes: its 208 development rows are all B5T development rows and its 32 historical rows are all
  B5T held rows. Its other 13 rows (H1, H2, He3 anchors; He4, Li6, Li7, Be9, B10, B11, C12, C13, N14, N15 light transfer) are outside B5T's roster.
- Errors are in MeV against the measured binding for both (B5T predicts the residual over a fixed formula; the 253 models predict the total with a fragment offset;
  the error of either against the measured value is the same quantity). B5T development rows are out-of-fold; 253 development rows are out-of-fold.

| Rows (same isotopes) | n | B5T principal RMSE | within 1 MeV | B4 baseline RMSE | BULK_INTENSIVE_TENSOR RMSE | within 1 | BULK_NORMALIZED_SPIN RMSE | within 1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| development (both contracts) | 208 | 1.9353 | 141 | 1.9225 | 2.0476 | 72 | 2.0718 | 72 |
| B5T held = 253 historical | 32 | 1.0644 | 30 | 1.1119 | 1.6707 | 13 | 1.4641 | 16 |
| all shared | 240 | 1.8431 | — | — | 2.0015 | — | 2.0014 | — |

B5T has the smaller absolute error on 171 of the 240 shared isotopes against either model.

## Reading

On the same isotopes B5T is better on both the development rows and the held rows, by a wider margin on the held rows. On these 240 rows B5T's own gain over
the B4 coordinate baseline is small (development 1.935 against 1.923; held 1.064 against 1.112): most of B5T's advantage over the 253-contract models here is
the B4 baseline trained on 1,982 rows against a model trained on 208. The tensor column of the 253 contract adds nothing on these rows (2.0015 against 2.0014).
The light isotopes are outside every tensor roster by B4's August roster rule (Z ≥ 8), a design choice in the record, not the owner's direction.
