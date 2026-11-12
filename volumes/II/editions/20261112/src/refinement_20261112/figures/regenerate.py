from pathlib import Path
from fractions import Fraction
import json
import hashlib
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ED=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
QA=ED/'qa/figure_previews'
QA.mkdir(parents=True,exist_ok=True)
G=ED/'evidence/refinement_20261112/GEN7/peers'
plt.rcParams.update({'font.family':'serif','font.serif':['DejaVu Serif'],
 'font.size':8.2,'axes.titlesize':9.0,'axes.labelsize':8.3,
 'xtick.labelsize':7.3,'ytick.labelsize':7.6,'legend.fontsize':7.0,
 'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.6,
 'lines.linewidth':1.5,'pdf.fonttype':42,'savefig.facecolor':'white'})
NAVY='#1b3f5b';TEAL='#16807b';RUST='#b95531';GRAY='#8b9296'
manifest=[]
def save(fig,name,data,source):
    fig.tight_layout(pad=.65)
    fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight',pad_inches=.035,metadata={'Author':'Sean Brady','Title':name.replace('_',' ')})
    fig.savefig(QA/(name+'.png'),bbox_inches='tight',pad_inches=.035,dpi=170)
    plt.close(fig)
    (OUT/(name+'.json')).write_text(json.dumps({'source':source,'display_data':data,'scope':'Typesetting plot of retained operands/formulas; no new scientific execution.'},indent=2)+'\n')
    manifest.append({'figure':name,'source':source,'pdf_sha256':hashlib.sha256((OUT/(name+'.pdf')).read_bytes()).hexdigest()})

# H003004: certified complete finite-core endpoints.
old=[32.67,34.68,38.88];new=[30.9533766184074,32.3311688245431,35.1767532368147]
fig,ax=plt.subplots(figsize=(3.35,2.55));y=np.arange(3)
ax.barh(y+.17,old,.3,color=GRAY,label='Earlier upper')
ax.barh(y-.17,new,.3,color=TEAL,label='Complete new upper')
for yy,v in zip(y-.17,new):ax.text(v+.25,yy,f'{v:.3f}',va='center',fontsize=7.2)
ax.set(yticks=y,yticklabels=['C333','C343','C444'],xlabel='Binding upper (source units)',xlim=(0,43))
ax.legend(loc='lower left',bbox_to_anchor=(0,1.005),ncol=2,frameon=False);ax.invert_yaxis();ax.grid(axis='x',alpha=.15)
save(fig,'atomic_bounds',{'earlier':old,'new':new},'H003004 / NUMERICAL_DISPLAY_RECEIPT.json')

fig,ax=plt.subplots(figsize=(3.35,2.35));v=[11191/20250,1.3129421370,1.6027627093]
ax.barh(np.arange(3),v,color=[GRAY,NAVY,TEAL],height=.52)
ax.set(yticks=range(3),yticklabels=['Original target','Harmonic-family floor','Benchmark one-hop'],xlabel='Sufficient all-proper margin',xlim=(0,1.86))
for y,x in enumerate(v):ax.text(x+.025,y,f'{x:.4f}',va='center',fontsize=7.3)
ax.grid(axis='x',alpha=.15)
save(fig,'li6_margins',{'margins':v},'H003006/H003008 / Li6 complete margin')

x=np.linspace(0,8,801);n=np.floor(x);r=x-n
q=(1-r)/(n+1)+r/(n+2)
ql=np.where(x<=1,1-x/3,1/np.maximum(x,1e-10)-1/(3*np.maximum(x,1e-10)**2))
fig,ax=plt.subplots(figsize=(3.35,2.65));ax.plot(x,ql,color=GRAY,label='Linear ramp')
ax.plot(x,q,color=TEAL,label='Sharp signed-ramp floor');ax.scatter(range(9),1/(np.arange(9)+1),s=13,color=TEAL,zorder=3)
ax.set(xlabel=r'Duration $T/(2\tau)$',ylabel=r'Residual fraction $E_{res}/D_{jump}$',ylim=(0,1.04),xlim=(0,8))
ax.legend(frameon=False);ax.grid(alpha=.15)
save(fig,'loading_floor',{'T_over_2tau':x.tolist(),'sharp':q.tolist(),'linear':ql.tolist()},'H003006/H003008 / continuum box-autocorrelation theorem')

