from pathlib import Path
import fitz, json, re, subprocess, hashlib
ROOT=Path(__file__).resolve().parent
TITLES=[('I','Original Write histories and an interacting source-field action'),('II','Retention, accumulation, and the finite ledger'),('III','The spherical accumulation kernel and the source-to-field interface'),('IV','Clocks, signals, and calibrated observation'),('V','Strong fields and the approach to unit accumulation'),('VI','Quantum routes, shared fields and retained physical records'),('VII','Horizon thermodynamics and accessible information'),('VIII','Cosmic inventory and the Hubble cascade'),('IX','Thermal history, recombination and CMB structure'),('X','Many-source accumulation and galaxy halos'),('XI','Carrier radiation and ringdown dynamics'),('XII','Cosmological fate and the completed boundary'),('A','Evidence, closures and remaining physical assignments')]
files=[ROOT/'assets'/f'ch{i:02d}_retained.pdf' if i<=5 else ROOT/f'chapter{i:02d}.pdf' for i in range(1,14)]
for f in files:
 if not f.exists(): raise SystemExit('Not ready: '+str(f))
entries=[];pos=4
for (roman,title),file in zip(TITLES,files):
 d=fitz.open(file); entries.append(dict(chapter=roman,title=title,start=pos,pages=len(d),file=str(file.relative_to(ROOT))));pos+=len(d)
rows='\n'.join(r'\textbf{'+x['chapter']+r'} & '+x['title']+r' & '+str(x['start'])+r'\\[9pt]' for x in entries)
front=r'''\input{preamble.tex}
\newcommand{\ChapterRoman}{Front matter}
\begin{document}\onecolumn\fancyhead[L]{\footnotesize SAM Volume I | Substrate and Accumulation}\thispagestyle{empty}
\begin{center}
\vspace*{0.8in}
{\small SUBSTRATE ACCUMULATION MODEL\par}\vspace{0.35in}
{\Huge\bfseries SAM Volume I\par}\vspace{0.15in}
{\LARGE Substrate and Accumulation\par}\vspace{0.18in}
{\large Chapters I--XII\par}\vspace{0.65in}
{\Large Sean Brady\par}\vspace{0.08in}
{\normalsize Originator and conceptual director\par}\vspace{0.5in}
{\large Unified expanded working edition\par}
{\normalsize 19 October 2026\par}
\end{center}
\vfill
\noindent This edition brings the twelve chapters into one continuous manuscript. Chapters I--V retain the submitted mathematical text; Chapter VI is retypeset from its integrated source without its separate contents pages. Chapters VII--XII are substantially expanded with worked derivations, explicit physical assumptions, and reproducible arithmetic checks. A reconciled evidence appendix replaces the earlier closing review and interface list.
\vspace{0.15in}
\noindent\small Chapters I--VI were developed with OpenAI ChatGPT and Codex, with the contributor credits recorded in the individual chapters retained. The submitted Chapter VII and initial VIII--XII drafts, and the earlier closing review, credit Claude/Claude Code under Sean Brady's direction. The present expansion, source recovery, editorial reconciliation and unified assembly were prepared with OpenAI ChatGPT and Codex. These credits describe the development history, not independent scientific endorsement.
\clearpage
\section*{Contents}
\noindent\begin{tabularx}{\textwidth}{@{}p{0.45in}Xr@{}}\toprule
\textbf{Chapter}&\textbf{Title}&\textbf{Page}\\\midrule
'''+rows+r'''
\bottomrule\end{tabularx}
\vspace{0.2in}
\noindent There is one volume-wide contents list and one continuous page sequence. Chapter and section bookmarks provide navigation within the PDF. Equations, figures, tables and references are numbered locally within their chapter; citations should therefore name the chapter as well as the local identifier.
\clearpage
\section*{How to read this edition}
\subsection*{A physical construction with its assumptions visible}
The volume moves from finite source histories and retained accounts to spatial response, clocks and signals, strong fields, quantum records, boundary thermodynamics, cosmic inventory, thermal history, halos, radiation and possible cosmic futures. The same word can describe different mathematical objects in these settings. A count is not automatically a mass; a propagation account is not automatically a density; a finite source calculation is not automatically a long-time cosmological law. Each join must identify the receiving law, its units, and the observable it supplies.

The expanded chapters separate exact identities, theorems under declared assumptions, results reported by retained computational records, and physical hypotheses awaiting selection or calibration. The new worked examples are analytic comparisons and finite arithmetic checks. They do not constitute new native GEN6 campaigns, new observational fits, or experimental validation. Where the submitted closing review claimed more than its evidence established, Appendix A records the narrower conclusion and the remaining interface.

\subsection*{Continuity with the submitted manuscript}
The latest submitted content, rather than an older shorter chapter, is the preservation baseline. Chapters I--III match their earlier formatting sources exactly. The integrated source for Chapter IV, Chapter V and Chapter VI was recovered from the archived research revision \texttt{6890eae4cb5f33c766c86ce10f43b5165a4c4157}. The original vector content of Chapters I--V is retained, with harmonized running headers and continuous folios. Chapter VI retains its complete source-derived body and proofs while changing its layout. Historical dates, receipt identifiers and claims of historical verification keep their original scope.

Some retained passages describe earlier development stages. Read them together with their later continuation and the current evidence appendix. A historical section's list of open tasks is not necessarily the final status of the chapter. Conversely, a conditional closure is not promoted to an unconditional physical law by inclusion in this volume. References to old packet pages identify those archived packets unless an explicit chapter and current volume page is given.

\subsection*{Sources, code and verification}
The companion source package contains the editable chapter sources, figures, manuscript build instructions, source-recovery provenance, new arithmetic checks and assembly verification. The evidence appendix inventories the earlier review's identifiers so that revised conclusions remain traceable. Historical native evidence and observational results are reported from their sources; they have not been represented as rerun for this edition.

The opening chapter's public data repository is \url{https://github.com/iwtbotiwtwot/sam_volume_I_i}; Chapter II's is \url{https://github.com/iwtbotiwtwot/sam_volume_I_ii}. Other chapter-specific source records and references remain with their respective chapters. The archived research revision used for source recovery is identified in the companion provenance manifest. Repository accessibility and the presence of a receipt do not replace checking its mathematical or empirical scope.

\subsection*{What the expansion is intended to accomplish}
The later chapters now explain the intermediate calculations that short drafts left implicit: thermodynamic balances and accessible information; the dimensionful inventory cascade; recombination and visibility; potential, force and halo inversion; radiative flux and spectral boundary conditions; and conservation, causal horizons and future evolution. Solved examples expose which conclusions follow from the stated equations and which require an additional physical law. This is a fuller working manuscript for scientific review, with no imposed chapter page limit.
\end{document}
'''
(ROOT/'front.tex').write_text(front)
for _ in range(2):
 r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','front.tex'],cwd=ROOT,capture_output=True,text=True)
 (ROOT/'front.build.log').write_text(r.stdout)
 if r.returncode:raise SystemExit(r.stdout[-2000:])
