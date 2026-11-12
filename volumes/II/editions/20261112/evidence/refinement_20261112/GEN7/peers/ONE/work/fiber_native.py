from pathlib import Path
import json,hashlib
from fractions import Fraction as F
P=Path.cwd();base=json.loads((P/'tasks/ONE7_ROBUSTNESS.job.json').read_text());steps=[]
def word(k,ops,pg,out,n):
 z=json.loads(json.dumps(base['steps'][0]));z['id']=k;z['purpose']='Bloch one-hop support/sector arithmetic for the analytical lattice localization theorem; not a finite substitute for the full Fock proof.';z['payload']['name']='ONE7_'+k;z['payload']['context']['basis']=list(range(n));z['payload']['data']={'operators':ops,'program':pg,'output':out};steps.append(z)
A=[['0']*7 for _ in range(7)]
for j in range(7):
 if j<6:A[j+1][j]=str(6-j)
 if j>0:A[j-1][j]=str(j)
e0=[['1' if i==0 else '0'] for i in range(7)];e6=[['1' if i==6 else '0' for i in range(7)]]
pg=[{'name':'a2','op':'multiply','inputs':['A','A']},{'name':'a3','op':'multiply','inputs':['a2','A']},{'name':'b','op':'multiply','inputs':['a3','e0']},{'name':'out','op':'multiply','inputs':['e6','b']}]
word('translation_three_hop_zero',{'A':A,'e0':e0,'e6':e6},pg,'out',1)
pg=[{'name':'a2','op':'multiply','inputs':['A','A']},{'name':'a3','op':'multiply','inputs':['a2','A']},{'name':'a6','op':'multiply','inputs':['a3','a3']},{'name':'b','op':'multiply','inputs':['a6','e0']},{'name':'out','op':'multiply','inputs':['e6','b']}]
word('translation_six_hop_reachable',{'A':A,'e0':e0,'e6':e6},pg,'out',1)
boundsfile=Path('/home/lilhelper/SAM_Research_Overflow/Courtroom_II/campaigns/volii_review_followups_20261111/03_car_fock_loading/RESULTS/LEAD_PUBLIC_REPLAY/LI6/BOUNDS.json');d=json.loads(boundsfile.read_text());gains=list(map(F,d['benchmark']['sector_gains']));vs=list(map(F,d['sector_potentials']));L=F(-728,3);D=F(9009,250)
upp=[D-35*v-g for v,g in zip(vs,gains)];proper=[L-u for u in upp];band=F(9,125);gap=1-band
word('sector_band_constants',{'L':[[str(L)]],'U':[[str(u) for u in upp]],'ones':[['1','1','1']]},[{'name':'lo','op':'multiply','inputs':['L','ones']},{'name':'out','op':'subtract','inputs':['lo','U']}],'out',1)
word('boson_gap_minus_bandwidth',{'A':[['1']],'B':[[str(band)]]},[{'name':'out','op':'subtract','inputs':['A','B']}],'out',1)
key='ONE7_FIBER_KINEMATICS';j={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'Anchor Bloch trial support, strict42/33 sector margins,321 countercontrol and optical-boson bandwidth arithmetic for the new explicit localization argument.','source_binding':base['source_binding'],'law_namespace':'SAM_land','precision_bits':256,'sources':[{'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [P/'PRECOMMIT.md',boundsfile,Path(__file__).resolve()]],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}};p=P/'tasks'/f'{key}.job.json';p.write_text(json.dumps(j,separators=(',',':'))+'\n');(P/'tasks'/f'{key}.json').write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':j['objective'],'job_path':str(p)},indent=2)+'\n');(P/'results/FIBER.json').write_text(json.dumps({'sector_upper':list(map(str,upp)),'proper_margins':list(map(str,proper)),'proper_margin_decimal':list(map(float,proper)),'bandwidth':str(band),'gap':str(gap)},indent=2)+'\n');print('sector margins',list(map(float,proper)),'gap',gap)
