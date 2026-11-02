#!/usr/bin/env python3
"""Attribution pass of 2 November 2026 (Sean Brady's decision of 2026-11-02, citing Courtroom II voli_provenance/01, H002821).
Removes Codex, ChatGPT and OpenAI from every form of authorship in the live Volume I sources; strips authorship and dates from
chapter heads; replaces each body credit sentence with the provenance the ledger established. Retained sources are not touched:
live copies are made under live_sources/. Every replacement is asserted to match exactly once and logged to
checks/attribution_pass_20261102.json. Standard library only."""
import shutil, json, re, hashlib, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent
LOG = []
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rep(path, old, new, count=1, regex=False):
    p = ROOT / path; s = p.read_text()
    n = len(re.findall(old, s)) if regex else s.count(old)
    assert n == count, f"{path}: expected {count} match(es) of {old[:60]!r}, found {n}"
    s2 = re.sub(old, new, s) if regex else s.replace(old, new)
    p.write_text(s2); LOG.append({"file": str(path), "old": old[:200], "new": new[:200], "matches": n})

# 1. live copies of the retained sources
for n in (1, 2, 3, 4, 5):
    src, dst = ROOT / "retained_sources" / f"ch{n:02d}", ROOT / "live_sources" / f"ch{n:02d}"
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src, dst)
LOG.append({"step": "live_sources copied from retained_sources ch01..ch05; retained_sources untouched"})

L = "live_sources"
STAMP = "First edition draft, 2 November 2026"
# pdfauthor and running headers in the five live chapters
for f in (f"{L}/ch01/chapter1_as_vii.tex", f"{L}/ch01/chapter1_expanded.tex", f"{L}/ch02/chapter2_source_field_formatted.tex",
          f"{L}/ch03/chapter3_formatted.tex", f"{L}/ch04/chapter.tex", f"{L}/ch05/chapter.tex"):
    rep(f, "pdfauthor={Sean Brady; OpenAI ChatGPT and Codex}", "pdfauthor={Sean Brady}")
    d = "16" if "ch04" in f or "ch05" in f else "15"
    rep(f, "\\fancyhead[R]{\\footnotesize Brady \\;|\\; " + d + " October 2026}", "\\fancyhead[R]{\\footnotesize " + STAMP + "}")

# chapter heads: title, chapter number only
rep(f"{L}/ch01/chapter1_as_vii.tex",
    "{\\large Volume I, Chapter VII \\textbullet\\ text of 15 October 2026\\par}\n\\vspace{0.5em}\n{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small OpenAI ChatGPT and Codex \\textbullet\\ AI research collaborators and co-authors\\par}\n{\\small Expanded chapter edition \\textbullet\\ 15 October 2026\\par}\n",
    "{\\large Chapter VII\\par}\n")
rep(f"{L}/ch01/chapter1_expanded.tex",
    "{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small OpenAI ChatGPT and Codex \\textbullet\\ AI research collaborators and co-authors\\par}\n{\\small Expanded chapter edition \\textbullet\\ 15 October 2026\\par}\n", "")
rep(f"{L}/ch02/chapter2_source_field_formatted.tex",
    "{\\large Chapter II \\textbullet\\ Source-to-field companion update\\par}\n\\vspace{0.5em}\n{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small OpenAI ChatGPT and Codex \\textbullet\\ Research collaborators and co-authors\\par}\n{\\small 15 October 2026\\par}\n",
    "{\\large Chapter II\\par}\n")
rep(f"{L}/ch03/chapter3_formatted.tex",
    "{\\large Chapter III \\textbullet\\ Source-bound development\\par}\n\\vspace{0.5em}\n{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small OpenAI ChatGPT and Codex \\textbullet\\ Research collaborators and co-authors\\par}\n{\\small 15 October 2026\\par}\n",
    "{\\large Chapter III\\par}\n")
rep(f"{L}/ch04/chapter.tex",
    "{\\large Chapter IV \\textbullet\\ Finite preparation and switched joint composition development\\par}\\vspace{0.5em}\n{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small OpenAI ChatGPT and Codex \\textbullet\\ Research collaborators and co-authors\\par}\n{\\small 16 October 2026\\par}\n",
    "{\\large Chapter IV\\par}\n")
rep(f"{L}/ch05/chapter.tex",
    "{\\large Chapter V \\textbullet Source, thermal and measurement development}\\\\[7pt]\n{\\normalsize Sean Brady}\\\\\n{\\small Originator and conceptual director}\\\\[3pt]\n{\\small OpenAI ChatGPT and Codex \\textbullet Research collaborators and co-authors}\\\\[5pt]\n{\\small 16 October 2026}\n",
    "{\\large Chapter V}\n")

