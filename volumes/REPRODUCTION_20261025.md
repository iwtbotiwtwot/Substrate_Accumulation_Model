# Reproduction build of the three volumes from their imported sources (2026-10-25)

Sean Brady: "Plan approved, installing texlive now- go on the reproduction build". TeX Live (XeLaTeX, pdfLaTeX) installed by Sean Brady; PyMuPDF 1.23.7 present.
Each volume built in a scratch copy of `volumes/<V>/src`; the repository sources were not modified except the one line noted. Comparison: `pdftotext -layout` page
texts of the rebuilt PDF against the recorded source PDF, page by page, whitespace-normalised.

| Volume | Source build | Rebuilt pages | Source pages | Pages with identical text | Remaining differences |
|---|---|---:|---:|---:|---|
| I | pdfLaTeX chapters VI–XII + appendix, PyMuPDF assembly with retained I–V | 240 | 240 | 125 of 240 | 115 pages at similarity ≥ 0.999: column-order and glyph artefacts of text extraction (e.g. a minus sign, a ligature), no word differences |
| II | XeLaTeX, three passes | 99 | 99 | 87 of 99 | 12 pages at similarity ≥ 0.9895: the same sentences extracted in a different column order |
| III (expanded, 107 pp) | XeLaTeX, three passes | 107 | 107 | 100 of 107 | 7 pages at similarity ≥ 0.9867: same cause |

Builds completed without errors; the XeLaTeX logs carry 116 (II) and 180 (III) over/underfull box notices, as the originals did. One fix was needed: Volume I's
`assemble_volume.py` called `apply_redactions(images=0, graphics=0)`, a keyword PyMuPDF 1.23.7 lacks; the repository copy now falls back without it. The six new
chapters of the Volume III Revised edition were converted from Markdown to LaTeX with pandoc 3.6.4 (`--top-level-division=chapter`, no warnings; tables as
longtable) into `volumes/III/src/revised_20261020/latex_from_md/` for insertion in the 28-chapter order of `manuscript/CHAPTERS.json`.

Reading: the imported sources are the volumes. Every later change is measured against these builds. Directed by Sean Brady. Executed with Claude Code.
