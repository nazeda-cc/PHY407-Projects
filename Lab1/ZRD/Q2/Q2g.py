# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:20:09 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q2_function import Population as popu
from random import random
from Q2_fit import fit

r = 3.738
p = 75                                     #set iterations
x0_1 = 0.1
epsilon = random()*10**-8                   #generate random epsilon
x0_2 = x0_1 + epsilon

x_1 = popu(x0_1, r, p)                      #iteration
x_2 = popu(x0_2, r, p)

delta = []
f = []
year = np.arange(0,p,1)

#calculate difference
for i in range(p):
    delta.append(abs(x_2[i]-x_1[i]))

#calculate fit function
for i in range(p):
    f.append(fit(12**-8, 0.35, i))
    
plt.plot(year, delta, label = '$\delta$')
plt.plot(year, f, label = 'fit, $12^{-8}e^{0.35p}$')
plt.legend()
print(len(f))
plt.xlabel('p (years)')
plt.ylabel('x')
plt.title('Q2g Difference fit plot')
plt.semilogy()