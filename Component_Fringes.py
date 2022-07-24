# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 08:46:23 2022

@author: 91992
"""
import numpy as np
import math as mt
import matplotlib as plt
import sys
import matplotlib.pyplot as pl
def UnBox(ax=None):
    if not ax: ax = pl.gca() #Get current Axis
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
def ShowOrSave():
    if len(sys.argv)==1:
        pl.show()
    else:
        plotFile=sys.argv[1]
        plt.savefig(plotFile,bbox_inches="tight")
    
def FringePattern(npix,frequency,flux,correlatedFlux,phase,envelopeWidth,):
    x=np.linspace(-npix/2+1,npix/2,npix)
    envelope=np.exp(-x**2/(2*envelopeWidth**2))
    return flux+correlatedFlux*envelope*np.cos(2*mt.pi*frequency*x+phase)

def FringePatterns(npix=400):
    return([
    FringePattern(npix,frequency=0.050,flux=1.2,correlatedFlux=0.6,phase=-mt.pi/3,envelopeWidth=66),
    FringePattern(npix,frequency=0.3,flux=0.5,correlatedFlux=0.5,phase=0,envelopeWidth=44),
    FringePattern(npix,frequency=0.15,flux=0.9,correlatedFlux=0.5,phase=mt.pi/2,envelopeWidth=20)])

fig,ax=pl.subplots(3,1,sharex=True,sharey=True,figsize=(6,4))
for i,fringe in enumerate(FringePatterns()):
    pl.sca(ax[i])
    pl.plot(fringe,color="k")
    pl.ylabel("intensity")
    pl.ylim(0,1.9)
    UnBox()
pl.xlabel("pixel")
ShowOrSave()
pl.savefig(fig)

pl.figure(figsize=(6,4))
summedFringe=sum(FringePatterns())
pl.plot(summedFringe,color="k")
pl.ylabel("intensity")
pl.xlabel("pixel")
UnBox()
ShowOrSave()
pl.savefig()