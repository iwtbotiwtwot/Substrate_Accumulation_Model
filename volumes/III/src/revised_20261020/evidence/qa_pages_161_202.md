# Visual QA pages 161 through 202

Reviewed all 42 rendered PNGs individually at their native 935 by 1210 pixel resolution using original-detail image display. Source: `qa/final/page-161.png` through `qa/final/page-202.png`, the 202-page render supplied for this assignment. No manuscript or render files edited.

## Delivery blocking layout defects

- **Pages 166 and 167:** The five-column billion-index results table is not rendered as a table. Its cells appear as a single vertical stream of paragraphs. The preceding paragraph beginning “All 64 seeds” is displaced into a narrow right-hand column near the bottom of page 166, leaving a very large blank region. Three header labels begin at the bottom of page 166 and the remaining labels and all data continue vertically on page 167. Rebuild this table and remove any floating/wrapping positioning.
- **Page 169:** The three-column resource comparison table is also a single vertical stream of cells. Its preceding explanatory paragraph is displaced into a narrow right-hand column in the upper third, leaving most of the upper-left page blank. Rebuild this table and its surrounding flow.

## Equation conversion artifacts

- **Page 171:** The displayed coefficient equations contain literal `&` alignment markers before equals signs in both rows.
- **Page 173:** The first-error probability bound contains a literal `&` before the inequality sign.
- **Page 175:** Multiple displayed update, G, and Delta equations contain literal `&` alignment markers before equals signs.
- **Page 177:** All three displayed JC1 polynomial equations contain literal `&` alignment markers before equals signs.

The formulas otherwise remain legible and inside the text area. Strip alignment markers or construct proper aligned equations, then re-render affected pages.

## Smaller editorial typography issues

- **Pages 187, 188, 189 and 190:** Prose contains literal words such as `mathcal C_S` and `mathcal I_e(S)` where a typeset mathematical symbol or an ordinary phrase is intended. Example: page 187 “and mathcal C_S denotes” and “The symbol mathcal C_S”; page 188 “Identify mathcal C_S”; page 189 “does not define mathcal C_S”; page 190 “mathcal I_e(S)” and “Recover mathcal C_S”.
- **Pages 200 and 201:** A handful of retained source descriptions have omitted spaces: “inputs:1441objects”, “transfer:34recipes,32donor”, “actual54”, “query:16context”, “48case”, “selection:55917checks”, and “completion:64questions,32probes”. Source paths/hashes themselves are readable.

## Pages otherwise reviewed

161–165, 168, 170, 172, 174, 176, 178–186, 191–202 have no observed clipping, overlapping text, missing glyph boxes, unreadable equation text, or footer/page-number collision. Smaller prose issues noted above do not change that geometric assessment. Chapters and appendices start cleanly; source-register paragraphs fit the text area; headers/footers and page numbers are consistent.

The render does **not** pass final delivery QA until the broken tables and equation markers are corrected and the revised pages are inspected. All 42 assigned pages were reviewed; this was not a spot check.
