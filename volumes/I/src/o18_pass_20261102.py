#!/usr/bin/env python3
"""O18 pass (Sean Brady, 2026-11-02): the magic bell's question stated as it arose; what the magic is named; the answer withheld for
the reader; Section 8's 'third reading' collision with Section 4 fixed; Section 11 register line. Applied to ch01_concepts.tex and
its derived body01_concepts.tex; each replacement asserted once; logged."""
import json, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent; LOG = []
E = [
 ("The question that separated the clock from the road was practical: how can accumulation be reconciled with the need to adjust the clocks in GPS satellites? The thought experiment that answered it is the magic bell.",
  "The question that separated the clock from the road was practical and, at the time, unanswerable in concept: if accumulation is correct and a road delay exists, why do the clocks in GPS satellites need adjusting at all? The thought experiment that met it is the magic bell, and it was the first place the clock and the road appeared as two separate effects."),
 ("The question is not answered in this volume, by decision. Its value is the two things it forces apart.",
  "The bell is the magic: it is granted knowledge, on one planet, of the moment of an event on the other, which no signal can supply. The volume does not answer the question; the reader is invited to. Its value here is the two things it forces apart."),
 ("The clock in motion is the third reading of the lift, after the clock at rest and the ruler, and Chapter~IV develops it.",
  "The clock in motion is the clock reading of Section~\\ref{sec:c1-readings} extended to a moving clock, and Chapter~IV develops it."),
 ("The question of the magic bell is open by decision.", "The magic bell is a thought experiment, not a test; the volume leaves its question to the reader."),
]
for f in ("ch01_concepts.tex", "body01_concepts.tex"):
    p = ROOT / f; s = p.read_text()
    for old, new in E:
        n = s.count(old); assert n == 1, f"{f}: {n} of {old[:60]!r}"
        s = s.replace(old, new); LOG.append({"file": f, "old": old[:160], "new": new[:160]})
    p.write_text(s)
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG}, open(ROOT / "checks" / "o18_pass_20261102.json", "w"), indent=1)
print(len(LOG), "replacements applied")
