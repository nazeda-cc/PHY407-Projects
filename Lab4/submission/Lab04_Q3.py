# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 04:51:21 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
from Lab04_Q3functions import solve_parta, solve_partb
from Lab04_Q3functions import wien_f, wien_rhs, wien_dfdx, binary, newton, relaxation
import matplotlib
font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15}
matplotlib.rc('font', **font)


##################### Part (a) #####################
crange = np.arange(0, 3, 0.01)  # define range of c values
xvals = np.zeros((crange.shape[0])) # array for roots
# compute root for each c value
for i in range(crange.shape[0]):
    xvals[i] = solve_parta(crange[i])

# plot results
plt.figure(figsize=(8, 8)) 
plt.plot(crange, xvals, lw=3)
plt.xlabel('c')
plt.ylabel('Root of x = 1 - exp(-cx)')
plt.grid()


##################### Part (b) #####################
omegarange = np.arange(0, 1, 0.1)   # define array of omega values
xvals = np.zeros((omegarange.shape[0])) # array for roots
iters = np.zeros((omegarange.shape[0])) # array for number of iterations
# find the root for each omega value
for i in range(omegarange.shape[0]):
    xvals[i], iters[i] = solve_partb(2, omegarange[i])

# plot results
plt.figure(figsize=(12, 6)) 
plt.subplot(1, 2, 1)
plt.plot(omegarange, iters, lw=3)
plt.xlabel('$\omega$')
plt.ylabel('Number of iterations used for convergence')
plt.grid()
plt.subplot(1, 2, 2)
plt.plot(omegarange, xvals, lw=3)
plt.gca().ticklabel_format(useOffset=False)
plt.xlabel('$\omega$')
plt.ylabel('Final root for x = 1 - exp(-2x)')
plt.subplots_adjust(wspace=0.5, right=0.98, left=0.05)
plt.grid()


##################### Part (c) #####################
# define physical constants in SI units
h = 6.62607004e-34
c = 299792458
kb = 1.38064852e-23

# define initial gueses for binary search
x1 = 0.01
x2 = 100
# find root and return number of iter's with different methods
xbinary, n1 = binary(wien_f, x1, x2, 1e-6)
xrelax, n2 = relaxation(wien_rhs, x2, 1e-6)
xnewton, n3 = newton(wien_f, wien_dfdx, x2, 1e-6)

# calculate Wien's constant
bbinary = h*c/kb/xbinary
brelax = h*c/kb/xrelax
bnewton = h*c/kb/xnewton

# calculate Sun's surface temp
lamb = 502e-9
tempb = bbinary/lamb
tempr = brelax/lamb
tempn = bnewton/lamb

# print results
print('Binary Wien constant, Sun temp, and number of iterations: ', bbinary, tempb, n1)
print('Relaxation Wien constant, Sun temp, and number of iterations: ', brelax, tempr, n2)
print('Newton Wien constant and, Sun temp, number of iterations: ', bnewton, tempn, n3)

# visualize the difference
plt.figure(figsize=(8, 8))
plt.bar([1, 2, 3], [n1, n2, n3])
plt.ylabel('Number of iterations used for convergence')
plt.xlabel('Numerical method')
plt.xticks([1, 2, 3], ['Binary search', 'Relaxation', "Newton's method"])
plt.grid()