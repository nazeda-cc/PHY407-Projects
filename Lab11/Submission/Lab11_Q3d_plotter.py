# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:17:50 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


# Load energy array and temperature array from the simulation
E = np.load('Q3d_E.npy')
T = np.load('Q3d_T.npy')

# prepare arrays for temperature, mean of energy and std of energy
tarray = np.arange(10, 0, -0.5)
Estd = np.zeros(20)
Emean = np.zeros(20)

# loop over to calculate mean and std of E
curr = 0
for i in range(20):
    Estd[i] = np.std(E[curr*500000:(curr+1)*500000])
    Emean[i] = np.mean(E[curr*500000:(curr+1)*500000])
    curr += 1
    

# visualize E vs T plot
plt.figure(figsize=(10, 8))
plt.errorbar(tarray, Emean, yerr=Estd, capsize=5, lw=2.5)
plt.xlabel('Temperature')
plt.ylabel('Energy')
plt.grid()
plt.title('Energy versus Temperature for Protein Folding')
plt.savefig('Q3d.png', dpi=300)
plt.show()