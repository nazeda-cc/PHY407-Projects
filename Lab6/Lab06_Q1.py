# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 03:23:06 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
from Lab06_Q1functions import f
plt.rcParams.update({'font.size': 16})

# define step size
h = 0.01
# define array for time points
tpoints = np.arange(0, 10, h)

# initial positions and velocities
vx0 = 0
vy0 = 1
x0 = 1
y0 = 0
# arrays for positions and velocities
xpoints = [x0]
ypoints = [y0]

# array for current state of the system (x, y, vx, vy)
r = np.array([x0, y0, vx0, vy0], float)

# iterate over time points to perform the RK4 calculations
for t in tpoints:
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6
    
    # save positions
    xpoints.append(r[0])
    ypoints.append(r[1])
    
# visualize the orbit
plt.figure(figsize=(8, 8))
plt.plot(xpoints, ypoints, lw=3)
plt.scatter(x0, y0, c='k', marker='x', s=500, label='Initial position')
plt.grid()
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
