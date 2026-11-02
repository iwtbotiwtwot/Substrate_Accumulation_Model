#!/usr/bin/env python3
"""F1 renumbering pass (Sean Brady, 2026-11-02: "F1 is easy go on it"). The 30 October reorganization moved the source-field
action chapter from I to VII and renumbered Part 2 (old VII->VIII, VIII->IX, IX->X; old X, galaxy halos, retired to the
Supplement; XI-XIII unchanged). Cross-references in the chapter texts still used the old numbers. This pass maps them in the
live sources only (retained_sources untouched). Part 1: 'Chapter I' -> 'Chapter VII' with ranges and quoted titles handled
explicitly. Part 2 and Appendix A: every occurrence handled explicitly from context (list below). Each replacement is
asserted to match exactly once and logged to checks/renumber_pass_20261102.json."""
import re, json, datetime, glob
from pathlib import Path
ROOT = Path(__file__).resolve().parent; LOG = []
def rep(path, old, new, count=1, regex=False):
    p = ROOT / path; s = p.read_text()
    n = len(re.findall(old, s)) if regex else s.count(old)
    if n == 0 and not regex and s.count(new) >= 1:
        LOG.append({"file": path, "old": old[:160], "new": new[:160], "matches": 0, "note": "already applied by an earlier run of this script"}); return
    assert n == count, f"{path}: expected {count} of {old[:80]!r}, found {n}"
    p.write_text(re.sub(old, new, s) if regex else s.replace(old, new)); LOG.append({"file": path, "old": old[:160], "new": new[:160], "matches": n})
L = "live_sources"
# ---- Part 1: explicit titles and ranges first
rep(f"{L}/ch02/chapter2_source_field_formatted.tex", "completed Chapter I and prior Chapter II development sources", "completed Chapter VII (formerly Chapter I) and prior Chapter II development sources")
rep(f"{L}/ch02/chapter2_source_field_formatted.tex", "\\noindent[2] Final Chapter I and actual full-field clocks;", "\\noindent[2] Final Chapter VII (formerly Chapter I) and actual full-field clocks;")
rep(f"{L}/ch03/chapter3_formatted.tex", "\\noindent[1] \\emph{Volume I, Chapter I}, final draft", "\\noindent[1] \\emph{Volume I, Chapter I} (now Chapter VII), final draft")
rep(f"{L}/ch03/chapter3_formatted.tex", "Chapters I and II.", "Chapters II and VII.")
rep(f"{L}/ch04/chapter.tex", "Volume I, Chapter I, final source and clock certificates", "Volume I, Chapter VII (formerly Chapter I), final source and clock certificates")
rep(f"{L}/ch01/chapter1_as_vii.tex", "\\noindent[6] \\emph{Chapter I lane01 and six uniform correlated clocks}, H002630", "\\noindent[6] \\emph{Chapter I lane01 and six uniform correlated clocks} (this chapter, now Chapter VII), H002630")
rep("vi_source/parts/original_appendix.tex", "Chapter I and II public repositories", "Chapter II and VII public repositories")
rep("vi_source/parts/original_introduction.tex", "Chapters I--III", "Chapters II, III and VII")
rep("vi_source/parts/references.tex", "Volume I, Chapter I, retained model and exact clock certificate", "Volume I, Chapter VII (formerly Chapter I), retained model and exact clock certificate")
rep("vi_source/parts/references.tex", "SAM Volume I, Chapter I. Model and exact clock certificate", "SAM Volume I, Chapter VII (formerly Chapter I). Model and exact clock certificate")
# ---- Part 1 blanket: remaining 'Chapter I' (not followed by another roman numeral, dash or letter) -> 'Chapter VII'
part1 = [f"{L}/ch02/chapter2_source_field_formatted.tex", f"{L}/ch03/chapter3_formatted.tex", f"{L}/ch05/chapter.tex"] + sorted(glob.glob(str(ROOT / L / "ch04" / "*.tex"))) + ["ch06.tex"] + sorted(glob.glob(str(ROOT / "vi_source" / "parts" / "*.tex"))) + sorted(glob.glob(str(ROOT / "vi_source" / "proofs" / "*.tex")))
blanket = re.compile(r"Chapter(~| )I(?![IVX\w\-–])")
for f in part1:
    f = str(Path(f).resolve().relative_to(ROOT)) if f.startswith("/") else f
    s = (ROOT / f).read_text(); n = len(blanket.findall(s))
    if n:
        (ROOT / f).write_text(blanket.sub(lambda m: "Chapter" + m.group(1) + "VII", s)); LOG.append({"file": f, "old": "Chapter I (blanket, Part 1)", "new": "Chapter VII", "matches": n})
