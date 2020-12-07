# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:46:26 2020

@author: rundo
"""

import numpy as np
from random import random, randrange
from matplotlib import pyplot as plt


def energyfunction(J_, dipoles):
    """ function to calculate energy """
    energy_row = -J_*np.sum(dipoles[0:-1, :]*dipoles[1:, :])    #adding rows
    energy_col = -J_*np.sum(dipoles[:, 0:-1]*dipoles[:, 1:])    #adding columns
    return energy_row + energy_col


def acceptance(Enew, E, T):
    """ Function for acceptance probability; to be completed """
    # Do stuff here
    return random() < np.exp((E-Enew)/(T*kB))  # result is True of False


# define constants
kB = 1.0
T = 1
J = 1.0
l = 20
#num_dipoles = l**2
N = 100000

# generate array of dipoles and initialize diagnostic quantities
dipoles = np.ones((l, l), int)  # hint: this will not work
for i in range(l):
    for j in range(l):
        dipoles[i, j] = randrange(0, 2)
        if dipoles[i, j] == 0:
            dipoles[i, j] = -1

energy = []  # empty list; to add to it, use energy.append(value)
magnet = []  # empty list; to add to it, use magnet.append(value)

E = energyfunction(J, dipoles)
energy.append(E)
magnet.append(np.sum(dipoles))


print(dipoles)

plt.figure()
plt.imshow(dipoles, cmap = 'binary')
plt.title('T=%i'%T)
plt.show()

#%%
for i in range(N):
    picked_x = randrange(l)  # choose a victim
    picked_y = randrange(l)
    dipoles[picked_x, picked_y] *= -1  # propose to flip the victim
    Enew = energyfunction(J, dipoles)  # compute Energy of proposed new state

    # calculate acceptance probability
    if acceptance(Enew, E, T):
        E = Enew
    else:
        dipoles[picked_x, picked_y] *= -1
    
    # store energy and magnetization
    energy.append(E)
    magnet.append(np.sum(dipoles))
    
    #animation code
    '''
    if i%1000 == 0:
        plt.figure()
        plt.imshow(dipoles, cmap = 'binary')
        plt.title('T=%i'%T)
        plt.axis('off')
        #plt.show()
        plt.savefig('anime/T=1_%i.png' % i)
    '''
    
    

# plot energy, magnetization
plt.figure()
plt.imshow(dipoles, cmap = 'binary')
plt.title('T=%i'%T)
plt.axis('off')
#plt.savefig('anime/T=1_final.png')
plt.show()

plt.figure(figsize = (8, 6))
plt.plot(magnet, '-', linewidth = 1)
plt.title('Q2, Total magnitization with T=%i'%T)
plt.xlabel('Number of iterations')
plt.ylabel('$M$ Total magnitization')
plt.show()

plt.figure(figsize = (8, 6))
plt.plot(energy, '-', linewidth = 1)
plt.title('Q2, Total Energy with T=%i'%T)
plt.xlabel('Number of iterations')
plt.ylabel('$E$ Total energy')
plt.show()

