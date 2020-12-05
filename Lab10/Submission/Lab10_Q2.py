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
        
d = 10          #set dimension

N = 1000000     #number of sampling points

V = np.empty(0)


n_v = 30        # time of iterations

for i in range(n_v):
    V = np.append(V, volume(d, N))


# numerical standard deviation and volume result
print('Standard deviation in V is:', np.std(V))
print('The average volume V of the hyper-sphere is:', np.average(V))