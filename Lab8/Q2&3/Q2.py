# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:18:17 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt

L = 1
J = 50
dx = L/J
dt = 0.01


g = 9.81
eta_b = 0
H = 0.01
A = 0.002
sigma = 0.05
miu = 0.5

x = np.arange(0, L+dx, dx)

u = np.zeros(J+1, float)
eta = np.zeros(J+1, float)

u_new = np.zeros(J+1, float)
eta_new = np.zeros(J+1, float)

avg = np.average(A*np.exp(-(x-miu)**2/sigma**2))
eta = H + A*np.exp(-(x-miu)**2/sigma**2) - avg



t = 0
t_end = 5

eta_0 = np.copy(eta)

t_error = 1e-5

while t <= t_end:
    for j in range(J+1):
        if j == 0:

            u_new[j] = 0
            eta_new[j] = eta[j] - (u[j+1]*eta[j+1] - u[j]*eta[j])*dt/dx
            
        elif j == J:

            u_new[j] = 0
            eta_new[j] = eta[j] - (u[j]*eta[j] - u[j-1]*eta[j-1])*dt/dx
            
        else:
            u_new[j] = u[j] - ((u[j+1]**2 - u[j-1]**2)/2 + g*(eta[j+1]-eta[j-1]))*dt/(2*dx)
            eta_new[j] = eta[j] - (u[j+1]*eta[j+1] - u[j-1]*eta[j-1])*dt/(2*dx)
            
        
    if t - 1 <= t_error:
        eta_1 = np.copy(eta)
    if t - 4 <= t_error:
        eta_4 = np.copy(eta)
    
    u = np.copy(u_new)
    eta = np.copy(eta_new)
    
    t += dt
  
plt.figure(1, figsize = (8, 8))
plt.plot(x, eta_0, label = 't=0s')
plt.plot(x, eta_1, label = 't=1s')
plt.plot(x, eta_4, label = 't=4s')
plt.ylabel('$\eta$, Free surface height (m)')
plt.xlabel('x (m)')
plt.title('Q2, Wave forms in one plot')
plt.legend()

