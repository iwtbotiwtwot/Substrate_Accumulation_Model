from pathlib import Path
import json,hashlib,sys
from fractions import Fraction as F
sys.set_int_max_str_digits(0);R=Path.cwd();a=json.loads((R/'evidence/native_audit.json').read_text());p=R/'REPORT.md';s=p.read_text();s=s.replace('changes the original quadratic contraction by an interval contained in[0.7319,0.7326].','changes the original quadratic contraction by the native rational interval[402384528779/549755813888,402726553379/549755813888], contained in[0.7319,0.7326].')
s=s.replace('produces strictly positive full7-minus6 gain; native solve residuals remain exactly zero.', 'produces full7-minus6 gain in[561461163/10^20,561461164/10^20], strictly positive; native solve residuals remain exactly zero.')
marker='Native final receipt tally/readback is appended below as the window proceeds.'
s=s.replace(marker,'Final readback:16 completed submissions,493 mathematical nodes in those completed submissions, three properly declared failing controls, one failed wrapper, and three unadmitted caller-contract corrections. The two failed mathematical-check programs additionally retain six completed arithmetic-prefix outputs (one star word, five core-control products); they are not counted as completed programs. No MISSING_RECEIPT, in-flight or uncollected admission remains. All54 core matrices,162 receivers and37 exact linked equalities were read and checked; all610 bound source-hash occurrences still match. Arithmetic and receipt counts describe custody, not an external-verification level.')
s+='\n\n| Native key | Final status | Receipt SHA256 |\n|---|---|---|\n'
for r in a['tasks']:s+=f"| {r['key']} | {r['status']} | `{r['receipt_sha256']}` |\n"
root=Path('/home/lilhelper/SAM_Research_Overflow/ironclad-235-source-clock-20261105T181633Z/runs/duck/gen7_20261112T043202Z/workers/G6_03/tasks')
for key,name in [('THREE_CONTROL_STAR_V3','000_false_uniformity.output.json'),('THREE_CORE_CONTROL_V3','004_defect.output.json')]:
 q=root/key/'gen6'/name;s+=f"\nRetained completed control-prefix output `{key}/{name}` SHA256 `{hashlib.sha256(q.read_bytes()).hexdigest()}`.\n"
s+=f"\nFull readback/audit SHA256 `{hashlib.sha256((R/'evidence/native_audit.json').read_bytes()).hexdigest()}`; linked containment/positivity audit SHA256 `{hashlib.sha256((R/'evidence/linked_point_audit.json').read_bytes()).hexdigest()}`. THREE_CONTROL_STAR is a wrapper failure, not a successful hypothesis control. STAR_V2, CORE_CONTROL and CORE_CONTROL_V2 are unadmitted and have no mathematical receipts; their rejection reasons and corrected successors are recorded above. No research submission will be made in the final180seconds.\n"
p.write_text(s);print('report bytes',len(s.encode()),'words',len(s.split()))