dp=json.loads((G/'FOUR/results/C12_DP.json').read_text());paths=dp['paths']
num=lambda v:float(Fraction(v))
a=np.array([num(p['variation']) for p in paths]);b=np.array([num(p['storage']) for p in paths]);c=np.array([num(p['gross']) for p in paths])
fig,ax=plt.subplots(figsize=(3.35,2.95));sc=ax.scatter(a,b,c=c,cmap='viridis',s=27,alpha=.85)
ix=dp['pareto_indices'];ax.scatter(a[ix],b[ix],s=63,facecolors='none',edgecolors=RUST,linewidths=.8)
for word,offset in [('AABCBC',(3,-16)),('CCABAB',(-52,11)),('AABBCC',(8,-12))]:
 i=next(i for i,p in enumerate(paths) if p['word']==word)
 ax.annotate(word,(a[i],b[i]),xytext=offset,textcoords='offset points',fontsize=6.8)
ax.set(xlabel='Full quadratic variation',ylabel='Required storage (zero initial capital)');ax.grid(alpha=.15)
cb=fig.colorbar(sc,ax=ax,pad=.03,shrink=.86);cb.set_label('Gross positive work',fontsize=7.3)
save(fig,'c12_paths',paths,'GEN7 FOUR / C12_DP.json, all 30 exact paths')

star=json.loads((G/'THREE/evidence/star_host.json').read_text());om=[num(v['Omega']) for v in star['layers'] if v['k']<=4]
x=np.linspace(.0001,1,1000);C=lambda a:.25*a*(-np.log(a)-1+a)
fig,ax=plt.subplots(figsize=(3.35,2.65));ax.plot(x,C(x),color=NAVY)
ax.axvline(.20318786997998,color=GRAY,ls=':',lw=.8)
for k,a in enumerate(om,1):
 ax.scatter(a,C(a),color=TEAL,s=24,zorder=3);ax.annotate(f'k={k}',(a,C(a)),xytext={1:(4,5),2:(6,-13),3:(5,6),4:(-20,-13)}[k],textcoords='offset points',fontsize=7)
ax.set(xlabel=r'Observed rate moment $a=\Omega_k$',ylabel=r'Short-wait coefficient $C(a)$',xlim=(0,1),ylim=(0,.046));ax.grid(alpha=.15)
save(fig,'star_memory',{'Omega':om,'C':[float(C(a)) for a in om]},'GEN7 THREE / star_host.json and exact C(a)')

fig,ax=plt.subplots(figsize=(3.35,2.7));bands=[(3.4208196027e-6,3.4208514025e-6),(3.41219962633e-6,3.41223131098e-6),(9.70571116858e-5,2.503534522325e-4)]
for y,(lo,hi) in zip([3,2,1],bands):
 ax.plot([lo,hi],[y,y],color=TEAL,lw=4,solid_capstyle='butt');ax.scatter([math.sqrt(lo*hi)],[y],s=19,color=NAVY,zorder=3)
ax.scatter([7.678577136e-9],[0],marker='<',s=40,color=RUST)
ax.set_xscale('log');ax.set(xlim=(3e-9,6e-4),ylim=(-.6,3.6),yticks=[0,1,2,3],yticklabels=['Fitted clock cap','Uniform, wait 4','Signed chain, 1/3','Signed pairs, 1/3'],xlabel='Three-time conditional information (nats)')
ax.grid(axis='x',which='major',alpha=.17)
save(fig,'memory_certificates',{'bands':bands,'signed_fitted_clock_upper':7.678577136e-9},'H003005; H003007/TWO-F03 completed chain; models and waits kept separate')

x=np.linspace(.1,3.0,600)
fig,ax=plt.subplots(figsize=(3.35,2.65));ax.plot(x,17/15-27/(25*x),color=TEAL,label='Carbon444 upper envelope')
ax.plot(x,23/15-256/(75*x),color=NAVY,label='Oxygen upper envelope')
ax.axhline(0,color=GRAY,lw=.7);ax.axvline(81/85,color=TEAL,lw=.7,ls=':');ax.axvline(256/115,color=NAVY,lw=.7,ls=':')
ax.set(xlabel=r'Rotor constant times radial sum $BR$',ylabel=r'Upper envelope for $(K_2-S_2)/R$',xlim=(.1,3),ylim=(-4,1.3));ax.legend(frameon=False,loc='lower right');ax.grid(alpha=.15)
save(fig,'rotor_tail',{'carbon_zero':81/85,'oxygen_zero':256/115,'carbon_upper':'17/15 - 27/(25 BR)','oxygen_upper':'23/15 - 256/(75 BR)'},'GEN7 TWO-M04, sufficient full-C2 inequalities')