f=fitz.open(ROOT/'front.pdf')
if len(f)!=3: raise SystemExit('Front matter must have 3 pages; got '+str(len(f)))
out=fitz.open();out.insert_pdf(f);toc=[[1,'Title',1],[1,'Contents',2],[1,'How to read this edition',3]]
for ent,file in zip(entries,files):
 d=fitz.open(file);offset=len(out);out.insert_pdf(d)
 toc.append([1,('Appendix A' if ent['chapter']=='A' else 'Chapter '+ent['chapter'])+' — '+ent['title'],offset+1])
 if ent['chapter'] not in ['I','II','III','IV','V']:
  for level,title,page in d.get_toc():
   if page>0:toc.append([min(level+1,4),title,offset+page])
 for j in range(offset,len(out)):
  p=out[j]
  # The common typography leaves these running-furniture bands clear of body text.
  p.add_redact_annot(fitz.Rect(0,0,p.rect.width,39),fill=(1,1,1))
  p.add_redact_annot(fitz.Rect(0,750,p.rect.width,792),fill=(1,1,1))
  p.apply_redactions(images=0,graphics=0)
  p.draw_rect(fitz.Rect(0,0,p.rect.width,44),color=None,fill=(1,1,1))
  label='Appendix A' if ent['chapter']=='A' else 'Chapter '+ent['chapter']
  p.insert_text((49,36),'SAM Volume I | '+label,fontname='tiro',fontsize=8,color=(0,0,0))
  right='Brady | Unified expanded edition';w=fitz.get_text_length(right,fontname='tiro',fontsize=8)
  p.insert_text((563-w,36),right,fontname='tiro',fontsize=8)
  p.draw_line((49,42),(563,42),color=(.35,.35,.35),width=.3)
  folio=str(j+1);w=fitz.get_text_length(folio,fontname='tiro',fontsize=8)
  p.insert_text(((612-w)/2,765),folio,fontname='tiro',fontsize=8)
out.set_toc(toc)
# Link each contents title to its final page.
for ent in entries:
 for rect in out[1].search_for(ent["title"]):
  out[1].insert_link({"kind":fitz.LINK_GOTO,"from":rect,"page":ent["start"]-1})
out.set_metadata(dict(title='SAM Volume I: Substrate and Accumulation — Unified Expanded Edition',author='Sean Brady',subject='Twelve-chapter unified working manuscript, 19 October 2026',keywords='SAM, substrate accumulation, quantum records, cosmology'))
(ROOT.parent/'pdf').mkdir(exist_ok=True)
final=ROOT.parent/'pdf'/'SAM_Volume_I_Unified_Expanded_Chapters_I-XII_20261019.pdf'
out.save(final,garbage=4,deflate=True)
(ROOT/'checks'/'assembly.json').write_text(json.dumps(dict(pages=len(out),chapters=entries,output=final.name,sha256=hashlib.sha256(final.read_bytes()).hexdigest()),indent=2))
print(final,len(out))
