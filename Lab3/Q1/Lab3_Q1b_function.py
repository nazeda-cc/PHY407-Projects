# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:25:52 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *

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

def P(u, T_a, t):
    delta = 4.3 + 0.145 * T_a + 0.00196 * (T_a**2)
    u_avg = 11.2 + 0.365 * T_a + 0.00706 * (T_a**2) + 0.9 * np.log(t)
    
    N = 100
    x, w = gaussxwab(N, 0, u)
    integral = 0
    for i in range(N):
        integral += w[i] * np.exp(-(u_avg - x[i])**2 / (2 * delta**2))
    
    return integral / (np.sqrt(2*np.pi) * delta)