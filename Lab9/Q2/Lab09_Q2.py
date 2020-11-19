# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:18:17 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab09_Q2functions import *


P = 32
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

time =   np.arange(0, T+tau, tau) 

Dx = np.pi*c*tau / (2*Lx)
Dy = np.pi*c*tau / (2*Ly)
#plt.figure(figsize = (8, 6))
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
            
    #Jz = idst2(J_new)
    E = idst2(Ehat_new)
    Hx = idHxt2(X_new)
    Hy = idHyt2(Y_new)
    
    Hx_trace.append(Hx[0][P//2])
    Hy_trace.append(Hy[P//2][0])
    E_trace.append(E[P//2][P//2])
    
    

    
    #plt.pcolormesh(x, y, E)
    #plt.colorbar()
    #plt.show()



 
plt.figure(figsize = (6, 6))
plt.plot(time, Hx_trace, label = 'Hx')
plt.xlabel('Time ($t$)')
plt.ylabel('$H_x$')
plt.grid(True)
plt.title('Q2e, Plot of $H_x$ at (0.5, 0), $\omega = \omega_0^{1,1}$')
plt.show()

plt.figure(figsize = (6, 6))
plt.plot(time, Hy_trace, label = 'Hy')
plt.xlabel('Time ($t$)')
plt.ylabel('$H_y$')
plt.title('Q2e, Plot of $H_y$ at (0, 0.5), $\omega = \omega_0^{1,1}$')
plt.grid(True)
plt.show()

plt.figure(figsize = (6, 6))
plt.plot(time, E_trace, label = 'E')
plt.xlabel('Time ($t$)')
plt.ylabel('$E_z$')
plt.title('Q2e, Plot of $E_z$ at (0.5, 0.5), $\omega = \omega_0^{1,1}$')
plt.grid(True)
plt.show()

plt.figure(figsize = (6, 6))
plt.plot(time, Hx_trace, label = '$H_x$')
plt.plot(time, Hy_trace, label = '$H_y$')
plt.plot(time, E_trace, label = '$E_z$')
plt.xlabel('Time ($t$)')
plt.ylabel('$E_z$, $H_x$, $H_y$')
plt.title('Q2e, Combined plot, $\omega = \omega_0^{1,1}$')
plt.grid(True)
plt.legend()
plt.show()


#%% Transform testing code for Q2b
Hx = np.random.rand(N, N)
Hx[:, 0] = 0
Hx[:, -1] = 0
Hx[0, :] = Hx[1, :]
Hx[-1, :] = Hx[-2, :]
print(Hx)
print(Hx - idHxt2(dHxt2(Hx)))
print('--------------------')


Hy = np.random.rand(N,N)
Hy[:, 0] = Hy[:, 1]
Hy[:, -1] = Hy[:, -2]
Hy[0, :] = 0
Hy[-1, :] = 0
print(Hy)
print(Hy - idHyt2(dHyt2(Hy)))
print('--------------------')

EJ = np.random.rand(N,N)
EJ[:, 0] = 0
EJ[:, -1] = 0
EJ[0, :] = 0
EJ[-1, :] = 0
print(EJ)
print(EJ - idst2(dst2(EJ)))
print('--------------------')


