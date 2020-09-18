# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:28:32 2020

@author: rundo
"""

import numpy as np

def calculate_x(x0, r, pmax):
    """This function calculates the array of x
    INPUT:
    x0[float]: the initial normalized population x0
    r[float]: the maximum reproduction rate r
    pmax[int]: the total number of years

    OUTPUT:
    x[float]: an array of values xp for each year p
    """
    x = np.zeros((pmax))
    x[0] = x0
    for p in range(1, pmax):
        x[p] = r*(1 - x[p-1])*x[p-1]

    return x
