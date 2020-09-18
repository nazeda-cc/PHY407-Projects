# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:45:59 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
def Euler_Cromer(x_0, y_0, vx_0, vy_0, d_t, t):

    M_s = 2*(10**30)
    steps = int(t / d_t)    #calculate total number of steps
    x = [None]*steps        #initialize arrays
    y = [None]*steps
    vx = [None]*steps
    vy = [None]*steps
    x[0] = x_0              #take initial values
    y[0] = y_0
    vx[0] = vx_0
    vy[0] = vy_0
    for i in range(0, steps-1):             #Euler Cromer method
        r = np.sqrt(x[i] ** 2 + y[i] ** 2)  #calculate r
        x[i+1] = x[i] + vx[i] * d_t
        vx[i+1] = vx[i] - spc.G * M_s * x[i+1] * d_t / r**3
        y[i+1] = y[i] + vy[i] * d_t
        vy[i+1] = vy[i] - spc.G * M_s * y[i+1] * d_t / r**3

    return x, y, vx, vy

def Euler_Cromer_GR(x_0, y_0, vx_0, vy_0, d_t, t):

    M_s = 2*(10**30)
    a = 0.01 * spc.au**2
    steps = int(t / d_t)    #calculate total number of steps
    x = [None]*steps        #initialize arrays
    y = [None]*steps
    vx = [None]*steps
    vy = [None]*steps
    x[0] = x_0              #take initial values
    y[0] = y_0
    vx[0] = vx_0
    vy[0] = vy_0
    for i in range(0, steps-1):             #Euler Cromer method
        r = np.sqrt(x[i] ** 2 + y[i] ** 2)  #calculate r
        x[i+1] = x[i] + vx[i] * d_t
        vx[i+1] = vx[i] - (1 + a/r**2) * spc.G * M_s * x[i+1] * d_t / r**3
        y[i+1] = y[i] + vy[i] * d_t
        vy[i+1] = vy[i] - (1 + a/r**2) * spc.G * M_s * y[i+1] * d_t / r**3

    return x, y, vx, vy