fig,ax=plt.subplots(figsize=(3.35,2.6));values=[18,21,36,36];labels=['Phase9','Source11','Real8','Complex6'];xx=np.arange(4)
ax.bar(xx,values,color=[GRAY,GRAY,TEAL,NAVY],width=.58);ax.axhline(36,color=RUST,ls=':',lw=.8)
for i,v in enumerate(values):ax.text(i,v+.7,str(v),ha='center',fontsize=8)
ax.set(xticks=xx,xticklabels=labels,ylabel='Identified symmetric-kernel parameters',ylim=(0,41),yticks=[0,12,24,36]);ax.grid(axis='y',alpha=.15)
ax.text(2,3,'64 readings',ha='center',va='bottom',rotation=90,color='white',fontsize=7);ax.text(3,3,'66 readings',ha='center',va='bottom',rotation=90,color='white',fontsize=7)
save(fig,'tomography_rank',{'rank':values,'unknowns':36,'source_span':[9,11,8,6],'readings':[None,None,64,66]},'GEN7 ONE-T1/T2/T3 / exact full-image designs')

r=np.logspace(-5,4,700);a=1/(1+4*r[:,None]*np.arange(4));S1=a.sum(axis=1);S2=(a*a).sum(axis=1)
theta=r*S1/4;p=S1*S1/(4*S2);q=4*(a*a*np.arange(4)).sum(axis=1)/S2
fig,axs=plt.subplots(2,1,figsize=(3.35,3.4),sharex=True)
axs[0].semilogx(theta,p,color=NAVY);axs[1].semilogx(theta,q,color=TEAL)
for rr in [.01,.1,1,10,100]:
 aa=1/(1+4*rr*np.arange(4));s1=aa.sum();s2=(aa*aa).sum();tt=rr*s1/4
 axs[0].scatter(tt,s1*s1/(4*s2),s=15,color=RUST);axs[1].scatter(tt,4*(aa*aa*np.arange(4)).sum()/s2,s=15,color=RUST)
axs[0].set(ylabel=r'Incidence $p$',ylim=(.2,1.04));axs[1].set(ylabel=r'Placement response $q$',xlabel=r'Scale-free placement $\theta=\tau/\epsilon$',ylim=(-.2,6.2))
for ax in axs:ax.grid(alpha=.15)
save(fig,'he3_chart',{'theta':theta.tolist(),'p':p.tolist(),'q':q.tolist()},'GEN7 FOUR-CHART / exact four-pole factor and six rational-r controls')

fig,ax=plt.subplots(figsize=(3.35,2.55));values=[.054037,382.443,883.75];yy=np.arange(3)
ax.barh(yy,values,color=[GRAY,TEAL,NAVY],height=.52)
ax.set(yticks=yy,yticklabels=['IR upper cap','Band lower guarantee','High-frequency upper cap'],xlabel='Difference-amplitude number norm',xlim=(0,1110));ax.grid(axis='x',alpha=.15)
for y,v,label in zip(yy,values,['< 0.054037','> 382.443','≤ 883.75']):ax.text(max(v,7)+12,y,label,va='center',fontsize=7.3)
save(fig,'continuum_receiver',{'full_norm_lower':1266.24722856428927038757,'IR_upper':.054037,'band_lower':382.443,'high_upper':883.75},'GEN7 FOUR-R01/R02 / full outgoing number and energy forms')

fig,axs=plt.subplots(2,1,figsize=(3.35,3.35))
values=[1/192,.005154454667189959]
axs[0].barh([1,0],np.array(values)*1000,color=[TEAL,RUST],height=.5)
axs[0].set(xlim=(5.10,5.23),yticks=[0,1],yticklabels=['Hazard depth 1/48','One marked attempt'],xlabel=r'Isolated transfer $\times 10^3$ (acceptance 1/4)')
T=np.linspace(4,20,161)
axs[1].plot(T,.18892416368715884*T+.06022430801813990,color=NAVY)
axs[1].scatter([16],[3.0830109270126814],s=19,color=TEAL)
axs[1].set(xlabel=r'Held duration $T/\tau$',ylabel=r'Variance of $N_T$')
for ax in axs:ax.grid(axis='x',alpha=.15)
save(fig,'contact_variance',{'isolated_transfers':values,'variance_slope':.18892416368715884,'variance_intercept':.06022430801813990,'variance16':3.0830109270126814},'GEN7 FOUR-C01/C02 / isolated frozen contact and centered held Gaussian law')
(OUT/'FIGURE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Built {len(manifest)} scientific figures with formula/data sidecars.')
