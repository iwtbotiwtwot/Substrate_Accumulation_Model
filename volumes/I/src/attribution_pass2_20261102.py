#!/usr/bin/env python3
"""Attribution pass 2 of 2 November 2026 (Sean Brady: the body of the work carries no person's or agent's name unless an outside
source is credited; appendix, source registers and citations point to the run, test or folder, to be replaced by SAMA entries).
Applies to the live sources only; retained_sources untouched. Each replacement asserted to match exactly once; logged."""
import json, re, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent; LOG = []
def rep(path, old, new, count=1, regex=False):
    p = ROOT / path; s = p.read_text()
    n = len(re.findall(old, s, flags=re.S)) if regex else s.count(old)
    assert n == count, f"{path}: expected {count} of {old[:70]!r}, found {n}"
    p.write_text(re.sub(old, new, s, flags=re.S) if regex else s.replace(old, new)); LOG.append({"file": path, "old": old[:160], "new": new[:160], "matches": n})
L = "live_sources"
# Chapter II
rep(f"{L}/ch02/chapter2_source_field_formatted.tex", r"\\noindent\[12\] voli\\_chapter2\\_physical3\\_20261015:[^\n]*",
    r"\\noindent[12] voli\\_chapter2\\_physical3\\_20261015: source-bound physical-development packet; GEN6 Duck run chapter2-physical-protocols-20261015-01 (Duck 1.2.2, core 0.10.2; 15 native tasks); H002635. Provenance trace: Courtroom~II case voli\\_provenance/01 (H002821).", regex=True)
rep(f"{L}/ch02/chapter2_source_field_formatted.tex", "\\noindent[1] Owner Chapter II draft and verification ZIP, 15 October 2026.", "\\noindent[1] Chapter II draft and verification ZIP, 15 October 2026 (H002634).")
# Chapter VII (and the expanded copy)
for f in (f"{L}/ch01/chapter1_as_vii.tex", f"{L}/ch01/chapter1_expanded.tex"):
    rep(f, "The weighted-form, reference, and Duhamel construction was written with OpenAI Codex in GEN6 Duck run chapter1-lane01-20261015-01 (Duck 1.2.2, core 0.10.2) under Sean Brady's direction, receiving the original source rules and retained hard preparation.",
        "The weighted-form, reference, and Duhamel construction receives the original source rules and retained hard preparation (GEN6 Duck run chapter1-lane01-20261015-01, Duck 1.2.2, core 0.10.2; H002630).")
    rep(f, "\\noindent[1] S. Brady. \\emph{Original Write histories and a coupled source-field action}, v1.1, 15 October 2026. Owner-supplied manuscript.",
        "\\noindent[1] \\emph{Original Write histories and a coupled source-field action}, v1.1, 15 October 2026. Supplied manuscript; GEN6 Duck runs write-coupling-clock-20261015-01 and chapter1-lane01-20261015-01 (H002628, H002630).")
    rep(f, "\\noindent[2] S. Brady. \\emph{A Reference-Centered Clock Positivity Condition}, 15 October 2026. Owner-supplied refinement note.",
        "\\noindent[2] \\emph{A Reference-Centered Clock Positivity Condition}, 15 October 2026. Supplied refinement note.")
    rep(f, "Owner-supplied roadmap;", "Supplied roadmap;")
# Chapter III
rep(f"{L}/ch03/chapter3_formatted.tex", "\\noindent[1] S. Brady. \\emph{Volume I, Chapter I}", "\\noindent[1] \\emph{Volume I, Chapter I}")
rep(f"{L}/ch03/chapter3_formatted.tex", r"\\noindent\[8\] S\. Brady\. \\emph\{Chapter III local action and actual clock continuation\}, \\nolinkurl\{voli_chapter3_local_action2_20261015\}, GEN6 Duck run chapter3-local-action-20261015-03 \(Duck 1\.2\.3, core 0\.10\.2; 17 native tasks\), directed by Sean Brady, selections and prose written with OpenAI Codex:",
    r"\\noindent[8] \\emph{Chapter III local action and actual clock continuation}, \\nolinkurl{voli_chapter3_local_action2_20261015}; GEN6 Duck run chapter3-local-action-20261015-03 (Duck 1.2.3, core 0.10.2; 17 native tasks); H002641:", regex=True)
