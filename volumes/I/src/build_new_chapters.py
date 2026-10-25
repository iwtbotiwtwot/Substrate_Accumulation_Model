from pathlib import Path
import re,subprocess,json,sys
ROOT=Path(__file__).resolve().parent
TITLES={6:'Quantum routes, shared fields and retained physical records',7:'Horizon thermodynamics and accessible information',8:'Cosmic inventory and the Hubble cascade',9:'Thermal history, recombination and CMB structure',10:'Many-source accumulation and galaxy halos',11:'Carrier radiation and ringdown dynamics',12:'Cosmological fate and the completed boundary',13:'Home: information on an endless chain of two-dimensional closed spheres',14:'Evidence, closures and remaining physical assignments',15:'Supplement: retired targets (Chapter X of the 19 October 2026 edition)'}
ROMANS={6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII',13:'XIII',14:'Appendix',15:'Supplement'}
selected={int(x) for x in sys.argv[1:]} if len(sys.argv)>1 else set(TITLES)
for i,title in TITLES.items():
 if i not in selected: continue
 p=ROOT/('closure_appendix.tex' if i==14 else 'supplement_retired.tex' if i==15 else f'ch{i:02d}.tex')
 if not p.exists():continue
 body=p.read_text()
 abstract=''
 match=re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',body,re.S)
 if match:
  abstract=match.group(1).strip();body=body[:match.start()]+body[match.end():]
 (ROOT/f'body{i:02d}.tex').write_text(body)
 roman=ROMANS[i]
 opener=r'''\input{preamble.tex}
\newcommand{\ChapterRoman}{'''+roman+r'''}
\hypersetup{pdftitle={SAM Volume I: '''+title+r'''},pdfauthor={Sean Brady}}
\begin{document}
'''+(r'\fancyhead[L]{\footnotesize SAM Volume I | Supplement}' if i==15 else r'\fancyhead[L]{\footnotesize SAM Volume I | Appendix A}' if i==14 else '')+r'''
\twocolumn[{
\begin{center}
{\small SAM VOLUME I\par}
\vspace{0.4em}
{\LARGE\bfseries '''+title+r'''\par}
\vspace{0.4em}
{\large '''+('Appendix' if i==14 else 'Supplement to Volume I' if i==15 else 'Chapter '+roman)+r'''\par}
\vspace{0.5em}
{\large Sean Brady\par}
{\small Originator and conceptual director\par}
{\small Research development with OpenAI ChatGPT and Codex\par}
{\small Edition of 25 October 2026 (text of the unified expanded edition, 19 October 2026)\par}
\end{center}
'''
 if abstract:opener+=r'\begin{minipage}{0.97\textwidth}\noindent\textbf{Abstract.} '+abstract+r'\end{minipage}'+'\n'
 opener+=r'\vspace{0.9em}}]'+'\n'+r'\input{body'+f'{i:02d}'+r'.tex}'+'\n'+r'\end{document}'+'\n'
 (ROOT/f'chapter{i:02d}.tex').write_text(opener)
 for run in range(2):
  r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',f'chapter{i:02d}.tex'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  (ROOT/f'chapter{i:02d}.build.log').write_text(r.stdout)
  if r.returncode: print(f'FAIL {i}: '+r.stdout[-1800:]);break
 else: print('BUILT',i)
