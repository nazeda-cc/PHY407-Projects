# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:53:27 2020

@author: rundo
"""

from matplotlib import pyplot as plt
from Lab05_Q1function import *
import numpy as np
from numpy import fft
#from fft_ts import *


file = open('sunspots.txt')
spots = file.readlines()

month = []
count = []

for i in range(len(spots)):
    spots[i] = spots[i].split('\t')
    spots[i][1] = spots[i][1].strip('\n')
    spots[i][0] = int(spots[i][0])
    spots[i][1] = float(spots[i][1])
    month.append(spots[i][0])
    count.append(spots[i][1])


#%%
plt.figure(figsize = (10, 5))
plt.plot(month, count, linewidth=0.5)
plt.xlabel('Months')
plt.ylabel('Spots count')
plt.title('Q1a, Sunspots count cycle')

#%%
#plt.figure(2)

spec = fft.fft(count)
x1 = np.arange(5, len(spec))
x2 = np.arange(5, 75)
x3 = np.arange(3000, len(spec))

#fig, (spectrum, zoom, zoom2) = plt.subplots(3, 1, figsize = (8,18))
plt.figure(4)
plt.plot(x1, abs(spec[5:])**2)
plt.xlabel('$k$, Frequency spectrum')
plt.ylabel('Spectrum magnitude, $|c_k|^2$')
plt.title('Entire spectrum plot, zero ignored')

plt.figure(2)
plt.plot(x2, abs(spec[5:75])**2)
plt.xlabel('$k$, Frequency spectrum')
plt.ylabel('Spectrum magnitude, $|c_k|^2$')
plt.title('Zoomed, $k$ up to 75')


plt.figure(3)
plt.plot(x3, abs(spec[3000:])**2)
#plt.plot(x2, abs(spec[5:75])**2)
plt.xlabel('$k$, Frequency spectrum')
plt.ylabel('Spectrum magnitude, $|c_k|^2$')
plt.title('Zoomed, $k$ from 3000 up to max')

'''
spectrum.set(, ylabel = )
spectrum.set_title('$k$ up to 200')
zoom.set(xlabel = '$k$, Frequency spectrum', ylabel = 'Spectrum magnitude, $|c_k|^2$')
zoom.set_title()
zoom2.set(xlabel = '$k$, Frequency spectrum', ylabel = 'Spectrum magnitude, $|c_k|^2$')
zoom2.set_title('Zoomed, $k$ from 3000 up to max')
#plt.xlabel('Frequency spectrum')
#plt.ylabel('Spectrum magnitude')


#plt.subplots(2)
'''

