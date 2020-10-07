# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 02:00:14 2020

@author: Zirui Wan
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from lab04_Q2functions import Hmatrix, psi_sq, psi, simpson

# convert all the constants to SI units
L = 5e-10
ev = 1.60218e-19
a = 10*ev
M = 9.1094e-31
Q = 1.6022e-19
hbar = 1.05457e-34


# define number of grid cells
mmax = nmax = 10
# calculate Hermite matrix
H = Hmatrix(mmax, nmax)
# calculate eigen values and vectors
w, v = la.eig(H)
# sort w.r.t energy level (eigen values)
indicies = np.argsort(w)
eigs = w[indicies]/ev
print('First 10 energy levels (eV) with mmax=nmax=10: ', eigs)

# Increase the number of grids from 10 to 100 now
# define number of grid cells
mmax = nmax = 100
# calculate eigen values and vectors
H = Hmatrix(mmax, nmax)  
w, v = la.eig(H)
# sort w.r.t energy level (eigen values)
indicies = np.argsort(w)
eigs = w[indicies]/ev
print('First 10 energy levels (eV) with mmax=nmax=100: ', eigs[:10])


# Find the ground state wavefunction
E0 = eigs[0]
print("Ground state energy (eV): ", E0)
evector0 = v[:, indicies[0]]    # Use the index to find the eigenvector
E1 = eigs[1]
print("First excited state energy (eV): ", E1)
evector1 = v[:, indicies[1]]    # Use the index to find the eigenvector
E2 = eigs[2]
print("Second excited state energy (eV): ", E2)
evector2 = v[:, indicies[2]]    # Use the index to find the eigenvector

xrange = np.linspace(0, L, mmax)
psi0= psi(xrange, evector0, mmax)
a0 = simpson(psi_sq, 0, L, evector0, mmax)
psi1= psi(xrange, evector1, mmax)
a1 = simpson(psi_sq, 0, L, evector1, mmax)
psi2= psi(xrange, evector2, mmax)
a2 = simpson(psi_sq, 0, L, evector2, mmax)

plt.plot(xrange, psi0**2/a0, label='Ground state')
plt.plot(xrange, psi1**2/a1, label='First excited state')
plt.plot(xrange, psi2**2/a2, label='Second excited state')
plt.legend(bbox_to_anchor=(1.5, 1.0))
plt.grid()
plt.xlabel('x (m)')
plt.ylabel('Probability density function $|\psi(x)|^2$')