# body credit sentences (ledger rows), with the provenance the ledger established
rep(f"{L}/ch02/chapter2_source_field_formatted.tex",
    "New mathematical constructions: Codex. Sean Brady: originator/conceptual director. OpenAI ChatGPT and Codex: research collaborators and co-authors.",
    "Source-bound physical-development packet from GEN6 Duck run chapter2-physical-protocols-20261015-01 (Duck 1.2.2, core 0.10.2; 15 native tasks), directed by Sean Brady; constructions written with OpenAI Codex (Courtroom~II case voli\\_provenance/01, H002821).")
rep(f"{L}/ch03/chapter3_formatted.tex", "\\noindent[1] Brady, ChatGPT and Codex. \\emph{Volume I, Chapter I}", "\\noindent[1] S. Brady. \\emph{Volume I, Chapter I}")
rep(f"{L}/ch03/chapter3_formatted.tex", "\\noindent[8] Brady, ChatGPT and Codex. \\emph{Chapter III local action and actual clock continuation}, \\nolinkurl{voli_chapter3_local_action2_20261015}:",
    "\\noindent[8] S. Brady. \\emph{Chapter III local action and actual clock continuation}, \\nolinkurl{voli_chapter3_local_action2_20261015}, GEN6 Duck run chapter3-local-action-20261015-03 (Duck 1.2.3, core 0.10.2; 17 native tasks), directed by Sean Brady, selections and prose written with OpenAI Codex:")
rep(f"{L}/ch04/nonuniform_continuation.tex", "This is a new Codex receiving construction.",
    "This receiving construction was written with OpenAI Codex in campaign voli\\_chapter4\\_observation1\\_20261016 (GEN6 Duck run chapter4-observation-20261016-01, Duck 1.2.3, core 0.10.2) on the uniform theorem and residual-energy map computed there, under Sean Brady's direction.")
rep(f"{L}/ch04/transport_continuation.tex", "This is an explicit propagation construction by Codex, following the amplitude-friction representation retained in Ref.~[19];",
    "This propagation construction was written with OpenAI Codex in campaign voli\\_chapter4\\_observation1\\_20261016 (GEN6 Duck run chapter4-observation-20261016-01, Duck 1.2.3, core 0.10.2) under Sean Brady's direction, following the amplitude-friction representation retained in Ref.~[19];")
rep(f"{L}/ch04/chapter.tex", "S. Brady, OpenAI ChatGPT and Codex.", "S. Brady.", count=4)
rep(f"{L}/ch05/chapter.tex",
    "The following is an explicitly Codex-originated candidate for apparatus\nand progress on a fixed background. It is not a selected SAM\nsource--geometry law.",
    "The following apparatus candidate was written with OpenAI Codex in\ncampaign voli\\_chapter5\\_localization2\\_20261016 (GEN6 Duck run\nchapter5-localization-20261016-01, Duck 1.2.3, core 0.10.2) under Sean\nBrady's direction, on a fixed background; its exhaust and residual\nenergy--momentum balance was checked by one native operator-word task\nwhose own context labels it a Codex diagnostic. It is not a selected SAM\nsource--geometry law.")
rep(f"{L}/ch05/chapter.tex", "\\bibitem{unified} S. Brady, OpenAI ChatGPT and Codex.", "\\bibitem{unified} S. Brady.")
for f in (f"{L}/ch01/chapter1_as_vii.tex", f"{L}/ch01/chapter1_expanded.tex"):
    rep(f, "The weighted-form, reference, and Duhamel construction is a Codex contribution developed within this collaboration, receiving the original source rules and retained hard preparation.",
        "The weighted-form, reference, and Duhamel construction was written with OpenAI Codex in GEN6 Duck run chapter1-lane01-20261015-01 (Duck 1.2.2, core 0.10.2) under Sean Brady's direction, receiving the original source rules and retained hard preparation.")
    rep(f, "Brady, with ChatGPT and Codex.", "S. Brady.", count=2)

# 2. live chapters I, VI, Appendix A
rep("chapter01_concepts.tex",
    "{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small Research development with OpenAI ChatGPT and Codex; concept chapter drafted with Claude Code\\par}\n{\\small First edition draft, 30 October 2026\\par}\n", "")
rep("ch01_concepts.tex",
    "OpenAI ChatGPT and Codex: the mathematical development of Chapters~II to~VI from which the derived statements are drawn.",
    "The mathematical development of Chapters~II to~VII, from which the derived statements are drawn, was produced in GEN6 Duck runs on the Substrate Ledger Computer (15--17 October 2026) directed by Sean Brady and operated by OpenAI Codex, which wrote their prose (Courtroom~II case \\texttt{voli\\_provenance/01}, H002821).")
