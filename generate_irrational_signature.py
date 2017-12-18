# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 17:37:07 2015

@author: Ilia
"""

import numpy as np

if __name__ == '__main__':
    c_max = 100
    d_max = 100
    
#    theta = 2**0.5;
    theta = 0.7
    c = np.arange(c_max)
    d = np.arange(d_max)
    C,D=np.meshgrid(c,d)
    S = C + D*theta
    iS = np.argsort(S.flatten())
    cn = C.flatten()[iS]
    
    from matplotlib import pyplot as plt
    plt.figure()
    plt.plot(cn,marker='.',linestyle='-')
    
    w,=np.where(cn == 0)
    dw=np.diff(w)
    plt.figure()
    plt.plot(dw,marker='.',linestyle='none')
    #    >>> 2**0.5
    #1.4142135623730951
    #>>> (99-1.09)/(68.95-0.4)
    #1.4283005105762216
    #>>> 

def MakeIrrationalSignature(theta,c_min,c_max,d_min,d_max,ret_d=False):
    c = np.arange(c_min,c_max)
    d = np.arange(d_min,d_max)
    C,D = np.meshgrid(c,d)
    S = C + D*theta
    iS = np.argsort(S.flatten())
    cn = C.flatten()[iS]
    if not ret_d:
        return cn
    else:
        return cn,D.flatten()[iS]

def GetClippedSignature(theta,c_max,d_max,ret_d=False):
    cn,dn = MakeIrrationalSignature(theta,0,c_max,0,d_max,ret_d=True)
    cutoff_ind = np.where(np.logical_or(dn==d_max-1,cn==c_max-1) )[0][0]
    if not ret_d:
        return cn[:cutoff_ind]
    else:
        return cn[:cutoff_ind],dn[:cutoff_ind]
