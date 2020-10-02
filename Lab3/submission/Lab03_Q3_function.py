# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:31:44 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
import struct
######################### Function to read the target file ##################
def read_and_show(file):
    f = open(file, 'rb')
    Lat = np.ones([1201, 1201], int)*0      #initiate elevation matrix
    
    for i in range(len(Lat)):
        for j in range(len(Lat)):
            
            buf = f.read(2)

            if struct.unpack('>h', buf)[0] <= -10000:   #calculate the elevation
                                                        #if the value is invalid
                Lat[i][j] = (Lat[i-1][j] + Lat[i][j-1]) / 2
            
            else:
                Lat[i][j] = struct.unpack('>h', buf)[0]

    return Lat
##############################################################################


######################### Function to calculate gradient #####################
def gradient(Lat, h):
    grad = np.ones([len(Lat), len(Lat)], list)*0
    length = len(grad)
    
    for i in range(length):                 #loop through rows (y axis)
    
        if i == 0:                          #check if at top end
        
            for j in range(length):         #loop through columns (x axis)
                grad[i][j] = [0,0]
            
                if j == 0:                  #check if at left end
                    #forward derivative for y
                    grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                    #forward derivative for x
                    grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
                
                elif j == length - 1:       #check if at right end
                    #forward derivative for y
                    grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                    #backward derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
                
                else:
                    #forward derivative for y
                    grad[i][j][0] = (Lat[i][j] - Lat[i+1][j]) / h
                    #central derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
                
        elif i == length - 1:               #check if at bottom end
        
            for j in range(length):         #loop through columns (x axis)
                grad[i][j] = [0,0]
            
                if j == 0:                  #check if at left end
                    #backward derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                    #forward derivative for x
                    grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
            
                elif j == length - 1:       #check if at right end
                    #backward derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                    #backward derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
            
                else:
                    #backward derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i][j]) / h
                    #central derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
                
        else:                               #not at top or bottom
        
            for j in range(length):         #loop through columns (x axis)
                grad[i][j] = [0,0]
            
                if j == 0:                  #check if at left end
                    #central derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                    #forward derivative for x
                    grad[i][j][1] = (Lat[i][j] - Lat[i][j+1]) / h
                
                elif j == length - 1:       #check if at right end
                    #central derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                    #backward derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j]) / h
            
                else:                       #not left or right end
                    #central derivative for y
                    grad[i][j][0] = (Lat[i-1][j] - Lat[i+1][j]) / (2*h)
                    #central derivative for x
                    grad[i][j][1] = (Lat[i][j-1] - Lat[i][j+1]) / (2*h)
    
    return grad
##############################################################################

####################### function to generate relief map ######################
def intensity(grad, phi):
    #initiate relief map matrix
    intens = np.ones([len(grad), len(grad)], float)*0

    for i in range(1201):
        for j in range(1201):
        
            n = np.sqrt(grad[i][j][0]**2 + grad[i][j][1]**2 + 1)    #calculate norm
            intens[i][j] = - (-np.cos(phi) * grad[i][j][1] +        #calculate intensity
                             np.sin(phi) * grad[i][j][0]) / n
    return intens
##############################################################################

