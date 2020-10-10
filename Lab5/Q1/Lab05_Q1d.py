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
    
    
piano_spec = fft.rfft(piano)
trumpet_spec = fft.rfft(trumpet)

plt.figure(1)
plt.plot(abs(piano_spec[:10000]))
plt.figure(2)
plt.plot(abs(trumpet_spec[:10000]))