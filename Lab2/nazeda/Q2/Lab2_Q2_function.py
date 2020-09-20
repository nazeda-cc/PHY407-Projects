# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:56:16 2020

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

######Simpson method###########
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
    #for real part
    return np.exp(t**2)

def expo_neg(t):
    #for imaginary part
    return np.exp(-t**2)    
#################################################

#############Dawson's function################
def Daws(x, n, method):
    
    #Due to the integral method we use, it only supports input to be
    #pure real or pure imaginary.

    x = complex(x)
    if method == 'Trap':
        integral_real = Trap(expo, 0, x.real, n)            #calculate real part
        integral_imag = Trap(expo_neg, 0, x.imag, n)        #calculate imaginary part
        return (np.exp(-x.real**2) * integral_real,         #return result a complex number
                np.exp(x.imag**2) * integral_imag) 
    
    
    elif method == 'Simp':
        integral_real = Simp(expo, 0, x.real, n)            #calculate real part
        integral_imag = Trap(expo_neg, 0, x.imag, n)        #calculate imaginary part
        return (np.exp(-x.real**2) * integral_real,  #return result a complex number
                np.exp(x.imag**2) * integral_imag)
    
    elif method == 'Scipy':
        #return special.dawsn(x)
        return (special.dawsn(x.real), 
                (special.dawsn(x.imag * 1j)).imag)
    
    else:
        return 'Input error :D'
'''        
    if sign == '-':
        if method == 'Trap':
            integral = Trap(expo_neg, 0, x, n)
            return np.exp(-x**2) * integral
    
        elif method == 'Simp':
            integral = Simp(expo_neg, 0, x, n)
            return np.exp(-x**2) * integral
    
        elif method == 'Scipy':
            return special.dawsn(x)
    
        else:
            return 'Input error :D'
'''