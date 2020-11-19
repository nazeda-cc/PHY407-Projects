# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:08:10 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab09_Q2functions import *


P = 16
Lx = 1
Ly = 1
tau = 0.01
N = 2000
T = N * tau
J0 = 1
m = 1
n = 1
c = 1
omega = 3.75

x = np.linspace(0, Lx, P)
y = np.linspace(0, Ly, P)

x_points, y_points = np.meshgrid(x, y)

Jz = np.zeros((P, P))
Hx = np.zeros((P, P))
Hy = np.zeros((P, P))
E = np.zeros((P, P))

Jz_new = np.zeros((P, P))
Hx_new = np.zeros((P, P))
Hy_new = np.zeros((P, P))
E_new = np.zeros((P, P))

X_new = np.zeros((P, P))
Y_new = np.zeros((P, P))
Ehat_new = np.zeros((P, P))
J_new = np.zeros((P, P))

Hx_trace = []
Hy_trace = []
E_trace = []

E_max = []

time =   np.arange(0, T+tau, tau) 

Dx = np.pi*c*tau / (2*Lx)
Dy = np.pi*c*tau / (2*Ly)
#plt.figure(figsize = (8, 6))
E_max_trace = []
d_omega = 0.1

for omega in np.arange(0,9+d_omega, d_omega):
    #E_trace = []
    
    
    Jz = np.zeros((P, P))
    Hx = np.zeros((P, P))
    Hy = np.zeros((P, P))
    E = np.zeros((P, P))

    Jz_new = np.zeros((P, P))
    Hx_new = np.zeros((P, P))
    Hy_new = np.zeros((P, P))
    E_new = np.zeros((P, P))

    X_new = np.zeros((P, P))
    Y_new = np.zeros((P, P))
    Ehat_new = np.zeros((P, P))
    J_new = np.zeros((P, P))
    
    Emax = 0
    
    print(omega)
    for t in time:
    
    
        Jz = J0 * np.sin(m*np.pi*x_points/Lx) * np.sin(n*np.pi*y_points/Ly)*np.sin(omega*t)
    
        X = dHxt2(Hx)
        Y = dHyt2(Hy)
        Ehat = dst2(E)
        J = dst2(Jz)

        for q in range(P):
            for p in range(P):
                Ehat_new[q][p] = ((1 - (p**2)*(Dx**2) - (q**2)*(Dy**2)) * Ehat[q][p] \
                                  + 2*q*Dy*X[q][p] + 2*p*Dx*Y[q][p] + tau * J[q][p]) / (1 + \
                                    (p**2)*(Dx**2) + (q**2)*(Dy**2))
                                                                      
                X_new[q][p] = X[q][p] - q*Dy*(Ehat_new[q][p] + Ehat[q][p])
                Y_new[q][p] = Y[q][p] - p*Dx*(Ehat_new[q][p] + Ehat[q][p])
            
    
        E = idst2(Ehat_new)
        Hx = idHxt2(X_new)
        Hy = idHyt2(Y_new)
    
        if abs(E[P//2][P//2]) > Emax:
            Emax = E[P//2][P//2]
        
        #E_trace.append(E[P//2][P//2])
    
    #print(len(E_trace))
    E_max_trace.append(abs(Emax))
    print(E_max_trace[-1])
    
    

    
    #plt.pcolormesh(x, y, E)
    #plt.colorbar()
    #plt.show()

plt.figure(figsize = (8,8))
plt.plot(np.arange(0,9+d_omega,d_omega), E_max_trace)
plt.xlabel('Driven frequency ($\omega$)')
plt.ylabel('$Maximum apmplitude |E_z|_{max}$')
plt.title('Q2d, Maximum apmplitude vs Driven frequency plot')
plt.grid(True)
plt.show()

''' 
plt.figure(figsize = (6, 6))
plt.plot(time, Hx_trace, label = 'Hx')
plt.plot(time, Hy_trace, label = 'Hy')
plt.plot(time, E_trace, label = 'E')
plt.legend()
plt.show()
'''