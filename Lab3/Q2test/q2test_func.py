# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:02:11 2020

@author: rundo
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:31:49 2020

@author: Zirui Wan
"""


import numpy as np

def H(n, x):
    """ Function to compute Hermite polynomial in nth energy level of 1-D
    quantum harmonic oscillator.
    INPUT:
        n [integer]: number of energy level
        x [float]: position variable
        
    OUTPUT:
        h [float]: Hermite polynomials calculated
    """
    if n==0:
        h = 1
    elif n==1:
        h = 2*x
    else:
        h = 2*x*H(n-1, x)-2*(n-1)*H(n-2, x)
    return h
    

def psi(n, x):
    """ Function to compute wavefunction in nth energy level of 1-D
    quantum harmonic oscillator.
    INPUT:
        n [integer]: number of energy level
        x [float]: position variable
        
    OUTPUT:
        psi [float]: wavefunction calculated
    """
    psi = 1/(np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)*H(n, x)
    return psi
    


def gaussxw(N):
    """ Function to do Gaussian sampling between -1 and 1
    INPUT:
        N [integer]: number of sampling points
    OUTPUT:
        x [float]: location of sampled points
        w [float]: weights of these points
    """
    # Initial approximation to roots of the Legendre polynomial
    a = np.linspace(3, 4*N-1, N)/(4*N + 2)
    x = np.cos(np.pi* a + 1/(8 * N * N * np.tan(a)))
    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta  > epsilon:
        p0 = np.ones(N,float)
        p1 = np.copy(x)
        for k in range(1, N):
            p0, p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = np.max(np.abs(dx))
    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    return x, w

def gaussxwab(N, a, b):
    """ Function to do Gaussian sampling between a and b
    INPUT:
        N [integer]: number of sampling points
        a [float]: lower bound
        b [float]: upper bound
    OUTPUT:
        x [float]: location of sampled points
        w [float]: weights of these points
    """
    x, w = gaussxw(N)
    return 0.5*(b-a)*x + 0.5*(b+a), 0.5*(b-a)*w


def integrate_ab(function, n, a, b):
    """ Function to do the integral using Gaussian quad's
    
    INPUT:
        function [function]: function takes x as input
        a [float]: lower bound
        b [float]: upper bound
    OUTPUT:
        I [float]: integral computed
    """
    # define N
    N = 100
    # call gausswx for xi, wi
    x, w = gaussxwab(N, a, b)
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for k in range(N):
        I += w[k]*function(n, x[k])
        
    return I


def integrate(function, n):
    """ Function to do the integral using Gaussian quad's
    
    INPUT:
        function [function]: function takes x as input
    OUTPUT:
        I [float]: integral computed
    """
    # define N
    N = 100
    # call gausswx for xi, wi
    x, w = gaussxw(N)
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for k in range(N):
        I += w[k]*function(n, x[k])
        
    return I


def dpsidx_square(n, x):
    """ Function to do derivative using central differences
    
    INPUT:
        n [integer]: energy level
        z [float]: transformed x variable
    OUTPUT:
        dfdx [float]: 
            
    p^2
    """

    h = 1e-8
    #newx = z/(1-z**2)
    #xprev = newx - h
    #xnext = newx + h
    dfdx = ((psi(n, x+h) - psi(n, x-h)) / (2*h))**2
    #dfdx = dfdx**2*(1+z**2)/(1-z**2)**2
    return dfdx

def dpsidx(n, x):
    '''
    p
    '''
    h = 1e-8
    #newx = z/(1-z**2)
    #xprev = newx - h
    #xnext = newx + h
    dfdx = (psi(n, x+h) - psi(n, x-h)) / (2*h)
    #dfdx = dfdx*(1+z**2)/(1-z**2)
    return dfdx


    

def xpsi_sq(n, x):
    """ Function to do squared x*wavefunction
    
    INPUT:
        n [integer]: energy level
        z [float]: transformed x variable
    OUTPUT:
        xpsi_sq [float]: integrand
        
    x^2
    """
    #newx = z/(1-z**2)
    xpsi_sq = (x**2) * (psi(n, x)**2)
    #*(1+z**2)/(1-z**2)**2
    return xpsi_sq

def xpsi(n, x):
    '''
    x
    '''
    
    #newx = z/(1-z**2)
    xpsi = x * (psi(n, x)**2)
    return xpsi


def mean_xsq(n):
    """ Function to compute mean squared x between -inf and inf.
    INPUT:
        n [integer]: number of energy level
        
    OUTPUT:
        mean_xsq [float]: mean position
        
    <x^2>
    """
    mean_xsq = integrate_ab(xpsi_sq, n, -10, 10)
    return mean_xsq
    
    
def mean_psq(n):
    """ Function to compute squared derivative of psi between -inf and inf.
    INPUT:
        n [integer]: number of energy level
        
    OUTPUT:
        mean_psq [float]: mean momentum
        
    <p^2>
    """
    mean_psq = integrate_ab(dpsidx_square, n, -10, 10)
    return mean_psq

def mean_x(n):
    '''
    <x>
    '''
    
    mean_x = integrate_ab(xpsi, n, -10, 10)
    
    return mean_x

def mean_p(n):
    '''
    <p>
    '''
    
    mean_p = integrate_ab(dpsidx, n, -10, 10)
    
    return mean_p
    

def energy(n):
    """ Function to compute energy level of this oscillator.
    INPUT:
        n [integer]: number of energy level
        
    OUTPUT:
        E [float]: calculated energy
    """
    xsq = mean_xsq(n)
    psq = mean_psq(n)
    E = 1/2*(xsq + psq)
    return E