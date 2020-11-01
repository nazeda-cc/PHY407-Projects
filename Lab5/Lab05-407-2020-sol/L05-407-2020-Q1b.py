# This script contains the answers to Q1b of Lab05, about the Dow
# Author: Nico Grisouard


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


font = {'family': 'normal', 'size': 14}  # font size
rc('font', **font)

# Q2a ------------------------------------------------------------------------|
y = np.loadtxt("dow.txt")

plt.figure(1, figsize=(10, 3))
plt.plot(y, label='raw DJIA')
plt.grid()
plt.xlabel('Time (days)')
plt.ylabel('DJIA index')
plt.autoscale(enable=True, axis='x', tight=True)


# Q2b ------------------------------------------------------------------------|
fy = np.fft.rfft(y)


# Q2c ------------------------------------------------------------------------|
N_coeffs = len(fy)
fy_lopass = 1*fy
fy_lopass[N_coeffs//10:] = 0.

y_lopass = np.fft.irfft(fy_lopass)

plt.plot(y_lopass, '--', label='low-pass filtered')  # , 'r--')


# Q2d ------------------------------------------------------------------------|
fy_vlopass = 1*fy
fy_vlopass[int(0.02*N_coeffs):] = 0.

y_vlopass = np.fft.irfft(fy_vlopass)

plt.plot(y_vlopass, label='very-low-pass filtered')
plt.legend()
plt.tight_layout()
plt.savefig('dow.png', dpi=150)

plt.figure(2, figsize=(10, 3))
plt.plot(y, label='raw DJIA')
plt.plot(y_lopass, '--', label='low-pass filtered')
plt.plot(y_vlopass, '-.', label='very-low-pass filtered')
plt.grid()
plt.xlim([400., 500.])
plt.ylim([7000., 12000.])
plt.xlabel('Time (days)')
plt.ylabel('DJIA index')
plt.legend()
plt.tight_layout()
plt.savefig('dow_close.png', dpi=150)

# plt.show()
