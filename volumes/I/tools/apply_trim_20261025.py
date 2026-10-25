#!/usr/bin/env python3
"""Apply the Volume I trim of 2026-10-25, Option A (volumes/I/TRIM_PLAN_20261025.md).

Moves Chapter X (page markers 208..216) whole into a new Appendix B after the closing review; adds Part headers, a trimmed-edition
contents block, an edition note, status lines under the Part 2 chapters, the Appendix B preface and one cut note. No original line is
edited or deleted. Checks: block hash before and after; multiset of original lines unchanged apart from additions; line count; page
markers present exactly once. Directed by Sean Brady. Executed with Claude Code.
"""
import hashlib, json, sys, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'SAM_Volume_I.md'
REPORT = ROOT / 'TRIM_REPORT_20261025.json'
TAG = '[Addition, 2026-10-25]'

def h(lines): return hashlib.sha256('\n'.join(lines).encode('utf-8')).hexdigest()[:16]

L = SRC.read_text(encoding='utf-8').split('\n')
assert len(L) == 35403, len(L)
rep = {'before_lines': len(L), 'checks': {}}

# --- block identities on the pre-trim file (1-indexed inclusive ranges from the plan)
def rng(a, b): return L[a-1:b]
assert h(rng(30891, 32165)) == 'a628c78b2acc2790', 'Chapter X body hash differs from the plan'
X = rng(30882, 32156)
assert L[30882-1] == '<!-- page 208 -->' and L[32157-1] == '<!-- page 217 -->'
hx = h(X); rep['chapter_X'] = {'lines': [30882, 32156], 'count': len(X), 'sha256_16_before': hx}

# --- anchors
def idx(pred, start=0, desc=''):
    for i in range(start, len(L)):
        if pred(L[i]): return i
    raise SystemExit('anchor not found: ' + desc)
i_page3 = idx(lambda s: s == '<!-- page 3 -->', 0, 'page 3')
i_page4 = idx(lambda s: s == '<!-- page 4 -->', 0, 'page 4')
i_page181 = idx(lambda s: s == '<!-- page 181 -->', 0, 'page 181')
i_runres = idx(lambda s: s.startswith('# Run results received into Volume I'), 0, 'run results')
assert i_runres == 35071-1
chapter_heads = {}
for ch, ln in [('VII', 27235), ('VIII', 28566), ('IX', 29741), ('XI', 32166), ('XII', 33366)]:
    assert L[ln-1] == f'Chapter {ch}', (ch, L[ln-1])
    j = idx(lambda s: s.startswith('Unified expanded edition | 19 October 2026'), ln-1, ch)
    assert j - (ln-1) < 8
    chapter_heads[ch] = j

