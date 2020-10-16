# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:27:44 2020

@author: rundo
"""

from matplotlib import pyplot as plt
from Lab05_Q1function import *
import numpy as np
from numpy import fft

file = open('dow.txt')
dow = file.readlines()



for i in range(len(dow)):
    dow[i] = dow[i].strip('\n')
    dow[i] = float(dow[i])

#%%
spec = fft.rfft(dow)
for i in range(int(0.1*len(spec)), len(spec)):
    spec[i] = 0
#plt.figure()
#plt.plot(abs(spec)**2)

dow_a = fft.irfft(spec)
plt.figure(1)
plt.plot(dow, label = 'Original data')
plt.plot(dow_a, 'r', linewidth = 1, label = 'Smoothened data')
plt.xlabel('Days')
plt.ylabel('Dow Jones Industrial Average')
plt.legend()
plt.title('Q1b, with all but first 10% set as zero')

#%%
spec = fft.rfft(dow)
for i in range(int(0.02*len(spec)), len(spec)):
    spec[i] = 0
    
dow_a = fft.irfft(spec)
plt.figure(2)
plt.plot(dow, label = 'Original data')
plt.plot(dow_a, 'r', linewidth = 1, label = 'Smoothened data')
plt.xlabel('Days')
plt.ylabel('Dow Jones Industrial Average')
plt.title('Q1b, with all but first 2% set as zero')
plt.legend()