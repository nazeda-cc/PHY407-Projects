# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:20:09 2020

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

delta = []

for i in range(p):
    delta.append(x_2[i]-x_1[i])
    
plot