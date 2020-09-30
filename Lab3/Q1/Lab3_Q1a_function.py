# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:07:56 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *

######Trapezoidal method#######
def Trap(f, a, b, n):
    
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i*h)
        
    return integral * h
###############################

######Simpsons method###########
def Simp(f, a, b, n):
    
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)
    
    return (1/3) * h * integral
################################


##############Gaussian method here##########
def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w
#############################################


######exponential for integration inside Dawson's function########
def expo(t):
    return np.exp(t**2)
######################################################

#############Dawson's function###################
def Daws(x, n, method):
    
    if method == 'Trap':
        #apply Trapezoidal method
        integral_real = Trap(expo, 0, x, n)            
        return np.exp(-x**2) * integral_real         
    
    
    elif method == 'Simp':
        #apply Simpsons method
        integral_real = Simp(expo, 0, x, n)            
        return np.exp(-x**2) * integral_real    
    
    elif method == 'Scipy':
        #use scipy library
        return special.dawsn(x)
    
    elif method == 'Gauss':
        #apply gauss method
        integral = 0
        s, w = gaussxwab(n, 0, x)
        for i in range(n):
            integral += w[i] * expo(s[i])
        return np.exp(-x**2) * integral
    
    else:
        return 'Input error :D'