# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:04:56 2020

@author: rundo
"""
import numpy as np

def fit(a, lamda, p):
    return a * np.exp(lamda * p)