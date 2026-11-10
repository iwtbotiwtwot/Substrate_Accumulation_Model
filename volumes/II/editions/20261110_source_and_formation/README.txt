SAM Volume II - Matter and Finite Closure
Revised source and formation edition, 10 November 2026
Sean Brady

DELIVERY
pdf/SAM_Volume_II_Revised_Edition_20261110.pdf - 117-page revised edition.
src/ - complete editable XeLaTeX source and both retained scientific figures.
evidence/ - 40 selected report, proof and response-operand snapshots.
EVIDENCE_MANIFEST.json - original locations and SHA-256 hashes of those snapshots.
COVERAGE.json - new claims and source-to-chapter map.
baseline/ - hashes and metadata identifying the unchanged prior manuscript.
qa/ - final build, reference/credit/custody checks and page review record.

The prior 5 November PDF and all original Volume II files remain unchanged.
This copy expands Chapters XI, XII and XVI and adds two appendices. Chapter V
has a revised contextual bridge and a table layout repair; its historical
numerical comparisons are unchanged. The PDF contains no Codex/OpenAI credits.

BUILD
Install XeLaTeX with the standard packages named in src/preamble.tex, then run:
  bash build.sh
The script builds in tmp/pdfs/build, performs three passes, and writes the PDF
and logs to the paths above. It needs no scientific engine or campaign rerun.
The output's contents and pagination are reproducible; PDF creation timestamps
can alter its byte hash.

EVIDENCE AND SCOPE
He3, free-reference, shared-field covariance and the nine Li6 claims retain
their completed internal separate-proof/code verification. Latest arrival,
loading, response, battery/clock and thermal constructions retain their stated
conditional analytical and internal-check scope. No new physical binding fit,
unit assignment, research window or remote push was performed for this edition.
The evidence snapshots are a reading packet, not the full scientific replay
archives. The owning paths in EVIDENCE_MANIFEST.json locate complete artifacts.

REVIEW
117 pages rendered with Poppler and reviewed in ten contact sheets; selected
new equation/table pages inspected at page scale. All original-file hashes
match. No unresolved citations/references, duplicate labels, overflowing boxes,
missing characters or out-of-page text were found. Both original figures are
retained. See qa/EDITION_CHECK.json and qa/VISUAL_REVIEW.json.

qa/check_edition.py performs local integration and preservation checks using
PyMuPDF. Its original-file comparison assumes the repository directory layout;
the supplied receipts remain available in the standalone source bundle.
prepare_evidence.py refreshes snapshots from the owning local repository only.
It is not needed to build the manuscript from this package.
