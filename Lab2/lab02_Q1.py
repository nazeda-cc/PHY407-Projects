# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:57:02 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
from functions_lab02_Q1 import dfdx, f


# define array of step size h
h = np.zeros((17))
for i in range(17):
    h[i] = 10**(i - 16)
    
# define and calculate the derivative with different step sizes
dff = np.zeros((17))
for i in range(17):
    dff[i] = (f(0.5+h[i]) - f(0.5))/h[i]

# calculate absolute errors between numerical and analytical derivatives
errors_f = abs(dff - dfdx(0.5))

# define and calculate the derivative with different step sizes
dfc = np.zeros((17))
for i in range(17):

    dfc[i] = (f(0.5+h[i]/2) - f(0.5-h[i]/2))/h[i]
# calculate absolute errors between numerical and analytical derivatives
errors_c = abs(dfc - dfdx(0.5))

# plot the errors versus step sizes
plt.figure(figsize=(8, 8))
plt.loglog(h, errors_f, lw=5, label='Forward difference scheme')
plt.loglog(h, errors_c, lw=5, label='Central difference scheme')
plt.grid(True, which="both", ls="--")
plt.legend(fontsize=20)
plt.xlabel('Size of step h', fontsize=20)
plt.ylabel('Absolute error between numerical and analytical derivative', fontsize=20)