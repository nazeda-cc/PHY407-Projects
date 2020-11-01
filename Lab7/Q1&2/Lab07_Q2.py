# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:33:04 2020

@author: Zirui Wan
"""


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
from Lab07_Q2functions import bulirsch

delta = 1e3/3.154e7
AU = 149597870700  # Astronomical unit from wiki page

r = [1.4710e11, 0, 0, 3.0287e4]
H = 604800 # time step in seconds (1 week)
tpoints = np.arange(0, 4.73e+7, H)
xpoints, ypoints = bulirsch(r, tpoints, H, delta)

plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)
plt.plot(np.array(xpoints)/AU, np.array(ypoints)/AU, lw=3)
plt.grid()
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.scatter(0, 0, s=500, marker='*', color='y', label='Sun')
plt.scatter(-0.0167, 0, s=250, marker='d', color='red', label='The other focus of orbit')
plt.scatter(1.4710e11/AU, 0, s=500, marker='x', color='k' , label='Initial location')
plt.legend(loc=1)


r = [4.4368e12, 0, 0, 6.1218e3]
H = 6048000 # time step in seconds (10 weeks)
tpoints = np.arange(0, 4.73e+10, H)
xpoints, ypoints = bulirsch(r, tpoints, H, delta)

    
plt.subplot(1, 2, 2)
plt.plot(np.array(xpoints)/AU, np.array(ypoints)/AU, lw=3)
plt.grid()
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.xlim((-55, 55))
plt.ylim((-55, 55))
plt.scatter(0, 0, s=500, marker='*', color='y', label='Sun')
plt.scatter(-20, 0, s=250, marker='d', color='red', label='The other focus of orbit')
plt.scatter(4.4368e12/AU, 0, s=500, marker='x', color='k', label='Initial location')
plt.legend(loc=1)