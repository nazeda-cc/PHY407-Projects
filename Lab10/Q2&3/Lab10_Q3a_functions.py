# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:38:19 2020

@author: rundo
"""
import numpy as np
from numpy import random

def p(x):
    
    return x**2


def f_w(x):
    
    return 1 / (np.exp(x) + 1)

def f(x):
    
    return x**(-0.5) / (np.exp(x) + 1)

def w(x):
    
    return x**(-0.5)



def mean(N):
    
    result = 0
    
    for i in range(N):
        
        result += f(random.random())
        
    return result / N


def importance(N):
    
    result = 0
    for i in range(N):
        
        result += f_w(p(random.random()))
        
    return 2 * result / N

