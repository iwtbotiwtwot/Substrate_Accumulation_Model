"""Reproduce Volume I explanatory vector figures; no observational data.
Run: MPLCONFIGDIR=/tmp/mpl-volume python make_explanatory_figures.py
Dependencies: numpy, matplotlib. Analytic formulas are printed in chapters VII, X, XII.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/mpl-volume')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':8.5,
 'axes.labelsize':9,'axes.titlesize':10,'legend.fontsize':8,
 'xtick.labelsize':8,'ytick.labelsize':8,'axes.spines.top':False,
 'axes.spines.right':False,'axes.linewidth':0.65,'lines.linewidth':1.7,
 'pdf.fonttype':42,'ps.fonttype':42,'savefig.dpi':180})
BLUE='#24557A'; ORANGE='#A65323'; GRAY='#737373'
def make():
    fig,axs=plt.subplots(1,2,figsize=(7.14,2.9))
    fig.subplots_adjust(left=.085,right=.98,bottom=.20,top=.84,wspace=.38)
    for ax in axs:
        ax.grid(axis='y',color='#DDDDDD',linewidth=.5)
        ax.set_axisbelow(True)
    return fig,axs
def save(fig,name):
    fig.savefig(OUT/(name+'.pdf'))
    fig.savefig(OUT/(name+'.png'))
    plt.close(fig)

# VII: adopted Schwarzschild/Hawking/quarter-area bridge; exact finite ledger.
fig,(ax,bx)=make()
m=np.geomspace(.1,10,500)
ax.loglog(m,1/m,color=BLUE,label=r'$T_H/T_{\rm ref}=m^{-1}$')
ax.loglog(m,m*m,color=ORANGE,linestyle='--',label=r'$S_H/S_{\rm ref}=m^2$')
ax.set(xlabel=r'Mass ratio $m=M/M_{\rm ref}$',ylabel='Normalized quantity',xlim=(.1,10),ylim=(.01,100),title='(a) Conditional horizon scalings')
ax.legend(loc='upper left',frameon=False)
x=np.linspace(0,1,600)
bx.plot(x,2/(1+np.sqrt(1-x)),color=BLUE,label='Exact finite ledger')
bx.axhline(1,color=GRAY,linestyle='--',linewidth=1,label='Differential limit')
bx.set(xlabel=r'Fraction of entries lost $x=j/N$',ylabel=r'$\Delta E_j/(j k_B T_H(M))$',xlim=(0,1),ylim=(.95,2.08),title='(b) Finite-step energy correction')
bx.legend(loc='upper left',frameon=False)
bx.text(.03,.36,'Continuous envelope of\nallowed integer transitions',transform=bx.transAxes,fontsize=7.5,color=GRAY)
save(fig,'ch07_horizon_scalings')

# X: X denotes halo-to-baryon, not total-to-baryon, circular support.
fig,(ax,bx)=make()
x=np.linspace(0,8,500); marker=10/np.pi
for axis in (ax,bx):
    axis.axvline(marker,color=GRAY,linestyle=':',linewidth=1)
    axis.set_xlim(0,8)
    axis.set_xlabel(r'Halo-to-baryon support ratio $X$')
ax.plot(x,x/(1+x),color=BLUE)
ax.plot(marker,marker/(1+marker),'o',color=ORANGE,markersize=4)
ax.set(ylabel=r'Support fraction $f_{\rm supp}=X/(1+X)$',ylim=(0,1),title='(a) Residual support fraction')
ax.annotate(r'$X=10/\pi$'+'\n'+r'$f_{\rm supp}\simeq0.76094$',xy=(marker,marker/(1+marker)),xytext=(4.1,.42),fontsize=8,arrowprops={'arrowstyle':'-','color':GRAY,'lw':.6})
bx.plot(x,np.sqrt(1+x),color=BLUE)
bx.plot(marker,np.sqrt(1+marker),'o',color=ORANGE,markersize=4)
bx.set(ylabel=r'Speed ratio $V_{\rm obs}/V_{\rm bar}=\sqrt{1+X}$',ylim=(1,3.1),title='(b) Corresponding speed ratio')
bx.annotate(r'$\sqrt{1+10/\pi}\simeq2.0453$',xy=(marker,np.sqrt(1+marker)),xytext=(3.7,1.45),fontsize=8,arrowprops={'arrowstyle':'-','color':GRAY,'lw':.6})
fig.text(.5,.015,'Illustrative algebra only: no galaxy measurements or radial profile are plotted.',ha='center',fontsize=7.5,color=GRAY)
save(fig,'ch10_support_mapping')

# XII: two distinct domains; late-time adapter deliberately neglects radiation.
fig,(ax,bx)=make()
z=np.linspace(0,5,500)
ax.plot(z,(1-(1+z)**-3)/np.pi,color=BLUE)
ax.axhline(1/np.pi,color=ORANGE,linestyle='--',linewidth=1)
ax.text(3.05,.326,r'$A_{\rm los}\to1/\pi$',color=ORANGE,fontsize=8)
ax.set(xlabel=r'Redshift $z$ (fixed observer)',ylabel=r'Past-cone accumulation $A_{\rm los}$',xlim=(0,5),ylim=(0,.36),title='(a) Declared past-cone road law')
a=np.linspace(1,5,500); om=1/np.pi; ol=1-om
bx.plot(a,np.sqrt(om*a**-3+ol),color=BLUE,label=r'$H_{\rm native}(a)/H_0$')
bx.axhline(np.sqrt(ol),color=ORANGE,linestyle='--',linewidth=1,label=r'Native limit $\sqrt{\Omega_\Lambda}$')
bx.axhline(ol**1.5,color=GRAY,linestyle=':',linewidth=1.3,label=r'Distance fit $\Omega_\Lambda^{3/2}$')
bx.set(xlabel=r'Future scale factor $a$ (today: $a=1$)',ylabel=r'Normalized rate or fit coefficient',xlim=(1,5),ylim=(.50,1.04),title='(b) Conditional background adapter')
bx.legend(loc='upper right',bbox_to_anchor=(1,.49),frameon=False,fontsize=7.3)
fig.text(.5,.015,'Distinct limits: increasing past-cone redshift does not represent future-time evolution.',ha='center',fontsize=7.5,color=GRAY)
save(fig,'ch12_distinct_limits')
