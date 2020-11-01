# This script contains the answers to Q1c of Lab05, about the Dow
# Author: Nicolas Grisouard

import numpy as np
import matplotlib.pyplot as plt
import dcst
from matplotlib import rc

font = {'family': 'normal', 'size': 15}  # font size
rc('font', **font)


# Q1ca -----------------------------------------------------------------------|
y = np.loadtxt("dow2.txt")

plt.figure(1, figsize=(10, 4))
plt.plot(y, label='raw DJIA')
plt.grid()
plt.xlabel('Time (days)')
plt.ylabel('DJIA index')
plt.autoscale(enable=True, axis='x', tight=True)

fy = np.fft.rfft(y)
N_coeffs = len(fy)
fy_lopass = 1*fy
fy_lopass[int(0.02*N_coeffs):] = 0.
y_lopass = np.fft.irfft(fy_lopass)

plt.plot(y_lopass, '--', label='low-pass filtered')

# Q1cb -----------------------------------------------------------------------|
cty = dcst.dct(y)
cty_lopass = 1*cty
cty_lopass[int(0.02*N_coeffs):] = 0.
y_lopass_ct = dcst.idct(cty_lopass)

plt.plot(y_lopass_ct, ':', label='low-pass filtered, CT')

plt.legend()
plt.tight_layout()
plt.savefig('dow-nonperiodic.png', dpi=150)

# plt.show()
