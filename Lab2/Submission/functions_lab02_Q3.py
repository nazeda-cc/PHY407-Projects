# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:56:14 2020

@author: Zirui Wan
"""

import numpy as np


alpha = 20e-6
lamb = 500e-9  # wavelength is 500 nm
focal = 1  # focal length is 1 m
d = 10e-2  # screen width is 10 cm
beta = alpha/2


def q(u):
    """ Function to calculate transmission function
    INPUT:
    u [float] : distance from slit to central line of the ten slits
    OUTPUT:
    qu [float] : transmission function
    """
    qu = np.sin( alpha * u) ** 2
    return qu


def I(x, q):
    """ Function to calculate intensity using Simpson's rule
    INPUT:
    x [float] : location on the screen
    q [function] : transmission function which takes 1 input
    OUTPUT:
    I [float] : intensity at x on the screen
    """
    
    I = 0
    
    # define slits here
    du = 1e-6
    u = np.arange(-9.e-05, 9.e-05+du, du)
    # two terminal points
    a = u[0]
    b = u[-1]
    I = np.sqrt(q(a))*np.exp(2j*np.pi*a*x/lamb/focal)      \
        + np.sqrt(q(b))*np.exp(2j*np.pi*b*x/lamb/focal)

    # calculate the two summing terms
    summ = 0
    for k in range(1, int(u.shape[0]/2)):
        unow = a + (2*k - 1)*du
        summ = summ + np.sqrt( q(unow) )*np.exp(2j*np.pi*unow*x/lamb/focal)
    I += summ*4
    summ = 0
    for k in range(1, int(u.shape[0]/2 - 1)):
        unow = a + (2*k)*du
        summ += np.sqrt( q(unow) )*np.exp(2j*np.pi*unow*x/lamb/focal)
        
    I += summ*2
    I = I*1/3*du
    I = np.abs(I)
    return I




# define a new transmission function
def qnew(u):
    """ Function to calculate transmission function
    INPUT:
    u [float] : distance from slit to central line of the ten slits
    OUTPUT:
    qu [float] : transmission function
    """
    qu = np.sin( alpha * u) ** 2 * np.sin( beta * u) ** 2
    return qu





# define a new transmission function
def q_square(u):
    """ Function to calculate transmission function
    INPUT:
    u [float] : distance from slit to central line of the ten slits
    OUTPUT:
    qu [float] : transmission function
    """
    if u < -1.5e-5 or u > 2.5e-5:
        qu = 1
    else:
        qu = 0
    return qu

def I_square(x):
    """ Function to calculate intensity using Simpson's rule
    INPUT:
    x [float] : location on the screen
    q_square [function] : function for square slits
    OUTPUT:
    I [float] : intensity at x on the screen
    """
    
    I = 0
    
    # define slits here
    du = 1e-6
    u = np.arange(-4.5e-05, 4.5e-05+du, du)
    # two terminal points
    a = u[0]
    b = u[-1]
    I = np.sqrt(q_square(a))*np.exp(2j*np.pi*a*x/lamb/focal)      \
        + np.sqrt(q_square(b))*np.exp(2j*np.pi*b*x/lamb/focal)

    # calculate the two summing terms
    summ = 0
    for k in range(1, int(u.shape[0]/2)):
        unow = a + (2*k - 1)*du
        summ = summ + np.sqrt( q_square(unow) )*np.exp(2j*np.pi*unow*x/lamb/focal)
    I += summ*4
    summ = 0
    for k in range(1, int(u.shape[0]/2 - 1)):
        unow = a + (2*k)*du
        summ += np.sqrt( q_square(unow) )*np.exp(2j*np.pi*unow*x/lamb/focal)
        
    I += summ*2
    I = I*1/3*du
    I = np.abs(I)
    return I