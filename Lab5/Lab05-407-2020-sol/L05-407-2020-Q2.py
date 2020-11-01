# This script contains the answers to Q2 of Lab05, about image deconvolution.
# Author: Nico Grisouard

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

ftsz = 12
font = {'family': 'normal', 'size': ftsz}  # font size
rc('font', **font)


# Q4a ------------------------------------------------------------------------|
b = np.loadtxt('blur.txt')
plt.figure(figsize=(4, 4))
plt.imshow(b, cmap='gray')
plt.tight_layout()
plt.savefig('blurred.png')

rows, cols = b.shape


# Q4b ------------------------------------------------------------------------|
sigma = 25
gauss = np.empty((rows, cols))
for i in range(rows):
    ip = i
    if ip > rows/2:
        ip -= rows  # bottom half of rows moved to negative values
    for j in range(cols):
        jp = j
        if jp > cols/2:
            jp -= cols  # right half of columns moved to negative values

        gauss[i, j] = np.exp(-.5*(ip**2 + jp**2)/sigma**2)  # compute gaussian

plt.figure(figsize=(5, 5))
plt.imshow(gauss, cmap='gray')
plt.tight_layout()
plt.savefig('psf.png')


# Q4c ------------------------------------------------------------------------|
Fg = np.fft.rfft2(gauss)
Fb = np.fft.rfft2(b)

Fa = 0*Fb
for k in range(Fb.shape[0]):
    for l in range(Fb.shape[1]):
        if abs(Fg[k, l]) > 1e-3:
            Fa[k, l] = Fb[k, l]/Fg[k, l]/rows/cols
        else:
            Fa[k, l] = Fb[k, l]/rows/cols

a = np.fft.irfft2(Fa)

plt.figure(figsize=(4, 4))
plt.imshow(a, cmap='gray')
plt.tight_layout()
plt.savefig('unblurred.png')

# plt.show()
