# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:54:09 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab06_Q3function import *
#np.seterr(divide='ignore', invalid='ignore')
N = 16
Lx = 4.0
Ly = 4.0

dx = Lx/np.sqrt(N)
dy = Ly/np.sqrt(N)


x_grid = np.arange(dx/2 - 4, Lx - 4, dx)
y_grid = np.arange(dy/2 - 4, Ly - 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = xx_grid.flatten()
y_initial = yy_grid.flatten()
#########
x_grid = np.arange(dx/2 , Lx , dx)
y_grid = np.arange(dy/2 - 4, Ly - 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
#####
x_grid = np.arange(dx/2 + 4, Lx + 4, dx)
y_grid = np.arange(dy/2 - 4, Ly - 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
###########
x_grid = np.arange(dx/2 - 4, Lx - 4, dx)
y_grid = np.arange(dy/2, Ly, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
#################
x_grid = np.arange(dx/2, Lx, dx)
y_grid = np.arange(dy/2, Ly, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
##################
x_grid = np.arange(dx/2 + 4, Lx + 4, dx)
y_grid = np.arange(dy/2, Ly, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
######################
x_grid = np.arange(dx/2 - 4, Lx - 4, dx)
y_grid = np.arange(dy/2 + 4, Ly + 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
##########################
x_grid = np.arange(dx/2 , Lx , dx)
y_grid = np.arange(dy/2 + 4, Ly + 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())
############################
x_grid = np.arange(dx/2 + 4, Lx + 4, dx)
y_grid = np.arange(dy/2 + 4, Ly + 4, dy)
xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)
x_initial = np.append(x_initial, xx_grid.flatten())
y_initial = np.append(y_initial, yy_grid.flatten())

index = np.arange(0, 144, 16)
color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for i in range(0, 9):
    plt.scatter(x_initial[index[i]:index[i]+16], y_initial[index[i]:index[i]+16], c = color[i])

#initial trace list
x_points = []
y_points = []

for i in range(0, N):
    x_points.append([])
    x_points[i].append(x_initial[i+64])
    y_points.append([])
    y_points[i].append(y_initial[i+64])

#fx, fy = f(x_initial, y_initial)

h = 0.01
tpoints = np.arange(0, 10, h)

vx = np.zeros(N, float)
vy = np.zeros(N, float)

vx_half = np.zeros(N, float)
vy_half = np.zeros(N, float)

x = x_initial
y = y_initial


dvx, dvy = f_c(x_initial, y_initial)
for i in range(N):
    vx_half[i] += 0.5 * h * dvx[i]
    vy_half[i] += 0.5 * h * dvy[i]
    #x[i] = x_points[i][-1]
    #y[i] = y_points[i][-1]
    
for t in tpoints:
    for i in range(N):
        #x[i] = x_points[i][-1]
        #y[i] = y_points[i][-1]
        
        x[i+64] = np.mod(x[i+64] + h * vx_half[i], 4)
        y[i+64] = np.mod(y[i+64] + h * vy_half[i], 4)
        
        x_points[i].append(x[i + 64])
        y_points[i].append(y[i + 64])
    
    for i in range(N):
        x[i] = x[i+64] - 4
        x[i+32] = x[i+64] + 4
        x[i+48] = x[i+64] - 4
        x[i+80] = x[i+64] + 4
        x[i+96] = x[i+64] - 4
        x[i+128] = x[i+64] + 4
        
        y[i] = y[i+64] - 4
        y[i+16] = y[i+64] - 4
        y[i+32] = y[i+64] - 4
        y[i+96] = y[i+64] + 4
        y[i+112] = y[i+64] + 4
        y[i+128] = y[i+64] + 4
        
        
    kx = h * f_c(x, y)[0][:]
    ky = h * f_c(x, y)[1][:]
    
    for i in range(N):
        vx[i] = vx_half[i] + 0.5*kx[i]
        vy[i] = vy_half[i] + 0.5*ky[i]
        
        vx_half[i] += kx[i]
        vy_half[i] += ky[i]


plt.figure(figsize=(8, 8))
for i in range(N):
    plt.plot(x_points[i], y_points[i])
#plt.legend()
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.show()
















