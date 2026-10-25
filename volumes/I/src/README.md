# SAM Volume I — unified expanded edition

## Deliverables and scope

This package builds the complete twelve-chapter PDF, not a replacement for only the later chapters. `assets/ch01_retained.pdf` through `ch05_retained.pdf` preserve the submitted mathematical content. Their editable sources are under `retained_sources/`. `ch06.tex` and `vi_source/` retain the latest integrated quantum chapter in the common two-column layout, without its separate contents. `ch07.tex` through `ch12.tex` are expanded chapter bodies. `closure_appendix.tex` replaces the previous closing review and interface appendix with an evidence reconciliation.

The volume uses Letter paper, Times-family text, two columns for chapters, a single contents list, one continuous page sequence, and chapter-local equation/reference numbering. The front matter explicitly preserves the distinct contributor histories.

## Build

Requirements: Python 3, PyMuPDF (`fitz`), NumPy for the page comparison, a normal pdfLaTeX/TeX Live installation including the packages listed in `preamble.tex`, and Matplotlib only if regenerating the explanatory plots.

From this directory:

1. Run `python figures/make_explanatory_figures.py` if regenerating the new figures; the supplied vector PDFs can otherwise be used directly.
2. Run `python build_new_chapters.py` to build Chapters VI–XII and the evidence appendix. This runs pdfLaTeX twice for each chapter.
3. Run `python assemble_volume.py` to build the three-page front matter and combine all chapters with harmonized headers, folios and bookmarks.
4. Run the standalone `checks/check_ch*.py` programs for the new arithmetic examples. These do not require GEN6 or any remote service.

The assembled PDF is written in the sibling `pdf/` directory. Keep the directory structure when rebuilding. If editing an early chapter, run `python rebuild_retained.py` to compile the retained source trees, replace the matching baseline PDFs, and then reassemble. The helper applies the two documented Chapter IV build-configuration spelling fixes in a working copy. The assembly script derives chapter page positions from the actual PDFs.

## What was and was not verified

The new check scripts verify specified algebraic and numerical examples. The source-recovery manifest pins the recovered archived manuscript files. The assembly checks verify page sizes, running folios, retained body content, chapter coverage and selected text properties. Rendered-page inspection checks typesetting, including equation overflow and figure readability.

No new native GEN6 campaign, SPARC fit, CMB likelihood, black-hole simulation, or experimental run was carried out to create this edition. Historical receipt counts and result statements retain their original scope. A typesetting or arithmetic check is not an independent verification of every physical claim in a manuscript of this size.

## Evidence and provenance

The uploaded complete manuscript of 19 October 2026 is the content baseline. Chapters I–III exactly match the earlier local formatting PDFs. Sources for the current IV–VI were recovered from `iwtbotiwtwot/SAM_Research_Project`, branch `archive/phase2-discovery-final-20261017`, commit `6890eae4cb5f33c766c86ce10f43b5165a4c4157`. The pinned paths and SHA checks are recorded in the provenance files.

This compact package does not redistribute the full historical native-evidence archives. The original chapters identify those records. Retained baseline pages are included to avoid silently replacing a newer result with an older editable predecessor.
