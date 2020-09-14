# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:44:06 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q2_function import Population as popu


p = 100
x_1 = popu(0.1, 2, p)
x_2 = popu(0.1, 2.5, p)
x_3 = popu(0.1, 3, p)
x_4 = popu(0.1, 3.5, p)
x_5 = popu(0.1, 4, p)

year = np.linspace(0,99,num=100)

plt.figure(figsize = (20,10))

plt.plot(year,x_1, label='r=2', linewidth=1)
plt.plot(year,x_2, label='r=2.5', linewidth=1)
plt.plot(year,x_3, label='r=3', linewidth=1)
plt.plot(year,x_4, label='r=3.5', linewidth=1)
plt.plot(year,x_5, label='r=4', linewidth=1)
plt.legend()


