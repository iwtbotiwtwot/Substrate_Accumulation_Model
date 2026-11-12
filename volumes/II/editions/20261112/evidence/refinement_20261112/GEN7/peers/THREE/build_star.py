from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib,datetime
ROOT=Path.cwd(); OUT=ROOT/'evidence';OUT.mkdir(exist_ok=True)
def dump(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def st(x):return str(x)
def hashp(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pow2(n):return F(2)**n
signs=list(product((-1,1),repeat=4));rays=[(1,)+p for p in product((-1,1),repeat=3)];hidden=list(product((-1,1),repeat=8))
Z=[];eng=F(0);total=F(0);m1=F(0);m2=F(0);mineng=100;deg=0;rows=[]
for s in signs:
    z=F(0);e=F(0);a1=F(0);a2=F(0)
    for hs in hidden:
        score=sum(h*sum(pj*sj for pj,sj in zip(p,s)) for h,p in zip(hs,rays))
        wt=pow2(score//2);z+=wt;e-=wt*score
        portfield=sum(h*p[0] for h,p in zip(hs,rays));rate=1/(1+pow2(s[0]*portfield));a1+=2*wt*rate;a2+=4*wt*rate**2
        if -score<mineng:mineng=-score;deg=1
        elif -score==mineng:deg+=1
    Z.append(z);total+=z;eng+=e;m1+=a1;m2+=a2;rows.append({'s':s,'Z':st(z),'E_num':st(e),'mu1':st(a1/z),'mu2':st(a2/z)})
assert len(set(Z))==1 and Z[0]==F(10625,8) and eng/total==F(-708,85) and m1==m2
pp=[1/(1+pow2(-sum(p))) for p in rays]
def conv(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
layer=[F(1)]
for p in pp:layer=conv(layer,[1-p,p])
ks=[];pk=[F(1)];h=F(59049,85000)
for k in range(1,6):
    pk=conv(pk,layer);rate=[1/(1+pow2(-8*k+2*j)) for j in range(8*k+1)]
    omega=2*sum(p*r for p,r in zip(pk,rate));second=4*sum(p*r*r for p,r in zip(pk,rate))
    assert omega==second and h**(2*k)<=omega<=h**k
    ks.append({'k':k,'Omega':st(omega),'variance':st(omega*(1-omega)),'Omega_float':float(omega),'field_probabilities':list(map(st,pk))})
assert ks[0]['Omega']==st(m1/total)
broken=[Z[i]/(pow2(sum(signs[i])//2)+pow2(-sum(signs[i])//2)) for i in range(16)]
assert broken[0]!=broken[1]
res={'classification':'HOST_EXACT_RAT','definition':'E=-J sum_p h_p p.s, p=(1,p2,p3,p4), x=log2/2','rows':rows,'total_partition':st(total),'energy_over_J':st(eng/total),'ground_energy_over_J':mineng,'ground_degeneracy':deg,'mu1':st(m1/total),'mu2':st(m2/total),'layers':ks,'single_layer_port_field_probabilities':list(map(st,layer)),'broken_missing_++++':list(map(st,broken)),'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'star_host.json',res)
BIND={'$source':True}
def word(name,ops,prog,out,basis):return {'name':name,'source_binding':BIND,'context':{'basis':basis,'field':{'radicand':0},'units':{'energy':'J','time':'one attempt per physical boundary spin'},'history':{'source':'VolumeII VII.2 eight sign rays','preparation':'complete Gibbs x=log2/2'},'spectral_coordinate':'lambda(-L)'},'data':{'operators':ops,'program':prog,'output':out}}
def source(p):return {'path':str(p),'sha256':hashp(p)}
def job(key,steps):
    p=ROOT/(key+'.job.json');dump(p,{'schema':'SAM_ONE_PRINCIPLE_NATIVE_JOB_V1','objective':key,'precision_bits':384,'sources':[source(ROOT/'PREDICTIONS.md'),source(ROOT/'build_star.py'),source(OUT/'star_host.json')],'steps':steps,'readouts':{s['id']:{'status':'DERIVED_NATIVE','value':{'$step':s['id'],'path':[]}} for s in steps}});dump(ROOT/(key+'.task.json'),{'kind':'gen6_job','key':key,'purpose':'Independent lane THREE exact source verification; see sealed predictions','job_path':str(p)})
for k in range(1,5):
    n=8*k+1;ops={'seed':[[1]]+[[0] for _ in range(n-1)]};prog=[];last='seed'
    for t in range(8*k):
        p=pp[t%8];T=[[st((1-p) if i==j else p if i==j+1 else 0) for j in range(n)] for i in range(n)]
        # Keep every spin factor separately; multiplication acts on the previous probability polynomial.
        ops['T'+str(t)]=T;prog.append({'name':'p'+str(t),'op':'multiply','inputs':['T'+str(t),last]});last='p'+str(t)
    rr=[1/(1+pow2(-8*k+2*j)) for j in range(n)]
    ops['moment_rows']=[[st(2*r) for r in rr],[st(4*r*r) for r in rr]];prog.append({'name':'moments','op':'multiply','inputs':['moment_rows',last]})
    job('THREE_STAR_K'+str(k),[{'id':'moments','operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Exact Bernoulli factor contraction for mu1 and mu2','payload':word('THREE_STAR_K'+str(k),ops,prog,'moments',['mu1','mu2']),'checks':[{'predicate':'native_contract'}]}])
# Independent column multiplication for all16 conditional rows.
ops={'seed':[[1] for _ in range(16)]};prog=[];last='seed'
for j,p in enumerate(rays):
    vals=[pow2(sum(a*b for a,b in zip(p,s))//2)+pow2(-sum(a*b for a,b in zip(p,s))//2) for s in signs]
    ops['Z'+str(j)]=[[st(vals[i] if i==q else 0) for q in range(16)] for i in range(16)]
    prog.append({'name':'z'+str(j),'op':'multiply','inputs':['Z'+str(j),last]});last='z'+str(j)
part=word('THREE_ALL16_PARTITIONS',ops,prog,last,[str(s) for s in signs])
# Native exact control certifies lost uniformity at two actual boundary rows.
control=word('THREE_MISSING_RAY_CONTROL',{'rows':[[st(broken[0])],[st(broken[1])]],'difference':[[1,-1]]},[{'name':'defect','op':'multiply','inputs':['difference','rows']}],'defect',['lost_uniformity'])
energy=word('THREE_CALORIMETRY',{'weighted_energy':[[st(eng)]],'inverse_Z':[[st(1/total)]]},[{'name':'E','op':'multiply','inputs':['weighted_energy','inverse_Z']}],'E',['energy_over_J'])
job('THREE_STAR_LEDGER',[{'id':'partition','operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'All16 full conditional partitions from8 factors','payload':part,'checks':[{'predicate':'native_contract'}]},{'id':'control','operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Reachable missing-ray failure of uniformity; expected nonzero defect','payload':control,'checks':[{'predicate':'native_contract'}]},{'id':'energy','operation':'GEN3_SOURCE_OPERATOR_WORD','purpose':'Complete Gibbs energy/J from4096-state weighted numerator','payload':energy,'checks':[{'predicate':'native_contract'}]}])
print('states',len(signs)*len(hidden),'Z',total,'E/J',eng/total,'ground',mineng,deg)
for x in ks:print(x['k'],x['Omega_float'])
print('missing-ray difference',broken[0]-broken[1])
