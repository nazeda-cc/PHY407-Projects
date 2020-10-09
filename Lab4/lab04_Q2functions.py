# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 04:14:04 2020

@author: Zirui Wan
"""


import numpy as np


# convert all the constants to SI units
L = 5e-10
ev = 1.60218e-19
a = 10*ev
M = 9.1094e-31
Q = 1.6022e-19
hbar = 1.05457e-34

def Hmn(m, n):
    """ Function to calculate entry in the Hermite matrix at m, n
    INPUT:
        m, n [int]: coordinates of entry
    OUTPUT:
        hmn [float]: calcualted entry
    """
    if m != n:
        if (m%2==0 and n%2==0) or (m%2==1 and n%2==1):
            hmn = 0
        else:
            hmn = -8*a*m*n/(np.pi**2 * (m**2 - n**2)**2)
    else:
        hmn = a/2 + np.pi**2*hbar**2*m**2/(2*M*L**2)
    
    return hmn



def Hmatrix(mmax, nmax):
    """ Function to calculate the Hermite matrix
    INPUT:
        mmax, nmax [int]: size of the matrix
    OUTPUT:
        H [2x2 float]: calcualted matrix
    """
    H = np.zeros((mmax, nmax))
    for m in range(1, mmax+1):
        for n in range(1, nmax+1):
            H[m-1, n-1] = Hmn(m, n)
    return H



def psi(x, evector, mmax):
    """ Function to calculate the wavefunction using the eigen vectors
    INPUT:
        x [float]: array of location
        evector [float]: array of the eigen vector
        mmax [int]: size of this eigen vector
    OUTPUT:
        p [float]: calculated wave function
    """
    p = 0.0
    for i in range(mmax):
        p += evector[i]*np.sin(i*np.pi*x/L)
    return p

def psi_sq(x, evector, mmax):
    """ Function to calculate the squared wavefunction using the eigen vectors
    INPUT:
        x [float]: array of location
        evector [float]: array of the eigen vector
        mmax [int]: size of this eigen vector
    OUTPUT:
        p2 [float]: calculated wave function squared
    """
    p2 = np.abs(psi(x, evector, mmax))**2
    return p2




def simpson(f, a, b, evector, mmax):
    """ Function to calculate the integral using Simpson's rule
    INPUT:
        f : function name
        a [float]: lower bound
        b [float]: upper bound
        evector [float]: array of the eigen vector
        mmax [int]: size of this eigen vector
    OUTPUT:
        S [float]: calculated integral of the function between a and b
    """
    h=(b-a)/mmax
    k=0.0
    x=a + h
    for i in range(1, int(mmax/2) + 1):
        k += 4*f(x, evector, mmax)
        x += 2*h

    x = a + 2*h
    for i in range(1, int(mmax/2)):
        k += 2*f(x, evector, mmax)
        x += 2*h
    S = (h/3)*(f(a, evector, mmax) + f(b, evector, mmax) + k)
    return S 

