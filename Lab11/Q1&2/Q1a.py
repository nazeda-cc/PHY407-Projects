# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt,exp
from numpy import empty
from random import random,randrange, seed
#from visual import sphere,curve,display
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import numpy as np



# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s

# Choose N city locations and calculate the initial distance


# Set up the graphics
'''
plt.figure(1, figsize = (8, 8))
#display(center=[0.5,0.5])
for i in range(N):
    
    if i == 0:
        plt.scatter(r[i, 0], r[i, 1], color = 'r', s = 60)
    else:
        plt.scatter(r[i, 0], r[i, 1], color = 'c', s = 60)

    plt.plot([r[i][0], r[i+1][0]], [r[i][1], r[i+1][1]], color = 'k', linewidth = 1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Initial path with seed=100214')
plt.show()
'''
#init_d = distance()
#print('Initial', distance())
# Main loop
optD = []
for power in range(1, 11):
    
    seed(100214)
    N = 25
    R = 0.02
    Tmax = 10.0
    Tmin = 1e-3
    tau = 1e2
    
    r = empty([N+1,2],float)
    for i in range(N):
        r[i,0] = random()
        r[i,1] = random()
    r[N] = r[0]
    D = distance()
    
    
    
    
    s = 2**power
    seed(s)
    t = 0
    T = Tmax
    while T>Tmin:

        # Cooling
        t += 1
        T = Tmax*exp(-t/tau)

    # Update the visualization every 100 moves

        # Choose two cities to swap and make sure they are distinct
        i,j = randrange(1,N),randrange(1,N)
        while i==j:
            i,j = randrange(1,N),randrange(1,N)

    # Swap them and calculate the change in distance
        oldD = D
        r[i,0],r[j,0] = r[j,0],r[i,0]
        r[i,1],r[j,1] = r[j,1],r[i,1]
        D = distance()
        deltaD = D - oldD

    # If the move is rejected, swap them back again
        if random()>exp(-deltaD/T):
            r[i,0],r[j,0] = r[j,0],r[i,0]
            r[i,1],r[j,1] = r[j,1],r[i,1]
            D = oldD


    optD.append(distance())
    plt.figure(2, figsize = (8, 8))

    for i in range(N):
    
        if i == 0:
            plt.scatter(r[i, 0], r[i, 1], color = 'r', s = 60)
        else:
            plt.scatter(r[i, 0], r[i, 1], color = 'c', s = 60)

        plt.plot([r[i][0], r[i+1][0]], [r[i][1], r[i+1][1]], color = 'k', linewidth = 1)
    
    plt.title('Final path with seed=%i, '%s + 'tau = %i'%tau, fontsize = 20)
    plt.show()
    end_d = distance()
    #print('Initial', init_d)
    #print('Seed = %i, Optimized:'%s, distance())
    print(s, '&', distance(), '\\')
    print('\hline')
    #print('Difference:', init_d-end_d)

print(optD)
print(np.average(optD))
print(np.std(optD))