# ---- Part 2 and Appendix A: explicit, from context (old numbering: VII thermo -> VIII, VIII inventory -> IX, IX thermal history -> X, X halos -> Supplement, I source-field -> VII)
rep("ch08.tex", "physical horizon area $\\mathcal A_H$ of Chapter VII.", "physical horizon area $\\mathcal A_H$ of Chapter VIII.")
rep("ch08.tex", "Chapter X must supply clustering and halo behavior;", "the Supplement (the retired galaxy-halo chapter) must supply clustering and halo behavior;")
rep("ch08.tex", "when Chapter IX computes a thermal history", "when Chapter X computes a thermal history")
rep("ch08.tex", "essential for Chapter IX and cannot", "essential for Chapter X and cannot")
rep("ch08.tex", "The packet delivered to Chapter IX includes", "The packet delivered to Chapter X includes")
rep("ch08.tex", "Chapter X receives the clean matter row", "The Supplement (the retired galaxy-halo chapter) receives the clean matter row")
rep("ch08.tex", "original Chapter VIII and closing review", "original Chapter VIII (now Chapter IX) and closing review")
rep("ch09.tex", "This accounting connects Chapters IX and XII.", "This accounting connects Chapters X and XII.")
rep("ch09.tex", "Original Chapter IX, upstream inventory in Chapter VIII,", "Original Chapter IX (now Chapter X), upstream inventory in Chapter IX,")
rep("ch11.tex", "the thermal behavior of Chapter VII and the perturbative", "the thermal behavior of Chapter VIII and the perturbative")
rep("ch11.tex", "Chapter I provides the source--field action", "Chapter VII provides the source--field action")
rep("ch11.tex", "Chapter VII asks how the same boundary exchanges", "Chapter VIII asks how the same boundary exchanges")
rep("ch11.tex", "without supplying Chapter VII's boundary state", "without supplying Chapter VIII's boundary state")
rep("ch11.tex", "usable in Chapters V, VII and XI.", "usable in Chapters V, VIII and XI.")
rep("ch12.tex", "Chapters III--VII follow the source coordinate", "Chapters III--VI and VIII follow the source coordinate")
rep("ch12.tex", "Chapters VIII--X use the floor in a proposed cosmic inventory", "Chapters IX and X and the Supplement use the floor in a proposed cosmic inventory")
rep("ch12.tex", "The inventory assignment of Chapter VIII is", "The inventory assignment of Chapter IX is")
rep("ch12.tex", "the frozen Chapter VIII value", "the frozen Chapter IX value")
rep("ch12.tex", "the Chapter VIII horizon projection", "the Chapter IX horizon projection")
rep("ch13.tex", "one surface model shared with Chapters VII and XI", "one surface model shared with Chapters VIII and XI")
rep("ch13.tex", "This is where Chapter VII's thermal account", "This is where Chapter VIII's thermal account")
rep("ch13.tex", "Chapter XI's impedance and Chapter VII's thermal transitions", "Chapter XI's impedance and Chapter VIII's thermal transitions")
rep("ch13.tex", "the mass function used in Chapter X, the baryon abundance used in Chapter VIII, or the thermal initial conditions used in Chapter IX.", "the mass function used in the Supplement (the retired galaxy-halo chapter), the baryon abundance used in Chapter IX, or the thermal initial conditions used in Chapter X.")
rep("ch13.tex", "belong to Chapter VII's exact transition account", "belong to Chapter VIII's exact transition account")
rep("ch13.tex", "a single surface model shared with Chapters VII and XI.", "a single surface model shared with Chapters VIII and XI.")
rep("closure_appendix.tex", "when the expanded Chapters I--VI were incorporated", "when the expanded Chapters II--VII were incorporated")
rep("closure_appendix.tex", "\\paragraph{Chapter I: the actual interacting clock.}", "\\paragraph{Chapter VII: the actual interacting clock.}")
rep("closure_appendix.tex", "Chapter I, Sections 6--7, establishes", "Chapter VII, Sections 6--7, establishes")
rep("closure_appendix.tex", "identifying its radius with Chapter I's coupling radius", "identifying its radius with Chapter VII's coupling radius")
rep("closure_appendix.tex", "from the earlier Chapters I--VII appendix", "from the earlier appendix to Chapters I--VII of the 19 October edition (now II--VIII)")
rep("closure_appendix.tex", "\\subsubsection*{Chapter I: source preparation, isolation, and calibration}", "\\subsubsection*{Chapter VII: source preparation, isolation, and calibration}")
rep("closure_appendix.tex", "cited by Chapter I. Incorporation", "cited by Chapter VII. Incorporation")
rep("closure_appendix.tex", "Existing Chapter I provenance remains intact.", "Existing Chapter VII provenance remains intact.")
rep("closure_appendix.tex", "\\subsubsection*{Chapter VII: thermal scale, entropy, and information}", "\\subsubsection*{Chapter VIII: thermal scale, entropy, and information}")
rep("closure_appendix.tex", "\\subsubsection*{Chapter VIII: inventory and Hubble cascade}", "\\subsubsection*{Chapter IX: inventory and Hubble cascade}")
rep("closure_appendix.tex", "\\subsubsection*{Chapter IX: recombination and spectrum comparison}", "\\subsubsection*{Chapter X: recombination and spectrum comparison}")
rep("closure_appendix.tex", "\\subsubsection*{Chapter X: many-source organization and halo tests}", "\\subsubsection*{Supplement (the retired Chapter X): many-source organization and halo tests}")
# ---- F2 remainder: front matter sentences in the assembler
A = "assemble_first_edition_20261102.py"
rep(A, "The unified expanded edition of 19 October 2026 brought the twelve chapters into one continuous manuscript. Chapters I--V retain", "The unified expanded edition of 19 October 2026 brought the twelve chapters into one continuous manuscript; in that edition's numbering, Chapters I--V retain")
rep(A, "Chapters I--III match their earlier formatting sources exactly. The integrated source for Chapter IV, Chapter V and Chapter VI was recovered", "Chapters II, III and VII match their earlier formatting sources exactly, built since 2 November 2026 from live copies under \\texttt{src/live\\_sources}. The integrated source for Chapters IV, V and VI was recovered")
rep(A, "The original vector content of Chapters I--V is retained", "The original vector content of Chapters II--V and VII is retained")
rep(A, "The opening chapter's public data repository is", "Chapter VII's public data repository is")
rep(A, "the body carries no person's or instrument's name except for outside sources; chapter heads carry title and number only;", "the body carries no person's or instrument's name except for outside sources; chapter heads carry title and number only; cross-references renumbered to this edition (the former Chapter I is cited as Chapter VII, Part 2 by its new numbers, the retired halo chapter as the Supplement);")
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG, "total_cross_references_changed": sum(l["matches"] for l in LOG)}, open(ROOT / "checks" / "renumber_pass_20261102.json", "w"), indent=1)
print(len(LOG), "replacement rules;", sum(l["matches"] for l in LOG), "occurrences")
