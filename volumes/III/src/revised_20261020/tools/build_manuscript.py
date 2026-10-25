from pathlib import Path
import json, re, subprocess, hashlib, unicodedata, copy
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[1]
OLD=Path('/home/lilhelper/Documents/Codex/2026-10-19/we/work/volume_iii/expanded')
BASE=ROOT/'manuscript/baseline_edited'
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
WORK=ROOT/'manuscript'; WORK.mkdir(exist_ok=True)
PANDOC='/tmp/sam-volume-tooling/pandoc-3.8.3/bin/pandoc'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def plain_inline(xs):
 out=''
 for x in xs:
  t=x['t']; c=x.get('c')
  if t in ['Str','Code','Math']:out+=c if t=='Str' else c[-1]
  elif t in ['Space','SoftBreak','LineBreak']:out+=' '
  elif t in ['Emph','Strong','SmallCaps','Strikeout','Superscript','Subscript']:out+=plain_inline(c)
  elif t in ['Span','Link']:out+=plain_inline(c[1])
  elif t=='Quoted':out+=plain_inline(c[1])
 return out
def inlines(s):
 a=[]
 for i,w in enumerate(s.split()):
  if i:a.append({'t':'Space'})
  a.append({'t':'Str','c':w})
 return a
def parse(s,fmt):
 p=subprocess.run([PANDOC,'-f',fmt,'-t','json'],input=s,text=True,capture_output=True,check=True)
 return json.loads(p.stdout)
def section_md(s):return parse(s,'markdown+tex_math_dollars')['blocks']

# Each item retains a source chapter or supplies a source-reviewed full chapter.
spec=[
 ('body01.tex','N100 Grammar and Exact Work','base'),
 ('body02.tex','SAM Language and Exact Program Semantics','base'),
 ('body03.tex','Exact State Spaces and Thermodynamics','base'),
 ('n5000_chapter.md','Exact Joint Densities at N5000','new'),
 ('n2000_chapter.md','N2000 Ground States and Low Energy Physics','new'),
 ('exact_01.tex','Joint State Spaces and Layered Exact Sources','base'),
 ('body04.tex','The Algebra of a Complete Write','base'),
 ('body05.tex','Lifecycle Reception and Carrier Return','base'),
 ('body06.tex','Directional History and Event Reels','base'),
 ('history_chapter.md','Equal Observable States and Executable Histories','new'),
 ('body07.tex','Ordinal Selection and the Delegated Exact Engine','base'),
 ('body08.tex','Starbreaker Formation on Its Own Grammar','base'),
 ('applications_01.tex','Source Histories and Inverse Reconstruction','base'),
 ('runtime_01.tex','Exact Values Certified Functions and Retained Composition','base'),
 ('runtime_02.tex','Executable Methods and Learned Questions','base'),
 ('exchange_chapter.md','Exact Exchange and Symbolic Matter','new'),
 ('applications_02.tex','Exact Application Reuse and Learned Reconstruction','base'),
 ('response_01.tex','Certified Source Integration and Retained Response','base'),
 ('rh_chapter.md','Signed Arithmetic Energy and Conditional Continuation','new'),
 ('body09.tex','Reciprocal History and the Arithmetic Interface','base'),
 ('arithmetic_01.tex','Signed Arithmetic Sources and Transition Storage','base'),
 ('body10.tex','Prime Coordinates and Exact Mersenne Factors','base'),
 ('arithmetic_02.tex','Reusable Mersenne Certificates and Arithmetic Compilers','base'),
 ('prime_main.md','Prime Event Computation and Microscopic Reliability','new'),
 ('prime_continuation.tex','Prime Event Continuation and Retained Clocks','custom'),
 ('body11.tex','Jacobian Maps Return and Retained History','base'),
 ('body12.tex','Relational Composition','base'),
 ('connections_01.tex','Computational Interfaces Across the Three Volumes','base')]

