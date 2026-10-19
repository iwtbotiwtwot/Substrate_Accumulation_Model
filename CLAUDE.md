# CLAUDE.md — Substrate Accumulation Model (documentation and provenance)

Read in full before doing anything in this repository. The research rules of the ironclad repository's CLAUDE.md (roles,
ideas versus instructions, tiers, attribution, reporting registers, Duck change control §13) apply here unchanged; this file
adds what is specific to this repository.

## 1. Purpose and scope

- This repository documents the three volumes of the Substrate Accumulation Model and the provenance of every statement made
  about them. It is the Courtroom's successor for **documentation and provenance only** (Sean Brady, 2026-10-19: "I only want to
  apply courtroom discipline to documentation and provenance I don't want to make everything a test").
- Research runs happen in `ironclad`. Here they are recorded, interpreted for the volumes, and linked by commit, campaign path
  and history entry. Bulk data never comes here; hashes do.
- The living text of each volume is `volumes/<N>/SAM_Volume_<N>.md`. It is edited in place. Every edit is one line in the
  volume's `CHANGELOG.md` naming the run or decision it came from. The source PDF and its hash stay in `source/` and
  `SOURCE.json`; the living text may depart from the PDF, and the change log is the record of how.

## 2. Procedure at the conclusion of any run or test (mandatory)

Sean Brady, 2026-10-19: "I am terrible at remembering to commit and sync that should be procedure at the conclusion of any run
or 'test'." Therefore, when a run or test concludes, in this order and before reporting to Sean:

1. `runs/<date>_<name>/RECORD.md` from `templates/RUN_RECORD.md`: what ran, where (ironclad campaign path, commit, history
   entry), what it showed with the four tags, what it changes or opens in which volume and chapter, what failed.
2. If the run changes the living text: edit `volumes/<N>/SAM_Volume_<N>.md`, add the line to `CHANGELOG.md`.
3. Ideas to `ideas/IDEAS.md` (status `open`); Sean's decisions to `decisions/DECISIONS.md` in his words.
4. `scripts/conclude.sh "<message>"`: refreshes `SHA256SUMS`, checks every `runs/` folder has a `RECORD.md`, commits everything,
   pushes `main`. If the push is refused by the environment, print the exact command for Sean to run and say so in the report.
5. Report to Sean with the commit hash. A run is not concluded until step 4 has happened.

The same procedure is written into ironclad's CLAUDE.md §14 for runs recorded there.

## 3. Writing in the volumes

- Engineering labels only for run outcomes; the three classification phrases of the Courtroom are never used here unless Sean
  issues one himself.
- Every number in the living text that came from a run carries its source in a footnote or a change-log line: campaign,
  result key, commit.
- When something is an idea, say so; when it is a reading of a declared chart, say so; when it is the manuscript's own prior
  statement, cite the page marker.
- Directed by Sean Brady. Executed with Claude Code. Earlier credit (ChatGPT, Codex) is never removed.

## 4. Hardware and environment

As in ironclad's CLAUDE.md §12: T500 (this machine) runs everything; the i9 is a read-only archive; no CUDA anywhere.
