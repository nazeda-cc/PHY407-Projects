# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:15:47 2020

@author: rundo
"""

import numpy as np
from numpy import random



def volume(dim, N):
    count = 0
    for i in range(N):
    
        r = 2 * random.rand(dim) - 1
    
        if np.sqrt(np.sum(r**2)) < 1:
            count += 1
            
    return count * 2**dim / N
        
d = 20

N = 1000000


#expect value for V, <V>

V = np.empty(0)
n_v = 10

for i in range(n_v):
    V = np.append(V, volume(d, N))

    
v_avg = np.average(V)
v2_avg = np.average(V**2)
print('<V>=', v_avg)
print('<V^2>', v2_avg)
print('var V=', np.sqrt(v2_avg - v_avg**2))