def roman(n):
 out=''
 for k,v in [(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:
  while n>=k:out+=v;n-=k
 return out

def prep_tex(s):
 s=re.sub(r'\\bookchapter\{[^}]*\}\s*(?:\\label\{[^}]+\})?', '',s,count=1,flags=re.S)
 s=re.sub(r'\\samref\{([^}]+)\}',lambda m:r' \textnormal{['+m[1]+']}',s)
 s=re.sub(r'\\cite\{([^}]+)\}',lambda m:r' \textnormal{['+m[1]+']}',s)
 s=re.sub(r'\\ref\{([^}]+)\}',lambda m:labels.get(m[1],m[1]),s)
 s=s.replace('~',' ')
 s=s.replace('\\allowbreak','')
 s=re.sub(r'\\(clearpage|onecolumn|twocolumn|phantomsection|tightlist|FloatBarrier)\b','',s)
 s=re.sub(r'\\markboth\{[^}]*\}\{[^}]*\}','',s)
 s=s.replace(r'\ii',r'\mathrm{i}').replace(r'\dd',r'\mathrm{d}')
 s=s.replace(r'\Tr',r'\operatorname{Tr}').replace(r'\Span',r'\operatorname{span}')
 s=s.replace(r'\Var',r'\operatorname{Var}').replace(r'\Cov',r'\operatorname{Cov}')
 s=s.replace(r'\norm{',r'\operatorname{norm}{')
 for old,new in [(r'\texttt{mathcal\ C\_S}',r'\(\mathcal C_S\)'),(r'\texttt{mathcal\ C}',r'\(\mathcal C\)'),(r'\texttt{mathcal\ I\_e(S)}',r'\(\mathcal I_e(S)\)')]:s=s.replace(old,new)
 return s

labels={}
for n,(file,title,kind) in enumerate(spec,1):
 if kind=='base':
  p=BASE/file
  if not p.exists():raise SystemExit('Awaiting edited baseline '+str(p))
  for label in re.findall(r'\\label\{([^}]+)\}',p.read_text()):labels[label]=roman(n)
labels['v3-prime-event']=roman(25)

blocks=[]; chapter_map=[]
for n,(file,title,kind) in enumerate(spec,1):
 p=(BASE if kind=='base' else WORK)/file
 if not p.exists():raise SystemExit('Awaiting chapter '+str(p))
 s=p.read_text()
 if kind in ['base','custom']:
  j=parse(prep_tex(s),'latex')
 else:
  s=re.sub(r'^# .*?\n','',s,count=1)
  j=parse(s,'markdown+tex_math_dollars')
 content=j['blocks']
 if file=='prime_continuation.tex':
  # The separate projection result complements the retained source-clock account.
  extra=(WORK/'prime_memory_extra.md').read_text()
  content+=section_md(extra)
 if file=='body08.tex' and (WORK/'starbreaker_supplement.md').exists():
  extra=(WORK/'starbreaker_supplement.md').read_text()
  extra=re.sub(r'^# .*?\n','',extra,count=1)
  content+=section_md(extra)
 # Pandoc's TeX reader maps subsection to level 2. Markdown chapters use the same ladder.
 for b in content:
  if b['t']=='Header':
   b['c'][0]=max(2,b['c'][0])
   h=plain_inline(b['c'][2])
   h=h.replace('Li-6','Li 6').replace('Li-7','Li 7').replace('N=','N ')
   h=re.sub(r'\\[a-zA-Z]+','',h)
   h=re.sub(r'[^\w\s]',' ',h)
   h=' '.join(h.split())
   b['c'][2]=inlines(h)
 content=[b for b in content if not(b['t']=='Para' and not plain_inline(b['c']).strip() and all(x['t']!='Math' for x in b['c']))]
 blocks.append({'t':'Header','c':[1,[f'chapter-{n}',[],[]],inlines('Chapter '+roman(n)+' '+title)]})
 blocks+=content
 chapter_map.append({'number':n,'roman':roman(n),'title':title,'source':str(p.relative_to(ROOT)),'sha256':sha(p),'blocks':len(content)})

app=WORK/'appendices.md'
if app.exists():blocks+=section_md(app.read_text())

# Normalize punctuation and remove empty raw nodes before DOCX serialization.
def walk(o):
 if isinstance(o,list):
  result=[]
  for x in o:
   if isinstance(x,dict) and x.get('t') in ['RawBlock','RawInline'] and x.get('c',[''])[0]=='latex':continue
   if isinstance(x,dict) and x.get('t')=='Str':
    match=re.fullmatch(r'(\d+)\^(\d+|[A-Za-z])([.,;:]?)',x['c'])
    if match:
     result.append({'t':'Math','c':[{'t':'InlineMath'},match[1]+'^{'+match[2]+'}']})
     if match[3]:result.append({'t':'Str','c':match[3]})
     continue
   result.append(walk(x))
  return result
 if isinstance(o,dict):
  if o.get('t')=='Str':o['c']=o['c'].replace('—','; ').replace('–','-').replace('\u2011','-')
  if o.get('t')=='Code':
   code=re.sub(r'\\+\s+',' ',o['c'][1]).replace('\u00a0',' ')
   math_codes={'2^99 I_2':r'2^{99}I_2','P_C4^4=I':r'P_{C4}^{4}=I','p^-':r'p^{-}','beta_p':r'\beta_p','gamma_p':r'\gamma_p','k=b*2^e':r'k=b\,2^{e}'}
   if code in math_codes:return {'t':'Math','c':[{'t':'InlineMath'},math_codes[code]]}
   o['c'][1]=code
  if o.get('t')=='Math':
   m=o['c'][1]
   m=re.sub(r'(?<!\\)\bsum_',r'\\sum_',m)
   m=re.sub(r'(?<!\\)\bepsilon_',r'\\epsilon_',m)
   m=re.sub(r'\{\\rm\s+([^{}]+)\}',r'\\mathrm{\1}',m)
   m=re.sub(r'\\rm\s+([A-Za-z]+)',r'\\mathrm{\1}',m)
   m=re.sub(r'\{\\cal\s+([^{}]+)\}',r'\\mathcal{\1}',m)
   m=m.replace(r'\notag','').replace(r'\nonumber','')
   # LibreOffice exposes align markers in Pandoc OMML. Retain matrix columns,
   # while displaying each aligned relation as a centered equation line.
   stack=[];parts=[];pos=0
   for token in re.finditer(r'\\(?:begin|end)\{[^}]+\}|&',m):
    parts.append(m[pos:token.start()]);tok=token.group()
    if tok.startswith(r'\begin'):
     env=tok.split('{',1)[1][:-1];stack.append(env);parts.append(tok)
    elif tok.startswith(r'\end'):
     if stack:stack.pop()
     parts.append(tok)
    elif any(e in ['matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix','array','cases'] for e in stack):parts.append(tok)
    pos=token.end()
   parts.append(m[pos:]);m=''.join(parts)
   m=re.sub(r'\\binom\s+([A-Za-z])\s*([A-Za-z])',r'\\binom{\1}{\2}',m)
   # Sentence punctuation is text, not part of the mathematical operand.
   m=re.sub(r'([.,;])\s*(\\end\{(?:equation\*?|align\*?|aligned)\})',r'\2',m)
   m=re.sub(r'[.,;]\s*$','',m)
   o['c'][1]=m
  return {k:walk(v) for k,v in o.items()}
 return o
blocks=walk(blocks)
ast={'pandoc-api-version':j['pandoc-api-version'],'meta':{},'blocks':blocks}
(WORK/'manuscript.json').write_text(json.dumps(ast,ensure_ascii=False))
(WORK/'CHAPTERS.json').write_text(json.dumps(chapter_map,indent=2))

# Reference styles establish a restrained single-column research monograph.
ref=Document(); sec=ref.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.74);sec.bottom_margin=Inches(.7)
sec.left_margin=Inches(.9);sec.right_margin=Inches(.85)
sec.header_distance=Inches(.28);sec.footer_distance=Inches(.3)
for nm in ['Normal','Body Text','First Paragraph']:
 if nm not in ref.styles:ref.styles.add_style(nm,WD_STYLE_TYPE.PARAGRAPH)
 st=ref.styles[nm];st.font.name='Liberation Serif';st.font.size=Pt(10.5)
 st.font.color.rgb=RGBColor(0,0,0)
 st.paragraph_format.line_spacing=1.08;st.paragraph_format.space_after=Pt(4)
 st.paragraph_format.widow_control=True
for nm,size in [('Title',25),('Subtitle',14),('Heading 1',19),('Heading 2',13),('Heading 3',11),('Heading 4',10.5)]:
 st=ref.styles[nm];st.font.name='Liberation Serif';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0)
 st.font.bold=nm!='Subtitle';st.paragraph_format.keep_with_next=True
 st.paragraph_format.space_before=Pt(12);st.paragraph_format.space_after=Pt(6)
 if nm=='Heading 1':st.paragraph_format.page_break_before=True
