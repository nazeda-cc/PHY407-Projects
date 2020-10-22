# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 05:51:01 2020

@author: Zirui Wan
"""

import numpy as np

# define constants
sigma = 1
epsilon = 1
m = 1



def U(r):
    """ Function to calculate Lennard-Jones potential given radius r
    INPUT:
        r[float]: radius from center of potential
    OUTPUT:
        uu[float]: calculated L-J potential
    """
    uu = 4*epsilon*((sigma/r)**12 - (sigma/r)**6)
    return uu
    
def acc(r):
    """ Function to calculate force due to Lennard-Jones potential given radius r
    INPUT:
        r[float]: radius from center of potential
    OUTPUT:
        ff[float]: calculated L-J force
    """
    ff = 48*epsilon*(sigma**12/r**13 - sigma**6/2/r**7)/m
    return ff


def f(r, t):
    """ Function calculate first-order derivatives for the Verlet algorithm.
    INPUT:
        r[floats]: array of the state of the system: 4 positions (x1, y1, x2, y2)
        t[float]: time
    OUTPUT:
        fr[floats]: array of accelerations for 2 particles along x and y directions
    """
    # extract x, y, vx, vy information from the state array
    r1 = r[:2]
    r2 = r[2:]

    # calculate radius of orbit squared
    dx1 = r1[0] - r2[0]
    dy1 = r1[1] - r2[1]
    dx2 = r2[0] - r1[0]
    dy2 = r2[1] - r1[1]
    rr1 = np.sqrt(dx1**2 + dy1**2)
    rr2 = np.sqrt(dx2**2 + dy2**2)
    
    # calculate accelaration on particle 1
    fvx1 = acc(rr1)*dx1/rr1
    fvy1 = acc(rr1)*dy1/rr1
    # calculate accelaration on particle 2
    fvx2 = acc(rr2)*dx2/rr2
    fvy2 = acc(rr2)*dy2/rr2
    
    fr = np.array([fvx1, fvy1, fvx2, fvy2])
    return fr
