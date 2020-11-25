# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:08:10 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab09_Q2functions import *

#Set all constants
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


#initiate grids
x = np.linspace(0, Lx, P)
y = np.linspace(0, Ly, P)

x_points, y_points = np.meshgrid(x, y)


#initiate arrays for J, H, E
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

E_max_trace = []
d_omega = 0.5   #set step size for omega


#loop for all omega values
for omega in np.arange(0,9+d_omega, d_omega):

    
    #reset values of J, H, E
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
    
    #temparol loop
    for t in time:
    
    
        Jz = J0 * np.sin(m*np.pi*x_points/Lx) * np.sin(n*np.pi*y_points/Ly)*np.sin(omega*t)
    
        X = dHxt2(Hx)
        Y = dHyt2(Hy)
        Ehat = dst2(E)
        J = dst2(Jz)

        #Crank-Nicolson scheme
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
        
        #update max value
        if abs(E[P//2][P//2]) > Emax:
            Emax = E[P//2][P//2]
        
    
    #append Emax for each omega
    E_max_trace.append(abs(Emax))
    print(E_max_trace[-1])
    
    

    

#plot
plt.figure(figsize = (8,8))
plt.plot(np.arange(0,9+d_omega,d_omega), E_max_trace)
plt.xlabel('Driven frequency ($\omega$)')
plt.ylabel('$Maximum apmplitude |E_z|_{max}$')
plt.title('Q2d, Maximum apmplitude vs Driven frequency plot')
plt.grid(True)
plt.show()

