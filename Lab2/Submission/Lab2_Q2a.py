# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:17:07 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from Lab2_Q2a_function import *
from time import time


############# a i ############################################################
print('----------Q2a i----------')
x = 4
n = 8           #set N=8 slices
print('D(4), Trapezoidal rule: ', Daws(x, n, 'Trap'))
print('D(4), Simpsons rule: ', Daws(x, n, 'Simp'))
print('D(4), Scipy special function: ', Daws(x, n, 'Scipy'))
print('Difference between Trapesoidal rule & Scipy special function: ', abs(
    Daws(x, n, 'Trap') - Daws(x, n, 'Scipy')))
print('Difference between Simpsons rule & Scipy special function: ', abs(
    Daws(x, n, 'Simp') - Daws(x, n, 'Scipy')))
print('--------------------------\n')

#show the differences graphically
y_trap = []
y_simp = []
y_scipy = []
x = np.arange(-5, 6, 0.1)
for i in x:
    y_trap.append(Daws(i, n, 'Trap'))
    y_simp.append(Daws(i, n, 'Simp'))
    y_scipy.append(Daws(i, n, 'Scipy'))
    
plt.figure()
plt.plot(x, y_trap, label = 'Trapezoidal rule')
plt.plot(x, y_simp, label = 'Simpsons rule')
plt.plot(x, y_scipy, label = 'scipy.special.dawsn')
plt.legend()
plt.xlabel('$x$', fontsize=15)
plt.ylabel('$D(x)$', fontsize=15)
plt.title('Q1a Comparison between Trap, Simp, and scipy func')
##############################################################################



####### a ii #################################################################


x = 4
n = 2
power = 19

error_trap = []
error_simp = []

for i in range(3, power):
    n = 2**i
    error_trap.append(abs(Daws(x, n, 'Trap') - 
                          Daws(x, n, 'Scipy')))
    error_simp.append(abs(Daws(x, n, 'Simp') - 
                          Daws(x, n, 'Scipy')))

plt.figure(figsize=(6,8))
plt.plot(range(3, power), error_trap, label = 'Trapezoidal method')
plt.plot(range(3, power), error_simp, label = 'Simpsons method')
plt.plot([2.5,18],[10**-9,10**-9], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.xlabel('Powers of $N=2^n$', fontsize=15)
plt.ylabel('Errors', fontsize=15)
plt.title('Error calculation for Dawson function\n(Respect to scipy.special.dawsn)')
plt.legend()
plt.show()

#time consumption
start = time()
for i in range(0,50):
    Daws(x, 2**17, 'Trap')
end = time()
time_trap = (end - start) / 50

start = time()
for i in range(0,50):
    Daws(x, 2**10, 'Simp')
end = time()
time_simp = (end - start) / 50

start = time()
for i in range(0,50):
    Daws(x, 2, 'Scipy')
end = time()
time_scipy = (end - start) / 50
print('----------Q2a ii----------')
print('Average Time consumption, Trapezoidal method, n=17: ', time_trap, 's')
print('Average Time consumption, Simpsons method, n=10: ', time_simp, 's')
print('Average Time consumption, scipy.special.dawns: ', time_scipy, 's')
print('--------------------------\n')




############################### a iii ########################################

x = 4
n_1 = 32
n_2 = 64

#Trapezoidal method
I1_trap = Daws(x, n_1, 'Trap')          #calculate I1 and I2
I2_trap = Daws(x, n_2, 'Trap')
error_trap = abs(I2_trap - I1_trap) / 3

#Simpson's method
I1_simp = Daws(x, n_1, 'Simp')          #calculate I1 and I2
I2_simp = Daws(x, n_2, 'Simp')
error_simp = abs(I2_simp - I1_simp) / 15
print('----------Q2a iii----------')
print('Error of Trapezoidal method, N1=32 N2=64:', error_trap)
print('Error of Simpsons method, N1=32 N2=64:', error_simp)
print('--------------------------\n')

