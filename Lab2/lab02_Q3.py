# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:08:47 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from functions_lab02_Q3 import q, I, d, qnew, I_square



###############################################################################
#############################    Part (a-d)  ##################################
###############################################################################

# step size on the screen
dx = 1e-5
# define the screen here
x = np.arange(-d/2, d/2+dx, dx)
y = np.arange(0, 0.05, 1e-4)
# this is the array for the intensity levels
Ix = np.zeros((x.shape[0]))

# calcualte invensities
for i in range(x.shape[0]):
    Ix[i] = I(x[i], q)

# convert the intensity array into a 2-d densiyt map  
dens = np.repeat(Ix[np.newaxis, :], y.shape[0], axis=0)

# visualize!
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(x, Ix, lw=3)
plt.xlim((-0.05, 0.05))
plt.grid(ls='--')
plt.ylabel(r'$\mathcal{I}(x) (W/m^2$)', fontsize=20)
plt.xlabel('x (m)', fontsize=20)
plt.subplot(2, 1, 2)
im = plt.pcolormesh(x, y, dens, cmap=cm.coolwarm)
plt.xlabel('Width of screen (m)', fontsize=17)
plt.ylabel('Height of screen (m)', fontsize=20)
divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("bottom", size="5%", pad=0.5)
plt.colorbar(im, cax=cax, orientation='horizontal', label=r'$\mathcal{I}(x) (W/m^2$)')
plt.subplots_adjust(hspace=0.1)



###############################################################################
#############################    Part (e) i ###################################
###############################################################################



# this is the array for the intensity levels
Ix = np.zeros((x.shape[0]))

# calcualte invensities
for i in range(x.shape[0]):
    Ix[i] = I(x[i], qnew)

# convert the intensity array into a 2-d densiyt map  
dens = np.repeat(Ix[np.newaxis, :], y.shape[0], axis=0)

# visualize!
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(x, Ix, lw=3)
plt.xlim((-0.05, 0.05))
plt.grid(ls='--')
plt.ylabel(r'$\mathcal{I}(x) (W/m^2$)', fontsize=20)
plt.xlabel('x (m)', fontsize=20)
plt.subplot(2, 1, 2)
im = plt.pcolormesh(x, y, dens, cmap=cm.coolwarm)
plt.xlabel('Width of screen (m)', fontsize=17)
plt.ylabel('Height of screen (m)', fontsize=20)
divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("bottom", size="5%", pad=0.5)
plt.colorbar(im, cax=cax, orientation='horizontal', label=r'$\mathcal{I}(x) (W/m^2$)')
plt.subplots_adjust(hspace=0.1)



###############################################################################
#############################   Part (e) ii  ##################################
###############################################################################


# this is the array for the intensity levels
Ix = np.zeros((x.shape[0]))

# calcualte invensities
for i in range(x.shape[0]):
    Ix[i] = I_square(x[i])

# convert the intensity array into a 2-d densiyt map  
dens = np.repeat(Ix[np.newaxis, :], y.shape[0], axis=0)

# visualize!
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(x, Ix, lw=3)
plt.xlim((-0.05, 0.05))
plt.grid(ls='--')
plt.ylabel(r'$\mathcal{I}(x) (W/m^2$)', fontsize=20)
plt.xlabel('x (m)', fontsize=20)
plt.subplot(2, 1, 2)
im = plt.pcolormesh(x, y, dens, cmap=cm.coolwarm)
plt.xlabel('Width of screen (m)', fontsize=17)
plt.ylabel('Height of screen (m)', fontsize=20)
divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("bottom", size="5%", pad=0.5)
plt.colorbar(im, cax=cax, orientation='horizontal', label=r'$\mathcal{I}(x) (W/m^2$)')
plt.subplots_adjust(hspace=0.1)