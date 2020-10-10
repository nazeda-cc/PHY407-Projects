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

#%%
#plt.figure(2)
x1 = np.arange(5, 200)
x2 = np.arange(5, 75)

fig, (spectrum, zoom) = plt.subplots(2, 1, figsize = (8,12))
spec = fft.fft(count)
spectrum.plot(x1, abs(spec[5:200])**2)
zoom.plot(x2, abs(spec[5:75])**2)
spectrum.set(xlabel = '$k$, Frequency spectrum', ylabel = 'Spectrum magnitude')
spectrum.set_title('$k$ up to 200')
zoom.set(xlabel = '$k$, Frequency spectrum', ylabel = 'Spectrum magnitude')
zoom.set_title('Zoomed, $k$ up to 75')
#plt.xlabel('Frequency spectrum')
#plt.ylabel('Spectrum magnitude')


#plt.subplots(2)

