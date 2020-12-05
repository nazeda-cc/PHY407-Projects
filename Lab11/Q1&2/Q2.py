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
    energy = -J_*np.sum(dipoles[0:-1]*dipoles[1:])
    return energy


def acceptance(Enew, E, T):
    """ Function for acceptance probability; to be completed """
    # Do stuff here
    return random() < np.exp((E-Enew)/(T*kB))  # result is True of False


# define constants
kB = 1.0
T = 2
J = 1.0
l = 20
num_dipoles = l**2
N = 100000

# generate array of dipoles and initialize diagnostic quantities
dipoles = np.ones(num_dipoles, int)  # hint: this will not work
for i in range(num_dipoles):
    dipoles[i] = randrange(0, 2)
    if dipoles[i] == 0:
        dipoles[i] = -1

energy = []  # empty list; to add to it, use energy.append(value)
magnet = []  # empty list; to add to it, use magnet.append(value)

E = energyfunction(J, dipoles)
energy.append(E)
magnet.append(sum(dipoles))


print(dipoles)
dipoles_plot = dipoles.reshape(l, l)
plt.figure()
plt.imshow(dipoles_plot, cmap = 'Greys')
plt.colorbar()


for i in range(N):
    picked = randrange(num_dipoles)  # choose a victim
    dipoles[picked] *= -1  # propose to flip the victim
    Enew = energyfunction(J, dipoles)  # compute Energy of proposed new state

    # calculate acceptance probability
    if acceptance(Enew, E, T):
        E = Enew
    else:
        dipoles[picked] *= -1
    
    # store energy and magnetization
    energy.append(E)
    magnet.append(sum(dipoles)) 
    
    

dipoles_plot = dipoles.reshape(l, l)
plt.figure()
plt.imshow(dipoles_plot, cmap = 'Greys')
plt.colorbar()

plt.figure()
plt.plot(magnet, '-', linewidth = 0.5)

plt.figure()
plt.plot(energy, '-', linewidth = 0.5)
# plot energy, magnetization
