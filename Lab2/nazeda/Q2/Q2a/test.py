# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:24:47 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from Lab2_Q2a_function import *


x = 4
n = 2
power = 19
is_imag = 0
## Trapezoidal method ####

integral_trap = []
error_trap = []
for i in range(5, power):
    n = 2**i
    integral_trap.append(Daws(x, n, 'Trap')[is_imag])

for i in range(0, len(integral_trap) - 1):
    error_trap.append(abs(integral_trap[i+1]-integral_trap[i]) * (1/3))
    
## Simpsons method #######
integral_simp = []
error_simp = []
for i in range(5, power):
    n = 2**i
    integral_simp.append(Daws(x, n, 'Simp')[is_imag])

for i in range(0, len(integral_simp) - 1):
    error_simp.append(abs(integral_simp[i+1]-integral_simp[i]) * (1/3))
    
print(error_trap)
print(error_simp)
plt.plot(range(5, power-1), error_trap)
plt.plot(range(5, power-1), error_simp)
plt.semilogy()