# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:04:02 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from Lab2_Q2a_function import *

############# a i ############################################################
x = 4
n = 8
print('Trapezoidal rule: ', Daws(x, n, 'Trap')[0])
print('Simpsons rule: ', Daws(x, n, 'Simp')[0])
print('Scipy: ', Daws(x, n, 'Scipy')[0])
##############################################################################



####### a ii #################################################################

###Real part###
x = 4
n = 2
power = 19
is_imag = 0  #this variable determines whether looks at real or imaginary part

error_trap = []
error_simp = []

for i in range(3, power):
    n = 2**i
    error_trap.append(abs(Daws(x, n, 'Trap')[is_imag] - 
                          Daws(x, n, 'Scipy')[is_imag]))
    error_simp.append(abs(Daws(x, n, 'Simp')[is_imag] - 
                          Daws(x, n, 'Scipy')[is_imag]))

plt.figure(figsize=(6,8))
plt.plot(range(3, power), error_trap, label = 'Trapezoidal method')
plt.plot(range(3, power), error_simp, label = 'Simpsons method')
plt.plot([2.5,18],[10**-9,10**-9], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error calculation for Dawson function real part \n \
          (Respect to scipy.special.dawsn)')
plt.legend()
plt.show()

###Imaginary part###
x = 0.5j
n = 2
power = 19
is_imag = 1  #this variable determines whether looks at real or imaginary part

error_trap = []
error_simp = []

for i in range(3, power):
    n = 2**i
    error_trap.append(abs(Daws(x, n, 'Trap')[is_imag] - 
                          Daws(x, n, 'Scipy')[is_imag]))
    error_simp.append(abs(Daws(x, n, 'Simp')[is_imag] - 
                          Daws(x, n, 'Scipy')[is_imag]))

plt.figure(figsize=(6,8))
plt.plot(range(3, power), error_trap, label = 'Trapezoidal method')
plt.plot(range(3, power), error_simp, label = 'Simpsons method')
plt.plot([2.5,18],[10**-9,10**-9], linestyle = '--', linewidth = 1)
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error calculation for Dawson function imaginary part \n \
          (Respect to scipy.special.dawsn)')
plt.legend()
plt.show()
##############################################################################

############################### a iii ########################################

####### Real part ################################
x = 4
n = 2
power = 19
is_imag = 0
## Trapezoidal method ####

integral_trap = []
error_trap = []
for i in range(5, power):
    n = 2**i
    integral_trap.append(Daws(x, n, 'Trap')[is_imag])

for i in range(0, len(integral_trap) - 1):
    error_trap.append(abs(integral_trap[i+1]-integral_trap[i]) * (1/3))
    
## Simpsons method #######
integral_simp = []
error_simp = []
for i in range(5, power):
    n = 2**i
    integral_simp.append(Daws(x, n, 'Simp')[is_imag])

for i in range(0, len(integral_simp) - 1):
    error_simp.append(abs(integral_simp[i+1]-integral_simp[i]) * (1/3))
    
print(error_trap)
print(error_simp)
plt.figure(figsize=(6,8))
plt.plot(range(5, power-1), error_trap, label = 'Trapezoidal method')
plt.plot(range(5, power-1), error_simp, label = 'Simpsons method')
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error estimation for Dawson function real part \n \
          (using textbook method)')
plt.legend()
plt.show()

####### Imaginary part ################################
x = 0.5j
n = 2
power = 19
is_imag = 1
## Trapezoidal method ####

integral_trap = []
error_trap = []
for i in range(5, power):
    n = 2**i
    integral_trap.append(Daws(x, n, 'Trap')[is_imag])

for i in range(0, len(integral_trap) - 1):
    error_trap.append(abs(integral_trap[i+1]-integral_trap[i]) * (1/3))
    
## Simpsons method #######
integral_simp = []
error_simp = []
for i in range(5, power):
    n = 2**i
    integral_simp.append(Daws(x, n, 'Simp')[is_imag])

for i in range(0, len(integral_simp) - 1):
    error_simp.append(abs(integral_simp[i+1]-integral_simp[i]) * (1/3))
    
print(error_trap)
print(error_simp)
plt.figure(figsize=(6,8))
plt.plot(range(5, power-1), error_trap, label = 'Trapezoidal method')
plt.plot(range(5, power-1), error_simp, label = 'Simpsons method')
plt.semilogy()
plt.xlabel('Powers of $N=2^n$')
plt.ylabel('Errors')
plt.title('Error estimation for Dawson function imaginray part \n \
          (using textbook method)')
plt.legend()
plt.show()