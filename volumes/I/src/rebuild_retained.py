"""Optional rebuild of early chapters after editing their retained TeX sources."""
from pathlib import Path
import shutil,subprocess
ROOT=Path(__file__).resolve().parent
entries={1:'chapter1_expanded.tex',2:'chapter2_source_field_formatted.tex',3:'chapter3_formatted.tex',4:'chapter.tex',5:'chapter.tex'}
for n,entry in entries.items():
 source=ROOT/'retained_sources'/f'ch{n:02d}';work=ROOT/'retained_build'/f'ch{n:02d}'
 shutil.copytree(source,work,dirs_exist_ok=True)
 if n==4:
  p=work/entry;s=p.read_text().replace('[utf 8]','[utf8]').replace('ps 2pk 35.map','ps2pk35.map');p.write_text(s)
 for _ in range(2):subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',entry],cwd=work,check=True)
 shutil.copy2(work/Path(entry).with_suffix('.pdf'),ROOT/'assets'/f'ch{n:02d}_retained.pdf')
print('Retained chapter PDFs rebuilt. Run assemble_volume.py to regenerate the volume.')
