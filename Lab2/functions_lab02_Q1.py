# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:56:14 2020

@author: Zirui Wan
"""

import numpy as np



def f(x):
    """ Function to calculate the function given x
    INPUT:
    x [float] is the input value
    OUTPUT:
    y [float] is the result outputted by the function
    """
    y = np.exp(-x**2)
    return y


def dfdx(x):
    """ Function to calculate the analytical derivative of f w.r.t. given x
    INPUT:
    x [float] is the input value
    OUTPUT:
    dfdx [float] is the analytical value of derivative of f
    """
    dfdx = -2*x*f(x)
    return dfdx

