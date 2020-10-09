# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:29:18 2020

@author: rundo
"""
#%%
import numpy as np
import time
from numpy.linalg import solve
from numpy.random import rand
import scipy as sp
from Lab04_Q1_function import *
from matplotlib import pyplot as plt

r1 = 1000 
r3 = 1000
r5 = 1000
r2 = 2000
r4 = 2000
r6 = 2000

c1 = 1e-6
c2 = 0.5e-6

x_plus = 3
omega = 1000

#generate the matrix
A = np.array([[1/r1 + 1/r4 + c1*omega*1j, -c1*omega*1j, 0], 
              [-c1*omega*1j, 1/r2 + 1/r5 + (c1+c2)*omega*1j, -c2*omega*1j], 
              [0, -c2*omega*1j, (1/r3 + 1/r6 + c2*omega*1j)]])
v = np.array([x_plus/r1, x_plus/r2, x_plus/r3], complex)

#calculate with Partial Pivot
x = PartialPivot(A, v)

v1, w1 = (np.abs(x[0]), np.angle(x[0], deg=True))
v2, w2 = (np.abs(x[1]), np.angle(x[1], deg=True))
v3, w3 = (np.abs(x[2]), np.angle(x[2], deg=True))

#print(x)
print('----------- R6 = 2k Om -------------------')
print('The amplitude for V1 is', v1, 'V.', 'The phase is', w1, 'degree')
print('The amplitude for V2 is', v2, 'V.', 'The phase is', w2, 'degree')
print('The amplitude for V3 is', v3, 'V.', 'The phase is', w3, 'degree')

t = np.arange(0, 0.0125, 0.0000005)


v1ta = (x[0]*np.exp(omega*t*1j)).real
v2ta = (x[1]*np.exp(omega*t*1j)).real
v3ta = (x[2]*np.exp(omega*t*1j)).real
v0ta = (3*np.exp(omega * t*1j)).real



plt.figure(2)
plt.plot(t, v0ta, 'k-.', label = '$V_+$')
plt.plot(t, v1ta, label = '$V_1$')
plt.plot(t, v2ta, label = '$V_2$')
plt.plot(t, v3ta, label = '$V_3$')

plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
plt.title('Q1c, $R_6$=2k$\Omega$')
plt.legend()
plt.show()


#%%    Replace R6 with an inductor
r1 = 1000 
r3 = 1000
r5 = 1000
r2 = 2000
r4 = 2000
r6 = 2000j

c1 = 1e-6
c2 = 0.5e-6

x_plus = 3
omega = 1000

A = np.array([[1/r1 + 1/r4 + c1*omega*1j, -c1*omega*1j, 0], 
              [-c1*omega*1j, 1/r2 + 1/r5 + (c1+c2)*omega*1j, -c2*omega*1j], 
              [0, -c2*omega*1j, (1/r3 + 1/r6 + c2*omega*1j)]])
v = np.array([x_plus/r1, x_plus/r2, x_plus/r3], complex)

x = PartialPivot(A, v)
#print(x)
v1, w1 = (np.abs(x[0]), np.angle(x[0], deg=True))
v2, w2 = (np.abs(x[1]), np.angle(x[1], deg=True))
v3, w3 = (np.abs(x[2]), np.angle(x[2], deg=True))


t = np.arange(0, 0.0125, 0.0000005)

v1ta = (x[0]*np.exp(omega*t*1j)).real
v2ta = (x[1]*np.exp(omega*t*1j)).real
v3ta = (x[2]*np.exp(omega*t*1j)).real
v0ta = (3*np.exp(omega * t*1j)).real

print('----------- R6 replaced by an inductor -----------------')
print('The amplitude for V1 is', v1, 'V.', 'The phase is', w1, 'degree')
print('The amplitude for V2 is', v2, 'V.', 'The phase is', w2, 'degree')
print('The amplitude for V3 is', v3, 'V.', 'The phase is', w3, 'degree')


plt.figure(3)
plt.plot(t, v0ta, 'k-.', label = '$V_+$')
plt.plot(t, v1ta, label = '$V_1$')
plt.plot(t, v2ta, label = '$V_2$')
plt.plot(t, v3ta, label = '$V_3$')

plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
plt.title('Q1c, $R_6$ replaced by an inductor')
plt.legend()
