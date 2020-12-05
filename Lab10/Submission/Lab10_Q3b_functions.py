# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:41:55 2020

@author: rundo
"""
import numpy as np
from numpy import random


def f_w(x):
    
    return np.sqrt(2*np.pi) * np.exp(((x-5)**2)/2 - 2*np.abs(x-5))

def f(x):
    return np.exp(-2 * np.abs(x-5))

def mean(N):
    
    result = 0
    
    for i in range(N):
        result += f(10*random.random())
        
    return 10 * result / N

def importance(N):
    
    result = 0
    
    for i in range(N):
        
        x = random.normal(5, 1)
        
        if x < 0:               # just in case the draw is out of range
            x = 0               # See report for detailed discussion
        elif x > 10:
            x = 10
        
        result += f_w(x)
    
    return result / N
