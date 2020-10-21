# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:46:09 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab06_Q3function import *


N = 16
Lx = 4.0
Ly = 4.0

dx = Lx/np.sqrt(N)
dy = Ly/np.sqrt(N)

x_grid = np.arange(dx/2, Lx, dx)
y_grid = np.arange(dy/2, Ly, dy)

xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)

x_initial = xx_grid.flatten()
y_initial = yy_grid.flatten()

x_points = []
y_points = []

for i in range(0, N):
    x_points.append([])
    x_points[i].append(x_initial[i])
    y_points.append([])
    y_points[i].append(y_initial[i])

#fx, fy = f(x_initial, y_initial)

h = 0.01
tpoints = np.arange(0, 100, h)

vx = np.zeros(N, float)
vy = np.zeros(N, float)

vx_half = np.zeros(N, float)
vy_half = np.zeros(N, float)

x = np.zeros(N, float)
y = np.zeros(N, float)


dvx, dvy = f(x_initial, y_initial)
for i in range(N):
    vx_half[i] += 0.5 * h * dvx[i]
    vy_half[i] += 0.5 * h * dvy[i]
    x[i] = x_points[i][-1]
    y[i] = y_points[i][-1]

uenergy = []
kenergy = []
    
for t in tpoints:
    for i in range(N):
        #x[i] = x_points[i][-1]
        #y[i] = y_points[i][-1]
        
        x[i] += h * vx_half[i]
        y[i] += h * vy_half[i]
        
        x_points[i].append(x[i])
        y_points[i].append(y[i])
    
    
    kx = h * f(x, y)[0][:]
    ky = h * f(x, y)[1][:]
    
    for i in range(N):
        vx[i] = vx_half[i] + 0.5*kx[i]
        vy[i] = vy_half[i] + 0.5*ky[i]
        
        vx_half[i] += kx[i]
        vy_half[i] += ky[i]
       
    uenergy.append(u(x, y))
    kenergy.append(k_energy(vx, vy))
    

total = []
for i in range(len(uenergy)):
    total.append(uenergy[i]+kenergy[i])

plt.figure()
for i in range(N):
    plt.plot(x_points[i], y_points[i])
#plt.legend()
#plt.xlim(-8, 12)
#plt.ylim(-8, 12)
plt.show()

plt.figure()
plt.plot(uenergy)
plt.plot(kenergy)
plt.plot(total)
plt.show()
    
    
    

    
    
    
    
    
    
    
    