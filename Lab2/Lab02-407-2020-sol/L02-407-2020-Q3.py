#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Authors: Pauj J. Kushner and Nicolas Grisouard
Diffraction gratings: The purpose of this exercise is to
  create a code that will calculate and plot diffraction patterns in a
  manner similar to what we might see visually for a diffraction grating.

'''
# import required packages, including plotting
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import intfuncs as fi


def q(z):
    """ Define function q """
    alpha = np.pi/spacing  # Wavenumber for slits
    if case == 0:  # 5.19c
        return np.sin(alpha * z)**2
    if case == 1:  # 5.19e.i
        return np.sin(alpha * z)**2 * np.sin(0.5*alpha*z)**2
    if case == 2:  # 5.19e.ii
        if (0 < z < 10e-6):
            return 1.0
        elif (70e-6 < z < 90e-6):
            return 1.0
        else:
            return 0.0


def ig(z, x):
    """ Define function ig
    Integrand, given wavenumber of light k, focal length of light f """
    return q(z)**0.5 * np.exp(1j*k_wn*x*z/f)


# Define constants for grating
spacing = 20e-6  # Slit spacing in m
w = 10 * spacing  # Width of grating in m
lam = 500e-9  # Wavelength of the light
k_wn = 2 * np.pi / lam  # Wavenumber of the light
ws = 0.1  # Width of the screen, in m
hs = 250  # height in pixels
steps = 1000  # steps across the screen
f = 1.0  # focal length of lens
case = 2  # sub-question selector
font = {'family': 'normal',
        'size': 12}
rc('font', **font)


# set limits of integration for Simpson's rule, and other parameters
a, b = -w/2, w/2
N = 1000
h = (b - a)/N
result = np.empty([hs, steps + 1], float)

# calculate the integral using Simpson's rule
# x = - ws/2 + ws*i/steps

# Main loop
for i in range(steps + 1):
    x = - ws/2 + ws*i/steps
    s = fi.simps_int(a, b, steps, lambda z: ig(z, x))
    for j in range(hs):  # looping for clarity, but it is inefficient
        result[j, i] = abs(h*s/3)

# Make the density plot
plt.figure(figsize=(9, 2))
plt.imshow(result, extent=[-ws/2, ws/2, 0, ws/6], vmax=result.max())
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.set_cmap('cividis')
cb = plt.colorbar()
cb.ax.set_ylabel('Intensity (non-squared)')
plt.savefig('Lab02_Q3_case{0:d}.png'.format(case))
plt.show()
