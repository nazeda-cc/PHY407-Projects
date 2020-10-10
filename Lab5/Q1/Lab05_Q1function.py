# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:54:35 2020

@author: rundo
"""
import numpy as np

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c