# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:31:25 2020

@author: rundo
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:52:59 2020

@author: rundo
"""
import numpy as np
from numpy import random
from matplotlib import pyplot as plt


def gauss(sigma):
    #My own gaussian random function
    r = np.sqrt(-2*sigma*sigma*np.log(1-random.random()))
    theta = 2*np.pi*random.random()
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    return x, y

def f(x, y):
    #Function to be optimized
    return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x) + (y-1)**2

#Set parameters
Tmax = 100.0
Tmin = 1e-6
tau = 1e4

#initial value for x and y
x = 25
y = 0

#trace for plotting
x_trace = [x]
y_trace = [y]

t = 0
T = Tmax
T_trace = [T]

#Main loop
while T > Tmin:
    
    t += 1
    T = Tmax * np.exp(-t/tau)
    
    
    
    dx, dy = gauss(5)
    
    old_f = f(x, y)
    
    x += dx
    y += dy
    
    diff = f(x, y) - old_f
    
    #Random walk and restrict in the domaine
    if random.random() > np.exp(-diff/T) or x<0 or x>50 or y<-20 or y>20:
        x -= dx
        y -= dy
    
    #Update trace every 1000 iterations
    if t%1000==0:
        x_trace.append(x)
        y_trace.append(y)
        T_trace.append(T)

#Code for plotting    
print('Optimized x value is:', x)
print('Optimized y value is:', y)
plt.figure()
plt.plot(T_trace, x_trace, '.')
plt.axis([Tmax, Tmin, min(x_trace)-1, max(x_trace)+1])
plt.xlabel('Temperature')
plt.ylabel('x value')
plt.title('Q1b ii, x value while the system is cooling')
plt.semilogx()



plt.figure()
plt.plot(T_trace, y_trace, '.')
plt.axis([Tmax, Tmin, min(y_trace)-1, max(y_trace)+1])
plt.xlabel('Temperature')
plt.ylabel('y value')
plt.title('Q1b ii, y value while the system is cooling')
plt.semilogx()