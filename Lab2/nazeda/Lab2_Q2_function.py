# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:56:16 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special

def Trap(f, a, b, n):
    
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i*h)
        
    return integral * h


def Simp(f, a, b, n):
    
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)
    
    return (1/3) * h * integral

def expo(t):

    return np.exp(t**2)    

def Daws(x, n, method):
    
    if method == 'Trap':
        integral = Trap(expo, 0, x, n)
        return np.exp(-x**2) * integral
    
    elif method == 'Simp':
        integral = Simp(expo, 0, x, n)
        return np.exp(-x**2) * integral
    
    elif method == 'Scipy':
        return special.dawsn(x)
    
    else:
        return 'Input error :D'