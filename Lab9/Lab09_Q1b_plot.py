# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:17:25 2020

@author: Zirui Wan
"""


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
from Lab09_Q1functions import pdf

# define constants
L = 1e-8
x = np.linspace(-L/2, L/2, 1024)
x = x[1:-1]


# load energy, expected position, time from the zipped outputs
npzfile = np.load('Lab09_harmonic.npz')
phi0s = npzfile['phi0']
Es = npzfile['E']
Xs = npzfile['X']
T = npzfile['T']

# plot normalization and energy versus time
plt.figure(figsize=(12, 9))
plt.subplot(2, 1, 1)
plt.plot(T, phi0s)
plt.grid()
plt.ylabel('Normalization of wavefunction')
plt.xlabel('Time (s)')
plt.title('Normalization vs time')
plt.ylim((0.99, 1.01))


plt.subplot(2, 1, 2)
plt.plot(T, Es)
plt.ylabel('Energy')
plt.xlabel('Time (s)')
plt.title('Energy vs time')
plt.grid()
plt.ylim((0.99*Es[0], 1.01*Es[0]))
plt.subplots_adjust(hspace=0.4)


# plot expected location versus time
plt.figure(figsize=(8, 8))
plt.plot(T, Xs)
plt.grid()
plt.ylabel('<X>', fontsize=18)
plt.xlabel('Time (s)', fontsize=18)
plt.title('<X> vs time', fontsize=18)

inow = 0
plt.scatter(T[inow], Xs[inow], s=300, color='red', label='t=0')
inow = int(len(T)/4)
plt.scatter(T[inow], Xs[inow], s=300, color='blue', label='t=T/4')
inow = int(len(T)/2)
plt.scatter(T[inow], Xs[inow], s=300, color='orange', label='t=T/2')
inow = int(len(T)*3/4)
plt.scatter(T[inow], Xs[inow], s=300, color='green', label='t=3T/4')
plt.legend()
plt.suptitle('Harmonic oscillator potential')
plt.savefig('Q1c2.png', dpi=300)


# plot wavefunction and probability density function versus time for different t
plt.figure(figsize=(12, 20))
inow = 0
phinow = np.load('Lab09_harmonic_phi.npy')[inow]
plt.subplot(4, 2, 1)
plt.plot(x, phinow, color='red')
plt.ylabel(r'$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$ at t=0')
plt.grid()
plt.xlim((-L/2, L/2))

plt.subplot(4, 2, 2)
plt.plot(x, pdf(phinow), color='red')
plt.ylabel(r'$\psi$*$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$*$\psi$ at t=0')
plt.grid()
plt.xlim((-L/2, L/2))

inow = int(len(T)/4)
phinow = np.load('Lab09_harmonic_phi.npy')[inow]
plt.subplot(4, 2, 3)
plt.plot(x, phinow, color='blue')
plt.ylabel(r'$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$ at t=T/4')
plt.grid()
plt.xlim((-L/2, L/2))

plt.subplot(4, 2, 4)
plt.plot(x, pdf(phinow), color='blue')
plt.ylabel(r'$\psi$*$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$*$\psi$ at t=T/4')
plt.grid()
plt.xlim((-L/2, L/2))


inow = int(len(T)/2)
phinow = np.load('Lab09_harmonic_phi.npy')[inow]
plt.subplot(4, 2, 5)
plt.plot(x, phinow, color='orange')
plt.ylabel(r'$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$ at t=T/2')
plt.grid()
plt.xlim((-L/2, L/2))

plt.subplot(4, 2, 6)
plt.plot(x, pdf(phinow), color='orange')
plt.ylabel(r'$\psi$*$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$*$\psi$ at t=T/2')
plt.grid()
plt.xlim((-L/2, L/2))


inow = int(len(T)*3/4)
phinow = np.load('Lab09_harmonic_phi.npy')[inow]
plt.subplot(4, 2, 7)
plt.plot(x, phinow, color='green')
plt.ylabel(r'$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$ at t=3T/4')
plt.grid()
plt.xlim((-L/2, L/2))

plt.subplot(4, 2, 8)
plt.plot(x, pdf(phinow), color='green')
plt.ylabel(r'$\psi$*$\psi$')
plt.xlabel('x (m)')
plt.title(r'$\psi$*$\psi$ at t=3T/4')
plt.grid()
plt.xlim((-L/2, L/2))

plt.subplots_adjust(hspace=0.4)
plt.suptitle('Harmonic oscillator potential', y=0.92)

plt.savefig('Q1c1.png', dpi=300)