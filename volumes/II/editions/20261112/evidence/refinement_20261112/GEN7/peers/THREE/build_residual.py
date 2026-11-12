from pathlib import Path
import json,gzip,hashlib
from interval_tools import *
ROOT=Path.cwd();OUT=ROOT/'evidence';PROJECT=Path('/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4');EDGE=PROJECT/'spin_source_moments_gcp1_20261017/cloud_runs/spin-source-moments-20261017-054112/extracted/results/science/profiles';SOURCES={}
def read(p):
    p=Path(p);b=p.read_bytes();SOURCES[str(p)]={'path':str(p),'sha256':hashlib.sha256(b).hexdigest()};return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def output(p):return read(p)['output']
def one(ident):
    fam=ident.split('_')[0];edge=output(EDGE/ident/(ident+'_INTEGRAL.json.gz'));res=output(EDGE/ident/(ident+'_RESULT.json.gz'));old=output(PROJECT/'spin_difference_fifth1/native1'/fam/(ident+'_RESULT.json.gz'));up=output(PROJECT/'spin_upper_source1_20261014'/('pilot3' if fam=='V000' else 'native1')/fam/(ident+'_RESULT.json.gz'));original=read(PROJECT/'spin_conditional_variance1/sources/original'/(ident+'.json.gz'))['job']
    G=arr(old['G5']);D=arr(old['D5']);G4=[r[:4] for r in G[:4]];D4=[r[:4] for r in D[:4]];W=arr(old['projected_matrices']['W']);lam=W[0][1]/W[0][0]
    pd=[aa(v) for v in up['coefficient_pd']];qd=[aa(v) for v in up['coefficient_qd']];pe=[aa(v) for v in up['coefficient_pe']];qe=[aa(v) for v in up['coefficient_qe']]
    c=[r[0] for r in solve(G,[[r[4]] for r in D])];port=solve(arr(old['projected_matrices']['V']),arr(old['projected_matrices']['Ds']))
    bc=[[arb(1),arb(0),-port[0][0],-port[0][1],qd[0]],[arb(0),arb(1),-port[1][0],-port[1][1],qd[1]],[arb(0),arb(0),arb(1),arb(0),-pd[0]],[arb(0),arb(0),arb(0),arb(1),-pd[1]],[arb(0),arb(0),arb(0),arb(0),arb(1)],[arb(0)]*5,[arb(0)]*5]
    ck=[arb(0),arb(0),qd[0],qd[1],-pd[0],-pd[1],arb(1)];vr=[ck[i]-dot(bc[i],c) for i in range(7)]
    ve=[qe[0]-lam*qd[0],qe[1]-lam*qd[1],-pe[0]+lam*pd[0],-pe[1]+lam*pd[1],-lam,arb(1),arb(0)];V=tr([ve,vr]);E=[[aa(v) for v in r] for r in edge['core_edge_Gram']];M=mm(mm(tr(V),E),V)
    # Reconstruct full couplings from their original action identities, not the old residual-output cache.
    H4=solve(G4,D4);k=[r[4] for r in D];J11=aa(old['J']);J21=aa(up['J21']);F11=aa(up['F11']);t=mm(tr(H4),[[x] for x in k[:4]]);t[2][0]+=J11;t[3][0]+=J21
    h=[t[i][0]-dot(D[i],c) for i in range(4)]+[F11-dot(D[4],c)];be=F11-dot(k,c);dW=W[1][1]-W[0][1]**2/W[0][0];cross=J21-lam*J11;B=[[dW,cross],[cross,be]];H=tr([[arb(0),arb(0),arb(0),dW,cross],h])
    N=int(old['N_exact']);beta=aa(original['beta']);a=beta/N;E0=a/(arb.pi()/4)**2;pay=up['payments'];de=(sup(aa(pay['B_h_e']))+sup(lam)*sup(aa(pay['B_h_d'])))**2+(2*sup(beta)*(12+4*sup(lam)))**2*E0;dr=aa(res['scalar_certificate']['delta_pi_squared']);ds=[upper(de),upper(dr)];amps=[2,2,4,12,160,480,6400];R=[dot([sup(x) for x in v],[arb(n) for n in amps]) for v in [ve,vr]]
    center=[[mid(M[i][j]) for j in range(2)] for i in range(2)];center[0][1]=center[1][0]=(center[0][1]+center[1][0])/2;radii=[sum((sup(M[i][j]-center[i][j]) for j in range(2)),arb(0)) for i in range(2)];Mbar=[[center[i][j]+(radii[i]+80*R[i]**2*E0 if i==j else 0) for j in range(2)] for i in range(2)]
    Le=960+320*sup(lam)+4*sup(pe[0]-lam*pd[0])+12*sup(pe[1]-lam*pd[1])+(5*sup(beta)+4)*(12+4*sup(lam));bge=upper(2*(N-20)*a*a*Le*Le);bgr=upper(aa(res['scalar_certificate']['complete_background']));bg=[bge,bgr];eta=upper((40*sum(ds)/sum(Mbar[i][i] for i in range(2))).sqrt());Jbar=[[(1+eta)*Mbar[i][j]+(40*(1+1/eta)*ds[i]+2*bg[i] if i==j else 0) for j in range(2)] for i in range(2)]
    histories=[];g=[G[i][0] for i in range(5)]+[arb(0),arb(0)]
    for ix in [0,18,36]:
        xi=aa(old['rows'][ix]['xi_exact']);K=[[xi*G[i][j]+D[i][j] if i<5 and j<5 else H[i][j-5] if i<5 else H[j][i-5] if j<5 else xi*B[i-5][j-5]+Jbar[i-5][j-5] for j in range(7)] for i in range(7)];x=[r[0] for r in solve(K,[[x] for x in g])];val=dot(g,x)*xi/G[0][0];oldval=aa(res['rows'][ix]['normalized_lower']);histories.append({'index':ix,'xi':old['rows'][ix]['xi_exact'],'matrix':wm(K),'rhs':wm([[x] for x in g]),'value':wi(val),'old':wi(oldval),'resolved_separation':bool(val.lower()>oldval.upper()),'midpoint_gain':fl(val-oldval),'normalization':wi(xi/G[0][0])})
    oldvr=[aa(r[0]) for r in res['source_residual_coefficients']['entries']];assert all(x.overlaps(y) for x,y in zip(oldvr,vr))
    return {'id':ident,'N':str(N),'beta':wi(beta),'lambda':wi(lam),'coefficients':wm(V),'edge':wm(E),'core':wm(M),'G5':wm(G),'D5':wm(D),'c':wm([[x] for x in c]),'B':wm(B),'H':wm(H),'Mbar':wm(Mbar),'delta':list(map(wi,ds)),'background':list(map(wi,bg)),'eta':wi(eta),'Jbar':wm(Jbar),'original_scalar_cap':res['scalar_certificate']['receiving_exact_upper'],'histories':histories}
