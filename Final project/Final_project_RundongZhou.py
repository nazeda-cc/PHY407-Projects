# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:09:09 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy import random
from matplotlib import animation

def f(x, y, vx, vy, gamma, kB, T, N):
    #Function to calculate force with random process
    
    fx = np.zeros(N, float)
    fy = np.zeros(N, float)
    for i in range(len(x)):
        #viscosity
        fx[i] -= gamma * vx[i]
        fy[i] -= gamma * vy[i]
        
        #random process here
        rx, ry = gauss(1)
        fx[i] += np.sqrt(2*gamma*kB*T) * rx
        fy[i] += np.sqrt(2*gamma*kB*T) * ry
        
        #apply lennard-jones potential
        for j in range(len(x)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                temp = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                fx[i] += temp * dx
                fy[i] += temp * dy
                
    return fx, fy


def f_d(x, y, vx, vy, gamma, N):
    #Function to calculate force without random process
    fx = np.zeros(N, float)
    fy = np.zeros(N, float)
    for i in range(len(x)):
        #viscosity
        fx[i] -= gamma * vx[i]
        fy[i] -= gamma * vy[i]
        #apply lennard-jones potential
        for j in range(len(x)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                temp = 48/((dx**2 + dy**2)**7) - 24/((dx**2 + dy**2)**4)
                fx[i] += temp * dx
                fy[i] += temp * dy
                
    return fx, fy

def u(x, y):
    #calculate potential energy
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                result += 4/(dx**2 + dy**2)**6 - 4/(dx**2 + dy**2)**3
                
                
    return result/2

   
def k_energy(vx, vy):
    #kinetic energy 
    result = 0
    for i in range(len(vx)):
        result += 0.5 * vx[i]**2
        result += 0.5 * vy[i]**2
        
    return result

def gauss(sigma):
    #2-D gauss random numbers
    r = np.sqrt(-2*sigma*sigma*np.log(1-random.random()))
    theta = 2*np.pi*random.random()
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    return x, y

def avg_distance(x, y):
    #calculate the average distances between particles and their closest 2 neighbours
    all_dis = []
    for i in range(len(x)):
        dis = []
        for j in range(len(x)):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                dis.append(np.sqrt(dx**2+dy**2))
        dis = np.sort(dis)
        all_dis.append(dis[0])
        all_dis.append(dis[1])
    
    return np.average(all_dis)

#set constants
N = 9   #please only use square numbers 1, 4, 9, 16, 25...
Lx = np.sqrt(N)
Ly = np.sqrt(N)
gamma = 0.25
kB = 1
Tmax = 100  #starting temperature
T = Tmax
tau = 10



dx = Lx/np.sqrt(N)
dy = Ly/np.sqrt(N)

x_grid = np.arange(dx/2, Lx, dx)
y_grid = np.arange(dy/2, Ly, dy)

xx_grid, yy_grid = np.meshgrid(x_grid, y_grid)

x_initial = xx_grid.flatten()
y_initial = yy_grid.flatten()

x_points = []
y_points = []

for i in range(0, N):
    x_points.append([])
    x_points[i].append(x_initial[i])
    y_points.append([])
    y_points[i].append(y_initial[i])


#set time steps
h = 0.01
tpoints = np.arange(0, 80, h)


#regular verlet method setup
vx = random.rand(N)-0.5
vy = random.rand(N)-0.5

vx_initial = np.copy(vx)
vy_initial = np.copy(vy)

vx_half = np.zeros(N, float)
vy_half = np.zeros(N, float)

x = np.zeros(N, float)
y = np.zeros(N, float)


dvx, dvy = f(x_initial, y_initial, vx, vy, gamma, kB, T, N)
for i in range(N):
    vx_half[i] += 0.5 * h * dvx[i]
    vy_half[i] += 0.5 * h * dvy[i]
    x[i] = x_points[i][-1]
    y[i] = y_points[i][-1]
    

#initiate energy arrays
uenergy = []
kenergy = []
T_trace = []   

totalE = u(x, y) + k_energy(vx, vy)

#modified Verlet method iteration
for t in tpoints:
    
    T = Tmax * np.exp(-t/tau)       #cooling
    
    #Box boundary conditions
    for i in range(N):
        
        if x[i] >= Lx:
            x[i] = Lx
            vx[i] *= -1
            vx_half[i] *= -1
        elif x[i] <= 0:
            x[i] = 0
            vx[i] *= -1
            vx_half[i] *= -1
            
        if y[i] >= Ly:
            y[i] = Ly
            vy[i] *= -1
            vy_half[i] *= -1
        elif y[i] <= 0:
            y[i] = 0 
            vy[i] *= -1
            vy_half[i] *= -1
        
        x[i] += h * vx_half[i]
        y[i] += h * vy_half[i]
        
        x_points[i].append(x[i])
        y_points[i].append(y[i])
    
    

    kx, ky = f(x, y, vx_half, vy_half, gamma, kB, T, N)
    kx *= h
    ky *= h
    

    vx = vx_half + 0.5 * kx
    vy = vy_half + 0.5 * ky
    
    #Markov chain method
    old_totalE = totalE
    U = u(x, y)
    K = k_energy(vx, vy)
    #calculate total energy at each step
    totalE = U + K
    delta = totalE - old_totalE
    
    #revoke a random precess
    if random.random() > np.exp(-delta/(kB*T)):

        vx = vx_half - 0.5 * kx
        vy = vy_half - 0.5 * ky
        

        kx, ky = f_d(x, y, vx_half, vy_half, gamma, N)
        kx *= h
        ky *= h
        

        vx = vx_half + 0.5*kx
        vy = vy_half + 0.5*ky
        U = u(x, y)
        K = k_energy(vx, vy)
        #calculate total energy at each step
        totalE = U + K
        



    vx_half += kx
    vy_half += ky
    
        
        
    #caculate kinetic and potential energy for each step
    uenergy.append(U)
    kenergy.append(K)
    T_trace.append(T)



total = []
for i in range(len(uenergy)):
    total.append(uenergy[i]+kenergy[i])



#plotting
plt.figure(figsize = (10, 10))
sty = [None, None,None,None,None,None,None,None,None,'-.','-.','-.','-.','-.','-.','-.']
for i in range(N):
    plt.plot(x_points[i], y_points[i], linewidth=0.5)       #if you dont want trajectory
                                                            #comment out this line
    plt.scatter(x_points[i][-1], y_points[i][-1], c='r', s = 80)
    plt.arrow(x_initial[i], y_initial[i], vx_initial[i]*0.3, vy_initial[i]*0.3, color = 'c', head_width = 0.05)
    
plt.axis([0, np.sqrt(N), 0, np.sqrt(N)])
plt.scatter(x_initial, y_initial, c='k', s = 80)
plt.scatter(-10, -10, c='r', label='Final position')
plt.scatter(-10, -10, c='k', label='Initial position')
plt.arrow(-10, -10, 0.3, 0.3, color = 'c', head_width = 0.001, label='Initial speed')
plt.xlabel('$x$ axis', fontsize = 18)
plt.ylabel('$y$ axis', fontsize = 18)
plt.grid(True)
plt.title('Molecule system of %i particles'%N, fontsize = 18)
plt.legend()
plt.show()

plt.figure(figsize = (10, 8))
plt.plot(T_trace, uenergy, label = 'Potential Energy', linestyle = '-.')
plt.plot(T_trace, kenergy, label = 'Kinetic Energy', linestyle = '-.')
plt.plot(T_trace, total, label = 'Total energy of the system', color = 'r')
plt.axis([max(T_trace), min(T_trace), min(total)-5, max(kenergy)+5])
plt.semilogx()
plt.xlabel('Temperature of the system', fontsize = 18)
plt.ylabel('Energy value', fontsize = 18)
plt.title('Energy of the system', fontsize = 18)
plt.legend()
plt.show()

print('Average distance between particles:')
print(avg_distance(x, y))


#%% Animation code
fig = plt.figure(figsize = (10,10))
ax1 = plt.axes(xlim=(0, np.sqrt(N)), ylim=(0,np.sqrt(N)))
plt.xlabel('x')
plt.ylabel('y')

lines = []
points = []

for index in range(N):
    lobj = ax1.plot([], [], lw=0.5)[0]
    lines.append(lobj)
    lobj = ax1.plot([], [], 'ko')[0]
    points.append(lobj)


def init():
    for line in lines:
        line.set_data([],[])
        
    for point in points:
        point.set_data([],[])
    return lines, points


def animate(i):
    for n in range(N):
        lines[n].set_data(x_points[n][:i], y_points[n][:i])
        points[n].set_data(x_points[n][i-1:i], y_points[n][i-1:i])
    return lines, points

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=80, interval=100, blit=False)

anim.save('xsda.mp4', fps=30)

plt.show()
    
    