# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:04:02 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from Lab2_Q2_function import *

'''
def f(x):
    
    return x**4 - 2*x + 1

print(Trap(f, 0, 2, 10))
print(Simp(f, 0, 2, 10))
'''

x = 4
n = 20
print('Trapezoidal rule: ', Daws(x, n, 'Trap'))
print('Simpsons rule: ', Daws(x, n, 'Simp'))
print('Scipy: ', Daws(x, n, 'Scipy'))