for nm in ['Verbatim Char','Source Code']:
 if nm in ref.styles:ref.styles[nm].font.name='Liberation Mono';ref.styles[nm].font.size=Pt(8.3)
ref.save(WORK/'reference.docx')
p=subprocess.run([PANDOC,str(WORK/'manuscript.json'),'-f','json','-t','docx','--reference-doc',str(WORK/'reference.docx'),'-o',str(OUT/'SAM_Volume_III_Revised.docx')],text=True,capture_output=True,check=True)
(WORK/'conversion_warnings.txt').write_text(p.stderr)
conversion_warning_count=len(p.stderr)
doc=Document(OUT/'SAM_Volume_III_Revised.docx')
for nm,size in [('Normal',10.5),('Body Text',10.5),('First Paragraph',10.5),('Title',25),('Subtitle',14),('Heading 1',19),('Heading 2',13),('Heading 3',11),('Heading 4',10.5)]:
 st=doc.styles[nm]
 st.font.name='Liberation Serif';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0)
 rf=st.element.get_or_add_rPr().find(qn('w:rFonts'))
 if rf is not None:
  for a in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:
   rf.attrib.pop(qn('w:'+a),None)
for border in list(doc._element.xpath('//w:pBdr')):
 border.getparent().remove(border)
for border in list(doc.styles.element.xpath('.//w:pBdr')):
 border.getparent().remove(border)

