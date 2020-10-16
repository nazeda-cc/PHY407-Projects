# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:06:39 2020

@author: Zirui Wan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy.fft import rfft2, irfft2

# Load data from the file.
ifile = np.loadtxt("blur.txt")
# Output the blurred photo.
plt.figure()
plt.imshow(ifile, cmap=cm.Greys_r)
plt.title("Blurred photo")
plt.gray()


# Set number of rows and columns from the shape of the data.
L, K = len(ifile), len(ifile[0])

# Set sigma of gaussian point spread function.
sigma = 25
# Initialize the discrete point spread function.
gauss = np.zeros((L, K))

# Calculate the discrete point spread function.
for i in range(L):
    ip = i
    if ip > L/2:
        ip -= L   # bottom half of rows moved to negative values
    for j in range(K):
        jp = j
        if jp > K/2:
            jp -= K   # right half of columns moved to negative values
        gauss[i, j] = np.exp(-(ip**2+jp**2)/(2.0*sigma**2))   # compute gaussian

# Output the point spread function.
plt.figure()
plt.imshow(gauss, vmax=1e-2, cmap=cm.Greys_r)
plt.title("Point spread function")
plt.gray()

# Get Fourier transform coefficients for point spread function and blurred photo.
f = rfft2(gauss)
# Get Fourier transform coefficients for point spread function.
b = rfft2(ifile)
# Initialize Fourier transform coefficients for unblurred photo.
a = np.zeros((len(f), len(f[0])), complex)

# Calculate FT coefficients for unblurred photo.
for i in range(len(a)):
    for j in range(len(a[0])):
        if f[i, j] <= 1e-3:
            a[i, j] = b[i, j]/L/K
        else:
            a[i, j] = b[i, j]/f[i, j]/L/K

# Get the unblurred photo by inversely fourier transforming the coefficients.
y = irfft2(a)
# Output the unblurred photo.
plt.figure()
plt.imshow(y, cmap=cm.Greys_r)
plt.title("Unblurred photo")
plt.gray()