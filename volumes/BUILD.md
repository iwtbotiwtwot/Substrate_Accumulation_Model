# Building the volumes from source (2026-10-25)

The living texts are the typeset sources under `volumes/<V>/src/`; PDFs are derived from them and the pdftotext dumps are retired to the conversion record.
Provenance and hashes: `volumes/SRC_MANIFEST_20261025.json`.

| Volume | Source | Engine | Build |
|---|---|---|---|
| I | `volumes/I/src` (ch06–ch12.tex, closure_appendix.tex, preamble.tex; Chapters I–V as retained PDFs in `assets/` with their .tex under `retained_sources/`) | pdfLaTeX | `python build_new_chapters.py` then `python assemble_volume.py` (needs PyMuPDF `fitz`, NumPy) |
| II | `volumes/II/src` (main.tex, preamble.tex, 19 chapter files, bibliography.tex, figures/) | XeLaTeX (`xdvipdfmx`) | `xelatex main.tex` ×3 |
| III | `volumes/III/src/expanded_20261019` (book.tex, 22 chapter files) as the LaTeX base; `volumes/III/src/revised_20261020` for the 191-page chapter order (`manuscript/CHAPTERS.json`) and the six new chapters (Markdown, to be converted to LaTeX with pandoc and inserted in that order) | XeLaTeX; pandoc for the six Markdown chapters | `xelatex book.tex` ×3 after the six chapters are converted and included |

Tooling present on this machine: pandoc 3.6.4 (`~/.local/bin`), LibreOffice, pdftotext/pdfinfo, NumPy, Pillow. Missing: a TeX distribution with XeLaTeX and
pdfLaTeX (Times-family fonts, hyperref, the packages in each preamble), PyMuPDF, python-docx (only for rebuilding the Revised DOCX; not needed for the LaTeX route).
Install options: `sudo apt install texlive-xetex texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra python3-pip python3-fitz` (system), or allow the
Tectonic static binary download (user-local, no root). The first build step is a byte-for-page reproduction of the three current PDFs before any edit.
