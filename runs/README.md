# Runs

One folder per run or test that bears on the volumes, named `<YYYYMMDD>_<name>`, holding `RECORD.md` from
`../templates/RUN_RECORD.md`. The record points at ironclad; it does not copy data. `scripts/conclude.sh` refuses to commit while
a run folder lacks its record.
