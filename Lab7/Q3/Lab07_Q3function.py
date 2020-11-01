# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:11:43 2020

@author: rundo
"""
import numpy as np
from matplotlib import pyplot as plt
#set constants
global m, a, e, hbar, sigma, h, L, size, tsize, target

maxi = 30
size = 0.0005
tsize = 100000



m = 9.1094e-31

hbar = 1.0546e-34

e = 1.6022e-19
sigma = 8.854e-12



a = 5.29e-11
h = size * a
L = maxi * a


target = e/tsize


def V(r):
    return -(e**2) / (4*np.pi*sigma*r)

def f(R, S, r, E, l):
    dR = S / r**2
    dS = l*(l+1)*R + ((2*m*r**2)/(hbar**2))*(V(r)-E)*R
    
    return np.array([dR, dS], float)


def solve(E, l):
    
    R = 0
    S = 1
    trace = []
    for r in np.arange(h, L, h):
        k1 = h*f(R, S, r, E, l)
        k2 = h*f(R+0.5*k1[0], S+0.5*k1[1], r+0.5*h, E, l)
        k3 = h*f(R+0.5*k2[0], S+0.5*k2[1], r+0.5*h, E, l)
        k4 = h*f(R+k3[0], S+k3[1], r+h, E, l)
        
        R += (k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        S += (k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        trace.append(R)
        
    return [R, trace]

def normalize_simp(R):
    n = len(R)
    integral = R[0]**2 + R[-1]**2
    for i in range(1, n, 2):
        integral += 4 * R[i]**2
    for i in range(2, n, 2):
        integral += 2 * R[i]**2
        
    return (1/3)*(h/a)*integral


def Simp(f, a, b, n):
    
    h = (b - a) / n
    integral = f(a)**2 + f(b)**2
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)**2
    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)**2
    
    return (1/3) * h * integral


def R_1_0(r):
    c = 1/(np.sqrt(np.pi) * a**(3/2))
    return c * np.exp(-r/a)

def R_2_0(r):
    c = (2-r/a)/(4*np.sqrt(2*np.pi)*a**(3/2))
    return c*np.exp(-r/(2*a))

def R_2_1(r):
    c = (r/a)/(4*np.sqrt(2*np.pi)*a**(3/2))
    return c*np.exp(-r/(2*a))