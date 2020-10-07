# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 05:34:08 2020

@author: Zirui Wan
"""

import numpy as np


def f(x, c):
    """ Non-linear function for part (a)
    INPUT:
        x [float]: x variable
        c [float]: constant
    OUPUT:
        xprime [float]: root of the nonlinear equation
    """
    xprime = 1 - np.exp(-c*x)
    return xprime

def solve_parta(c):
    """ Function to solve f using relaxation method
    INPUT:
        c [float]: constant
    OUTPUT:
        xnew [float]: root found
    """
    xprev = 1
    xnew = 1 - np.exp(-c*xprev)
    while np.abs(xnew - xprev) > 1e-6:
        xprev = xnew
        xnew = f(xprev, c)
    return xnew

def solve_partb(c, omega):
    """ Function to solve f using over-relaxation method
    INPUT:
        c [float]: constant
        omega [float]: over-relaxation rate
    OUTPUT:
        xnew [float]: root found
        numiter [int]: number of iterations used
    """
    xprev = 1
    xnew = 1 - np.exp(-c*xprev)
    numiter = 1
    while np.abs(xnew - xprev) > 1e-6:
        xprev = xnew
        xnew = f(xprev, c)*(1 + omega) - omega*xprev
        numiter += 1
    
    return xnew, numiter



def wien_rhs(x):
    """ Function to compute right hand side of the Wien non-linear equation
    INPUT:
        x [float]: variable
    OUTPUT:
        xprime [float]: root found
    """
    xprime = 5 - 5*np.exp(-x)
    return xprime

def wien_f(x):
    """ Function to compute full equation of the Wien non-linear equation
    INPUT:
        x [float]: variable
    OUTPUT:
        f [float]: value of the equation
    """
    f = 5*np.exp(-x) + x - 5
    return f

def wien_dfdx(x):
    """ Function to compute derivative of the Wien non-linear equation
    INPUT:
        x [float]: variable
    OUTPUT:
        dfdx [float]: value of the derivative
    """
    dfdx = -5*np.exp(-x) + 1
    return dfdx


def binary(f, x1, x2, epsilon):
    """ Function to solve Wien's equation using binary search method
    INPUT:
        f : name of function
        x1 [float]: lower bound of initial guess
        x2 [float]: upper bound of initial guess
        epsilon [float]: target accuracy
    OUTPUT:
        x1 [float]: root found
        numiter [int]: number of iterations used
    """
    numiter = 0
    while np.abs(x1 - x2) > epsilon:
        xprime = (x1 + x2)/2
        if f(xprime)*f(x1) > 0:
            x1 = xprime
        else:
            x2 = xprime
        numiter += 1
    return x1, numiter


def relaxation(rhs, x0, epsilon):
    """ Function to solve Wien's equation using relaxation method
    INPUT:
        rhs : name of right-hand-side function
        x0 [float]: initial guess
        epsilon [float]: target accuracy
    OUTPUT:
        xnew [float]: root found
        numiter [int]: number of iterations used
    """
    xprev = x0
    xnew = rhs(xprev)
    numiter = 1
    while np.abs(xnew - xprev) > epsilon:
        xprev = xnew
        xnew = rhs(xprev)
        numiter += 1
    return xnew, numiter


def newton(f, dfdx, x0, epsilon):
    """ Function to solve Wien's equation using Newton's method
    INPUT:
        f : name of full equation function
        dfdx : name of the derivative function
        x0 [float]: initial guess
        epsilon [float]: target accuracy
    OUTPUT:
        xnew [float]: root found
        numiter [int]: number of iterations used
    """
    xprev = x0
    xnew = xprev - f(xprev)/dfdx(xprev)
    numiter = 1
    while np.abs(xnew - xprev) > epsilon:
        xprev = xnew
        xnew = xprev - f(xprev)/dfdx(xprev)
        numiter += 1
    return xnew, numiter

