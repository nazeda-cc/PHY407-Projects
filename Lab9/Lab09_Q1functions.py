# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:58:32 2020

@author: Zirui Wan
"""

import numpy as np

# define constants for the potential functions
L = 1e-8
m = 9.109e-31
sigma = L/25
kappa = 500/L
omega = 3e15
x = np.linspace(-L/2, L/2, 1024)
x = x[1:-1]
a = x[1] - x[0]
tau = 1e-18
hbar = 6.62607015e-34 / (2*np.pi)
V0 = 6e-17
x1 = L/4

def normal(phi, x):
    """ Function to calculate normalization factor of wave function
    INPUT:
        phi[float]: wavefunction
        x[float]: position array
    OUTPUT:
        phi0[float]: normalization factor
    """
    phi0 = np.sqrt( np.sum(np.conj(phi)*phi*a) )
    return phi0


def pdf(phi):
    """ Function to calculate probability density function of wave function
    INPUT:
        phi[float]: wavefunction
    OUTPUT:
        pdf[float]: probability density function
    """
    pdf = np.conj(phi)*phi
    return pdf


def energy(phi, HD):
    """ Function to calculate energy of wave function
    INPUT:
        phi[float]: wavefunction
        HD[2d array]: Hamiltonian matrix
    OUTPUT:
        E[float]: energy
    """
    E = np.matmul(HD, phi)
    E = np.conj(phi)*E
    E = np.sum( E * a)
    return E

def xhat(phi, x):
    """ Function to calculate energy of wave function
    INPUT:
        phi[float]: wavefunction
        x[float]: position array
    OUTPUT:
        xexp[float]: expected location <X>
    """
    xexp = np.sum( np.conj(phi)*x*phi * a)
    return xexp



def square(x):
    """ Function to calculate square potential
    INPUT:
        x[float]: position array
    OUTPUT:
        V[float]: potential
    """
    V = np.zeros((1022))
    return V


def oscillator(x):
    """ Function to calculate harmonic potential
    INPUT:
        x[float]: position array
    OUTPUT:
        V[float]: potential
    """
    V = np.zeros((1022))
    V[:] = 1/2*m*omega**2*x**2
    return V
    
def double(x):
    """ Function to calculate double-wall potential
    INPUT:
        x[float]: position array
    OUTPUT:
        V[float]: potential
    """
    V = np.zeros((1022))
    V[:] = V0* ((x**2)/(x1) - 1)**2
    return V


def hamilt(V):
    """ Function to calculate Hamiltonian matrix
    INPUT:
        x[float]: position array
        V[float]: potential
    OUTPUT:
        hd[2d array]: Halmiltonian matrix
    """
    A = -hbar**2/(2*m*a**2)
    B = V - 2*A
    D = np.diag(B, k=0)
    sup = A*np.eye(1022, k=1)
    sub = A*np.eye(1022, k=-1)
    hd = D + sub + sup
    return hd