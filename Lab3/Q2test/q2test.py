# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:02:11 2020

@author: rundo
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:31:49 2020

@author: Zirui Wan
"""


import numpy as np
import matplotlib.pyplot as plt
from q2test_func import *

# define array of x 
xrange = np.arange(-4, 4, 0.01)
plt.figure(figsize=(8, 6))
plt.plot(xrange, psi(0, xrange), label='n = 0')
plt.plot(xrange, psi(1, xrange), label='n = 1')
plt.plot(xrange, psi(2, xrange), label='n = 2')
plt.plot(xrange, psi(3, xrange), label='n = 3')
plt.grid()
plt.legend()
plt.xlabel('x', fontsize=15)
plt.ylabel('$\psi_n(x)$', fontsize=15)
plt.title('Wavefunctions for different n\'s')
plt.show()

# define array of new X's
xrange = np.arange(-10, 10, 0.01)
plt.figure(figsize=(8, 6))
plt.plot(xrange, psi(30, xrange), label='n = 30')
plt.grid()
plt.legend()
plt.xlabel('x', fontsize=15)
plt.ylabel('$\psi_n(x)$', fontsize=15)
plt.title('Wavefunction for n = 30')
plt.show()

# calculate and print uncertainties in position and momentum, and energy
for e in range(0, 16):
    print('n = %02d, sqrt(<x^2>)=%.3f, sqrt(<p^2>)=%.3f, E=%.3f' 
          %(e, np.sqrt(mean_xsq(e)- mean_x(e)**2), np.sqrt(mean_psq(e) - mean_p(e)**2), energy(e)))