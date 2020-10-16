# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:15:57 2020

@author: rundo
"""

from matplotlib import pyplot as plt
from Lab05_Q1function import *
import numpy as np
from numpy import fft
from dcst import *

file1 = open('piano.txt')
piano = file1.readlines()

file2 = open('trumpet.txt')
trumpet = file2.readlines()

for i in range(len(piano)):
    piano[i] = piano[i].strip('\n')
    piano[i] = float(piano[i])
    
for i in range(len(trumpet)):
    trumpet[i] = trumpet[i].strip('\n')
    trumpet[i] = float(trumpet[i])
    
    
plt.figure(3)
plt.plot(piano)
plt.title('Wave form of Piano')
plt.axis('off')
plt.figure(4)
plt.plot(trumpet)
plt.title('Wave form of Trumpet')    
plt.axis('off')
piano_spec = fft.rfft(piano)
trumpet_spec = fft.rfft(trumpet)

plt.figure(1)
plt.plot(abs(piano_spec[:10000]))
plt.xlabel('$k$, Frequency spectrum')
plt.ylabel('$|c_k|$, Spectrum magnitude')
plt.title('Q1d, Spectrum plot of piano')
plt.figure(2)
plt.plot(abs(trumpet_spec[:10000]))
plt.xlabel('$k$, Frequency spectrum')
plt.ylabel('$|c_k|$, Spectrum magnitude')
plt.title('Q1d, Spectrum plot of trumpet')

for i in range(len(piano_spec)):
    if piano_spec[i] > 3e7:
        print('Piano, k:', i)
        
for i in range(len(trumpet_spec)):
    if trumpet_spec[i] > 0.2e8:
        print('trumpet, k:', i)
        