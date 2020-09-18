# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:35:19 2020

@author: rundo
"""
import numpy as np


def mult(A, B, N):
    
    C = np.ones([N, N], float)*0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k] * B[k,j]
                
    return C