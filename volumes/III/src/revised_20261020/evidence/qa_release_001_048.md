# Release visual QA pages 1 through 48

Reviewed **every assigned page 1 through 48** of the latest 192-page edition in `qa/release/page-N.png`, using `tools.view_image` at original/native resolution. The actual images were emitted and inspected individually in eight batches of six pages. This review does not use the obsolete `qa/final` render. No manuscript, DOCX, PDF or PNG was edited.

## Result

**Layout and equation clipping checks pass across all 48 pages. One table typography correction remains on page 41 before an unqualified typography pass.** No black missing-glyph boxes, overlaps, cutoff text, footer collisions or broken table structures were found. The N5000 table and equation defects from the obsolete render are repaired.

## Repair confirmations

- **Page 30**: N5000 six-source summary is a proper five-column native table. All six results, bounds and lattice steps align, and the total fits. The preceding paragraph occupies normal body width; the abnormal blank region is gone.
- **Page 35**: critical-temperature comparison is a proper three-column table. All fractions and twelve-decimal numerical values fit. The global-onset paragraph spans normal body width.
- **Page 37**: the complete captured-probability formula, including its exponential and final closing delimiter, is fully visible inside the text margins. The three-column captured/omitted-probability table is intact, with all nine body entries readable.
- **Page 25**: the route-acceptance summation now displays a proper summation sign rather than italic letters spelling sum.
- **Page 27**: the physical energy scale in the partition-function introduction now displays a Greek epsilon.

## Remaining table typography issue

**Page 41, N2000 ground-state table.** The third-column header wraps inside the word magnetization, appearing as `magnetizat` then `ion`. The rightmost entropy-density values wrap their final decimal digit onto a second line in each row. For example the positive-fill value appears as `0.00034657` then `4`. The exact multiplicity column fits and no digits are missing, but decimals should remain on one line for confident comparison. Widen the entropy column, adjust the column font, or use explicitly rounded displayed values. Keep full exact multiplicities. This issue was sent to the parent promptly.

## Residual minor notation in inherited prose

These do not affect page geometry or readability and were already reported in the earlier review: literal caret powers in some N100 prose/bullets (pages 4, 5, 7, 9 and 17); visible escaped `same_run_repair` assignment on page 26; literal `epsilon_E` and `!=` in the firewall bullets on page 29; doubled terminal periods in a few connection bullets on pages 13 and 21. The main display equations are readable and have consistent visual scale.

## Every-page ledger

| Page | Inspected content | Status |
|---:|---|---|
| 1 | Cover, attribution, header and footer | PASS |
| 2 | Results and reading guide | PASS |
| 3 | Contents | PASS |
| 4 | N100 chapter opening and first equations | PASS layout |
| 5 | N100 definitions and distinctions | PASS layout |
| 6 | Source census fractions and derivation | PASS |
| 7 | Exact N100 construction and closure | PASS layout |
| 8 | Component work and convolution | PASS |
| 9 | Output comparison and work identity | PASS layout |
| 10 | Controls and compiler identifiers | PASS |
| 11 | Exact execution contracts and router | PASS |
| 12 | Routing qualification and authority | PASS |
| 13 | Chapter connections and end | PASS layout |
| 14 | SAM Language chapter opening | PASS |
| 15 | Version and source distinctions | PASS |
| 16 | Address-space equations and custody | PASS |
| 17 | Formal surface and reciprocal schedule | PASS layout |
| 18 | Decompositions and history equation | PASS |
| 19 | Receipts, controls and tape semantics | PASS |
| 20 | Compiler boundary and control bullets | PASS |
| 21 | Established results and connections | PASS layout |
| 22 | Exact state spaces chapter opening | PASS |
| 23 | Hamiltonian and density definitions | PASS |
| 24 | Exact route derivations | PASS |
| 25 | NTT/CRT, corrected summation and checklist | PASS |
| 26 | Custody deviation and retest | PASS layout |
| 27 | N96 spectrum and partition function | PASS |
| 28 | Thermal moments and response | PASS |
| 29 | Controls and source handoff | PASS layout |
| 30 | N5000 opening and repaired result table | PASS |
| 31 | Collective term and exact composition | PASS |
| 32 | Two encodings and moment validation | PASS |
| 33 | Completed computation, archive and reuse | PASS |
| 34 | Thermal normalization, pressure and motifs | PASS |
| 35 | Global-onset proof and repaired critical table | PASS |
| 36 | Critical amplitude, memory and exact window | PASS |
| 37 | Repaired probability equation and table | PASS |
| 38 | N2000 chapter opening and source definition | PASS |
| 39 | N2000 source/component table and contraction | PASS |
| 40 | N2000 completed-output table and validation | PASS |
| 41 | N2000 exact ground-state table | CORRECT numeric/header wrapping |
| 42 | Residual entropy limits and field thresholds | PASS |
| 43 | Gap table, entropy definitions and bin table | PASS |
| 44 | Controlled low-temperature capacity and table | PASS |
| 45 | Joint-measure reuse and chapter end | PASS |
| 46 | Joint-state chapter opening and transformations | PASS |
| 47 | Sparse correction and exact contractions | PASS |
| 48 | Retained inventory and layered exact successor | PASS |

Chapter starts, chapter-end whitespace, running header and centered page numbers are consistent. Equations remain within margins, including the long N5000 probability formula and the later two-line energy transformations. Only page 41 needs a focused renewed typography inspection after its table repair; if pagination changes, inspect the changed pages as well.