# Add a cover and a short results-first reading guide, then a deterministic linked contents list.
front=Document(WORK/'reference.docx')
front.add_paragraph('SAM Volume III',style='Title')
front.add_paragraph('Computation and Reciprocal History',style='Subtitle')
front.add_paragraph('Revised and expanded manuscript')
front.add_paragraph('Sean Brady\nOriginator and conceptual director')
front.add_paragraph('OpenAI ChatGPT and Codex\nAI research collaborators and co-authors')
front.add_paragraph('20 October 2026')
front.add_paragraph('Exact constructions, completed computations and reusable histories')
front.add_page_break()
front.add_paragraph('Results and reading guide',style='Title')
front.add_paragraph('This volume develops computation in the Substrate Accumulation Model through explicit constructions and retained results. A state-space count, a source operator or an ordered history becomes an operand for a later calculation. The central results are stated with the construction, method, validation and comparison that give each result its meaning.')
for title,text in [
 ('Exact joint densities at N5000','Six specified 5,000-spin complete Ising graphs have 1,530,259,992 primary energy magnetization boundary records. Each graph has 12,497,500 nonzero pair interactions. The retained integer counts account for every spin assignment; 96 paired encoding comparisons and the archived validation records establish the completed finite result. Chapter IV develops the full construction.'),
 ('Prime event reliability','An algebraically selected change to a seven-spin source increased exact billion-index trajectories from 1 of 64 to 47 of 64 seeds per profile; 13 of 16 fresh seeds were exact. The measured error reduction is 92.9701 percent across the paired profiles. Chapter XXIV explains the gate, derivation, data and budget comparisons. Chapter XXV preserves the later local trajectory through 1,039,515,000,000 decisions with zero errors and the separate eight-trillion continuation with three false emissions.'),
 ('Exact exchange and symbolic matter','Source operators resolve 35 arrangements into 19 spectral classes. Exact exchange spectra reach length 13 and account for 67,108,864 states. Completed exchange factors compose with 32 local-matter families in 2.011662 seconds of recorded assembly. Chapter XVI follows that derivation and reuse.'),
 ('Executable history','The histories [1,8] and [8,1] have the same sum, yet a common permitted connector gives 145/144 and 76/9, separated by 119/16. Chapters X, XII and XIII develop the sufficient-observation criterion, exact reconstruction and simulation results; the mathematical claims do not require an assumed physical energy scale.')]:
 front.add_paragraph(title,style='Heading 2');front.add_paragraph(text)
