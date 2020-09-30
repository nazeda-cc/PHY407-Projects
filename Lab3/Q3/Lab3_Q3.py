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


geneva = [46.2, 6.12]
cern = [46.25, 6.06]
Lausanne = [46.52, 6.61]
evian = [46.4, 6.59]

geneva_grid = [0, 0]
geneva_grid[0] = int((47 - geneva[0]) * 1200)
geneva_grid[1] = int((geneva[1] - 6) * 1200)





w = read_and_show(file)
#contour plot
plt.figure('contour', figsize = (12, 9))
latitude = np.linspace(47, 46, 1201)
longitude = np.linspace(6, 7, 1201)
plt.contourf(longitude, latitude, w, cmap = 'terrain', vmax = 3200, vmin = 400)
plt.colorbar(label = 'Altitude (m)')

plt.scatter(6.14, 46.2, c = 'r', s = 150)
plt.text(6.16, 46.2, 'Geneva', fontsize = 17, color = 'w')

plt.scatter(6.06, 46.25, c = 'r', s = 150)
plt.text(6.08, 46.25, 'CERN', fontsize = 17, color = 'w')

plt.scatter(6.61, 46.52, c = 'r', s = 150)
plt.text(6.63, 46.52, 'Lausanne', fontsize = 17, color = 'w')

plt.scatter(6.59, 46.4, c = 'r', s = 150)
plt.text(6.61, 46.4, 'Evian', fontsize = 17, color = 'w')


plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Lake Geneva contour plot')
plt.show()

#imshow
plt.figure('imshow', figsize = (12, 9))
plt.imshow(w, extent = [6, 7, 46, 47], cmap = 'terrain', vmax = 3200, vmin = 400)
plt.colorbar(label = 'Altitude (m)')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Lake Geneva more delicate plot')
plt.show()



grad = gradient(w, h)


phi = np.pi / 6
intens = intensity(grad, phi)

plt.figure('intensity', figsize = (12, 9))        
plt.imshow(intens, vmax = 0.01, vmin = -0.01, extent = [6, 7, 46, 47], cmap = 'gray')
plt.colorbar(label = 'Intensity')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Light intensity plot from southwest')
plt.show()





'''
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
plt.contourf(geneva_w, origin='upper', cmap = 'terrain', vmax = 3200, vmin = 400)
plt.show()

plt.figure(4)
plt.imshow(geneva_intensity, cmap = 'gray', extent = [6.04, 6.2, 46.12, 46.29])
plt.show
'''

                
                
                
                
                
                
                
                            
