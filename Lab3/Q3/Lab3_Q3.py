# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:06:57 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
import struct
from Lab3_Q3_function import *

file = 'N46E006.hgt'

h = 420

w = read_and_show(file)

plt.figure(1, figsize = (12, 9))
plt.imshow(w, extent = [6, 7, 46, 47])
plt.colorbar(label = 'Altitude (m)')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.show()

grad = gradient(w, h)


phi = - 5 * np.pi / 6
intens = intensity(grad, phi)

plt.figure(2, figsize = (12, 9))        
plt.imshow(intens, vmax = 0.2, vmin = -0.2, extent = [6, 7, 46, 47])
plt.colorbar(label = 'Intensity')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.show()

location = [46.2, 6.12]
location_grid = [0, 0]
location_grid[0] = int((47 - location[0]) * 1200)
location_grid[1] = int((location[1] - 6) * 1200)
geneva_w = np.ones([200,200], float)*0
geneva_intensity = np.ones([200,200], float)*0
for i in range(0, 200):
    for j in range(0, 200):
        geneva_w[i][j] = w[location_grid[0]-100+i][location_grid[1]-100+j]
        geneva_intensity[i][j] = intens[location_grid[0]-100+i][location_grid[0]-100+j]
        
plt.figure(3)
plt.imshow(geneva_w)
plt.show()

plt.figure(4)
plt.imshow(geneva_intensity)
plt.show


                
                
                
                
                
                
                
                            