front.add_paragraph('The N2000 physical analysis has its own chapter and provenance. Ground-state counts, entropy limits, excitation gaps and controlled low-temperature readouts belong to those specified sources. Conditional arithmetic continuation criteria retain their stated hypotheses. Finite calculations and universal implications are identified where they occur.')
front.add_paragraph('Reading this edition',style='Heading 2')
front.add_paragraph('The revised edition preserves the useful foundation and later additions of the attached 107-page manuscript. The chapter order groups exact counting, executable history, the mathematical runtime, matter, arithmetic and prime-event computation. Historical engine names remain attached to their source stages. Appendix A records the seven attachments and the source chains; Appendix B explains the substantive changes. No new scientific campaign forms part of this manuscript revision.')
front.add_page_break()
front.add_paragraph('Contents',style='Title')
for c in chapter_map:
 p=front.add_paragraph(style='Normal')
 p.paragraph_format.space_after=Pt(4)
 p.paragraph_format.keep_with_next=False
 link=OxmlElement('w:hyperlink');link.set(qn('w:anchor'),'chapter-'+str(c['number']))
 r=OxmlElement('w:r');t=OxmlElement('w:t');t.text=c['roman']+'  '+c['title'];r.append(t);link.append(r);p._p.append(link)
for title in ['Appendix A Sources and evidence','Appendix B Revision summary']:
 front.add_paragraph(title)

# Prepend front matter while keeping final document section geometry.
body=doc._element.body
for el in reversed(list(front._element.body)[:-1]):body.insert(0,copy.deepcopy(el))
for border in list(doc._element.xpath('//w:pBdr')):border.getparent().remove(border)
for sec in doc.sections:
 p=sec.header.paragraphs[0];p.text='SAM Volume III   |   Computation and Reciprocal History'
 p.style='Normal';p.paragraph_format.space_after=Pt(0)
 for r in p.runs:r.font.size=Pt(8);r.font.color.rgb=RGBColor(80,80,80)
 f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER
 r=f.add_run();fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');r._r.addnext(fld)
 for r in f.runs:r.font.size=Pt(8)

current_chapter=''
for p in doc.paragraphs:
 p.paragraph_format.widow_control=True
 if p.style.name=='Heading 1':current_chapter=p.text
 if p.style.name.startswith('Heading'):p.paragraph_format.keep_with_next=True
 # Pandoc's body paragraphs can carry an unwanted first-line indent from defaults.
 if p.style.name in ['Normal','Body Text','First Paragraph']:
  p.paragraph_format.first_line_indent=Pt(0)
  if current_chapter.startswith('Chapter XVI ') or current_chapter.startswith('Chapter XXIV '):
   p.paragraph_format.space_after=Pt(3)

