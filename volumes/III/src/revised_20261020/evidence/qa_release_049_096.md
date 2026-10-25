# Release visual QA pages 49 to 96

Every page from 49 through 96 of the new 192-page release was individually opened as its original-resolution PNG. Inspected files were qa/release/page-49.png through qa/release/page-96.png. No obsolete qa/final pages were used for this review. No manuscript files were edited.

## Result

Geometry and legibility PASS for all 48 pages. No clipping, overlapping text, black missing-glyph boxes, broken native tables, or collisions with footer page numbers were observed. A small number of conversion residues remain and are listed below for repair before an unqualified release pass.

## Exact remaining residues

1. Page 87 has literal alignment ampersands at the beginning of the second line of both large-integer displays: the expansions of 2^126 and 2^144 print an ampersand before the plus sign. Remove these two characters. Both displays otherwise fit the page.
2. Page 59 input-types list item prints literal TeX spacing backslashes in “BinarySurface,\ ContactOperator,\ AxisChannel”. Remove the two spacing backslashes. The line is otherwise legible.

Running headers appear at intervals of approximately three pages and are absent from many intervening pages. This behavior was already disclosed in the earlier QA report. Page numbers are continuous and correctly positioned on every inspected page. Confirm the intended running-header policy for the final edition.

## Repairs confirmed

- The quadratic norm display on page 69 no longer prints the alignment markers seen in the previous render.
- The native four-column receiver-recovery table on page 92 has proper inline geometry, explicit columns, readable cell contents, and no overlap with preceding or following prose.
- The connector formulas on page 73 clearly retain the squared numerator and correct rational values.
- Chapter starts on pages 50,57,66,73,76,84,95 have clear heading hierarchy and suitable top spacing.
- Mathematical expressions remain legible across the reviewed pages, including lower-envelope minimization on 49, reciprocal-history reconstruction on 53-54 and 67, Gram and tensor formulas on 68-70, ordinal comparisons on 78-81, Starbreaker spectra on 86-87, and receiver/matter formulas on 92-96.

## Page ledger

49 PASS; 50 PASS; 51 PASS; 52 PASS; 53 PASS; 54 PASS; 55 PASS; 56 PASS.

57 PASS; 58 PASS; 59 MINOR TEXT RESIDUE; 60 PASS; 61 PASS; 62 PASS; 63 PASS; 64 PASS.

65 PASS; 66 PASS; 67 PASS; 68 PASS; 69 PASS; 70 PASS; 71 PASS; 72 PASS.

73 PASS; 74 PASS; 75 PASS; 76 PASS; 77 PASS; 78 PASS; 79 PASS; 80 PASS.

81 PASS; 82 PASS; 83 PASS; 84 PASS; 85 PASS; 86 PASS; 87 MATH TEXT RESIDUE; 88 PASS.

89 PASS; 90 PASS; 91 PASS; 92 PASS; 93 PASS; 94 PASS; 95 PASS; 96 PASS.

This ledger is tied to the release render present at inspection time and does not certify a later rerender.
