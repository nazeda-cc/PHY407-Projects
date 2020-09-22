# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:00:08 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from matplotlib import pyplot as plt
from Lab2_Q2b_function import *
'''
######################## b i #################################################
x = np.arange(0, 20, 0.1)
y0 = []
y1 = []
y2 = []

for i in x:
    y0.append(J(0, i))
    
for i in x:
    y1.append(J(1, i))

for i in x:
    y2.append(J(2, i))

plt.figure(1)
plt.plot(x, y0, label = '$J_0$')
plt.plot(x, y1, label = '$J_1$')
plt.plot(x, y2, label = '$J_2$')
plt.xlabel('$x$')
plt.ylabel('$J_m(x)$')
plt.legend()
plt.title('Q2b, plot of $J_0$, $J_1$, and $J_2$, textbood Ex5.4(a)')
##############################################################################
'''
'''
######################## b ii ################################################
x = np.arange(0, 20, 0.1)
y0 = []
y1 = []
y2 = []

for i in x:
    y0.append(J(0, i))

plt.figure(2)
plt.plot(x, special.jv(0, x), label = 'scipy.special.Jv(0,x)')
plt.plot(x, y0, label = 'My function')
plt.xlabel('$x$')
plt.ylabel('$J_0(x)$')
plt.legend()
plt.title('Comparison between my bessel and scipy.special.jv, for $J_0(x)$')
plt.show()

for i in x:
    y1.append(J(1, i))

plt.figure(2)
plt.plot(x, special.jv(1, x), label = 'scipy.special.Jv(1,x)')
plt.plot(x, y1, label = 'My function')
plt.xlabel('$x$')
plt.ylabel('$J_1(x)$')
plt.legend()
plt.title('Comparison between my bessel and scipy.special.jv, for $J_1(x)$')
plt.show()    
##############################################################################
'''

########################### b iii ############################################
#in nanometer
'''
P = np.ones([2000,2000], float)*0
lam = 500
k = 2 * np.pi / lam
r = np.arange(0,1000)
I_r = [(0.5/k) ** 2]
for i in range(1, 1000):
    I_r.append((J(1, k*i) / (k*i)) ** 2)
plt.plot(r, I_r)
plt.semilogy()
'''
lam = 500
k = 2 * np.pi / lam

r = np.arange(0,1500)
I_r = [0.3]
for i in range(1, 1500):
    I_r.append((J(1, k*i) / (k*i)) ** 2)

plt.plot(r, I_r)
x = np.arange(-1000, 1001, 1)
y = np.arange(-1000, 1001, 1)
P = np.ones([2001,2001], float)*0
for i in range(0,2001):
    for j in range(0,2001):
        r = int(np.sqrt((i-1000)**2 + (j-1000)**2))
        P[i][j] = I_r[r]
plt.figure(figsize = (10,8))      
c = plt.pcolormesh(x, y, P, vmax = 0.007)
plt.colorbar(c) 
plt.show()
