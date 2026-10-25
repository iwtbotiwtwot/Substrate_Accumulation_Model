# Visual QA of rendered pages 1 through 40

Reviewed the actual PNGs `qa/final/page-1.png` through `page-40.png` individually, emitted through `tools.view_image` at original resolution. Review used native 110 DPI images at 100 percent, in eight batches of five pages. No manuscript, DOCX, PDF or image was edited. This report concerns the 202-page render assigned for review, before any subsequent repair or rerender.

## Result

**Corrections required before final delivery.** Most text and equations are legible and clean, but the three N5000 tables collapse into vertical streams and distort the preceding paragraph or equation. The probability formula is clipped at the right edge on page 39. These are substantive layout defects, not cosmetic preferences.

## Exact defects

1. **Pages 30 through 32, N5000 six-source result table.** Page 30 ends after two introductory paragraphs with roughly two thirds of the body blank. On page 31 the paragraph beginning “The computation also retained a second encoding” is squeezed into a narrow far-right column. The table starts near the lower left with each header and data cell on its own line rather than in five aligned columns. Its vertical stream continues on page 32 before normal body text resumes. Exact numerical values are visible but no longer organized as a usable table.
2. **Pages 37 and 38, critical-temperature comparison table.** On page 37 the paragraph beginning “is the first global ordering transition” is squeezed into a far-right narrow block. The critical-temperature table headers appear in a vertical stream near the lower left, followed on page 38 by one value per line. It must be restored to the three-column comparison.
3. **Pages 39 and 40, captured and omitted Gibbs probability table.** At the bottom of page 39, the preceding probability equation is moved far right. Its right side is **clipped beyond the page edge**, so the exponential factor is not fully visible. Below it the three table headers appear on separate lines at the left; page 40 continues with one value per line. Both the equation and table require repair.

## Smaller inherited typography issues

- Page 4 opening question, page 5 bullets/body, page 7 represented-configurations bullet and page 9 residual sentence retain literal caret powers such as `2^100` or `2^5` in prose; adjacent display equations use proper superscripts. Page 17 similarly contains literal `2^12=4,096` in body prose.
- Page 25 route-acceptance checklist item 3 renders the word `sum` as italic mathematical letters with a subscript instead of a summation operator. The intended closure formula is still inferable, but the operator typography should be corrected.
- Page 26 parent-seal paragraph displays escaped text resembling `same_run_repair\ =\` rather than a clean code-field assignment.
- Page 27 partition-function introduction renders the word epsilon as italic letters (`epsilon_E`) while the surrounding equation uses the Greek symbol. Page 29 firewall bullets also retain literal `epsilon_E` and `!=` notation.
- Page 13 and page 21 source-connection bullet text contains doubled terminal periods in some entries. No layout failure results.

## Page coverage

| Pages | Content visually inspected | Assessment |
|---|---|---|
| 1 | Cover and attribution | Clean; title, body and page number legible |
| 2 | Results and reading guide | Clean; headings and paragraphs fit |
| 3 | Contents | Clean; complete chapter list fits |
| 4 | N100 chapter opening | Clean layout; caret-power typography noted |
| 5 | N100 definitions and distinctions | Clean layout; caret-power typography noted |
| 6 | Source census derivation | Clean; displayed fractions and sums fit |
| 7 | N100 construction and closure | Clean layout; caret-power typography noted |
| 8 | Source symmetries and component work | Clean; bottom product equation remains visible above footer |
| 9 | Output comparison and work identity | Clean layout; caret-power prose noted |
| 10 | Controls and compiler boundary | Clean; long identifier wraps inside margins |
| 11 | Execution contracts and routing | Clean; list continuation is readable |
| 12 | Routing qualification and authority | Clean; bottom paragraph continues normally |
| 13 | Connections and chapter end | Clean layout; doubled periods noted |
| 14 | SAM Language chapter opening | Clean; heading fits width |
| 15 | Version boundaries and definitions | Clean |
| 16 | Address domain and source custody | Clean; sums, bounds and headings readable |
| 17 | Formal state surface and ordered lift | Clean layout; caret-power prose noted |
| 18 | Decomposition and history equation | Clean; equation clear above footer |
| 19 | Receipts, controls and tape semantics | Clean |
| 20 | Compiler boundary and controls | Clean; dense bullets fit |
| 21 | Result boundaries, sources and connections | Clean layout; doubled periods noted |
| 22 | Exact state spaces chapter opening | Clean |
| 23 | Hamiltonian and density definitions | Clean; equations and bullets readable |
| 24 | Exact-route derivations | Clean; all formulas fit |
| 25 | NTT, CRT and acceptance checklist | Clean layout; literal `sum` operator noted |
| 26 | Custody deviation and retest | Clean layout; escaped field text noted |
| 27 | N96 spectrum and partition function | Clean layout; spelled epsilon noted |
| 28 | Thermal moments and conditional response | Clean; moment equations readable |
| 29 | Controls, boundaries and source list | Clean layout; literal code-like notation noted |
| 30 | N5000 chapter opening | Abnormal blank body region caused by next-table layout |
| 31 | N5000 result paragraph and table | Major paragraph/table corruption |
| 32 | N5000 result-table continuation and source definition | Major table corruption above otherwise normal body |
| 33 | Collective interaction and composition | Clean; formulas and text fit |
| 34 | Exact arithmetic and validation | Clean; binomial and moment equations readable |
| 35 | Archive custody and reusable readouts | Clean; partition function and Hamiltonian fit |
| 36 | Thermal pressure and exact motif responses | Clean; all equations visible |
| 37 | First-onset theorem and comparison table | Major paragraph/table corruption |
| 38 | Critical-table continuation and fluctuations | Major table corruption above otherwise normal body/math |
| 39 | Boundary memory, exact window and probability | Major clipped probability formula and broken table |
| 40 | Probability-table continuation and chapter end | Major table corruption above otherwise normal ending |

## Scope of inspection

No missing-glyph black boxes were observed on any of the forty pages. Body type, hierarchy, ordinary chapter breaks, header text and centered page numbers were consistently legible. No unrelated paragraph or display-equation clipping, overlap or footer collision was found. Large blank space at ordinary chapter ends is acceptable; the blank space associated with the collapsed N5000 tables is not.

Read-only DOCX inspection found the first table uses a fixed layout and percentage width with grid columns, but no per-cell `tcW` widths. The cells reference `Compact`, and the table references `Table`, while those style definitions were not located in `styles.xml`. This is a diagnostic observation rather than a confirmed cause. An explicit inline table width and matching per-cell widths would give a concrete repair route. The table and probability-equation pages need renewed visual inspection after repair; changed pagination may require extending the review range.
