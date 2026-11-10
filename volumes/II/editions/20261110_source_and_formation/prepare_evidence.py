from pathlib import Path
import json,shutil,hashlib
E=Path(__file__).resolve().parent
R=E.parents[4]
S=E/'src'
C='Courtroom_II/campaigns/volii_relaxation_20261110/01_source_connected_certificates'
I='ironclad/campaigns'; A=I+'/volii_receiving_action_20261110'
H='Courtroom_II/campaigns/he3_relaxed_field_20261108/02_independent_verification/peers/VERIFIER'
items={
'NOV_A1':('Light sources: complete operators, preparations and relaxed He3',I+'/volii_a1_light_sources_20261108/RESEARCH_REPORT.md'),
'NOV_HE3_CASE':('Relaxed He3: complete normalized field payment',I+'/he3_relaxed_field_cr2_20261108/REPORT.md'),
'NOV_HE3_VERIFY':('Independent verification of the shared complete-payment statement',I+'/he3_relaxed_field_verification_20261108/REPORT.md'),
'NOV_CONSTRUCTOR':('Isotope constructor: source composition and exact complements',I+'/volii_isotope_constructor_20261108/RESEARCH_REPORT.md'),
'NOV_FREE':('Full free reference and retained-template preparation: verified case','Courtroom_II/campaigns/isotope_constructor_checks_20261108/01_free_reference/REPORT.md'),
'NOV_COV':('Shared-field covariance and actual signed source payment: verified case','Courtroom_II/campaigns/isotope_constructor_checks_20261108/02_shared_field_covariance/REPORT.md'),
'NOV_BRIDGE':('Actual Li6 bridge/action, coherent events and microscopic baselines',I+'/volii_li6_bridge_action_20261108/RESEARCH_REPORT.md'),
'NOV_COMMON_RECEIVER':('Actual He4 K4 plus H2: common fermionic receiver and complete currents',I+'/he4_k4_free_receiver_20261108/RESEARCH_REPORT.md'),
'NOV_JOINT':('Joint receiver and complete field continuation',I+'/volii_joint_receiver_field_20261110_w1/RESEARCH_REPORT.md'),
'NOV_RELAX':('Physical-source relaxation and common spatial energy certificates',I+'/volii_physical_relaxation_20261110_w2/RESEARCH_REPORT.md'),
'NOV_LI6_CASE':('Source-connected scalar certificates: nine claims held',C+'/REPORT.md'),
'NOV_LI6_CHANNEL':('Common Hamiltonian, full-Fock square and proper-channel lower',C+'/peers/CHANNEL/DERIVATION.md'),
'NOV_LI6_TRANSFER':('Finite actual-source transfer and parameter-box certificate',C+'/peers/TRANSFER/DERIVATION.md'),
'NOV_LI6_SYMMETRY':('Full flavor-preserving source map and unchanged-preparation certificate',C+'/peers/SYMMETRY/DERIVATION.md'),
'NOV_RECEIVING':('Receiving action and formation: completed investigation and review',A+'/RESEARCH_REPORT.md'),
'NOV_ARRIVAL':('Spatial source instrument: flavor factorization and work',A+'/peers/ONE/gen/SPATIAL_INSTRUMENT_REPAIR_WORKING.md'),
'NOV_CONTROL':('Flavor-preserving controls and source-response constructions',A+'/peers/ONE/REPORT.md'),
'NOV_LOADING':('Finite-time loading, energy-form errors and collective clock',A+'/peers/THREE/REPORT.md'),
'NOV_RESPONSE':('Receiving action and independent source-response tests',A+'/peers/FOUR/REPORT.md'),
'NOV_ACTION':('Canonical action family and response-calibrated robustness',A+'/peers/FOUR/gen/ACTION_FAMILY_AND_ROBUSTNESS.md'),
'NOV_BATTERY':('Finite coherent work reservoir: conditional global construction',A+'/peers/FOUR/gen/FINITE_BATTERY_WORKING.md'),
'NOV_THERMAL':('Full-Fock thermal energy and conditional spectral formation',A+'/peers/TWO/REPORT.md')}
extras=[I+'/he3_relaxed_field_cr2_20261108/DERIVATION.md',H+'/HYPOTHESES.md',H+'/DERIVATION_BEFORE_EXECUTION.md',H+'/NOTES.md',A+'/host/review/LEAD_CONSISTENCY_CHECK.json',A+'/host/review/lead_consistency_check.py',A+'/host/review/PRIMARY_SOURCE_READBACK.json',A+'/peers/FOUR/CLOSING_AUDIT.md',A+'/peers/FOUR/gen/STATIC_KERNEL_IDENTIFICATION.json',A+'/peers/FOUR/gen/FLAVOR_VERTEX_PROBES.json',A+'/peers/FOUR/gen/Q4_SOURCE600_REPAIR.json',A+'/RESULTS_INDEX.json',C+'/RESULTS/INTEGRATION.json',C+'/RESULTS/LEAD_REVIEW.json']
extras += [C+'/peers/'+t+'/HYPOTHESES.md' for t in ['CHANNEL','TRANSFER','SYMMETRY']]
extras += ['Courtroom_II/campaigns/isotope_constructor_checks_20261108/01_free_reference/peers/VERIFIER/SCOPE_CLARIFICATION.md']
paths=sorted({p for _,p in items.values()}|set(extras))
for rel in paths: assert (R/rel).is_file(),R/rel
manifest=[]
for rel in paths:
 src=R/rel; dest=E/'evidence'/rel
 dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dest)
 manifest.append({'original':str(src),'snapshot':str(dest.relative_to(E)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'bytes':src.stat().st_size})
(E/'EVIDENCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
p=S/'bibliography.tex'; s=p.read_text()
new='\n'
for key,(title,path) in items.items():
 new+='\\bibitem{'+key+'}\\emph{'+title+'}. SAM Research Project, November 2026.\nSource: \\path{'+path+'}. Selected snapshot and SHA-256 digest accompany this edition.\n\n'
new+=r'''\bibitem{NOV_NP_LIT} R. W. Hackenburg, ``Neutron-proton effective range parameters and zero-energy shape dependence,'' \emph{Physical Review C} \textbf{73}, 044002 (2006). \url{https://doi.org/10.1103/PhysRevC.73.044002}.

\bibitem{NOV_CAPTURE_LIT} M. Anders et al. (LUNA Collaboration), ``First direct measurement of the $^2\mathrm H(\alpha,\gamma)^6\mathrm{Li}$ cross section at Big Bang energies and the primordial lithium problem,'' \emph{Physical Review Letters} \textbf{113}, 042501 (2014). \url{https://doi.org/10.1103/PhysRevLett.113.042501}.

\bibitem{NOV_BATTERY_LIT} G. Chiribella, Y. Yang and R. Renner, ``Fundamental energy requirement of reversible quantum operations,'' \emph{Physical Review X} \textbf{11}, 021014 (2021). \url{https://doi.org/10.1103/PhysRevX.11.021014}.
'''
if '\\bibitem{NOV_A1}' not in s:p.write_text(s.replace('\\end{thebibliography}',new+'\n\\end{thebibliography}'))
old=json.loads((S/'CHAPTERS.json').read_text())
for row in old:
 extra={'nuclear_01.tex':'nuclear_20261110.tex','nuclear_02.tex':'formation_20261110.tex','scale_01.tex':'receiving_20261110.tex'}.get(row['file'])
 row['revision_20261110']=bool(extra)
 if extra:row['included_revision_source']=extra
 row['word_count']=len((S/row['file']).read_text().split())+(len((S/extra).read_text().split()) if extra else 0)
(S/'CHAPTERS.json').write_text(json.dumps(old,indent=2)+'\n')
(S/'EDITORIAL_SCOPE.json').write_text(json.dumps({'edition':'20261110_source_and_formation','baseline_pdf':'../../../pdf/SAM_Volume_II_20261105_authorship_draft.pdf','main_chapters':19,'appendices':['Conditional reservoirs, clocks and thermal formation','Evidence and scope of the November revision'],'expanded_chapters':[11,12,16],'new_scientific_runs':0,'originals_preserved':True,'authorship':'Sean Brady','new_ai_credit':False,'scope':'Verified He3/free-reference/covariance/Li6 inputs; conditional latest receiving/formation constructions clearly distinguished.'},indent=2)+'\n')
(E/'COVERAGE.json').write_text(json.dumps({'citations':{k:{'title':v[0],'owning_path':v[1]} for k,v in items.items()},'chapter_map':{'XI':['NOV_A1','NOV_HE3_CASE','NOV_HE3_VERIFY','NOV_FREE','NOV_COV','NOV_CONSTRUCTOR','NOV_BRIDGE','NOV_COMMON_RECEIVER','NOV_JOINT','NOV_RELAX','NOV_LI6_CASE','NOV_LI6_CHANNEL','NOV_LI6_TRANSFER','NOV_LI6_SYMMETRY'],'XII':['NOV_RECEIVING','NOV_ARRIVAL','NOV_CONTROL','NOV_LOADING'],'XVI':['NOV_RESPONSE','NOV_ACTION','NOV_CONSTRUCTOR'],'Appendix A':['NOV_BATTERY','NOV_LOADING','NOV_THERMAL'],'Appendix B':['NOV_HE3_VERIFY','NOV_FREE','NOV_COV','NOV_LI6_CASE','NOV_RECEIVING']}},indent=2)+'\n')
print('Copied',len(manifest),'selected evidence files;',sum(x['bytes'] for x in manifest),'bytes.')
