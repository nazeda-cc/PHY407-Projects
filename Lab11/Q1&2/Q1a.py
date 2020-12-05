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

seed(10)
N = 25
R = 0.02
Tmax = 10.0
Tmin = 1e-2
tau = 1e4

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
r = empty([N+1,2],float)
for i in range(N):
    r[i,0] = random()
    r[i,1] = random()
r[N] = r[0]
D = distance()

# Set up the graphics
plt.figure(figsize = (8, 8))
#display(center=[0.5,0.5])
for i in range(N):
    
    if i == 0:
        plt.scatter(r[i, 0], r[i, 1], color = 'r', s = 60)
    else:
        plt.scatter(r[i, 0], r[i, 1], color = 'c', s = 60)

    plt.plot([r[i][0], r[i+1][0]], [r[i][1], r[i+1][1]], color = 'k', linewidth = 1)


plt.show()

print(distance())
# Main loop
seed(12)
t = 0
T = Tmax
while T>Tmin:

    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Update the visualization every 100 moves
    '''
    if t%10000==0:
        plt.figure(figsize = (8, 8))

        for i in range(N):
    
            if i == 0:
                plt.scatter(r[i, 0], r[i, 1], color = 'r', s = 60)
            else:
                plt.scatter(r[i, 0], r[i, 1], color = 'c', s = 60)

            plt.plot([r[i][0], r[i+1][0]], [r[i][1], r[i+1][1]], color = 'k', linewidth = 1)


        plt.show()
        '''

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

plt.figure(figsize = (8, 8))

for i in range(N):
    
    if i == 0:
        plt.scatter(r[i, 0], r[i, 1], color = 'r', s = 60)
    else:
        plt.scatter(r[i, 0], r[i, 1], color = 'c', s = 60)

    plt.plot([r[i][0], r[i+1][0]], [r[i][1], r[i+1][1]], color = 'k', linewidth = 1)
plt.show()
print(distance())