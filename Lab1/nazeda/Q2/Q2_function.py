# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:41:05 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np

def Population(x_0, r, p):
    x = [None] * p                      #initialize x as an array
    x[0] = x_0                          #take initial value
    for i in range(0, p-1):
        x[i+1] = r * (1 - x[i]) * x[i]  #iteration
    return x