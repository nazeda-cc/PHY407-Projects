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
xa = solve(A, v)