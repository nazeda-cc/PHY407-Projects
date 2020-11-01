# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 05:51:45 2020

@author: Zirui Wan
"""

import numpy as np

# define constants
G = 6.6738e-11  # Newton's constant
M = 1.9891e30   # mass of Sun in kg

def f(r):
    """ Function calculate first-order and second-order derivatives.
    INPUT:
        r[floats]: array of the state of the system: 4 variables (x, y, vx, vy)
    OUTPUT:
        fr[floats]: array of first-order derivatives for the 4 variables
    """
    # extract x, y, vx, vy information from the state array
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    # calculate radius of orbit squared
    rr = np.sqrt(x**2 + y**2)
    # calculate first-order derivatives
    fx = vx
    fy = vy
    fvx = -G*M*x/rr**3
    fvy = -G*M*y/rr**3
    fr = np.array([fx, fy, fvx, fvy])
    return fr


def bulirsch(r, tpoints, H, delta):
    """ Function to calculate orbits using Bulirsch-Stoer algorithm.
    INPUT:
        r[floats]: array of the state of the system: 4 variables (x, y, vx, vy)
        tpoints[floats]: array of time points
        H[float]: the big time step
    OUTPUT:
        xpoints[floats]: array of calculated x positions
        ypoints[floats]: array of calculated y positions
    """
    xpoints = []
    ypoints = []
    # Do the "big steps" of size H
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        
        # Do one modified midpoint step to get things started
        n = 1
        r1 = r + 0.5*H*f(r)
        r2 = r + H*f(r1)
        
        # The array R1 stores the first row of the
        # extrapolation table, which contains only the single
        # modified midpoint estimate of the solution at the
        # end of the interval
        R1 = np.empty([1, 4], float)
        R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
        
        # Now increase n until the required accuracy is reached
        error = 2*H*delta
        
        while error > H*delta:
            n += 1
            h = H/n
    
            # Modified midpoint method
            r1 = r + 0.5*h*f(r)
            r2 = r + h*f(r1)
            for i in range(n-1):
                r1 += h*f(r2)
                r2 += h*f(r1)
    
            # Calculate extrapolation estimates.  Arrays R1 and R2
            # hold the two most recent lines of the table
            R2 = R1
            R1 =np. empty([n, 4], float)
            R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
            for m in range(1, n):
                epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
                R1[m] = R1[m-1] + epsilon
            error = np.sqrt(epsilon[0]**2 + epsilon[1]**2)
        # Set r equal to the most accurate estimate we have,
        # before moving on to the next big step
        r = R1[n-1]
        
    return xpoints, ypoints