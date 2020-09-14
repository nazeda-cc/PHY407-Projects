# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:36:37 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q2_function import Population as popu
from random import random

r = 3.738
p = 200                                     #set iterations
x0_1 = 0.1
epsilon = random()*10**-5                   #generate random epsilon
x0_2 = x0_1 + epsilon

x_1 = popu(x0_1, r, p)                      #iteration
x_2 = popu(x0_2, r, p)

year = np.arange(0,p,1)

plt.figure(figsize = (20,10))
plt.plot(year,x_1, linewidth=0.5, label='$x_0$')
plt.plot(year,x_2, linewidth=0.5, label='$x_0+\epsilon$')
plt.legend()
plt.xlabel('p (years)')
plt.ylabel('x')
plt.title('Q2f Population Evolution History')


