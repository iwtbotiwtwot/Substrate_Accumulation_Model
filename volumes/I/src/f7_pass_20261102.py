#!/usr/bin/env python3
"""F7 pass (Sean Brady, 2026-11-02: "go" on the two-sentence readback after Courtroom II voli_metric/02 HELD). Two sentences in
Chapter I (ch01_concepts.tex and its derived body01_concepts.tex); Appendix A II.2 unchanged. Each replacement asserted once; logged."""
import json, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent; LOG = []
E = [
 ("the alternative, background-normalized reading rescales the lift by $1/(1-A_0)$ and is labeled as a convention wherever it appears.",
  "the alternative, background-normalized reading would multiply every redshift coefficient by $1/(1-A_0)=1.0272$; with the gravitational calibration held fixed from orbit, the Gravity Probe~A and Tokyo Skytree redshift tests bound that factor at the $10^{-4}$ level, so the alternative is excluded, not conventional (Courtroom~II \\texttt{voli\\_metric/02})."),
 ("\\emph{Declared}: the radial ruler reading, tested by Cassini; the source-only convention for the floor;",
  "\\emph{Declared}: the radial ruler reading, tested by Cassini; the source-only reading of the floor, its alternative excluded by redshift tests (\\texttt{voli\\_metric/02});"),
]
for f in ("ch01_concepts.tex", "body01_concepts.tex"):
    p = ROOT / f; s = p.read_text()
    for old, new in E:
        n = s.count(old); assert n == 1, f"{f}: {n} of {old[:60]!r}"
        s = s.replace(old, new); LOG.append({"file": f, "old": old[:160], "new": new[:160]})
    p.write_text(s)
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG}, open(ROOT / "checks" / "f7_pass_20261102.json", "w"), indent=1)
print(len(LOG), "replacements applied")
