#!/usr/bin/env python3
"""Recency index of the SAM record, newest first.

Reads, without modifying anything:
  ironclad/SAM_HISTORY/HISTORY_INDEX.md and entries/   (H-entries, dated)
  SAM_Research_Project/GEN4/<campaign>/                 (campaign dirs; dated by name suffix or by the first H-entry citing them)
  Courtroom_II/campaigns/<campaign>/<case>/MANIFEST.json (cases, written_utc)
  Substrate_Accumulation_Model/volumes/*/concept_notes/  (concept notes, dated by filename)
  Substrate_Accumulation_Model/decisions/DECISIONS.md    (decision lines, dated)
and flags whether any volume source (volumes/*/src, including retained sources) cites the item
(by H-number or by campaign directory name).

Writes RECENT.md (last N days + the not-cited list) and RECENT_FULL.md (everything) in the doc repo root.
Protocol: protocols/RECORD_SEARCH_PROTOCOL.md. Directed by Sean Brady. Executed with Claude Code.
"""
import re, os, sys, json, datetime as dt
from pathlib import Path

OVER = Path(__file__).resolve().parents[2]           # SAM_Research_Overflow
DOC = OVER / 'Substrate_Accumulation_Model'
HIST = OVER / 'ironclad' / 'SAM_HISTORY'
GEN4 = OVER / 'SAM_Research_Project' / 'GEN4'
CRII = OVER / 'Courtroom_II' / 'campaigns'
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 21
QUEUE_DAYS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
VOLI = re.compile(sys.argv[3] if len(sys.argv) > 3 else r'voli|vol_i|volume i|chapter ?(i|ii|iii|iv|v|vi|vii)\b|clock|road|ruler|horizon|floor|a0|lapse|gps|shapiro|cassini|source[- ]action|write', re.I)
TODAY = dt.date.today()

def first_heading(p):
    try:
        for line in p.read_text(errors='replace').splitlines():
            s = line.strip()
            if s.startswith('#'):
                return s.lstrip('#').strip()[:140]
            if s and not s.startswith('---') and ':' not in s[:20]:
                return s[:140]
    except Exception:
        pass
    return ''

items = []  # dicts: date, kind, id, title, path, cited_by

# --- H entries
idx = (HIST / 'HISTORY_INDEX.md').read_text(errors='replace')
seen = set()
for m in re.finditer(r'entries/(H\d{6})_(\d{4}-\d{2}-\d{2})_([A-Za-z0-9_]+)\.md', idx):
    hid, d, t = m.groups()
    if hid in seen:
        continue
    seen.add(hid)
    line = idx[idx.rfind('\n', 0, m.start()) + 1: idx.find('\n', m.end())]
    summ = re.sub(r'\[`?H\d{6}`?\]\([^)]*\)|\[entry\]\([^)]*\)|`', '', line).strip(' |-—')
    summ = re.sub(r'\s+', ' ', summ)
    items.append(dict(date=d, kind='H-entry', id=hid, title=t.replace('_', ' ').lower()[:90], extra=summ[:200],
                      path=f'ironclad/SAM_HISTORY/entries/{hid}_{d}_{t}.md'))

# --- GEN4 dirs: date by suffix, else first citing H entry
cite_date = {}
entry_dir = HIST / 'entries'
for f in entry_dir.glob('H*.md'):
    md = re.match(r'(H\d{6})_(\d{4}-\d{2}-\d{2})_', f.name)
    if not md:
        continue
    hid, d = md.groups()
    try:
        txt = f.read_text(errors='replace')
    except Exception:
        continue
    for g in set(re.findall(r'GEN4/([A-Za-z0-9_]+)', txt)):
        if g not in cite_date or d < cite_date[g][0]:
            cite_date[g] = (d, hid)
for d_ in sorted(GEN4.iterdir()):
    if not d_.is_dir():
        continue
    name = d_.name
    ms = re.search(r'_(\d{8})$', name)
    if ms:
        s = ms.group(1); date = f'{s[:4]}-{s[4:6]}-{s[6:]}'; via = 'name'
    elif name in cite_date:
        date, via = cite_date[name][0], cite_date[name][1]
    else:
        date, via = None, None
    rep = d_ / 'REPORT.md'
    title = first_heading(rep) if rep.exists() else (first_heading(d_ / 'RESULT.md') if (d_ / 'RESULT.md').exists() else '')
    items.append(dict(date=date, kind='GEN4 campaign', id=name, title=title, extra=f'dated via {via}' if via else 'undated',
                      path=f'SAM_Research_Project/GEN4/{name}/'))

# --- Courtroom II cases
for man in sorted(CRII.glob('*/*/MANIFEST.json')):
    try:
        j = json.loads(man.read_text())
        d = j.get('written_utc', '')[:10]
    except Exception:
        d = None
    case = f'{man.parent.parent.name}/{man.parent.name}'
    items.append(dict(date=d or None, kind='Courtroom II case', id=case, title=first_heading(man.parent / 'REPORT.md'),
                      extra='', path=f'Courtroom_II/campaigns/{case}/'))