rep("ch06.tex", "New constructions and finite parameter choices are Codex contributions.",
    "New constructions and finite parameter choices in this chapter were written with OpenAI Codex under Sean Brady's direction on the retained Chapter~VI Hamiltonian and source sectors; finite matrices were checked by native SLC-GEN5-R1 calls (campaigns voli\\_chvi\\_foundation1, voli\\_chvi\\_source\\_decoder1, voli\\_chvi\\_detector\\_record1 and voli\\_chvi\\_shared\\_routes1, 17 October 2026; Courtroom~II case voli\\_provenance/01).")
rep("vi_source/parts/foundation_overlap.tex",
    "The quadratic refinement and robustness corollaries in this section are\nagent-originated derivations by OpenAI ChatGPT and Codex in the present work\nblock.",
    "The quadratic refinement and robustness corollaries in this section were\nderived with OpenAI Codex in campaign voli\\_chvi\\_foundation1\\_20261017\n(H002700) under Sean Brady's direction, with two native SLC-GEN5-R1\noperator-word checks.")
rep("vi_source/parts/decoder_decoder.tex",
    "The decoder and bounds below are agent-originated derivations by OpenAI\nChatGPT and Codex from the retained Chapter~I clock observable and its\nChapter~VI route interpretation.",
    "The decoder and bounds below were derived with OpenAI Codex in campaign\nvoli\\_chvi\\_source\\_decoder1\\_20261017 (H002701) under Sean Brady's\ndirection, from the retained Chapter~I clock observable and its\nChapter~VI route interpretation, with four native SLC-GEN5-R1 calls.")
rep("vi_source/parts/record_memory_channel.tex",
    "The new instrument, finite-write estimate and correlated-hold bounds are\nagent-originated derivations by OpenAI ChatGPT and Codex.",
    "The new instrument, finite-write estimate and correlated-hold bounds were\nderived with OpenAI Codex in campaign voli\\_chvi\\_detector\\_record1\\_20261017\nunder Sean Brady's direction, with four native SLC-GEN5-R1 calls.")
rep("vi_source/parts/references.tex", "S. Brady, OpenAI ChatGPT and Codex,", "S. Brady,", count=12)
rep("closure_appendix.tex",
    "Sean Brady is the originator and conceptual director. Chapters I--VI retain their recorded OpenAI ChatGPT and Codex research-collaboration and co-authorship credits, including the particular analytical and verification contributions named in their source registers. The supplied Chapters VII--XII and earlier closing materials retain their Claude/Claude Code contributions where recorded. This replacement synthesis is an OpenAI Codex editorial and scientific-consistency contribution based on the supplied complete working edition of 19 October 2026. It does not reattribute historical derivations, imply that a collaborator executed another's records, or claim a new native computation.",
    "Sean Brady is the project director. The content of Chapters II--VII was produced in GEN6 Duck runs on the Substrate Ledger Computer (15--17 October 2026) directed by Sean Brady and operated by OpenAI Codex, which wrote the chapter prose; Chapter VI's derivations were written with OpenAI Codex with native SLC-GEN5-R1 checks; Chapters I and VIII--XIII were drafted with Claude Code from the record and from the first Courtroom's sealed results of June and July 2026. The co-authorship credits that earlier editions carried were removed on 2 November 2026 as a breach of credit where credit is due (Courtroom~II case \\texttt{voli\\_provenance/01}, ironclad H002821); AI-assisted research contributions are credited in the front matter. The editorial synthesis of this appendix was prepared with OpenAI Codex from the working edition of 19 October 2026. It does not claim a new native computation.")

# 3. generators and preamble: chapter heads without authorship or dates; running header without a name
for f in ("build_first_edition_chapters.py", "build_new_chapters.py"):
    rep(f, "{\\large Sean Brady\\par}\n{\\small Originator and conceptual director\\par}\n{\\small Research development with OpenAI ChatGPT and Codex\\par}\n", "")
rep("build_first_edition_chapters.py", "{\\small First edition draft, 30 October 2026 (text of the edition of 25 October 2026)\\par}\n", "")
rep("build_first_edition_chapters.py", "\\fancyhead[R]{\\footnotesize Brady | First edition draft, 30 October 2026}", "\\fancyhead[R]{\\footnotesize " + STAMP + "}")
rep("build_new_chapters.py", r"\{\\small [^\n]*2026[^\n]*\\par\}\n", "", count=1, regex=True)
rep("preamble.tex", "\\fancyhead[R]{\\footnotesize Brady | Edition of 25 October 2026}", "\\fancyhead[R]{\\footnotesize " + STAMP + "}")

json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG},
          open(ROOT / "checks" / "attribution_pass_20261102.json", "w"), indent=1)
print(f"{len([l for l in LOG if 'file' in l])} replacements applied; log in checks/attribution_pass_20261102.json")
