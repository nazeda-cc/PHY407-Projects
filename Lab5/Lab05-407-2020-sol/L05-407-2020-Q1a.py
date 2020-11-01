# This script contains the answers to Q1a of Lab05, about sun spots
# Author: Nicolas Grisouard

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

font = {'family': 'normal', 'size': 16}  # font size
rc('font', **font)

# Q1a ----------
y = np.loadtxt("sunspots.txt")

plt.figure(1, figsize=(12, 4))
plt.plot(y[:, 0], y[:, 1])
plt.grid()
plt.xlabel('Time (months)')
plt.ylabel('Number of sun spots')
plt.autoscale(enable=True, axis='x', tight=True)
plt.tight_layout()
plt.savefig('Sunspots_1749.png', dpi=150)

ncycles = 24

print("I count 24 cycles in {0:.1f} months".format(y[-1, 0]))
print("That's one cycle every {0:.1f} months".format(y[-1, 0]/ncycles))

# Q1b -----------
fy = abs(np.fft.rfft(y[:, 1]))**2

plt.figure(2, figsize=(12, 7))
plt.subplot(211)
plt.loglog(fy)
plt.ylabel('$|c_k|^2$')
plt.grid()
plt.autoscale(enable=True, axis='x', tight=True)

plt.subplot(212)
plt.loglog(fy)
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$|c_k|^2$')
plt.xlim([20., 30.])
plt.ylim([1e8, 3e9])
rticks = range(21, 27, 2)
plt.xticks(rticks, labels=['{}'.format(ii) for ii in rticks])
plt.tight_layout()
plt.savefig('Sunspots_1749_ft.png', dpi=150)

# Visually, the peak is at k=24, the number of cycles we found.
print("The period is {0:.1f} months".format(y[-1, 0]/ncycles))
