# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:20:05 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from random import random
from Q3_mult import mult
from time import time

N = 160

A = np.ones([N, N], float)*3
B = np.ones([N, N], float)*4
C = np.ones([N, N], float)*0

d_0 = []
d_1 = []

Nx = np.arange(2,N,1)

#method referring to textbook
for i in range(2,N):
    start = time()
    C = mult(A, B, i)
    end = time()
    diff = end - start
    d_0.append(diff)
    print(i)

#numpy.dot 
for i in range(2,N):
    start = time()
    C_alt = np.dot(A, B)
    end = time()
    diff = end - start
    d_1.append(diff)
'''
####Plot vs N#####
plt.plot(Nx, d_0, label = 'Text book method')
plt.plot(Nx, d_1, label = 'numpy.dot')
plt.xlabel('N')
plt.ylabel('time (s)')
plt.title('Run time vs N')
plt.legend()
'''
#####Plot vs N^3####

for i in range(0,N-2):
    Nx[i] = Nx[i]**3
    
plt.plot(Nx, d_0, label = 'Text book method')
plt.plot(Nx, d_1, label = 'numpy.dot')
plt.xlabel('N$^3$')
plt.ylabel('time (s)')
plt.title('Run time vs N$^3$')
plt.legend()