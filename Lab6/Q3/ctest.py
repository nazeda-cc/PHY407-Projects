# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:20:53 2020

@author: rundo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:54:09 2020

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

################## Initiate the grid and 8 imaginary girds ####################
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
#############################################################################

######################## Plot initial grid ####################################
index = np.arange(0, 144, 16)
color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#d62728', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
mark = [None, None,None,None,'D',None,None,None,None]
siz = [None, None,None,None,60,None,None,None,None]
lab = [None, None,None,None, 'Inner most tile',None,None,None,None]
plt.figure(figsize = (10, 10))
for i in range(0, 9):
    plt.scatter(x_initial[index[i]:index[i]+16], y_initial[index[i]:index[i]+16]
                , c = color[i], marker = mark[i], s=siz[i], label = lab[i])
#plt.legend()
plt.xlabel('$x$ axis', fontsize = 18)
plt.ylabel('$y$ axis', fontsize = 18)
plt.title('Q3c, Initial condition with 8 shifted images', fontsize = 18)
plt.show()
#############################################################################

############################## Start iteration #################################
#initial trace list
x_points = []
y_points = []

#set iteration steps
h = 0.01
tpoints = np.arange(0, 10, h)


#append initial conditions
for i in range(0, 144):
    x_points.append([])
    x_points[i].append(x_initial[i])
    y_points.append([])
    y_points[i].append(y_initial[i])

#initial v(t) and v(t+0.5h)
vx = np.zeros(144, float)
vy = np.zeros(144, float)

vx_half = np.zeros(144, float)
vy_half = np.zeros(144, float)


x = x_initial
y = y_initial

#calculate the first v(t+0.5h)
dvx, dvy = f_ca(x_initial, y_initial)
for i in range(144):
    vx_half[i] += 0.5 * h * dvx[i]
    vy_half[i] += 0.5 * h * dvy[i]

#iteration begins   
for t in tpoints:
    for i in range(144):

        x[i] = x[i] + h * vx_half[i]
        y[i] = y[i] + h * vy_half[i]
        
        
    kx, ky = f_ca(x, y)
    for i in range(16):
        x[i+64] = np.mod(x[i+64], 4)
        y[i+64] = np.mod(y[i+64], 4)
    
    #update 8 imaginary shifted tiles
    for i in range(N):
        x[i] = x[i+64] - 4
        x[i+16] = x[i+64]
        x[i+32] = x[i+64] + 4
        x[i+48] = x[i+64] - 4
        x[i+80] = x[i+64] + 4
        x[i+96] = x[i+64] - 4
        x[i+112] = x[i+64]
        x[i+128] = x[i+64] + 4
        
        y[i] = y[i+64] - 4
        y[i+16] = y[i+64] - 4
        y[i+32] = y[i+64] - 4
        y[i+48] = y[i+64]
        y[i+80] = y[i+64]
        y[i+96] = y[i+64] + 4
        y[i+112] = y[i+64] + 4
        y[i+128] = y[i+64] + 4
    
    
    kx[:] = kx[:] * h
    ky[:] = ky[:] * h
    
    for i in range(144):
        vx[i] = vx_half[i] + 0.5*kx[i]
        vy[i] = vy_half[i] + 0.5*ky[i]
        
        vx_half[i] += kx[i]
        vy_half[i] += ky[i]
        
        x_points[i].append(x[i])
        y_points[i].append(y[i])

plt.figure(figsize=(10, 10))
for i in range(N):
    plt.plot(x_points[i+64], y_points[i+64])
    

plt.xlabel('$x$ axis', fontsize = 18)
plt.ylabel('$y$ axis', fontsize = 18)
plt.title('Q3c, Trajectories of 16 particles in the inner most tile', fontsize = 18)
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.show()
