# --- concept notes
for p in sorted(DOC.glob('volumes/*/concept_notes/*_2026*.md')):
    md = re.search(r'_(\d{8})\.md$', p.name)
    d = f'{md.group(1)[:4]}-{md.group(1)[4:6]}-{md.group(1)[6:]}' if md else None
    items.append(dict(date=d, kind='concept note', id=p.name, title=first_heading(p), extra='', path=str(p.relative_to(OVER))))

# --- decisions
dec = DOC / 'decisions' / 'DECISIONS.md'
if dec.exists():
    for i, line in enumerate(dec.read_text(errors='replace').splitlines(), 1):
        m = re.match(r'- (\d{4}-\d{2}-\d{2}) — (.*)', line)
        if m:
            items.append(dict(date=m.group(1), kind='decision', id=f'DECISIONS.md:{i}', title=m.group(2)[:150], extra='',
                              path=f'Substrate_Accumulation_Model/decisions/DECISIONS.md'))

# --- cited by volume sources?
vol_text = ''
for p in DOC.glob('volumes/*/src/**/*.tex'):
    try:
        vol_text += p.read_text(errors='replace') + '\n'
    except Exception:
        pass
vol_h = set(re.findall(r'H\d{6}', vol_text))
for it in items:
    if it['kind'] == 'H-entry':
        it['cited'] = it['id'] in vol_h
    elif it['kind'] == 'GEN4 campaign':
        it['cited'] = (it['id'] in vol_text)
    else:
        it['cited'] = None

dated = [i for i in items if i['date']]
undated = [i for i in items if not i['date']]
dated.sort(key=lambda i: (i['date'], i['kind'], i['id']), reverse=True)

def row(i):
    c = {True: 'yes', False: 'no', None: '—'}[i['cited']]
    t = (i['title'] or '').replace('|', '/')
    e = (i['extra'] or '').replace('|', '/')
    return f"| {i['date']} | {i['kind']} | `{i['id']}` | {t} | {c} | {e} |"

hdr = ('| date | kind | id | title / first line | cited by a volume source | note |\n'
       '|---|---|---|---|---|---|\n')
cut = (TODAY - dt.timedelta(days=DAYS)).isoformat()
recent = [i for i in dated if i['date'] >= cut]
qcut = (TODAY - dt.timedelta(days=QUEUE_DAYS)).isoformat()
uncited = [i for i in dated if i['date'] >= qcut and i['cited'] is False and i['kind'] in ('H-entry', 'GEN4 campaign') and VOLI.search(i['id'] + ' ' + (i['title'] or '') + ' ' + (i['extra'] or ''))]

intro = f"""# RECENT — the SAM record, newest first

Generated {TODAY.isoformat()} by `tools/recency_index.py` (read-only over the repositories). Protocol:
[protocols/RECORD_SEARCH_PROTOCOL.md](protocols/RECORD_SEARCH_PROTOCOL.md). Any lookup for a definition, a result or
direction starts at the top of this page and works down; nothing older is authority over anything newer.

Counts: {len(dated)} dated items ({sum(1 for i in dated if i['kind']=='H-entry')} H-entries,
{sum(1 for i in dated if i['kind']=='GEN4 campaign')} dated GEN4 campaigns, {sum(1 for i in dated if i['kind']=='Courtroom II case')} Courtroom II cases,
{sum(1 for i in dated if i['kind']=='concept note')} concept notes, {sum(1 for i in dated if i['kind']=='decision')} decisions); {len(undated)} undated GEN4 campaigns
(no date suffix and no citing H-entry; listed at the end of RECENT_FULL.md).
"cited by a volume source" = the H-number or campaign directory name appears somewhere under volumes/*/src.
The full list is [RECENT_FULL.md](RECENT_FULL.md).

## Last {DAYS} days ({len(recent)} items)

"""
sec2 = f"""
## Volume I–relevant record items of the last {QUEUE_DAYS} days not cited by any volume source ({len(uncited)})

Keyword filter (id/title/summary): `{VOLI.pattern}`. These are results the volume has not absorbed: a work queue for the refinement campaign, not a judgement. Rerun with a different third argument to change the filter.

"""
(DOC / 'RECENT.md').write_text(intro + hdr + '\n'.join(row(i) for i in recent) + '\n' + sec2 + hdr + '\n'.join(row(i) for i in uncited) + '\n')
(DOC / 'RECENT_FULL.md').write_text(f"# RECENT_FULL — every dated record item, newest first ({len(dated)})\n\nGenerated {TODAY.isoformat()}. See RECENT.md.\n\n" + hdr + '\n'.join(row(i) for i in dated) + f"\n\n## Undated GEN4 campaigns ({len(undated)})\n\n" + '\n'.join(f"- `{i['id']}` — {i['title']}" for i in undated) + '\n')
print(f'dated {len(dated)} undated {len(undated)} recent {len(recent)} uncited-recent {len(uncited)}')
