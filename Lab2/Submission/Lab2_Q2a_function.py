# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:17:07 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special

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

######exponential for integral inside Dawson's function########
def expo(t):
    return np.exp(t**2)
#################################################

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
    
    else:
        return 'Input error :D'
