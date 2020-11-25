# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 03:23:06 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
from numpy.linalg import solve
from Lab09_Q1functions import normal, oscillator, hamilt, energy, xhat


###############################################################################
###################  Simulation ###############################################
###############################################################################


# define constants
L = 1e-8
m = 9.109e-31
sigma = L/25
kappa = 500/L
tau = 1e-18
hbar = 6.62607015e-34 / (2*np.pi)


# define array of positions
x = np.linspace(-L/2, L/2, 1024)
x = x[1:-1]
a = x[1] - x[0]

# time steps and initial positon
N = 4000
x0 = L/5
T = np.arange(tau, (N+1)*tau, tau)


# calculate initial condition of wavefunction
phi = np.exp( -(x - x0)**2/(4*sigma)**2 + 1j*kappa*x )
phi0 = normal(phi, x)
phi = phi/phi0

# define potential
V = oscillator(x)
# calculate Hamiltanion matrix
HD = hamilt(V)
Lmat = np.eye(1022) + 1j*tau/(2*hbar)*HD
Rmat = np.eye(1022) - 1j*tau/(2*hbar)*HD

# define arrays for outputs
phi0s = []
Es = []
xexps = [] 
phis = np.zeros((len(T) + 1, len(phi)))
phis[0] = phi

# loop over to solve PDF
counter=1
for tnow in T:
    print(counter, ' / ', len(T))
    v = np.matmul(Rmat, phi)
    phi = solve(Lmat, v)
    phi0s.append( normal(phi, x) )
    Es.append( energy(phi, HD) )
    xexps.append( xhat(phi, x) )
    phis[counter] = phi
    counter += 1

# save outputs to zipped file
np.savez('Lab09_harmonic.npz', T=T, E=Es, X=xexps, phi0=phi0s)
np.save('Lab09_harmonic_phi.npy', phis)

