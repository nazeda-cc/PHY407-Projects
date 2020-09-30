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
plt.title('Lake Geneva altitude contour plot')
plt.show()

#imshow
plt.figure('imshow', figsize = (12, 9))
plt.imshow(w, extent = [6, 7, 46, 47], cmap = 'terrain', vmax = 3200, vmin = 400)
plt.colorbar(label = 'Altitude (m)')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Lake Geneva altitude smoooooth plot')
plt.show()



grad = gradient(w, h)


phi = np.pi / 6
intens = intensity(grad, phi)

plt.figure('intensity', figsize = (12, 9))        
plt.imshow(intens, vmax = 0.01, vmin = -0.01, extent = [6, 7, 46, 47], cmap = 'gray')
plt.colorbar(label = '\'Intensity\'')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Relief map plot, light from northeast')
plt.show()

###### zoom for geneva & cern ############################
geneva_w = np.ones([480,480], float)*0
geneva_intens = np.ones([480,480], float)*0

for i in range(0,480):
    for j in range(0,480):
        geneva_w[i][j] = w[720+i][j]
        geneva_intens[i][j] = intens[720+i][j]

long_geneva = np.linspace(6, 6.4, 480)
lat_geneva = np.linspace(46.4, 46, 480)

plt.figure('Geneva_contour', figsize = (8, 6))        
plt.contourf(long_geneva, lat_geneva, geneva_w, cmap = 'terrain')
plt.colorbar(label = 'Altitude (m)')
plt.scatter(6.14, 46.2, c = 'r', s = 100)
plt.text(6.16, 46.2, 'Geneva', fontsize = 15, color = 'w')
plt.scatter(6.06, 46.25, c = 'r', s = 100)
plt.text(6.08, 46.25, 'CERN', fontsize = 15, color = 'w')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Zoomed contour plot for Geneva & CERN')
plt.show()

plt.figure('Geneva_smoooth', figsize = (8,6))
plt.imshow(geneva_w, extent = [6, 6.4, 46, 46.4], cmap = 'terrain')
plt.colorbar(label = 'Altitude (m)')
plt.scatter(6.14, 46.2, c = 'r', s = 100)
plt.text(6.16, 46.2, 'Geneva', fontsize = 15, color = 'w')
plt.scatter(6.06, 46.25, c = 'r', s = 100)
plt.text(6.08, 46.25, 'CERN', fontsize = 15, color = 'w')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Zoomed smooooth altitude plot for Geneva & CERN')
plt.show()

plt.figure('Geneva_relief', figsize = (8,6))
plt.imshow(geneva_intens, extent = [6, 6.4, 46, 46.4], cmap = 'gray', vmax = 0.01, vmin = -0.01)
plt.colorbar(label = '\'Intensity\'')
plt.scatter(6.14, 46.2, c = 'r', s = 100)
plt.text(6.16, 46.2, 'Geneva', fontsize = 15, color = 'w')
plt.scatter(6.06, 46.25, c = 'r', s = 100)
plt.text(6.08, 46.25, 'CERN', fontsize = 15, color = 'w')
plt.title('Zoomed releaf map plot for Geneva & CERN')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.show()
###########################################################

##############zoom for lausanne & evian######################
laus_w = np.ones([480,480], float)*0
laus_intens = np.ones([480,480], float)*0

for i in range(0,480):
    for j in range(0,480):
        laus_w[i][j] = w[360+i][480+j]
        laus_intens[i][j] = intens[360+i][480+j]

long_laus = np.linspace(6.4, 6.8, 480)
lat_laus = np.linspace(46.7, 46.3, 480)
                
plt.figure('Lausanne_contour', figsize = (8, 6))          
plt.contourf(long_laus, lat_laus, laus_w, cmap = 'terrain') 
plt.colorbar(label = 'Altitude (m)')
plt.scatter(6.61, 46.52, c = 'r', s = 100)
plt.text(6.63, 46.52, 'Lausanne', fontsize = 15, color = 'w')
plt.scatter(6.59, 46.4, c = 'r', s = 100)
plt.text(6.61, 46.4, 'Evian', fontsize = 15, color = 'w')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Zoomed contour plot for Lausanne and Elvian')
plt.show()


plt.figure('Lausanne_smoooth', figsize = (8, 6))
plt.imshow(laus_w, extent = [6.4, 6.8, 46.3, 46.7], cmap = 'terrain')
plt.colorbar(label = 'Altitude (m)')
plt.scatter(6.61, 46.52, c = 'r', s = 100)
plt.text(6.63, 46.52, 'Lausanne', fontsize = 15, color = 'w')
plt.scatter(6.59, 46.4, c = 'r', s = 100)
plt.text(6.61, 46.4, 'Evian', fontsize = 15, color = 'w')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Zoomed smoooooth altitude plot for Lausanne and Elvian')
plt.show()

plt.figure('Lausanne_relief', figsize = (8, 6))
plt.imshow(laus_intens, extent = [6.4, 6.8, 46.3, 46.7], cmap = 'gray', vmax = 0.01, vmin = -0.01)
plt.colorbar(label = '\'Intensity\'')
plt.scatter(6.61, 46.52, c = 'r', s = 100)
plt.text(6.63, 46.52, 'Lausanne', fontsize = 15, color = 'w')
plt.scatter(6.59, 46.4, c = 'r', s = 100)
plt.text(6.61, 46.4, 'Evian', fontsize = 15, color = 'w')
plt.xlabel('Longitude, $^{\circ} E$', fontsize  = 15)
plt.ylabel('Latitude, $^{\circ} N$', fontsize  = 15)
plt.title('Zoomed relief map plot for Lausanne and Elvian')
plt.show()
####################################################################