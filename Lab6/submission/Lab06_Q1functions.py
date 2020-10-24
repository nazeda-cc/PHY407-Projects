# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 05:51:45 2020

@author: Zirui Wan
"""

import numpy as np

# define constants
G = 1
M = 10
L = 2

def f(r, t):
    """ Function calculate first-order derivatives for the RK4 algorithm.
    INPUT:
        r[floats]: array of the state of the system: 4 variables (x, y, vx, vy)
        t[float]: time
    OUTPUT:
        fr[floats]: array of first-order derivatives for the 4 variables
    """
    # extract x, y, vx, vy information from the state array
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    # calculate radius of orbit squared
    rsq = x**2 + y**2
    # calculate first-order derivatives
    fx = vx
    fy = vy
    fvx = -G*M*x/rsq/np.sqrt(rsq + L**2/4)
    fvy = -G*M*y/rsq/np.sqrt(rsq + L**2/4)
    fr = np.array([fx, fy, fvx, fvy])
    return fr
