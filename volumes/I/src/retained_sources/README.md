# Editable baseline: Volume I, Chapters I–V

These sources retain the submitted manuscript text. The final unified volume retains the original vector page content for these chapters, with harmonized headers and continuous folios. These files are supplied so the baseline remains editable.

Build each chapter from its own directory with pdfLaTeX, twice, using the entrypoint listed below. Standard TeX Live packages are required. I–III are self-contained TeX. IV uses the companion TeX inputs and two supplied figures. V is self-contained TeX plus its supplied figure.

| Chapter | Entrypoint | Submitted pages |
|---|---|---|
| I | ch01/chapter1_expanded.tex | 3–18 (16 pages) |
| II | ch02/chapter2_source_field_formatted.tex | 19–31 (13 pages) |
| III | ch03/chapter3_formatted.tex | 32–44 (13 pages) |
| IV | ch04/chapter.tex | 45–110 (66 pages) |
| V | ch05/chapter.tex | 111–144 (34 pages) |

For IV only, make these two build-configuration corrections in a working copy before compiling: replace [utf 8] with [utf8], and ps 2pk 35.map with ps2pk35.map. The supplied original source keeps its exact pinned bytes; these fixes affect encoding/font-map setup only, not manuscript text.

## Provenance
I–III sources are retained from their local formatting packages. Their original compiled PDFs match every page of the uploaded 244-page complete volume under whitespace-normalized text comparison. IV–V were recovered read-only from iwtbotiwtwot/SAM_Research_Project, archive/phase2-discovery-final-20261017, commit 6890eae4cb5f33c766c86ce10f43b5165a4c4157.
IV: GEN4/voli_chapter4_preparation7_20261016/manuscript.
V: GEN4/voli_joint_measurement1_20261016/manuscript/ch5/chapter.tex.
All recovered TeX files match pinned Git blob SHA1. All three supplied figures match upstream SHA256 manifests exactly. RECOVERY_REPORT.md documents the recovery. SHA256SUMS.json inventories this delivery tree. No research, remote or native computation scripts are included or required.

## Rebuild content check
IV rebuilt to 66 pages; V rebuilt to 34 pages. After Unicode ligature normalization, whitespace/hyphen normalization and removal of repeated headers/folios, all 244,436 IV characters and all 125,389 V characters are retained. IV has six extraction-order relocations involving Tables 5–8 and its two figures. V has one relocation involving Figure 1 and caption. These are PDF reading-order/float placement differences; per-page text equality is not claimed for regenerated IV–V. The final volume uses the original vector pages for those chapters.
