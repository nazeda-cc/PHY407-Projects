# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:38:19 2020

@author: Zirui Wan
"""

#################################################################
# This program simulates diffusion limited aggregation on an LxL grid.
# Particles are initiated until the centre point is filled.
#################################################################
from random import randrange, seed
import matplotlib.pyplot as plt
import numpy as np
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

#############################################################
# main program starts here
#############################################################



Lp=151 # size of domain
anchored=np.zeros((Lp,Lp),dtype=int) # array to represent whether each gridpoint has an anchored particle
anchored_points=[[],[]] # list to represent x and y positions of anchored points
centre_point=(Lp-1)/2 # middle point of domain
moving_points = [[centre_point], [centre_point]]


# set up animation of anchored points
animation_interval=20 # how many moves to make before
                      # updating plot of Brownian motion
                      
fig, ax = plt.subplots(figsize=(12, 12))
plt.title("Final distribution of DLA")
plt.plot(centre_point, centre_point, color='blue', marker='+', mew=12, ms=25)
moving_plot=ax.plot(centre_point, centre_point, color='red', marker='.', markersize=10)
anchored_plot=ax.plot(anchored_points[0], anchored_points[1], '.k',markersize=20)
plt.xlim([-1,Lp+1])
plt.ylim([-1,Lp+1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()


b = False
# the loop will not stop until the center point is stucked
curr = 0
while not b:
    print('Current number of particle: ', curr)
    xp = centre_point
    yp = centre_point
    i=0 # counter to keep track of animation of moving particle
    
    not_stuck=True
    # check if center point is stucked
    L = np.copy(anchored_points)
    while (centre_point in L[0]):
        the_index = list(L[0]).index(centre_point)
        if L[1][the_index] == centre_point:
            b = True
        L[0][the_index] = 0
        L[1][the_index] = 0
    if b == True:
        break
        
    while not_stuck:
        if xp==0 or xp==Lp-1 or yp==0 or yp==Lp-1:
            # Check if the particle has reached a wall
            anchored[ int(xp), int(yp) ]=1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)
            anchored_plot[0].set_xdata(anchored_points[0])
            anchored_plot[0].set_ydata(anchored_points[1])
        
            plt.draw()
            not_stuck=False
            moving_points = [[], []]
        elif np.any(anchored[ int(xp-1):int(xp+2), int(yp-1):int(yp+2)] == 1):
            # Check if particle is adjacent to an anchored particle
            anchored[int(xp), int(yp)]=1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)
            anchored_plot[0].set_xdata(anchored_points[0])
            anchored_plot[0].set_ydata(anchored_points[1])
            plt.draw()
            not_stuck=False
            moving_points = [[], []]
            
        else: # If neither of the above, move particle and continue
              # while loop
            i += 1
            xp,yp=nextmove(xp,yp)
    curr += 1


plt.savefig('Q1c.png')
plt.show()


