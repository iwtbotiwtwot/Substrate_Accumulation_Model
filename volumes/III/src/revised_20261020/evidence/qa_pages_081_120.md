# Visual QA of rendered pages 81 through 120

Reviewed all 40 actual page images, individually at their native 935 by 1210 pixel size, using `view_image` with original detail. These are 110 DPI renders in `qa/final/page-N.png` of `qa/final/SAM_Volume_III_Revised.pdf`. No manuscript or artifact was edited during this review.

## Defects requiring correction

| Rendered page | Location | Defect |
|---:|---|---|
| 93 | Bottom display giving the exact count for 2^126 | Literal alignment ampersands are printed. The long integer is split into an expression beginning `2^126 &=85070...·10^21` followed by `&+...`; it is not a clean mathematical display. Replace with an actual exact integer equation or valid aligned expression. |
| 94 | Upper third, exact count for 2^144 | The same malformed alignment/long-integer handling prints literal ampersands and a broken additive expression. |
| 100 | Upper paragraph and receiver comparison table | Severe table layout failure. The preceding census paragraph is squeezed into a narrow column on the right. The intended four-column table is rendered as one long vertical sequence of headers and cell values on the left. Large unused page area makes the comparison difficult to read. Source is the table in `manuscript/starbreaker_supplement.md`. |
| 106 | Top projected-memory display | All four display lines expose literal ampersands after their left-hand expressions. They should be alignment markers, not printed characters. |
| 119 | Upper paragraph and finite-chain spectrum table | Same severe table failure as page 100. The paragraph introducing the finite benchmark is squeezed into a narrow right column. The intended three-column spectrum table becomes a vertical list at the left. Source is the finite spectrum table in `manuscript/exchange_chapter.md`. |

The parent was notified as each defect was found. These five pages do not pass final layout QA in the reviewed render.

## Every-page inspection ledger

| Page | Result |
|---:|---|
| 81 | Body and receiver/current formulas readable; no clipping or overlap. |
| 82 | History weave and rank-two functional readable; chapter-end whitespace acceptable. |
| 83 | Chapter XI title and opening readable; no clipping or overlap. |
| 84 | Lists, subheads and selection formula readable. |
| 85 | Target equations and lists readable. |
| 86 | Source census, split equations and feature formulas readable. |
| 87 | Ordinal fitting, fractions and superscripts readable. |
| 88 | Normal equations and exact result fractions readable. |
| 89 | Correction lists readable and within margins. |
| 90 | Chapter-end text and footer readable. |
| 91 | Chapter XII title and opening readable. |
| 92 | Census equations and type list readable. |
| 93 | FAIL: malformed exact-count display at bottom; remaining content readable. |
| 94 | FAIL: malformed exact-count display near top; remaining content readable. |
| 95 | Comparison statistics and long identifier wrap readable; no clipping. |
| 96 | Trace-free correction equations and lists readable. |
| 97 | Error envelope and observability equations readable. |
| 98 | Spin/orbit and source text readable; chapter-end whitespace acceptable. |
| 99 | New closed-cycle formulas and source-channel text readable. |
| 100 | FAIL: table collapse and narrow-column paragraph. |
| 101 | Li6 family, score and repayment equations readable; text within margins. |
| 102 | Native-learning continuation readable; chapter-end whitespace acceptable. |
| 103 | Chapter XIII opening and propagation formula readable. |
| 104 | Two-channel response and inverse-source text readable. |
| 105 | Inverse-fiber and dynamics formulas readable. |
| 106 | FAIL: literal ampersands in top display; numerical memory table and remaining content readable. |
| 107 | Chapter XIV and exact-logarithm formulas readable. |
| 108 | Source kernel, mode sum and residual formulas readable. |
| 109 | Capacity and matrix-log formulas readable. |
| 110 | Retained-mathematics and partition formulas readable. |
| 111 | Chapter-end paragraphs readable; whitespace acceptable. |
| 112 | Chapter XV title, recipe polynomial and source-index text readable. |
| 113 | Learning and adaptive-precision text readable. |
| 114 | Acceptance inequality and inverse-reconstruction formulas readable. |
| 115 | Learned-query and persistent-history text readable. |
| 116 | Chapter-end source-language paragraphs readable; whitespace acceptable. |
| 117 | Chapter XVI opening, canonical local quartic and eigenvalues readable. |
| 118 | Swap, R matrix, transfer and Hamiltonian formulas readable. |
| 119 | FAIL: table collapse and narrow-column paragraph; later dimension formula readable. |
| 120 | Raw-pencil, L13 count and symbolic matter formulas readable. |

No missing-glyph boxes, clipped lines, or overlapping body text were observed elsewhere in this assigned range. Page numbers are centered and readable throughout. Chapter starts are clear. A minor consistency observation is that the running header appears on pages 81,84,87,...,120, with no visible equivalent on the intervening pages; the parent should confirm whether that every-third-page pattern is intended. This observation is separate from the five concrete defects above.

## Reinspection needed

After the parent repairs the source/count alignment and table layout, rerender the affected document and inspect the new locations of those equations and tables. Pagination may change, so the present page numbers identify this reviewed render only. This report does not certify a later render that was not inspected.
