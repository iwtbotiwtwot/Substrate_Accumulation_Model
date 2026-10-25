# Latest Volume I editable source recovery

Recovered read-only from iwtbotiwtwot/SAM_Research_Project, archived branch archive/phase2-discovery-final-20261017, pinned commit 6890eae4cb5f33c766c86ce10f43b5165a4c4157.

## Exact editable sources
- I: existing output/chapter1_expanded/chapter1_expanded.tex and included sections. Its rendered PDF matches latest uploaded volume pages 3–18, all 16 pages, under whitespace-normalized extracted text comparison.
- II: existing output/chapter2_source_field_formatted/chapter2_source_field_formatted.tex. Rendered PDF matches volume pages 19–31, all 13 pages.
- III: existing output/chapter3_formatted/chapter3_formatted.tex. Rendered PDF matches volume pages 32–44, all 13 pages.
- IV: IV/chapter.tex plus 36 companion TeX files from GEN4/voli_chapter4_preparation7_20261016/manuscript. Exact finite-preparation/switched-joint edition abstract and title. Original snapshot has two font/setup spelling defects: utf 8 and ps 2pk 35.map. Working-copy corrections are utf8 and ps2pk35.map. Original snapshot retained unchanged.
- V: V/chapter.tex is the latest source, from GEN4/voli_joint_measurement1_20261016/manuscript/ch5/chapter.tex. It includes the uploaded joint original-source protocol paragraph and compiles to 34 pages. V/chapter5_strong_fields.tex is the retained immediate predecessor from GEN4/voli_chapter5_localization2_20261016, not the latest manuscript entry point.
- VI: VI/chapter.tex plus parts/, proofs/, checks/new_rows.tex and external_references.tex from GEN4/voli_chvi_shared_routes1_20261017. Exact integrated 17 October title and abstract; all source fragments available. Includes three-page local contents that can be removed in unified publication.

## Authenticated graphics
The binary graphics were absent from Git tree but already present locally. SHA256 checks against their upstream retained manifests exactly match:
- IV/road_controls.pdf: 200cf87c8f013ba65390dd8df455bbd3a1a960bf26a110b21cc50bc55f6e5013
- IV/orbital_clock_controls.pdf: aafed8c32a69b1b1cb4ba76af5854a40ba78aafb4b18eb91b2a7aeaecd6afad1
- V/arrival_comparison.pdf: ed6ecbc0b1aa4f8a1af019c1d05963d6a6672878d309fa9f9c88e3253b5212c8
- VI/record_fringes.pdf: f522f5024370fd41145e78577a0f9b3e16bd352159eafb8e46a4a5c2319950d7

## Custody
RECOVERY_GIT_MANIFEST.json records source paths, original Git blob SHA1, recovery presence, and local SHA256. All 84 recovered text files match their exact pinned Git blob after correcting only the transfer wrapper's extra terminal newline. Sources are original, not PDF transcription. No native science or research scripts were executed; only TeX typesetting validation.

## Build environment
Use TEXMF=/usr/share/texlive/texmf-dist with writable format/cache path. Root prepared /tmp/volume_tex/pdflatex.fmt. Typical call: TEXMF=/usr/share/texlive/texmf-dist TEXFORMATS=/tmp/volume_tex TEXMFVAR=/tmp/volume_tex pdflatex -interaction=nonstopmode -halt-on-error chapter.tex. Two passes required for cross-references. The source fragments refer to current-directory paths; compile from each chapter directory or adjust paths in assembly working copies.
