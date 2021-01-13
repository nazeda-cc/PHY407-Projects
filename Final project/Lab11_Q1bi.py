# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:52:59 2020

@author: rundo
"""
import numpy as np
from numpy import random
from matplotlib import pyplot as plt


def gauss(sigma):
    r = np.sqrt(-2*sigma*sigma*np.log(1-random.random()))
    theta = 2*np.pi*random.random()
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    return x, y

def f(x, y):
    
    return x**2 - np.cos(4*np.pi*x) + (y-1)**2

Tmax = 100.0
Tmin = 1e-5
tau = 1e4

x = 2
y = 2

x_trace = [x]
y_trace = [y]

t = 0
T = Tmax
T_trace = [T]
while T > Tmin:
    
    t += 1
    T = Tmax * np.exp(-t/tau)
    
    
    
    dx, dy = gauss(1)
    
    old_f = f(x, y)
    
    x += dx
    y += dy
    
    diff = f(x, y) - old_f
    
    if random.random() > np.exp(-diff/T):
        x -= dx
        y -= dy
        
    if t%500==0:
        x_trace.append(x)
        y_trace.append(y)
        T_trace.append(T)
    
print('Optimized x value is:', x)
print('Optimized y value is:', y)
plt.figure()
plt.plot(T_trace, x_trace, '.')
plt.axis([Tmax, Tmin, min(x_trace)+1, max(x_trace)-1])
plt.xlabel('Temperature')
plt.ylabel('x value')
plt.title('Q1b i, x value while the system is cooling')
plt.semilogx()



plt.figure()
plt.plot(T_trace, y_trace, '.')
plt.axis([Tmax, Tmin, min(y_trace)+1, max(y_trace)-1])
plt.xlabel('Temperature')
plt.ylabel('y value')
plt.title('Q1b i, y value while the system is cooling')
plt.semilogx()