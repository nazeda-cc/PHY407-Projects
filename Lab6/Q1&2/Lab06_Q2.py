# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 05:51:01 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
from Lab06_Q2functions import U, acc, f

# define constants
sigma = 1
epsilon = 1
m = 1

# visualize the potential and force due to Lennard-Jones potential
rrange = np.linspace(1, 4, 100)
uu = U(rrange)
ff = acc(rrange)*m
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(rrange, uu, lw=3)
plt.axvline(1.12, color='k', ls='-.', label=r'$r_m \approx 1.12$')
plt.xlabel('r')
plt.ylabel('V(r)')
plt.title('V(r) vs. r')
plt.legend()
plt.grid()
plt.subplot(122)
plt.plot(rrange, ff, lw=3)
plt.axvline(1.12, color='k', ls='-.', label=r'$r_m \approx 1.12$')
plt.xlabel('r')
plt.ylabel('F(r)')
plt.title('F(r) vs. r')
plt.xlim((1, 2.5))
plt.ylim((-3, 5))
plt.legend()
plt.grid()

# define array for time steps
dt = 0.01
tpoints = np.arange(0, 1, dt)

###############################################################################
########################### First initial condition ###########################
###############################################################################
# initial states
r = np.array([4, 4, 5.2, 4], float)
v = np.array([0, 0, 0, 0], float)

# arrays for positions and velocities
x1points = [r[0]]
y1points = [r[1]]
x2points = [r[2]]
y2points = [r[3]]
vx1 = [v[0]]
vy1 = [v[1]]
vx2 = [v[2]]
vy2 = [v[3]]

# first step of Verlet algorithm
vhalf = v + dt/2*f(r, tpoints[0])
# iterate over Verlet algorithm
for t in tpoints[1:]:
    r = r + dt*vhalf
    k = dt*f(r, t+dt)
    vth = vhalf + k/2
    vt32h = vhalf + k
    vhalf = vt32h
    
    # save outputs
    x1points.append(r[0])
    y1points.append(r[1])
    x2points.append(r[2])
    y2points.append(r[3])
    vx1.append(vth[0])
    vy1.append(vth[1])
    vx2.append(vth[2])
    vy2.append(vth[3])

# visualize the motion of the particles
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x1points, y1points, 'b.', label=r'Particle 1')
plt.plot(x2points, y2points, 'r.', label=r'Particle 2')
plt.scatter(4, 4, c='b', marker='x', s=200, label='Initial $X_1$')
plt.scatter(5.2, 4, c='r', marker='x', s=200, label='Initial $X_2$')
plt.grid()
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(2, 2, 2)
plt.plot(tpoints, x1points, 'b')
plt.ylabel('$X_1$')
plt.grid()
plt.subplot(2, 2, 4)
plt.plot(tpoints, x2points, 'r')
plt.xlabel('time')
plt.ylabel('$X_2$')
plt.grid()
plt.suptitle('First initial condition')
plt.subplots_adjust(hspace=0.18, wspace=0.3, left=0.05, right=0.95, top=0.9, bottom=0.05)



###############################################################################
########################### Second initial condition ##########################
###############################################################################
# initial states
r = np.array([4.5, 4, 5.2, 4], float)
v = np.array([0, 0, 0, 0], float)

# arrays for positions and velocities
x1points = [r[0]]
y1points = [r[1]]
x2points = [r[2]]
y2points = [r[3]]
vx1 = [v[0]]
vy1 = [v[1]]
vx2 = [v[2]]
vy2 = [v[3]]

# first step of Verlet algorithm
vhalf = v + dt/2*f(r, tpoints[0])
# iterate over Verlet algorithm
for t in tpoints[1:]:
    r = r + dt*vhalf
    k = dt*f(r, t+dt)
    vth = vhalf + k/2
    vt32h = vhalf + k
    vhalf = vt32h
    
    # save outputs
    x1points.append(r[0])
    y1points.append(r[1])
    x2points.append(r[2])
    y2points.append(r[3])
    vx1.append(vth[0])
    vy1.append(vth[1])
    vx2.append(vth[2])
    vy2.append(vth[3])

# visualize the motion of the particles
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x1points, y1points, 'b.', label=r'Particle 1')
plt.plot(x2points, y2points, 'r.', label=r'Particle 2')
plt.scatter(4.5, 4, c='b', marker='x', s=200, label='Initial $X_1$')
plt.scatter(5.2, 4, c='r', marker='x', s=200, label='Initial $X_2$')
plt.grid()
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(2, 2, 2)
plt.plot(tpoints, x1points, 'b')
plt.ylabel('$X_1$')
plt.grid()
plt.subplot(2, 2, 4)
plt.plot(tpoints, x2points, 'r')
plt.xlabel('time')
plt.ylabel('$X_2$')
plt.grid()
plt.suptitle('Second initial condition')
plt.subplots_adjust(hspace=0.18, wspace=0.3, left=0.05, right=0.95, top=0.9, bottom=0.05)



###############################################################################
########################### Third initial condition ###########################
###############################################################################
# initial states
r = np.array([2, 3, 3.5, 4.4], float)
v = np.array([0, 0, 0, 0], float)

# arrays for positions and velocities
x1points = [r[0]]
y1points = [r[1]]
x2points = [r[2]]
y2points = [r[3]]
vx1 = [v[0]]
vy1 = [v[1]]
vx2 = [v[2]]
vy2 = [v[3]]

# first step of Verlet algorithm
vhalf = v + dt/2*f(r, tpoints[0])
# iterate over Verlet algorithm
for t in tpoints[1:]:
    r = r + dt*vhalf
    k = dt*f(r, t+dt)
    vth = vhalf + k/2
    vt32h = vhalf + k
    vhalf = vt32h
    
    # save outputs
    x1points.append(r[0])
    y1points.append(r[1])
    x2points.append(r[2])
    y2points.append(r[3])
    vx1.append(vth[0])
    vy1.append(vth[1])
    vx2.append(vth[2])
    vy2.append(vth[3])

# visualize the motion of the particles
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x1points, y1points, 'b.', label=r'Particle 1')
plt.plot(x2points, y2points, 'r.', label=r'Particle 2')
plt.scatter(2, 3, c='b', marker='x', s=200, label='Initial $X_1$')
plt.scatter(3.5, 4.4, c='r', marker='x', s=200, label='Initial $X_2$')
plt.grid()
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(2, 2, 2)
plt.plot(tpoints, x1points, 'b')
plt.ylabel('$X_1$')
plt.grid()
plt.subplot(2, 2, 4)
plt.plot(tpoints, x2points, 'r')
plt.xlabel('time')
plt.ylabel('$X_2$')
plt.grid()
plt.suptitle('Third initial condition')
plt.subplots_adjust(hspace=0.18, wspace=0.3, left=0.05, right=0.95, top=0.9, bottom=0.05)