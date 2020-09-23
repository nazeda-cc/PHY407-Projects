# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:00:08 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from matplotlib import pyplot as plt
from Lab2_Q2b_function import *

######################## b i #################################################
x = np.arange(0, 20, 0.1)
y0 = []                     #initiate arraysfor J0, J1, J2
y1 = []
y2 = []

for i in x:                 #Calculate values for J0
    y0.append(J(0, i))
    
for i in x:                 #Calculate values for J0
    y1.append(J(1, i))

for i in x:                 #Calculate values for J0
    y2.append(J(2, i))

#plot
plt.figure(1)
plt.plot(x, y0, label = '$J_0$')
plt.plot(x, y1, label = '$J_1$')
plt.plot(x, y2, label = '$J_2$')
plt.xlabel('$x$')
plt.ylabel('$J_m(x)$')
plt.legend()
plt.title('Q2b, plot of $J_0$, $J_1$, and $J_2$, textbood Ex5.4(a)')
##############################################################################

######################## b ii ################################################
x = np.arange(0, 20, 0.1)
y0 = []
y1 = []

for i in x:                 #Calculate values for J0, with my own bessel func.
    y0.append(J(0, i))

#Plot against scipy.special.jv(0,x)
plt.figure(2)
plt.plot(x, special.jv(0, x), label = 'scipy.special.jv(0,x)') #calculate & plot with scipy special func.
plt.plot(x, y0, label = 'My function J(0,x)')
plt.xlabel('$x$')
plt.ylabel('$J_0(x)$')
plt.legend()
plt.title('Comparison between my bessel and scipy.special.jv, for $J_0(x)$')
plt.show()

for i in x:                 #Calculate values for J1, with my own bessel func.
    y1.append(J(1, i))

#Plot against scipy.special.jv(1,x)
plt.figure(3)
plt.plot(x, special.jv(1, x), label = 'scipy.special.jv(1,x)')  #calculate & plot with scipy special func.
plt.plot(x, y1, label = 'My function J(1,x)')
plt.xlabel('$x$')
plt.ylabel('$J_1(x)$')
plt.legend()
plt.title('Comparison between my bessel and scipy.special.jv, for $J_1(x)$')
plt.show()    
##############################################################################


########################### b iii ############################################
#set parameters' unit in meter
lam = 500e-9
k = 2 * np.pi / lam

#calculate light insensity from r = 0nm to r = 1500nm
r = np.arange(0,1500)
I_r = [0.25]        #pre assign value for r = 0, since program does not perform well for limits
for i in range(1, 1500):
    I_r.append((J(1, k*i*1e-9) / (k*i*1e-9)) ** 2)


#generate the mesh grid
P = np.ones([2001,2001], float)*0   #initiate a 2001 by 2001 matrix, so it can cover -1um to 1um
for i in range(0,2001):
    for j in range(0,2001):
        radius = int(np.sqrt((i-1000)**2 + (j-1000)**2))    #calculate the radius for each point on the grid
        P[i][j] = I_r[radius]                   #simply assign light intensity to the point according to the radius
                                                #because of symmetry. tones of times saved!
        


plt.figure(figsize = (10,8))  
x = np.arange(-1000, 1001, 1)       #create axies for the plot
y = np.arange(-1000, 1001, 1)    
c = plt.pcolormesh(x, y, P, vmax = 0.01, shading='nearest')    #set max intensity at 0.01 for best sensitivity
plt.colorbar(c, label = 'Light Intensity')
plt.xlabel('$nm$')
plt.ylabel('$nm$')
plt.title('Q2b Diffraction Plot with pcolormesh')
plt.show()
