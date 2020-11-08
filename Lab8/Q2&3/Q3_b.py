# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:18:17 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation


L = 1
J = 150
dx = L/J
dt = 0.001



g = 9.81
eta_b = 0
H = 0.01
A = 2e-4
sigma = 0.1
miu = 0.5

x = np.arange(0, L+dx, dx)

eta_b = (1+np.tanh((x-0.5)*8*np.pi))*(H-4e-4)/2


u = np.zeros(J+1, float)
eta = np.zeros(J+1, float)

u_new = np.zeros(J+1, float)
eta_new = np.zeros(J+1, float)

u_half = np.zeros(J+1, float)
eta_half = np.zeros(J+1, float)

avg = np.average(A*np.exp(-(x)**2/sigma**2))
eta = H + A*np.exp(-(x)**2/sigma**2) - avg


#fig, ax = plt.subplots(figsize = (8, 8))
#ims = []

t = 0
t_end = 4.5

eta_0 = np.copy(eta)

t_error = 1e-5

while t <= t_end:
    for j in range(J+1):     
        if j == 0:
            u_new[j] = 0
            eta_new[j] = eta[j] - (u[j+1]*(eta[j+1]-eta_b[j+1]) - u[j]*(eta[j]-eta_b[j]))*dt/dx
            
            u_half[j] = (u[j+1]+u[j])/2 - ((u[j+1]**2 - u[j]**2)/2 + g*(eta[j+1]-eta[j]))*dt/(2*dx)
            eta_half[j] = (eta[j+1]+eta[j])/2 - (u[j+1]*(eta[j+1]-eta_b[j+1]) - u[j]*(eta[j]-eta_b[j]))*dt/(2*dx)
            
        elif j == J:
            u_new[j] = 0
            eta_new[j] = eta[j] - (u[j]*(eta[j]-eta_b[j]) - u[j-1]*(eta[j-1]-eta_b[j-1]))*dt/dx
            
            
        else:
            u_half[j] = (u[j+1]+u[j])/2 - ((u[j+1]**2 - u[j]**2)/2 + g*(eta[j+1]-eta[j]))*dt/(2*dx)
            eta_half[j] = (eta[j+1]+eta[j])/2 - (u[j+1]*(eta[j+1]-eta_b[j+1]) - u[j]*(eta[j]-eta_b[j]))*dt/(2*dx)
            
            u_new[j] = u[j] - ((u_half[j]**2 - u_half[j-1]**2)/2 + g*(eta_half[j]-eta_half[j-1]))*dt/(dx)
            eta_new[j] = eta[j] - (u_half[j]*(eta_half[j]-(eta_b[j+1]+eta_b[j])/2) - 
                                   u_half[j-1]*(eta_half[j-1]-(eta_b[j]+eta_b[j-1])/2))*dt/(dx)
            
    
        
    #im,  = ax.plot(x, eta, animated=True, color = 'c')
    #ax.set_ylabel('$\eta$, Free surface height (m)')
    #ax.set_xlabel('x (m)')
    #ims.append([im])
    
        
    if t - 1 <= t_error:
        eta_1 = np.copy(eta)
        
    if t - 2 <= t_error:
        eta_2 = np.copy(eta)

    if t - 4 <= t_error:
        eta_4 = np.copy(eta)
        

    u = np.copy(u_new)
    eta = np.copy(eta_new)
    
    t += dt
  
plt.figure(1, figsize = (8, 8))
plt.plot(x, eta_0, label = 't=0')
plt.plot(x, eta_1, label = 't=1')
plt.plot(x, eta_2, label = 't=2')
plt.plot(x, eta_4, label = 't=4')
plt.legend()
plt.ylabel('$\eta$, Free surface height (m)')
plt.xlabel('x (m)')
plt.title('Q3b, Wave forms in one plot')
plt.grid(True)
plt.show()

fig0, axs = plt.subplots(2, 1, figsize = (8, 8))
axs[0].plot(x, eta_0)
axs[0].set_ylabel('$\eta$ (m)')
axs[0].set_ylim(0.00995, 0.01025)
axs[0].grid(True)

axs[1].plot(x, eta_b, color = 'k')
axs[1].set_ylabel('$\eta _b$ (m)')
axs[1].set_xlabel('x (m)')
axs[1].grid(True)
axs[0].set_title('Wave form at t=0s')
plt.show()

fig0, axs = plt.subplots(2, 1, figsize = (8, 8))
axs[0].plot(x, eta_1)
axs[0].set_ylabel('$\eta$ (m)')
axs[0].set_ylim(0.00995, 0.01025)
axs[0].grid(True)

axs[1].plot(x, eta_b, color = 'k')
axs[1].set_ylabel('$\eta _b$ (m)')
axs[1].set_xlabel('x (m)')
axs[1].grid(True)
axs[0].set_title('Wave form at t=1s')
plt.show()

fig0, axs = plt.subplots(2, 1, figsize = (8, 8))
axs[0].plot(x, eta_2)
axs[0].set_ylabel('$\eta$ (m)')
axs[0].set_ylim(0.00995, 0.01025)
axs[0].grid(True)

axs[1].plot(x, eta_b, color = 'k')
axs[1].set_ylabel('$\eta _b$ (m)')
axs[1].set_xlabel('x (m)')
axs[1].grid(True)
axs[0].set_title('Wave form at t=2s')
plt.show()

fig0, axs = plt.subplots(2, 1, figsize = (8, 8))
axs[0].plot(x, eta_4)
axs[0].set_ylabel('$\eta$ (m)')
axs[0].set_ylim(0.00995, 0.01025)
axs[0].grid(True)

axs[1].plot(x, eta_b, color = 'k')
axs[1].set_ylabel('$\eta _b$ (m)')
axs[1].set_xlabel('x (m)')
axs[1].grid(True)
axs[0].set_title('Wave form at t=4s')
plt.show()


#plt.plot(x, eta_b, label = 'Bottom topography', color = 'k')
#plt.ylim(0.0095, 0.01025)
#ani = animation.ArtistAnimation(fig, ims, interval=5, repeat = False, blit=True)

#writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
#ani.save("movie.mp4", writer=writer)
