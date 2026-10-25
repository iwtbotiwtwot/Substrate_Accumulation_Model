from pathlib import Path
import json,hashlib,collections
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]; W=R/'manuscript'; E=R/'evidence'
OLD=Path('/home/lilhelper/Documents/Codex/2026-10-19/we/work/volume_iii/expanded')
ARCH=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project')
titles=[
 ('A1','N2000_PRE_Expanded_Rev3(1).pdf','Exact joint densities and low-energy structure of complete Ising graphs with tractable corrections','libfile_72e347f72e948191b8d066bde1da9383','27 September 2026'),
 ('A2','Prime_Event_PRE_Expanded_Rev3(1).pdf','Reliability and resource tradeoffs in hidden-spin feedback for prime-sequence computation','libfile_fedd048f461881919e053e75267bcecd','27 September 2026'),
 ('A3','SLC_Exact_Exchange_and_Symbolic_Matter_2026-09-20_Public_Link(2).pdf','The Substrate Ledger Computer Exact Exchange and Symbolic Matter','libfile_4d0db3cfb228819183cd6773a6fb107d','20 September 2026'),
 ('A4','SLC_Executable_History_Research_Paper_2026-09-14_Updated(4).pdf','The Substrate Ledger Computer Executable history as a research method','libfile_a358c994656081918071c95d6a37099e','14 September 2026'),
 ('A5','SLC_Starbreaker_ATOM3D_GEN3_2026-09-14(4).pdf','The Substrate Ledger Computer Starbreaker and ATOM3D','libfile_4a0c3368f88c8191a7109f1e47e4ee02','14 September 2026'),
 ('A6','SLC_Equal_Observable_States_Distinct_Executable_Histories.pdf','Equal Observable States Distinct Executable Histories','libfile_5dde2eba501c81918f7b149ee417c076','5 September 2026'),
 ('A7','SAM_Volume_III_Expanded.pdf','SAM Volume III Computation and Reciprocal History','libfile_f058ba1c5684819190f28a58586cc859','19 October 2026')]
