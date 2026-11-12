from pathlib import Path
import json,hashlib,re,fitz
E=Path(__file__).resolve().parents[1]; base=E.parents[1]
P=E/'pdf/SAM_Volume_II_Revised_Edition_20261110.pdf'
pdf=fitz.open(P); old=fitz.open(base/'pdf/SAM_Volume_II_20261105_authorship_draft.pdf')
text='\n'.join(p.get_text() for p in pdf); oldtext='\n'.join(p.get_text() for p in old)
(E/'qa/extracted_text.txt').write_text(text)
baseline=json.loads((E/'baseline/ORIGINAL_SHA256.json').read_text())
changed=[p for p,h in baseline.items() if not (base/p).exists() or hashlib.sha256((base/p).read_bytes()).hexdigest()!=h]
log=(E/'qa/latex-final.log').read_text()
alerts=re.findall(r'.*(?:Overfull|Missing character|undefined|multiply defined|LaTeX Error).*',log)
credits={term:{'baseline':len(re.findall(term,oldtext,re.I)),'revised':len(re.findall(term,text,re.I))} for term in ['Codex','OpenAI','ChatGPT','Claude']}
source_text='\n'.join(p.read_text() for p in (E/'src').glob('*.tex'))
labels=re.findall(r'\\label\{([^}]+)\}',source_text)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source_text)
keys=re.findall(r'\\bibitem\{([^}]+)\}',source_text)
cites=[]
for c in re.findall(r'\\(?:samref|cite)\{([^}]+)\}',source_text): cites+=c.split(',')
missing_refs=sorted(set(refs)-set(labels));missing_cites=sorted({c for c in cites if not c.startswith("#")}-set(keys))
# Check text glyph placement; line math accents and page numbers remain within page.
geometry=[]; empty=[]; badlinks=[]
for i,p in enumerate(pdf):
 if len(p.get_text().strip())<5:empty.append(i+1)
 for b in p.get_text('dict')['blocks']:
  if b.get('type')!=0:continue
  for line in b['lines']:
   for s in line['spans']:
    r=fitz.Rect(s['bbox'])
    if r.x0<-0.5 or r.y0<-0.5 or r.x1>p.rect.width+.5 or r.y1>p.rect.height+.5: geometry.append({'page':i+1,'text':s['text'],'box':list(r)})
 for link in p.get_links():
  if link.get('kind')==fitz.LINK_GOTO and not 0<=link.get('page',-1)<len(pdf):badlinks.append({'page':i+1,'link':link})
evidence=json.loads((E/'EVIDENCE_MANIFEST.json').read_text())
bad_evidence=[r['snapshot'] for r in evidence if hashlib.sha256((E/r['snapshot']).read_bytes()).hexdigest()!=r['sha256']]
result={'pages':len(pdf),'baseline_pages':len(old),'metadata':pdf.metadata,'baseline_files_checked':len(baseline),'changed_original_files':changed,'build_alerts':alerts,'credit_counts':credits,'missing_references':missing_refs,'missing_citations':missing_cites,'duplicate_labels':sorted({l for l in labels if labels.count(l)>1}),'out_of_page_text':geometry,'empty_pages':empty,'bad_internal_links':badlinks,'evidence_files':len(evidence),'evidence_hash_mismatches':bad_evidence,'pdf_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'toc':pdf.get_toc(),'pass':not(changed or alerts or missing_refs or missing_cites or geometry or badlinks or bad_evidence or any(v['revised']>v['baseline'] for v in credits.values()))}
(E/'qa/EDITION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['toc','metadata']},indent=2))
assert result['pass']
