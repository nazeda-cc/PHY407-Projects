# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:44:06 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q2_function import Population as popu


###Q2c##############
p = 100
x_1 = popu(0.1, 2, p)
x_2 = popu(0.1, 2.5, p)
x_3 = popu(0.1, 3, p)
x_4 = popu(0.1, 3.5, p)
x_5 = popu(0.1, 4, p)

year = np.linspace(0,99,num=100)

plt.figure(figsize = (20,10))

plt.plot(year,x_1, label='r=2', linewidth=1)
plt.plot(year,x_2, label='r=2.5', linewidth=1)
plt.plot(year,x_3, label='r=3', linewidth=1)
plt.plot(year,x_4, label='r=3.5', linewidth=1)
plt.plot(year,x_5, label='r=4', linewidth=1)
plt.legend()
plt.xlabel('p (years)')
plt.ylabel('x')
plt.title('Q2c Population Evolution History with different r')
####################



###Q2d inc = 0.1####
p = 2000
x = []
r = np.arange(2, 4.1, 0.1)
for i in r:
    x.append(popu(0.1, i, p))           #iteration for each r

s = [[],[]]

for i in range(0, 10):                  #r<3, only plot last 100
    for j  in np.arange(1999,1900,-1):
        s[0].append(r[i])
        s[1].append(x[i][j])

for i in range(10, 20):
    for j  in np.arange(1999,1000,-1):  #r>=3, plot last 1000
        s[0].append(r[i])
        s[1].append(x[i][j])
        
plt.figure(1)
plt.plot(s[0],s[1], 'k.', markersize = 0.1)
plt.title('$x_p$ vs r plot (increment = 0.1)')
plt.xlabel('r')
plt.ylabel('$x_p$')
########################

###Q2d inc = 0.005#######
p = 2000
x = []
r = np.arange(2, 4.005, 0.005)
for i in r:
    x.append(popu(0.1, i, p))               #iteration for each r

s = [[],[]]

for i in r:
    ind = np.where(r==i)[0][0]
    if i < 3:                               #r<3, only plot last 100
        for j  in np.arange(1999,1900,-1):
            s[0].append(i)
            s[1].append(x[ind][j])
    else:
                                            #r>=3, plot last 1000
        for j  in np.arange(1999,1000,-1):
            s[0].append(i)
            s[1].append(x[ind][j])
        
plt.figure(2)
plt.plot(s[0],s[1], 'k.', markersize = 0.05)
plt.title('$x_p$ vs r plot (increment = 0.005)')
plt.xlabel('r')
plt.ylabel('$x_p$')

###Q2e inc = 10e-5#######
p = 2000
x = []
r = np.arange(3.738, 3.745, 0.00001)
for i in r:
    x.append(popu(0.1, i, p))               #iteration for each r

s = [[],[]]

for i in r:
    ind = np.where(r==i)[0][0]
    for j  in np.arange(1999,1000,-1):
        s[0].append(i)
        s[1].append(x[ind][j])
        
plt.figure(3)
plt.plot(s[0],s[1], 'k.', markersize = 0.05)
plt.title('$x_p$ vs r plot (increment = $10^{-5}$)')
plt.xlabel('r')
plt.ylabel('$x_p$')
##########################
plt.shwo()

