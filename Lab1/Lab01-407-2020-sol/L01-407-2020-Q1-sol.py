# Author: Nicolas Grisouard, University of Toronto
# Planetary motion of Mercury

import numpy as np
import matplotlib.pyplot as plt

ftsz = 14  # font size for figures

# i. Define constants G and Ms -----------------------------------------------|
Ms = 1.  # [Solar mass] Solar mass
G = 39.5  # [AU**3/Ms/yr**2] gravitational constant
alpha = 0.01  # [AU**2] the GR constant

# ii. choose time step Dt, and a number N of time steps to execute,
Dt = 1.e-4  # [Earth years]
Duration = 1.  # [Earth years]
N = int(Duration/Dt)  # integer division

# iii. initialize an array of length $N$ containing all values of $t$. -------|
t = np.linspace(0., Duration, N)
# or
t = Dt*np.arange(0, N)

# iv. initialize empty arrays of lengths $N$ for $v_x$, $v_y$, $x$, $y$,  ----|
# and set the 1st value of each to their initial conditions (eqns. 10 in text).
x = 0*t
y = 0*t
vx = 0*t
vy = 0*t

x[0] = 0.47  # [AUs]
y[0] = 0.  # [AUs]
vx[0] = 0.  # [AUs]
vy[0] = 8.17  # [AUs]

for i in range(N-1):
    # v. compute $r = \sqrt{x^2 + y^2}$,  ------------------------------------|
    r = np.sqrt(x[i]**2 + y[i]**2)

    # vi. Update velocity first:  --------------------------------------------|
    vx[i+1] = vx[i] - Dt*G*Ms*x[i]*(1 + alpha/r**2)/r**3
    vy[i+1] = vy[i] - Dt*G*Ms*y[i]*(1 + alpha/r**2)/r**3

    # vii. Update positions with the new velocities  -------------------------|
    x[i+1] = x[i] + Dt*vx[i+1]
    y[i+1] = y[i] + Dt*vy[i+1]

# vii. Once loop is finished, compute angular momentum: ----------------------|
sigma = x*vy - y*vx


# ix. Plot -------------------------------------------------------------------|
plt.figure()  # Cartesian velocity components
plt.plot(t, vx, label='$v_x$')
plt.plot(t, vy, label='$v_y$')
plt.xlabel('time (Earth years)', fontsize=ftsz)
plt.ylabel('velocity (AU/(Earth year))', fontsize=ftsz)
plt.legend()
plt.grid()

if alpha < 1e-10:  # akin to alpha = 0
    plt.savefig('L01-Q1-Newt-vel.png', dpi=300)  # dpi stands for dots/inch
else:
    plt.savefig('L01-Q1-GR-vel.png', dpi=300)  # dpi stands for dots/inch

# Trajectory
plt.figure()
plt.plot(x, y)
plt.axhline(0., color='k')  # y=0 line
plt.axvline(0., color='k')  # x=0 line
plt.xlabel('$x$ (AU)', fontsize=ftsz)
plt.ylabel('$y$ (AU)', fontsize=ftsz)
plt.axis('image')
plt.grid()

if alpha < 1e-14:  # akin to alpha = 0
    plt.savefig('L01-Q1-Newt-traj.png', dpi=300)  # dpi stands for dots/inch
else:
    plt.savefig('L01-Q1-GR-traj.png', dpi=300)  # dpi stands for dots/inch

# angular momentum
plt.figure()
plt.plot(t, sigma)
plt.xlabel('time (Earth years)', fontsize=ftsz)
plt.ylabel('normalized angular momentum (AU$^2$/yr)', fontsize=ftsz)
plt.grid()

if alpha < 1e-10:  # akin to alpha = 0
    plt.savefig('L01-Q1-Newt-angmom.png', dpi=300)  # dpi stands for dots/inch
else:
    plt.savefig('L01-Q1-GR-angmom.png', dpi=300)  # dpi stands for dots/inch