def identity(p):return {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
attach=[];s='# Appendix A Sources and evidence\n\n'
s+='This appendix identifies the evidence used in the revised manuscript. Bracketed source keys in the chapters point to these entries. Page locators refer to the numbered PDF pages in the attached source, rather than to this edition. Exact mathematical identities, completed campaign results, numerical evaluations, conditional implications and editorial arithmetic retain their separate meanings.\n\n'
s+='## The seven attachments\n\n'
for key,name,title,lid,date in titles:
 p=R/'attachments'/name;rec={'key':key,'title':title,'file_name':name,'library_file_id':lid,'date':date,'pages':len(PdfReader(p).pages),**identity(p)};attach.append(rec)
 s+=f'**{key}** Sean Brady. *{title}*. {date}. {rec["pages"]} pages. Supplied filename: `{name}`. Library ID `{lid}`. SHA256 prefix `{rec["sha256"][:16]}`.\n\n'
s+='The four short source keys used in the SLC chapters are aliases: **EX = A3**, **RH = A4**, **SB = A5**, and **EQ = A6**. The attached expanded volume A7 is the revision baseline. Its SHA256 is `791be1b6acefeacac5b46c9911d070b7c2767ef17e43e79ced38a6150d01d2c8`; it matches the retained expanded PDF in the prior local delivery and its editable source edition. The live documentation repository holds the older 69-page source PDF with SHA256 `62fff442f4a6c5aab1ff5bbc5e2f4cd094823d75ecf0734cd333f0f743010d8f`. The revised volume therefore preserves the later expansion.\n\n'
s+='## Evidence chains for the principal results\n\n'
s+='**N5000.** Frozen parent sources feed the source-bound preparation, exact polynomial backend and paired-encoding production. The production archive manifest binds each source, boundary, count and digest. Lossless archive verification, source recovery and the later final-download receipt close the preserved custody chain. The total 1,530,259,992 is the editorial sum of the manifest\'s 96 primary K_MAJOR logical-row counts. It counts each joint measure once. `n5000_manifest_aggregation.json` in the companion evidence archive preserves that calculation. The complete bulk archive was not decompressed anew for this revision.\n\n'
s+='**N2000.** A1 distinguishes the original full joint-density production from later minimum/count and truncated-spectrum calculations reconstructed from the published source definitions. Its source and integer identities support the joint enumeration; its separate derivations support ground counts, commensurate entropy limits, field crossings and controlled canonical readouts. The later physical analysis does not claim a fresh readback of the original bulk shards. A1 reports the source archive DOI `10.5281/zenodo.22989862` and reproduction commit `9773a4e4757e7503bfe279c04459c1356681220d`.\n\n'
s+='**Prime event.** The pair/triple compiler and full 128-state dynamics define the gate. Seed replay identifies the one-bank weakness. The balance derivation and design records precede successor generation. The final matched and fresh reports supersede the older report whose successor run was pending. A2 additionally reports Poisson reanalysis, an ideal-history census and alternative budget/readout controls. Those new control values are attributed to A2; their analysis package was not separately materialized for this manuscript revision. Later source-derived gates, long raw trajectories and activity-clock experiments retain the distinct source keys in Chapter XXV.\n\n'
s+='**History exchange and arithmetic.** A3 through A6 supply complete derivations and finite result tables. Immutable archive entries H001563 and H001565 corroborate length-13 exchange closure and symbolic matter composition; H001428 corroborates the finite future-sign branch certificates. Their underlying campaigns remain identified in the attachment source sections. The conditional RH argument proves an implication from a uniform bound; finite prefix scans do not establish that hypothesis. Prime-event computation, the exact prime ruler and Mersenne work, and FEOP remain distinct programs unless an explicit source constructs an interface. No FEOP equivalence is asserted here.\n\n'
s+='## N5000 source register\n\nAll relative paths in the next two registers begin at `/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/`. A SHA256 prefix is shown for readability; full identities are in the companion source manifest.\n\n'
n5=json.loads((E/'n5000_sources.json').read_text())
for key,rows in __import__('itertools').groupby(n5,key=lambda x:x['id']):
 rows=list(rows);s+=f'**{key}** {rows[0]["title"]}.\n\n'
 for r in rows:s+=f'`{r["relative_path"]}`. SHA256 `{r["sha256"][:16]}`; {r["bytes"]:,} bytes.\n\n'
s+='## Prime event source register\n\n'
pe=json.loads((E/'prime_source_manifest.json').read_text())
desc={
 'PE2':['Final matched and fresh ensemble evidence',['GEN4/prime_balance1/REPORT.md','GEN4/prime_balance1/ANALYSIS.json','GEN4/prime_balance1/COMPARISON.json','GEN4/prime_balance1/HOLDOUT_ANALYSIS.json','GEN4/prime_balance1/FINAL_VERIFIED.json']],
 'PE3':['Prospective source derivation and qualification',['GEN4/prime_balance1/DERIVATION.md','GEN4/prime_balance1/DESIGN.md','GEN4/prime_balance1/POD_PLAN.md','GEN4/prime_balance1/HOLDOUT_PLAN.md','GEN4/prime_balance1/SOURCE_CHECK.json','GEN4/prime_balance1/QUALIFICATION_CHECK.json']],
 'PE4':['Original construction and first-error replay synthesis',['GEN4/prime_event_report2/REPORT.md']],
 'PE5':['Measured Ising boundary response to gate transfer',['GEN4/spin_prime_connection1/REPORT.md']],
 'PE6':['Exact hidden-spin projection and memory',['GEN4/prime_sam_dynamics1/REPORT.md']]}
extra=[]
for key,(title,paths) in desc.items():
 s+=f'**{key}** {title}.\n\n'
 for path in paths:
  p=ARCH/path
  if p.exists():
   rec={'key':key,'title':title,'path':str(p),'relative_path':path,**identity(p)};extra.append(rec)
   s+=f'`{path}`. SHA256 `{rec["sha256"][:16]}`.\n\n'
s+='## SLC source corroboration\n\n'
hist=['SAM_HISTORY/entries/H001563_2026-09-19_N72_GPU_COMPLETE_L13_CLOSURE.md','SAM_HISTORY/entries/H001565_2026-09-20_VOLII_EXCHANGE_FUSION_CURRENT_COLLECTIVE.md','SAM_HISTORY/entries/H001428_2026-09-14_FORCING_CURRENT_SOURCE_FUTURE_CONTROL.md']
for path in hist:
 p=ARCH/path
 if p.exists():
  rec={'key':p.name.split('_')[0],'path':str(p),'relative_path':path,**identity(p)};extra.append(rec)
  s+=f'**{rec["key"]}** `{path}`. SHA256 `{rec["sha256"][:16]}`.\n\n'
s+='## Retained source register from the expanded baseline\n\n'
s+='The following source keys are preserved from A7. They support the retained foundation and later runtime, response, matter, arithmetic and prime-clock material. These are the identities recorded by that edition. Full paths and original notes remain in the companion manifest. Sources marked public retain their repository and commit anchors. Historical engine versions describe their own stages.\n\n'
base=json.loads((OLD/'SOURCE_REGISTER.json').read_text())
for r in base:
 s+=f'**{r["key"]}** {r["title"]}. `{r["path"]}`. SHA256 `{r["sha256"][:16]}`.'
 if r.get('origin')=='public':s+=' Repository '+r.get('repository','')+'; commit `'+r.get('commit','')+'`.'
 s+='\n\n'
s+='The twelve foundation chapters also retain their direct links to the fixed SAMA source revision `4c2b5dc1649da5900c90b90d0ce56c223dbb7717`. Their supplied explanatory source manuscripts remain in the prior edition\'s source package; source identities were preserved during the chapter merge and reordering.\n\n'
s+='# Appendix B Revision summary\n\n'
s+='This revision expands the attached 107-page edition while retaining its useful research exposition. The change is organized around the completed mathematical and computational objects.\n\n'
for text in [
 '**A full N5000 chapter.** Adds the six-source construction, all primary record totals, packet and gateway factorization, two injective encodings, modular integer reconstruction, conditional closure and moment checks, measured production, archive and source-recovery chain, reusable responses and the separately normalized thermal and occupied-window results.',
 '**A full N2000 physics chapter.** Develops the attachment\'s exact ground states, degeneracies, commensurate residual-entropy derivation, excitation gaps, field thresholds, bin-sensitive finite entropy and controlled low-temperature heat capacities. Its source size and later physical-readout provenance remain distinct from N5000.',
 '**A full prime-event reliability chapter.** Explains the event-created sieve, seven-spin source, hidden-spin elimination, finite-state three-reading dynamics, first-error replay, prospective balance, matched and fresh ensembles, Poisson and ideal-census analysis, and explicit budget and temporal-confirmation comparisons. The later continuation and clocks receive a separate chapter.',
 '**Executable history and exact matter.** Adds the explicit equal-observation witness, sufficient-observation criterion, reversible reconstruction and weave. Gives exact exchange and symbolic matter a complete chapter from source quartics through Bethe checks, length-13 spectra, reusable composition, fusion and compatible collective interaction.',
 '**Starbreaker and arithmetic.** Restores the closed-cycle and complete two-channel receiver results, signed Li6 construction and native production counts. Adds the original signed Möbius energy, its history-sensitive modes and cancellation, finite continuation certificates and the precisely conditional RH implication.',
 '**An editorial pass through the full baseline.** Removes the duplicated Chapter I overview and derivation while retaining its additional controls, architecture and source labels. Replaces vague classification formulas with the actual nearby result, comparison and scope. Preserves negative outcomes and numerical successors in their relevant contexts.',
 '**Consistent presentation.** Uses one chapter hierarchy, editable mathematical equations, readable single-column pages, source keys and a linked contents list. Definitions introduce the principal new formulas. No flowcharts are included.'
]:s+=text+'\n\n'
s+='## Scope of verification for this edition\n\nThe revision used source reading, bounded arithmetic and transcription checks, source manifests, document structure checks and rendered-page inspection. It did not rerun historical scientific campaigns or alter installed research software, live sources, original volumes or sealed records. The N5000 record total, prime-gate balance and budget arithmetic, exact history witness, finite-state multiplicity totals and selected N2000 entropy and tail-bound values were checked as editorial arithmetic. Such checks catch transcription errors; they do not establish novelty or replace the scientific validations reported by each source.\n\n'
s+='The editable DOCX and PDF represent the same revised manuscript. The companion evidence archive retains the chapter source text, source manifests and editorial check records. Research bulk datasets remain at the canonical locations named by their own archives.\n'
(W/'appendices.md').write_text(s)
manifest={'baseline':attach[-1],'attachments':attach,'n5000_sources':n5,'prime_sources':extra,'baseline_retained_sources':base,'scientific_campaigns_run':False,'live_source_edits':False}
(E/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({'attachments':len(attach),'n5000_source_files':len(n5),'retained_sources':len(base),'appendix_words':len(s.split())}))
