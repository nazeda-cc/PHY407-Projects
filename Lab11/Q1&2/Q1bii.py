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
    r = np.sqrt(-2*sigma*sigma*np.log(1-random.random()))
    theta = 2*np.pi*random.random()
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    return x, y

def f(x, y):
    
    return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x) + (y-1)**2

Tmax = 100.0
Tmin = 1e-5
tau = 1e4

x = 25
y = 0

x_trace = [x]
y_trace = [y]

t = 0
T = Tmax
T_trace = [T]
while T > Tmin:
    
    t += 1
    T = Tmax * np.exp(-t/tau)
    
    
    
    dx, dy = gauss(5)
    
    old_f = f(x, y)
    
    x += dx
    y += dy
    
    diff = f(x, y) - old_f
    
    if random.random() > np.exp(-diff/T) or x<0 or x>50 or y<-20 or y>20:
        x -= dx
        y -= dy
        
    if t%1000==0:
        x_trace.append(x)
        y_trace.append(y)
        T_trace.append(T)
    
print(x, y)
plt.figure()
plt.plot(T_trace, x_trace, '.')
plt.axis([Tmax, Tmin, max(x_trace)+1, min(x_trace)-1])
plt.semilogx()



plt.figure()
plt.plot(T_trace, y_trace, '.')
plt.axis([Tmax, Tmin, max(y_trace)+1, min(y_trace)-1])
plt.semilogx()