# Chapter IV
rep(f"{L}/ch04/nonuniform_continuation.tex", r"This receiving construction was written with OpenAI Codex in campaign voli\\_chapter4\\_observation1\\_20261016 \(GEN6 Duck run chapter4-observation-20261016-01, Duck 1\.2\.3, core 0\.10\.2\) on the uniform theorem and residual-energy map computed there, under Sean Brady's direction\.",
    r"This receiving construction is developed in campaign voli\\_chapter4\\_observation1\\_20261016 (GEN6 Duck run chapter4-observation-20261016-01, Duck 1.2.3, core 0.10.2) on the uniform theorem and residual-energy map computed there.", regex=True)
rep(f"{L}/ch04/transport_continuation.tex", r"This propagation construction was written with OpenAI Codex in campaign voli\\_chapter4\\_observation1\\_20261016 \(GEN6 Duck run chapter4-observation-20261016-01, Duck 1\.2\.3, core 0\.10\.2\) under Sean Brady's direction, following",
    r"This propagation construction is developed in campaign voli\\_chapter4\\_observation1\\_20261016 (GEN6 Duck run chapter4-observation-20261016-01, Duck 1.2.3, core 0.10.2), following", regex=True)
rep(f"{L}/ch04/chapter.tex", "] S. Brady. ", "] ", count=5)
rep(f"{L}/ch04/continuum_update.tex", "The owner's review derives", "The Chapter IV review of 16 October 2026 (H002654) derives")
rep(f"{L}/ch04/radiation_energy_update.tex", "The owner's six-page review supplies", "The six-page Chapter IV review of 16 October 2026 (H002654) supplies")
# Chapter V
rep(f"{L}/ch05/chapter.tex", r"The following apparatus candidate was written with OpenAI Codex in\ncampaign .*?source--geometry law\.",
    "The following apparatus candidate is developed in campaign\nvoli\\\\_chapter5\\\\_localization2\\\\_20261016 (GEN6 Duck run\nchapter5-localization-20261016-01, Duck 1.2.3, core 0.10.2) on a fixed\nbackground; its exhaust and residual energy--momentum balance was checked\nby one native operator-word task\n(r2\\\\_source\\\\_law\\\\_photon\\\\_rocket\\\\_energy\\\\_recipient). It is not a selected SAM\nsource--geometry law.", regex=True)
rep(f"{L}/ch05/chapter.tex", "\\bibitem{unified} S. Brady.\n", "\\bibitem{unified}\n")
# Chapter VI
rep("ch06.tex", r"New constructions and finite parameter choices in this chapter were written with OpenAI Codex[^\n]*",
    r"New constructions and finite parameter choices in this chapter are developed in campaigns voli\\_chvi\\_foundation1, voli\\_chvi\\_source\\_decoder1, voli\\_chvi\\_detector\\_record1 and voli\\_chvi\\_shared\\_routes1 (17 October 2026; H002700, H002701, H002706), with finite matrices checked by native SLC-GEN5-R1 calls. Provenance trace: Courtroom~II case voli\\_provenance/01.", regex=True)
rep("vi_source/parts/foundation_overlap.tex", "The quadratic refinement and robustness corollaries in this section were\nderived with OpenAI Codex in campaign voli\\_chvi\\_foundation1\\_20261017\n(H002700) under Sean Brady's direction, with two native SLC-GEN5-R1\noperator-word checks.",
    "The quadratic refinement and robustness corollaries in this section are\ndeveloped in campaign voli\\_chvi\\_foundation1\\_20261017 (H002700), with two\nnative SLC-GEN5-R1 operator-word checks.")
rep("vi_source/parts/decoder_decoder.tex", "The decoder and bounds below were derived with OpenAI Codex in campaign\nvoli\\_chvi\\_source\\_decoder1\\_20261017 (H002701) under Sean Brady's\ndirection, from the retained Chapter~I clock observable and its\nChapter~VI route interpretation, with four native SLC-GEN5-R1 calls.",
    "The decoder and bounds below are developed in campaign\nvoli\\_chvi\\_source\\_decoder1\\_20261017 (H002701) from the retained\nChapter~I clock observable and its Chapter~VI route interpretation, with\nfour native SLC-GEN5-R1 calls.")
