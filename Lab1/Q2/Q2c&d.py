# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:44:06 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q2_function import Population as popu

'''
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
####################
'''

'''
###Q2d inc = 0.1####
p = 2000
x = []
r = np.arange(2, 4.1, 0.1)
for i in r:
    x.append(popu(0.1, i, p))

s = [[],[]]

for i in range(0, 10):
    for j  in np.arange(1999,1900,-1):
        s[0].append(r[i])
        s[1].append(x[i][j])

for i in range(10, 20):
    for j  in np.arange(1999,1000,-1):
        s[0].append(r[i])
        s[1].append(x[i][j])
        

plt.plot(s[0],s[1], 'k.', markersize = 0.1)
plt.title('$x_p$ vs r plot (increment = 0.1)')
plt.xlabel('r')
plt.ylabel('$x_p$')
########################
'''
###Q2d inc = 0.005#######
p = 2000
x = []
r = np.arange(2, 4.005, 0.005)
for i in r:
    x.append(popu(0.1, i, p))

s = [[],[]]

for i in r:
    ind = np.where(r==i)[0][0]
    if i < 3:
        for j  in np.arange(1999,1900,-1):
            s[0].append(i)
            s[1].append(x[ind][j])
    else:

        for j  in np.arange(1999,1000,-1):
            s[0].append(i)
            s[1].append(x[ind][j])
        

plt.plot(s[0],s[1], 'k.', markersize = 0.05)
plt.title('$x_p$ vs r plot (increment = 0.005)')
plt.xlabel('r')
plt.ylabel('$x_p$')



