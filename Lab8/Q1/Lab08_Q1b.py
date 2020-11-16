# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 03:23:06 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.rcParams.update({'font.size': 16})
from time import time

# Constants
M = 100
V1 = 1.
V2 = -1.
target = 1e-6

# define overrelaxation rate
omega = 0.99

# Create arrays to hold potential values
phi = np.zeros([M+1, M+1], float)
# define boundary conditions for the two charged panels
phi[20:80, 20] = V1
phi[20:80, 80] = V2
phiprime = np.empty([M+1, M+1], float)

# Main loop
delta = 1.
# Record start time
startclock = time()
while delta > target:

    # archive old states
    phiold = phi.copy()
    
    for i in range(1, M):
        for j in range(1, M):
            if i == 0 or i == M or j == 0 or j == M: # grounded box bdry condition
                phi[i, j] = phi[i, j]
            elif (j == 20 or j == 80) and (i>=20 and i<=80): # charged panels
                phi[i, j] = phi[i, j]
            else:
                phi[i, j] = (1+omega)*(phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1])/4 - omega*phi[i, j]

    # compute current accuracy
    delta = np. max(np.abs(phi-phiold))
    

# Get end time and print running time
endclock = time()
time_clock = endclock - startclock
print('Gauss-Seidel with overrelaxation (omega=%.1f) took %f seconds' % (omega, time_clock))

# contour levels
levels = np.linspace(-1., 1., 20)

fig, ax = plt.subplots(figsize=(10, 10))

# grid locations
xx = yy = np.arange(0, M+1, 1)

# add contour lines and label the contour lines
CS = plt.contour(xx, yy, phi, levels=levels, cmap=plt.cm.viridis, linewidths=2, linestyles='dashed')
plt.clabel(CS, inline=True, fontsize=15)

plt.title("Potential fields of parallel charged planes in a grounded box\nGauss-Seidei with overrelaxation rate $\omega=%.1f$"%omega)
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')

# calculate electric field
x, y = np.meshgrid(xx, yy)
Ey, Ex = np.gradient(-phi, yy, xx)
strm = ax.streamplot(x, y, Ex, Ey, color=phi, linewidth=3, cmap=plt.cm.viridis, density=0.3, arrowsize=5)

# generate continuous colorbar
norm = mpl.colors.Normalize(vmin=CS.cvalues.min(), vmax=CS.cvalues.max())
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
sm = plt.cm.ScalarMappable(norm=norm, cmap = CS.cmap)
sm.set_array([])
fig.colorbar(sm, orientation='vertical', cax=cax, label='Potential (V)')

plt.show()