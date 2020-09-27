# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:12:08 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from matplotlib import pyplot as plt
from Lab3_Q1a_function import *

######################## Q1a i ###################################
n = 3
for i in range(0, 9):
    N = 2**(n+i)
    print('N=', N)
    print('Trap:', Daws(4, N, 'Trap'))
    print('Simp:', Daws(4, N, 'Simp'))
    print('Gauss:', Daws(4, N, 'Gauss'))
    print('Scipy(True value):', Daws(4, N, 'Scipy'))
    print('---------------')
##################################################################

######################## Q1a ii ###################################
#relative error from scipy.special.dawsn
error_trap = []
error_simp = []
error_gauss = []
true_value = Daws(4, 1, 'Scipy')

n = np.arange(1, 14, 1)
for i in n:
    N = 2**i
    error_trap.append(abs(Daws(4, N, 'Trap') - true_value))
    error_simp.append(abs(Daws(4, N, 'Simp') - true_value))
    error_gauss.append(abs(Daws(4, N, 'Gauss') - true_value))

plt.figure(1)
plt.plot(n, error_trap, label = 'Trapezoidal rule')
plt.plot(n, error_simp, label = 'Simpsons rule')
plt.plot(n, error_gauss, label = 'Gaussian rule')
plt.plot([1,12],[10**-15,10**-15], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.legend()
plt.ylabel('Relative error')
plt.xlabel('$n$, Powers of $N=2^n$')
plt.title('Relative error from scipy.speical.dawsn(4)')
plt.show()

#Calculated error with textbook eqn.
calculated_error_trap = []
calculated_error_simp = []
calculated_error_gauss = []

n = np.arange(0, 13, 1)
for i in n:
    N_1 = 2**i
    N_2 = 2**(i+1)
    calculated_error_trap.append(abs(Daws(4, N_1, 'Trap') - Daws(4, N_2, 'Trap')) / 3)
    calculated_error_simp.append(abs(Daws(4, N_1, 'Simp') - Daws(4, N_2, 'Simp')) / 15)
    calculated_error_gauss.append(abs(Daws(4, N_1, 'Gauss') - Daws(4, N_2, 'Gauss')))
    
n = np.arange(1, 14, 1)
plt.figure(2)
plt.plot(n, calculated_error_trap, label = 'Trapezoidal rule')
plt.plot(n, calculated_error_simp, label = 'Simpsons rule')
plt.plot(n, calculated_error_gauss, label = 'Gaussian rule')
plt.plot([1,12],[10**-15,10**-15], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.legend()
plt.ylabel('Calculated error')
plt.xlabel('$n$, Powers of $N=2^n$')
plt.title('Calculated error for $D(4)$ with textbook eqn.')
plt.show()