rows=[]
for p in sorted(EDGE.iterdir()):
 if p.is_dir():
    rows.append(one(p.name));print(p.name,[[round(fl(x),10) for x in r] for r in arr(rows[-1]['core'])],flush=True)
assert len(rows)==54
out={'classification':'HOST_DIRECTED_ARB','profiles':rows,'sources':list(SOURCES.values()),'comparisons':162,'resolved_separations':sum(h['resolved_separation'] for r in rows for h in r['histories'])};(OUT/'residual_host.json').write_text(json.dumps(out,indent=2)+'\n')
print('profiles',len(rows),'separations',out['resolved_separations'])
for group in range(2):
    steps=[]
    for r in rows[group*27:(group+1)*27]:
        name=r['id'];V=arr(r['coefficients']);E=r['edge'];rb=E['row_basis'];cb=['r_e','r'];vv=wm(V,rb,cb);vt=wm(tr(V),cb,rb)
        for idx,data in [('left',{'matrix':vt,'right':E}),('core',{'matrix':{'$step':name+'_left','path':['result','output','matrix']},'right':vv})]:steps.append({'id':name+'_'+idx,'operation':'GEN3_COMPLEX_PRODUCT','purpose':'Independent retained seven-feature signed residual contraction','payload':{'source_binding':{'$source':True},'precision_bits':384,'data':data},'checks':[{'predicate':'native_contract'}]})
    key='THREE_RESIDUAL_CORE_'+str(group);job={'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':'54 original signed2x2 core residual blocks; half batch'+str(group),'precision_bits':384,'sources':list(SOURCES.values())+[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [ROOT/'PREDICTIONS.md',ROOT/'build_residual.py',ROOT/'interval_tools.py',OUT/'residual_host.json']],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps if s['id'].endswith('_core')}};(ROOT/(key+'.job.json')).write_text(json.dumps(job,indent=2)+'\n');(ROOT/(key+'.task.json')).write_text(json.dumps({'kind':'gen6_job','key':key,'purpose':'Reconstruct all54 native core blocks from original integrated edges and fresh coefficient solves','job_path':str(ROOT/(key+'.job.json'))},indent=2)+'\n')
