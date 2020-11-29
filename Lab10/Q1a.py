# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:38:19 2020

@author: Zirui Wan
"""

from random import randrange, seed
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 25})

# set randum seed for reproducibility
seed(12345)

def nextmove(x,y):
    """ Function to update position of particle by moving up/down/letf/right
    INPUT:
        x, y[float]: coordinates of the particle
    OUTPUT:
        x, y[float]: new coordinates of the particle
    """
    direction=randrange(1,5)
    # randomly choose a direction
    # 1 = up, 2 = down, 3 = left, 4=right
    if direction==1:
        #move up
        y+=1
    elif direction==2:
        #move down
        y-=1
    elif direction==3:
        #move right
        x+=1 
    elif direction==4:
        #move left
        x-=1
    else:
        print("error: direction isn't 1-4")
    return x,y



plt.ion()

# Define some constants
steps = 5000
Lp = 101 # size of box
centre_point = (Lp-1)/2
animation_interval=1 # how many moves to make before
                      # updating plot of Brownian motion


animation_interval = 15  # how many moves to make before updating plot of


# Setup the figure before starting animation
fig = plt.figure(figsize=(12, 12)) # Create window
plt.title('Brownian Motion Simulation')
plt.plot(centre_point, centre_point, color='blue', marker='+', mew=12, ms=25)
moving_plot=plt.plot(centre_point,centre_point, color='red', marker='.', markersize=8)
plt.xlim([-2,Lp+1])
plt.ylim([-2,Lp+1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# initial position is center point
xp = centre_point
yp = centre_point

i = 0
while i <= steps:
    xp_new, yp_new = nextmove(xp,yp)
    while xp_new<=0 or xp_new>=Lp-1 or yp_new<=0 or yp_new>=Lp-1:
        xp_new, yp_new=nextmove(xp,yp)
        
    xp = xp_new
    yp = yp_new
    i += 1
    if i%animation_interval==0:
        moving_plot[0].set_xdata(np.append(moving_plot[0].get_xdata(), xp))
        moving_plot[0].set_ydata(np.append(moving_plot[0].get_ydata(), yp))
        plt.draw()


plt.ioff()
plt.savefig('Q1a.png')
plt.show()
