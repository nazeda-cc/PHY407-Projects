# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:29:18 2020

@author: rundo
"""
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

A = np.array([[1/r1 + 1/r4 + c1*omega*1j, -c1*omega*1j, 0], 
              [-c1*omega*1j, 1/r2 + 1/r5 + (c1+c2)*omega*1j, -c2*omega*1j], 
              [0, -c2*omega*1j, (1/r3 + 1/r6 + c2*omega*1j)]])
v = np.array([x_plus/r1, x_plus/r2, x_plus/r3], complex)

x = PartialPivot(A, v)

v1, w1 = (np.abs(x[0]), np.angle(x[0]))
v2, w2 = (np.abs(x[1]), np.angle(x[1]))
v3, w3 = (np.abs(x[2]), np.angle(x[2]))


t = np.arange(0, 0.0125, 0.0000005)

'''
v1t = v1*np.exp(omega*t*1j + w1*1j).real
v2t = v2*np.exp(omega*t*1j + w2*1j).real
v3t = v3*np.exp(omega*t*1j + w3*1j).real
'''
v1ta = (x[0]*np.exp(omega*t*1j)).real
v2ta = (x[1]*np.exp(omega*t*1j)).real
v3ta = (x[2]*np.exp(omega*t*1j)).real
v0ta = (3*np.exp(omega * t*1j)).real


'''
plt.figure(1)
plt.plot(t, v1t)
plt.plot(t, v2t)
plt.plot(t, v3t)
'''
plt.figure(2)
plt.plot(t, v1ta, label = '$V_1$')
plt.plot(t, v2ta, label = '$V_2$')
plt.plot(t, v3ta, label = '$V_3$')
plt.plot(t, v0ta, label = '$V_+$')
plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
plt.title('$R_6$=2k$\Omega$')
plt.legend()
plt.show()
##################################################
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

v1, w1 = (np.abs(x[0]), np.angle(x[0]))
v2, w2 = (np.abs(x[1]), np.angle(x[1]))
v3, w3 = (np.abs(x[2]), np.angle(x[2]))


t = np.arange(0, 0.0125, 0.0000005)
v1t = v1*np.exp(omega*t*1j + w1*1j).real
v2t = v2*np.exp(omega*t*1j + w2*1j).real
v3t = v3*np.exp(omega*t*1j + w3*1j).real
v0t = (3*np.exp(omega * t*1j)).real
'''
v1ta = (x[0]*np.exp(omega*t*1j)).real
v2ta = (x[1]*np.exp(omega*t*1j)).real
v3ta = (x[2]*np.exp(omega*t*1j)).real
'''
plt.figure(3)
plt.plot(t, v1t, label = '$V_1$')
plt.plot(t, v2t, label = '$V_2$')
plt.plot(t, v3t, label = '$V_3$')
plt.plot(t, v0t, label = '$V_+$')
plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
plt.title('$R_6$ replaced by an inductor')
plt.legend()
'''
plt.figure(4)
plt.plot(t, v1ta)
plt.plot(t, v2ta)
plt.plot(t, v3ta)
'''