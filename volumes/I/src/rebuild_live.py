"""Build the live copies of Chapters II-V and VII (live_sources/, attribution pass of 2 November 2026) into assets/*_live.pdf."""
from pathlib import Path
import shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
entries={1:'chapter1_as_vii.tex',2:'chapter2_source_field_formatted.tex',3:'chapter3_formatted.tex',4:'chapter.tex',5:'chapter.tex'}
out={1:'ch07_write_histories_live.pdf',2:'ch02_live.pdf',3:'ch03_live.pdf',4:'ch04_live.pdf',5:'ch05_live.pdf'}
for n,entry in entries.items():
 source=ROOT/'live_sources'/f'ch{n:02d}';work=ROOT/'live_build'/f'ch{n:02d}'
 if work.exists(): shutil.rmtree(work)
 shutil.copytree(source,work)
 if n==4:
  p=work/entry;s=p.read_text().replace('[utf 8]','[utf8]').replace('ps 2pk 35.map','ps2pk35.map');p.write_text(s)
 for _ in range(2):
  r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',entry],cwd=work,capture_output=True,text=True)
  if r.returncode: print(f'FAIL ch{n:02d}:',r.stdout[-1500:]); sys.exit(1)
 shutil.copy2(work/Path(entry).with_suffix('.pdf'),ROOT/'assets'/out[n]); print('BUILT',out[n])
