# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:01:26 2020

@author: rundo
"""

from matplotlib import pyplot as plt
from Lab05_Q1function import *
import numpy as np
from numpy import fft
from dcst import *

file = open('dow2.txt')
dow = file.readlines()



for i in range(len(dow)):
    dow[i] = dow[i].strip('\n')
    dow[i] = float(dow[i])
    
#plt.plot(dow)
#%%
spec = fft.rfft(dow)
for i in range(int(0.02*len(spec)), len(spec)):
    spec[i] = 0
    
dow_a = fft.irfft(spec)
plt.figure(1)
plt.plot(dow)
plt.plot(dow_a, 'r', linewidth = 1)
plt.xlabel('Days')
plt.ylabel('Dow Jones Industrial Average')
plt.title('DFT')

#%%
spec = dct(dow)
for i in range(int(0.02*len(spec)), len(spec)):
    spec[i] = 0
    
dow_a = idct(spec)
plt.figure(2)
plt.plot(dow)
plt.plot(dow_a, 'r', linewidth = 1)
plt.xlabel('Days')
plt.ylabel('Dow Jones Industrial Average')
plt.title('DCT')