STATUS = {
'VII': f"{TAG} Part 2. This chapter adds to Part 1 the thermal premise: a static metric, a normalized Killing time, the Hawking conversion and the quarter-area entry convention (register T-13). The finite-entry staircase and its Catalan series are exact conditional mathematics; the entry convention is declared, not derived. Runs that touch it: volii_gate_1 (H002782; the hazard-as-temperature reading, received-results section).",
'VIII': f"{TAG} Part 2. This chapter adds the inventory premise: the floor A_0 = 1/(12π), the weight and the count d̂ = 3 (T-01, T-02, T-05), from which Ω_m = 1/π and the Hubble cascade follow as identities. The drafted ceiling section of 24 October belongs with this chapter. Runs: voli_ceiling_1–5 (H002776–H002778, H002780, H002781): four exact languages for the road, the lawfulness gate, one chart for the floored reservoir and the line of sight, the exponent as a count of directions; no run derived the floor, the weight or the count.",
'IX': f"{TAG} Part 2. This chapter adds the recombination premise and the two rulers (the drag ruler and the sound-horizon ruler) under one background ledger; its receiver lesson, that the ruler is chosen before the comparison is made, is the volume's clearest statement of the receiver thread. The native recombination lane and the external full-shape lane answer different questions and stay separate. No run has touched this chapter; the register's T-06 belongs to it.",
'XI': f"{TAG} Part 2. This chapter adds the carrier premise: the released carrier account as a radiation law, the ringdown rationals ω̂_R = 3/8 and γ̂ = 4/45 (T-08) and the radiated-energy ceiling Θ/R² = 1/8 (T-09), the last by the same uniform count-equals-energy weighting Volume II Chapter XVII uses. A boundary law R(ω) is the open operand. No run has touched this chapter.",
'XII': f"{TAG} Part 2. Sections 1–5, 7–8 and 20 carry the road law A_los(z) = (1/π)(1 − (1 + z)^(−3)) (T-10), the distinction of equal numbers under different operators, the background adapter and the finite-redshift tests; these are the sections the ceiling runs used (voli_ceiling_1–5), and the road is now one object with the floored reservoir on cosh²φ = e^(ds). Sections 6 and 9–19, the fate coefficient (T-11), the completed Home (T-12) and the crossing postulate (T-14), are retired targets: see Appendix B.",
}
CONTENTS = [
f"{TAG} Contents of the trimmed edition (25 October 2026)", "",
"| Part | Contents | Pages of the source PDF |", "|---|---|---|",
"| Front matter | title page, original contents, this contents block and the edition note | 1–3 |",
"| Part 1 — Substrate and accumulation | Chapters I–VI: I Original Write histories and an interacting source-field action; II Retention, accumulation, and the finite ledger; III The spherical accumulation kernel and the source-to-field interface; IV Clocks, signals, and calibrated observation; V Strong fields and the approach to unit accumulation; VI Quantum routes, shared fields and retained physical records | 4–180 |",
"| Part 2 — Extensions the program is working on | VII Horizon thermodynamics and accessible information; VIII Cosmic inventory and the Hubble cascade; IX Thermal history, recombination and CMB structure; XI Carrier radiation and ringdown dynamics; XII Cosmological fate and the completed boundary (its §6 and §9–19 labelled as retired targets) | 181–207, 217–234 |",
"| Appendix A — Evidence, closures and remaining physical assignments | the closing review, unchanged | 235–240 |",
"| Appendix B — Retired targets | preface; Chapter X Many-source accumulation and galaxy halos, moved whole | 208–216 |",
"| Received results and drafted sections | the October 2026 sections, unchanged | — |", "",
f"{TAG} Edition note. The edition of 25 October 2026 is a reordering of this living text with no change of text: whole blocks move, nothing inside a block is edited, nothing is deleted, and chapter numbers are unchanged. The chapters of Part 2 each carry a premise beyond Part 1; the status line under each chapter's title names it, with the register entry (`TARGETS_REGISTER_20261023.md`) that owns it. Appendix B holds retired targets with their text preserved in full. The source PDF (sha256 698b2316…, 240 pages) and the git history hold the original order; the trim plan is `TRIM_PLAN_20261025.md`.", ""]
PART1 = ["", f"{TAG} Part 1 — Substrate and accumulation (Chapters I–VI)", ""]
PART2 = ["", f"{TAG} Part 2 — Extensions the program is working on (Chapters VII–IX, XI–XII)", ""]
CUTNOTE = ["", f"{TAG} Chapter X, Many-source accumulation and galaxy halos (source PDF pages 208–216), has moved whole to Appendix B — Retired targets; its text is unchanged.", ""]
APPB = ["", f"{TAG} Appendix B — Retired targets", "",
f"{TAG} The chapters and sections gathered here were written as extensions of Part 1 and are retained in full, in their original words and numbering. They are retired from the body of the volume on Sean Brady's decision of 25 October 2026 because the targets they pursue await their own foundations and are not premises of the program: the halo coordinate X_∞ = 10/π (Chapter X; T-07), the fate coefficient H_∞ = H_0Ω_Λ^(3/2) (Chapter XII §6; T-11), the completed Home re-indexing and recurrence (Chapter XII §9–19; T-12; historical Home rules H000791, H000794–H000797) and the crossing postulate (T-14). The halo work remains of interest and is less connected to the rest of the volume than the other extensions; the SAM Research Project archive holds the SPARC campaign receipts the chapter cites, the Home rule entries, and the register entries that own each target (`TARGETS_REGISTER_20261023.md`). Chapter XII's §6 and §9–19 remain in place in Part 2, labelled by its status line (Option A of the trim plan). Nothing here is withdrawn; a retired target returns to the body when a construction supplies its foundation.", ""]

# --- assemble: insert from the bottom up so indices stay valid
additions = []
def ins(i, block, added=None):
    L[i:i] = block; additions.extend(block if added is None else added)
# Appendix B after the closing review, before the run-results section
ins(i_runres, APPB + X + [''], added=APPB + [''])
# remove Chapter X from its place (later indices already handled since i_runres > block)
del L[30882-1:32156]
ins(30882-1, CUTNOTE)
# status lines (descending order of position), part 2 header, part 1 header, contents (all above 30882 except XI, XII which shift by removal and cut-note)
shift = -len(X) + len(CUTNOTE)
for ch in ['XII', 'XI']:
    ins(chapter_heads[ch] + shift + 1, ['', STATUS[ch]])
for ch in ['IX', 'VIII', 'VII']:
    ins(chapter_heads[ch] + 1, ['', STATUS[ch]])
ins(i_page181, PART2)
ins(i_page4, PART1)
ins(i_page3, CONTENTS)

# --- checks
old = SRC.read_text(encoding='utf-8').split('\n')
new = L
# (i) block hash at new position
k = new.index('<!-- page 208 -->'); assert h(new[k:k+len(X)]) == hx, 'Chapter X hash changed'
rep['chapter_X']['new_first_line'] = k+1; rep['chapter_X']['sha256_16_after'] = h(new[k:k+len(X)])
# (ii) multiset
c_old = collections.Counter(old); c_new = collections.Counter(new); c_new.subtract(collections.Counter(additions))
assert all(v >= 0 for v in c_new.values()) and c_new == c_old, 'line multiset changed'
# (iii) count
assert len(new) == len(old) + len(additions), (len(new), len(old), len(additions))
# (iv) page markers
pm = [s for s in new if s.startswith('<!-- page ')]
assert len(pm) == len(set(pm)) == len([s for s in old if s.startswith('<!-- page ')]), 'page markers'
rep['checks'] = {'block_hash_unchanged': True, 'line_multiset_unchanged': True, 'line_count': len(new), 'addition_lines': len(additions), 'page_markers': len(pm), 'page_markers_unique': True}
rep['additions'] = {'contents_and_edition_note': len(CONTENTS), 'part_headers': len(PART1)+len(PART2), 'status_lines': 5, 'cut_note': len(CUTNOTE), 'appendix_B_preface_and_header': len(APPB)}
SRC.write_text('\n'.join(new), encoding='utf-8')
REPORT.write_text(json.dumps(rep, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps(rep, indent=1, ensure_ascii=False))
