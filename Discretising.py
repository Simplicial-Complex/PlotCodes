# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 09:18:07 2022

@author: 91992
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def Gaussian(x,centre,sigma,amplitude=1):
    return amplitude*(np.exp(-(x-centre)**2/(2*sigma**2)))


def f(x): 
    return Gaussian(x,centre=10,sigma=4.4,amplitude=2.5)+Gaussian(x,centre=3,sigma=2.5,amplitude=3.0)-0.04*x

def UnBox(ax=None):
    if not ax: ax = plt.gca() #Get current Axis
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
def ShowOrSave():
    if len(sys.argv)==1:
        plt.show()
    else:
        plotFile=sys.argv[1]
        plt.savefig(plotFile,bbox_inches="tight")
    
plt.figure(figsize=(6*0.6,4*0.6))
offset=0.08
newx=[]
newy=[]
for i in range(10):
    newx+=[i-offset,i,i+offset]
    newy+=[0,f(i),0]
plt.plot(newx,newy,color='0.0')
x=np.linspace(0,10,100)
y=f(x)
plt.plot(x,y,color='0.5')
plt.xlim(0,10)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
UnBox()
ShowOrSave()