widths=[
 [1.7,.65,1.6,1.3,1.5],[2.5,2.15,2.1],[2.5,2.15,2.1],
 [2.1,1.2,1.15,1.05,1.25],[2.4,1.65,1,1.7],[1.3,.8,.7,2.95,1.0],
 [1.8,1.25,1.3,2.4],[2.1,1.25,1.1,1.1,1.2],[3.5,3.25],
 [3.05,1.25,1.25,1.2],[1.2,4.2,1.35],[1.5,.8,.85,1.2,1.35,1.05],
 [.7,1.35,1.45,1.3,1.95],[1.5,1,1.2,2.25,.8],[2.1,.65,1.3,1.25,1.45],[3.45,1,2.3]]
for ti,old_table in enumerate(list(doc.tables)):
 # Rebuild into native inline Word tables with a defined style and explicit
 # widths. Pandoc's undefined Table/Compact styles break this renderer.
 table=doc.add_table(rows=len(old_table.rows),cols=len(old_table.columns))
 table.style='Table Grid';table.autofit=False
 ws=widths[ti];ws=[w*6.75/sum(ws) for w in ws]
 for ci,col in enumerate(table.columns):col.width=Inches(ws[ci])
 tw=table._tbl.tblPr.find(qn('w:tblW'));tw.set(qn('w:type'),'dxa');tw.set(qn('w:w'),'9720')
 for ri,row in enumerate(old_table.rows):
  for ci,cell in enumerate(row.cells):
   dst=table.cell(ri,ci);dst.width=Inches(ws[ci])
   for child in list(dst._tc):
    if child.tag!=qn('w:tcPr'):dst._tc.remove(child)
   for child in cell._tc:
    if child.tag!=qn('w:tcPr'):dst._tc.append(copy.deepcopy(child))
 parent=old_table._tbl.getparent();idx=parent.index(old_table._tbl)
 parent.remove(old_table._tbl);parent.insert(idx,table._tbl)
 for row_i,row in enumerate(table.rows):
  trPr=row._tr.get_or_add_trPr();cant=OxmlElement('w:cantSplit');trPr.append(cant)
  if row_i==0:
   repeat=OxmlElement('w:tblHeader');trPr.append(repeat)
  for cell in row.cells:
   for p in cell.paragraphs:
    p.style='Normal'
    p.paragraph_format.keep_with_next=False
    p.paragraph_format.space_after=Pt(3);p.paragraph_format.space_before=Pt(2)
    p.paragraph_format.line_spacing=1.0
    for r in p.runs:r.font.size=Pt(9)
    if row_i==0:
     for r in p.runs:r.bold=True

# Keep mathematical glyph size consistent with the body, including wide sums.
for mr in doc._element.xpath('//m:r'):
 rp=mr.find(qn('w:rPr'))
 if rp is None:rp=OxmlElement('w:rPr');mr.insert(0,rp)
 sz=rp.find(qn('w:sz'))
 if sz is None:sz=OxmlElement('w:sz');rp.append(sz)
 sz.set(qn('w:val'),'21')

doc.core_properties.title='SAM Volume III Computation and Reciprocal History'
doc.core_properties.author='Sean Brady'
doc.core_properties.subject='Revised expanded manuscript with source and evidence appendix'
doc.core_properties.comments='Manuscript revision directed by Sean Brady with OpenAI ChatGPT and Codex'
doc.save(OUT/'SAM_Volume_III_Revised.docx')
subprocess.run([PANDOC,str(WORK/'manuscript.json'),'-f','json','-t','plain','-o',str(WORK/'manuscript_plain.txt')],check=True,capture_output=True)
print(json.dumps({'chapters':len(chapter_map),'blocks':len(blocks),'docx_bytes':(OUT/'SAM_Volume_III_Revised.docx').stat().st_size,'conversion_warnings':conversion_warning_count,'word_count':len((WORK/'manuscript_plain.txt').read_text().split())}))