rep("vi_source/parts/record_memory_channel.tex", "The new instrument, finite-write estimate and correlated-hold bounds were\nderived with OpenAI Codex in campaign voli\\_chvi\\_detector\\_record1\\_20261017\nunder Sean Brady's direction, with four native SLC-GEN5-R1 calls.",
    "The new instrument, finite-write estimate and correlated-hold bounds are\ndeveloped in campaign voli\\_chvi\\_detector\\_record1\\_20261017, with four\nnative SLC-GEN5-R1 calls.")
rep("vi_source/parts/references.tex", "} S. Brady, ", "} ", count=6)
rep("vi_source/parts/references.tex", "S. Brady,\n", "", count=6)
# Chapter I credit paragraph (live body and derived body)
for f in ("ch01_concepts.tex", "body01_concepts.tex"):
    rep(f, r"Credit for the ideas is recorded as it fell\. Sean Brady:.*?Directed by Sean Brady\.",
        r"The provenance of these ideas and of the mathematical development they draw on is recorded outside the body of the volume: Courtroom~II case \\texttt{voli\\_provenance/01} (H002821) and the source registers of Chapters~II to~VII, which cite their runs, tests and folders.", regex=True)
# Appendix A
rep("closure_appendix.tex", "\\subsection*{Provenance and contribution statement}", "\\subsection*{Provenance}")
rep("closure_appendix.tex", r"Sean Brady is the project director\. The content of Chapters II--VII was produced.*?It does not claim a new native computation\.",
    "The content of Chapters II--VII was produced in GEN6 Duck runs on the Substrate Ledger Computer (15--17 October 2026; Duck 1.2.2 and 1.2.3, core 0.10.2), recorded in ironclad entries H002628--H002661 and H002700--H002706 and in the campaign folders cited in each chapter's source register; Chapter VI's derivations in the campaigns of 17 October 2026 with native SLC-GEN5-R1 checks; Chapters I and VIII--XIII from the record and from the first Courtroom's sealed CR results of June and July 2026. The co-authorship and in-chapter credits that earlier editions carried were removed on 2 November 2026; the trace is Courtroom~II case \\\\texttt{voli\\\\_provenance/01} (H002821, H002822). Provenance is cited by run, test and folder and will be replaced by SAMA entries as the atlas expands. The editorial synthesis of this appendix is based on the working edition of 19 October 2026 and claims no new native computation.", regex=True)
# Part 2 bibliographies
rep("ch07.tex", "\\item S. Brady, \\emph{SAM Unified Technical Synthesis, Volume I}", "\\item \\emph{SAM Unified Technical Synthesis, Volume I}")
rep("ch08.tex", "\\item S. Brady, \\emph{SAM Unified Technical Synthesis, Volume I}", "\\item \\emph{SAM Unified Technical Synthesis, Volume I}")
# Front matter (assembler): the paragraph after the note names no agent; revision paragraph updated
rep("assemble_first_edition_20261102.py", r"\\noindent\\small The trace behind this decision is Courtroom~II case.*?Directed by Sean Brady\. Executed with Claude Code\.",
    r"\\noindent\\small The trace behind this decision is Courtroom~II case \\texttt{voli\\_provenance/01\\_codex\\_credit\\_ledger} (ironclad H002821): every statement in the draft of 30 October 2026 that credited an AI collaborator with deriving, constructing, contributing or co-authoring, tied to the campaign, GEN6 Duck run, Duck and core version, native tasks and history entry that produced the content. The body of the volume now states its content without attribution to any person or instrument; outside sources are credited where they are used; appendix, source registers and citations point to the run, test or folder, to be replaced by SAMA entries as the atlas expands. The retained sources of 15 and 16 October 2026 under \\texttt{src/retained\\_sources} keep their recorded credits as history. Directed by Sean Brady. Executed with Claude Code.", regex=True)
rep("assemble_first_edition_20261102.py", "co-authorship credits to OpenAI ChatGPT and Codex removed throughout; chapter heads carry title and number only;",
    "co-authorship credits removed throughout; the body carries no person's or instrument's name except for outside sources; chapter heads carry title and number only;")
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG}, open(ROOT / "checks" / "attribution_pass2_20261102.json", "w"), indent=1)
print(f"{len(LOG)} replacements applied")
