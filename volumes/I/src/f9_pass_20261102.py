#!/usr/bin/env python3
"""F9 (Sean Brady, 2026-11-02: "go on F9"). Appendix A IX.1-IX.3 still instructed a check of the draft's second-peak comparator 520;
Chapter X already carries the corrected comparator. Planck 2015 results I, Table 7 (verified from the paper 2026-11-02): peaks
220.0+-0.5, 537.5+-0.7, 810.8+-0.7. One sentence replaced; asserted once; logged."""
import json, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent
old = "The earlier review identifies a likely second-peak comparator error: the draft's $520$ must not be retained without checking the cited peak definition and dataset."
new = "The earlier comparator's second peak, $520$, was a transcription error. The published Planck positions are $(220.0\\pm0.5,\\ 537.5\\pm0.7,\\ 810.8\\pm0.7)$ (Planck 2015 results I, Table 7), against the reported SAM peaks $(220,535,812)$, a $-0.47\\%$ difference at the second peak, as Chapter~X now states; an identical-estimator reanalysis remains outstanding."
p = ROOT / "closure_appendix.tex"; s = p.read_text(); assert s.count(old) == 1; p.write_text(s.replace(old, new))
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": [{"file": "closure_appendix.tex", "old": old, "new": new}],
           "source_verified": "Planck Collaboration, Planck 2015 results. I., A&A 594, A1 (2016); arXiv:1502.01582 Table 7 'Planck peak positions and amplitudes': 220.0+-0.5, 537.5+-0.7, 810.8+-0.7 (read 2026-11-02)"},
          open(ROOT / "checks" / "f9_pass_20261102.json", "w"), indent=1); print("1 replacement applied")
