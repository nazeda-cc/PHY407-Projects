# Author: Nico Grisouard, University of Toronto Physics
# Answer to questions related to finding roots and extrema

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.constants as pc  # physical constants


def f(x): return 5*(np.exp(-x) - 1.) + x


def df(x): return 1 - 5*np.exp(-x)


font = {'family': 'normal', 'size': 14}  # font size
rc('font', **font)

# Q3c ------------------------------------------------------------------------|
epsilon = 1e-6  # accuracy tolerance

# Binary search --------------------------------------------------------------|
x1 = 0.1  # lower bracket
x2 = 10.  # upper bracket

if f(x1)*f(x2) > 0.:  # I will assume we will never find the root right away
    raise NameError('Fct at brackets is of the same sign. Change brackets.')

i = 0  # iterations counter
while abs(x2-x1) > epsilon:
    i += 1
    xm = .5*(x1 + x2)
    if f(xm)*f(x1) > 0.:  # then the middle point is on same side as x1
        x1 = xm  # bring it closer to that side
    else:
        x2 = xm

print("Binary search: x = {0:.6f}, converged in {1} iterations"
      .format(0.5*(x1+x2), i))


# Newton's method ------------------------------------------------------------|
x1 = 1.  # is whatever at this point, just not too close to the guess
x2 = 10.  # initial guess
i = 0  # iterations counter
while abs(x2 - x1) > epsilon:
    i += 1
    x1 = x2
    x2 = x1 - f(x1)/df(x1)

print("Newton's method: x = {0:.6f}, converged in {1} iterations".format(
    x2, i))


# Secant method --------------------------------------------------------------|
x1 = 0.1  # lower bracket
x2 = 10.  # upper bracket
x3 = x2 - f(x2)*(x2-x1)/(f(x2) - f(x1))  # first iteration

i = 1  # iterations counter; I start at 1 because we've done it once before
while abs(x3 - x2) > epsilon:
    i += 1
    x1 = x2
    x2 = x3
    x3 = x2 - f(x2)*(x2-x1)/(f(x2) - f(x1))


print("Secant method: x = {0:.6f}, converged in {1} iterations".format(
    x2, i))


# Temperature of the Sun -----------------------------------------------------|
b = pc.Planck * pc.c / (pc.Boltzmann * x3)
lmbda = 502e-9  # [m] peak wavelength of Sun's spectrum

print("")
print("In any case, the temperature of the Sun is {0:.6e} K".format(b/lmbda))
