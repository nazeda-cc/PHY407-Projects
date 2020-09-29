# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:06:57 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
from Lab3_Q3_function import *
import struct

f = open('N46E006.hgt', 'rb')

Lat = np.ones([1201, 1201], int)*0


for i in range(1201):
    for j in range(1201):
        buf = f.read(2)
        Lat[i][j] = struct.unpack('>h', buf)[0]


plt.imshow(Lat, vmin = -100)
plt.colorbar()


#grad = gradient(Lat, 420)




grad = np.ones([1201, 1201], list)*0
h = 420
length = len(grad)

for i in range(length):
    #for j in range(len(grad)):
    #print(i)
        #grad[i][j] = [0,0]
        
    if i == 0:
        for j in range(length):
            grad[i][j] = [0,0]
            
            if j == 0:
                grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
                
            elif j == length - 1:
                grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
                
            else:
                grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
                
    elif i == length - 1:
         for j in range(length):
            grad[i][j] = [0,0]
            
            if j == 0:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
            
            elif j == length - 1:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
            
            else:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
                
    else:
        for j in range(length):
            grad[i][j] = [0,0]
            
            if j == 0:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
                
            elif j == length - 1:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
            
            else:
                grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
          
                
                
                
                
                
                
                
                
                

