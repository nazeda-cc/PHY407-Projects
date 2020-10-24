# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:36:36 2020

@author: rundo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:46:09 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt

#function to calculate force on each particle due to other N-1 particles
def f(x, y):
    fx = np.zeros(16, float)
    fy = np.zeros(16, float)
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                temp = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                fx[i] += temp * dx
                fy[i] += temp * dy
                
    return fx, fy


#function to calculate force on each particle in center tile due to other 9N-1 particles
def f_c(x, y):
    fx = np.zeros(16, float)
    fy = np.zeros(16, float)
    for i in range(16):
        for j in range(len(x)):
            if i+64 != j:
                dx = x[i+64] - x[j]
                dy = y[i+64] - y[j]
                temp = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                fx[i] += temp * dx
                fy[i] += temp * dy
                
    return fx, fy

#function for testing, not used
def f_ca(x, y):
    fx = np.zeros(144, float)
    fy = np.zeros(144, float)
    for i in range(144):
        for j in range(len(x)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                temp = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                fx[i] += temp * dx
                fy[i] += temp * dy
                
    return fx, fy





#potential energy
def u(x, y):
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                result += 4/(dx**2 + dy**2)**6 - 4/(dx**2 + dy**2)**3
                
                
    return result/2

#kinetic energy    
def k_energy(vx, vy):
    result = 0
    for i in range(len(vx)):
        result += 0.5 * vx[i]**2
        result += 0.5 * vy[i]**2
        
    return result


    

    
    
    
    
    
    
    
    