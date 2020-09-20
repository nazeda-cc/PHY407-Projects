# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:04:02 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from Lab2_Q2_function import *

''' Test code
def f(x):
    
    return x**4 - 2*x + 1

print(Trap(f, 0, 2, 10))
print(Simp(f, 0, 2, 10))
'''


### a i #####
x = 4
n = 8
print('Trapezoidal rule: ', Daws(x, n, 'Trap')[0])
print('Simpsons rule: ', Daws(x, n, 'Simp')[0])
print('Scipy: ', Daws(x, n, 'Scipy')[0])
############

''' Test code
x = np.arange(-1.5, 1.5, 0.01)
n = 8
T = []
S = []
Sci = []
for i in x:
    T.append(Daws(i*1j, n, 'Trap').imag) 
for i in x:
    S.append(Daws(i*1j, n, 'Simp').imag)
    
for i in x:
    Sci.append(Daws(i*1j, n, 'Scipy').imag)
plt.figure(1)
plt.plot(x, T)
plt.figure(2)
plt.plot(x, S)
plt.figure(3)
plt.plot(x, Sci)
plt.show()
'''

####### a ii #########

###Real part###
x = 4
n = 2
power = 19

error_trap = []
error_simp = []

for i in range(3, power):
    n = 2**i
    error_trap.append(abs(Daws(x, n, 'Trap')[0] - Daws(x, n, 'Scipy')[0]))
    error_simp.append(abs(Daws(x, n, 'Simp')[0] - Daws(x, n, 'Scipy')[0]))

plt.figure(figsize=(6,8))
plt.plot(range(3, power), error_trap, label = 'Trapezoidal method')
plt.plot(range(3, power), error_simp, label = 'Simpsons method')
plt.plot([2.5,18],[10**-9,10**-9], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error calculation for Dawson function real part')
plt.legend()

###Imaginary part###
x = 1.5j
n = 2
power = 19

error_trap = []
error_simp = []

for i in range(3, power):
    n = 2**i
    error_trap.append(abs(Daws(x, n, 'Trap')[1] - Daws(x, n, 'Scipy')[1]))
    error_simp.append(abs(Daws(x, n, 'Simp')[1] - Daws(x, n, 'Scipy')[1]))

plt.figure(figsize=(6,8))
plt.plot(range(3, power), error_trap, label = 'Trapezoidal method')
plt.plot(range(3, power), error_simp, label = 'Simpsons method')
plt.plot([2.5,18],[10**-9,10**-9], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error calculation for Dawson function imaginary part')
plt.legend()

plt.show()