# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:51:53 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special

######Simpsons method###########
def Simp(f, m, x, n):       #for bessel function, a = 0 and b = pi
                            #so instead of taking a & b, this simpson's method 
                            #takes parameters x and m
    h = (np.pi - 0) / n
    integral = f(0, m, x) + f(np.pi, m, x)
    for i in range(1, n, 2):
        integral += 4 * f(0 + i * h, m, x)
    for i in range(2, n, 2):
        integral += 2 * f(0 + i * h, m, x)
    
    return (1/3) * h * integral
################################

def J_cos(theta, m, x):     #cosine function inside the integral
    return np.cos(m * theta - x * np.sin(theta))


def J(m, x):                #Final bessel function
    return Simp(J_cos, m, x, 1000) / np.pi
    