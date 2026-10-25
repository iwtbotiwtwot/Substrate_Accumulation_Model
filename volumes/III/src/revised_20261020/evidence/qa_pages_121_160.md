# Visual QA of rendered pages 121 through 160

Inspected all 40 assigned PNG pages individually using `view_image` at original resolution. Each image is 935 by 1210 pixels, corresponding to the native 110 DPI render. Review target was `qa/final/SAM_Volume_III_Revised.pdf`, with page images under `qa/final/`. No document edits were made during this review.

## Findings requiring correction

- Page 121 has a severe layout defect. Its opening continuation paragraph runs in a narrow strip near the right margin, leaving most of the page blank. The exchange reuse table appears as a vertical stack of column headings and cell values near the lower left, rather than a readable table. The following paragraph resumes full width at the bottom.
- Page 134 has a severe table layout defect. The heading Complete finite scans locate the excursions sits in a narrow right strip. The finite scan table is flattened into a long vertical stack of headings and values on the left.
- Page 135 continues the flattened finite scan table with a stranded final value at the top. Under The current weighted state certifies a finite continuation, the explanatory paragraph runs in a narrow right strip, and the weighted state table begins as another vertical stack at the lower left.
- Page 136 continues the flattened weighted state table in the upper left. Its following prose and equations return to normal full width.
- Literal alignment ampersands are visible inside display equations on pages 128, 130, 131, 141, 145, 146, 147, 148, 149 and 157. These appear where TeX alignment markers should have been consumed. Examples include a theta and b theta on page 128, c and beta r on page 130, the d r bound on page 131, the completed Weil form on page 141, the prefix and admission definitions on page 145, the moment and covariance identities on page 146, the Gram definitions on page 147, aggregate and combine formulas on page 148, the completed square and numeric constants on page 149, and the candidate local channel on page 157.

## Page by page record

| Page | Inspection outcome |
|---|---|
| 121 | Defect narrow right strip and flattened exchange reuse table |
| 122 | Clean full width continuation and readable formulas |
| 123 | Clean chapter XVII opening and matter formulas |
| 124 | Clean text and exact probe formulas |
| 125 | Clean text and parity formulas |
| 126 | Clean text and numerical comparisons |
| 127 | Clean chapter ending |
| 128 | Normal layout but literal alignment ampersands in source path equations |
| 129 | Clean text and source integration account |
| 130 | Normal layout but literal alignment ampersands in residual equations |
| 131 | Normal layout but literal alignment ampersands in upper bound |
| 132 | Clean chapter XIX opening and energy formulas |
| 133 | Clean signed transport equations |
| 134 | Defect flattened scan table and narrow right heading |
| 135 | Defect table continuation and narrow right prose |
| 136 | Defect flattened weighted state table continuation then normal text |
| 137 | Clean chapter XX opening and formulas |
| 138 | Clean full width text and reciprocal history formulas |
| 139 | Clean text and source grading formulas |
| 140 | Clean logarithmic coordinate formulas |
| 141 | Normal layout but literal alignment ampersands in completed Weil form |
| 142 | Clean text and relational current formulas |
| 143 | Clean text and source authority lists |
| 144 | Clean chapter ending |
| 145 | Normal layout but literal alignment ampersands in prefix and admission formulas |
| 146 | Normal layout but literal alignment ampersands in moment covariance and bound formulas |
| 147 | Normal layout but literal alignment ampersands in Gram definitions |
| 148 | Normal layout but literal alignment ampersands in aggregate and combine formulas |
| 149 | Normal layout but literal alignment ampersands in square completion and constants |
| 150 | Clean text and transition storage formulas |
| 151 | Clean chapter XXII opening |
| 152 | Clean full width text and formulas |
| 153 | Clean sphere and multiplicative action formulas |
| 154 | Clean Lucas Lehmer and reciprocal voice formulas |
| 155 | Clean compiler and factor certificate formulas |
| 156 | Clean discovery chain and results |
| 157 | Normal layout but literal alignment ampersands in candidate local channel |
| 158 | Clean text and custody account |
| 159 | Clean chapter ending |
| 160 | Clean chapter XXIII opening and certificate formulas |

No clipped text, missing glyphs, obscured headers or footers, or incorrect page numbers were observed in this assigned range. Chapter breaks are consistent. The specific table and equation artifacts above prevent a clean QA approval until corrected and rerendered.
