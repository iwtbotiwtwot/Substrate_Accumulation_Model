# Substrate Accumulation Model — documentation and provenance record

The successor to the Courtroom repository. Courtroom discipline applies here to **documentation and provenance only**: every
statement about the three volumes says where it came from, every change to the living text is logged, and every run or test
that touches the work is recorded and committed when it concludes. Nothing here is a test harness and nothing is required to
be a test. Research runs execute in the `ironclad` repository (GEN6 Duck 2.0.0 and its method, `docs/DUCK_2.0_METHOD.md`
there); this repository holds what they mean for the volumes.

Sean Brady is the originator and conceptual director; OpenAI ChatGPT and Codex were research collaborators on earlier work
and keep their credit; Claude Code executes under Sean's direction.

## Layout

| path | what it holds |
|---|---|
| `volumes/Engine` | the authored SAM Engine Volume (SLC, GEN6 and the Duck: history, capabilities, method, connections to the volumes, collaborative examples), its `SOURCE.json` and `CHANGELOG.md`; no PDF source |
| `volumes/I`, `volumes/II`, `volumes/III` | the living Markdown of each volume (`SAM_Volume_*.md`), its `SOURCE.json` (PDF hash, pages, conversion), its `CHANGELOG.md`, and the source PDF under `source/` |
| `runs/` | one folder per run or test that bears on the volumes: `RECORD.md` from `templates/RUN_RECORD.md`, pointing at the ironclad campaign, commit and history entry; no bulk data |
| `decisions/DECISIONS.md` | Sean Brady's decisions, dated, in his words |
| `ideas/IDEAS.md` | ideas with status `open` / `adopted` / `dropped`; only Sean changes a status |
| `PROVENANCE.md` | how provenance is kept; the sources of record and their hashes (`SHA256SUMS`) |
| `scripts/conclude.sh` | the end-of-run procedure: hash, record, commit, sync |
| `CLAUDE.md` | standing instructions for every session in this repository |

## The one rule that is a procedure

At the conclusion of any run or test, before anything else: write the run record, update the volume text and its change log if
the run touched them, refresh `SHA256SUMS`, commit, and push. `scripts/conclude.sh "<message>"` does the mechanical part and
refuses to proceed if a run record is missing for a `runs/` folder.
