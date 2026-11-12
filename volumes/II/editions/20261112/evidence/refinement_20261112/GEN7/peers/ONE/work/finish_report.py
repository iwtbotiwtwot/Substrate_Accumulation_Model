import json,hashlib,pathlib
p=pathlib.Path('REPORT.md'); report=p.read_text(); t=json.load(open('results/TOMOGRAPHY.json')); audit=json.load(open('results/NATIVE_AUDIT.json'));d=json.load(open('results/DRESSED_DENSITY.json'))
s='\n## Exact design transformations and source custody\n\nThe following rows give the fixed transforms in the18-column order specified above; each row is one raw-source coefficient row. Entries containing i are Gaussian integers, with i²=−1. Thus X8=Xraw T8 and X6=Xraw T6 are specified exactly.\n'
for label in ['real8','complex6']:
 s+='\n'+label+':\n\n```text\n'+'\n'.join(' '.join((str(z['re'])+'+('+str(z['im'])+')i') if isinstance(z,dict) else str(z) for z in row) for row in t['designs'][label]['source_transform'])+'\n```\n'
s+='\nThe raw exterior coefficient operand is authoritative for signs and source ordering. Independent reconstruction acts in ascending Fourier-mode order within each of the four flavor masks, with flavor order proton-up,proton-down,neutron-up,neutron-down. This convention fixes every annihilation/creation sign. The complete inverse specification is the cofactor expression above with these transforms and this operand; saved inverse arrays were also checked entry by entry.\n\nSource SHA256 custody (paths shortened only by the declared roots):\n\n| Source | SHA256 |\n|---|---|\n'
h=json.load(open('results/SOURCE_CUSTODY.json'));h.update(d['source_hashes']);root='/home/lilhelper/SAM_Research_Overflow/ironclad/campaigns/volii_improvement_review_20261111/sources/receiving_action/peers/ONE/gen/SPATIAL_FLAVOR_DISCOVERY.json';h[root]=hashlib.sha256(pathlib.Path(root).read_bytes()).hexdigest();h[str(pathlib.Path('PRECOMMIT_PAIR.md').resolve())]=hashlib.sha256(pathlib.Path('PRECOMMIT_PAIR.md').read_bytes()).hexdigest()
for f,v in h.items():s+='| '+f+' | `'+v+'` |\n'
s+='''
# 3. Controls, Obstructions & Superseded Attempts

Predictions and failing-control expectations were committed before execution in the SHA-bound PRECOMMIT.md; the independent central-projector control was additionally committed in PRECOMMIT_PAIR.md. These are testable changes to the hypotheses, rather than relabellings of a null symmetry.

| Control or obstruction | Exact witness / expected result | Completed native readback and disposition |
|---|---|---|
| Invisible source11 kernel, then reachable repair | 6(B15=1,B04=−1/6) gives zero on all old columns, but new physical source-pair response144 | ONE7_RANK_CONTROLS plus ONE7_EXACT_NULLS; old invisibility and new nonzero both observed |
| Prematurely compressing density | Full ρ4² minus compressed square has raw source diagonal90; source norm15 gives normalized error6. Edge7 gives128/16=8 | ONE7_RANK_CONTROLS; rejected shortcut, positive omitted-image contribution |
| Too few independent real directions | Duplicating one real8 source direction makes the36-entry design singular | ONE7_SINGULAR_CONTROL_V3 overall COMPLETED; inner INVERTIBILITY_UNRESOLVED, as required by engine contract |
| Treating 5+1 as sole branch beyond its crossing | δ=10/3+1/100 makes the competing4+2 envelope lower by1/50 | ONE7_ROBUSTNESS; δ≤10/3 is retained |
| Uniform shift cancels between target and breakup | Sum of cell particle squares is36 for target,26 for5+1, giving nonzero margin shift5Δ/4 | ONE7_ROBUSTNESS and ONE7_DRESSED_DENSITY; cancellation rejected |
| Deleting C3 in the pair central polynomial | A full-parent basis direction has P411 diagonal1/6; the selected pair source has P411=0 and would be an unreachable control | ONE7_PAIR_SECTORS; full-parent witness used, selected pair null explicitly avoided |
| Conflating common-map error and known-input optimum | Squared-distance difference0.0000289339914409698435484…>0 | ONE7_ARRIVAL; optimization domains kept explicit |
| Assuming no intercell translate is reachable at any order | Three-hop endpoint vanishes, six-hop endpoint720 | ONE7_FIBER_KINEMATICS; finite order used, no all-orders claim |
| Promoting all flavor sectors from a weighted margin | The sufficient321 upper is20.8492111445889… above common breakup lower | ONE7_FIBER_KINEMATICS; only42 and33 receive the displayed isolated-band conclusion |

The initial rank task's rational null products returned enclosing intervals at zero. This establishes containment, not an exact-zero certificate by itself; ONE7_EXACT_NULLS supersedes that part with exact source-word integer products. Native rank and inverse calculations stayed at36×36 or below. Full density contractions used1795 physical rows but at most8 source columns; no large dense parent solve or rank was submitted.

Admission corrections: ONE7_SINGULAR_CONTROL was rejected before admission because expected_reason was supplied with expected_status=COMPLETED. ONE7_SINGULAR_CONTROL_V2 was rejected because supersedes named an unreturned admission rejection. V3 removed those invalid metadata fields, completed, and gave the intended inner singularity status. There was no admitted failed scientific task. A missing numpy import stopped a host successor generator before its final null-task file was written; the dedicated additional_native.py generated that file and it subsequently completed. The audit helper initially assumed status CERTIFIED instead of CERTIFIED_SOLVE and a mapping instead of a row-list solution; its corrected version checked all entries. A diagnostic read of a None-valued unused sector matrix and a plain python executable lookup also failed before producing scientific output; python3/the pinned .venv executable and explicit sector filtering resolved them. None changes a source hash or an already sealed input.

Calibration scope is substantive. The error bound for reconstructed B assumes known source Grams, common energy zero and the subtracted kinetic term; the complex scheme also assumes controlled relative phases. Source11 still has15 invisible directions. The one-hop continuation treats a common bounded instantaneous density perturbation of the full law. Altering receiver frequencies, vertices or hopping while only matching completed static B requires the explicit extra form-error allowance η derived above. The reported static tomography alone cannot set η=0. The arrival attainment assumes access to the stated full-flavor orbital alignment; central Gram information certifies its obstruction but does not construct a physical control apparatus. Fiber eigenvalues prove spectral existence in the declared lattice law; preparation, release and capture remain separate physical questions.

# 4. Exceptions-Only Custody Diff

There are11 completed native submissions containing127 completed native operations, with13713 exact rational/interval-entry readback checks in the local custody audit. Every key below has an on-disk completed receipt and every recorded program trace was read. The compact receipt SHA256 is printed; for spilled results this is the full RESULT.json hash, while results/NATIVE_AUDIT.json separately records both the compact receipt and full-return hashes. The analytical localization proof is labelled ANALYTICAL_PROOF: its infinite-dimensional assertion is not relabelled as a native finite-matrix certificate.

| Native key | Status | Operations | Receipt SHA256 |
|---|---|---:|---|
'''
for r in audit['receipts']:s+='| '+r['key']+' | '+r['status']+' | '+str(r['native_calls'])+' | `'+r['receipt_sha256']+'` |\n'
s+='\nMISSING_RECEIPT:0. Unadmitted schema corrections:2 (the singular-control attempts described above); neither is counted among the11. Superseded mathematical evidence: interval-only zero checks in ONE7_RANK_CONTROLS are replaced by ONE7_EXACT_NULLS. No baseline replay, external joint archive, N=5000 contraction, GEN2_HD_PRIMITIVES standalone call, or dense rational solve above64×64 was run. Scientific host commands were pinned and single-threaded. All tasks were admitted before the final180-second readback/assembly reserve. The written report carries every asserted result and qualification; ancillary work files are supporting custody, not additional delivered conclusions.\n'
p.write_text(report+s)
print('report bytes',p.stat().st_size,'lines',len(p.read_text().splitlines()))
