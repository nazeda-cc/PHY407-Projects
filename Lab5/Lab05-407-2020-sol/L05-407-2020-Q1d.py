# This script contains the answers to Q1d of Lab05, about the Dow
# Author: Nico Grisouard

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

ftsz = 13
font = {'family': 'normal', 'size': ftsz}  # font size
rc('font', **font)


# Q3a ------------------------------------------------------------------------|
pn = np.loadtxt("piano.txt")
tp = np.loadtxt("trumpet.txt")

tm_array = np.arange(len(pn))/44100  # this is the time array, in s, for a
# recording at 44100 Hz.

plt.figure(1, figsize=(10, 5))  # you want a bigger figure for all subplots

plt.subplot(221)
plt.plot(tm_array, pn)
plt.grid()
plt.xlabel('Time (seconds)')
plt.title('piano waveform', fontsize=ftsz)
plt.autoscale(enable=True, axis='x', tight=True)

plt.subplot(223)
plt.plot(tm_array, tp)
plt.grid()
plt.xlabel('Time (seconds)')
plt.title('trumpet waveform', fontsize=ftsz)
plt.autoscale(enable=True, axis='x', tight=True)


# Q2b ------------------------------------------------------------------------|
fpn = np.fft.rfft(pn)
ftp = np.fft.rfft(tp)
freqs = np.fft.rfftfreq(len(tp), d=1./44100)

plt.subplot(222)
plt.plot(freqs[:10000], abs(fpn[:10000])**2)
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.title('Power spectrum for piano', fontsize=ftsz)
plt.autoscale(enable=True, axis='x', tight=True)

plt.subplot(224)
plt.plot(freqs[:10000], abs(ftp[:10000])**2)
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.title('Power spectrum for trumpet', fontsize=ftsz)
plt.autoscale(enable=True, axis='x', tight=True)

plt.tight_layout()
plt.savefig('instruments.png', dpi=150)

plt.show()
