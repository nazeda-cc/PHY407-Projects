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

def read_and_show(file):
    f = open(file, 'rb')
    Lat = np.ones([1201, 1201], int)*0
    for i in range(len(Lat)):
        for j in range(len(Lat)):
            buf = f.read(2)

            if struct.unpack('>h', buf)[0] <= -10000:
                Lat[i][j] = (Lat[i-1][j] + Lat[i][j-1]) / 2
            else:
                Lat[i][j] = struct.unpack('>h', buf)[0]

    

    return Lat




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



def intensity(grad, phi):
    
    intens = np.ones([len(grad), len(grad)], float)*0

    for i in range(1201):
        for j in range(1201):
        
            #phi = - 5 * np.pi / 6
            n = np.sqrt(grad[i][j][0]**2 + grad[i][j][1]**2 + 1)
            intens[i][j] = - (-np.cos(phi) * grad[i][j][1] + 
                             np.sin(phi) * grad[i][j][0]) / n
    return intens

'''
def show_location(location, w):
    location_on_grid = [0, 0]
    location_on_grid[0] = int((47 - location[0]) * 1200)    #y axis
    location_on_grid[1] = int((location[1] - 6) * 1200)     #x axis
    
    result_w = np.ones([200,200], float)*0
    result_intensity = np.ones([200,200], float)*0
    
    if location[0] < 100:
        if location[1] < 100:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[i][j]
            
        elif location[1] > 1100:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[i][1000+j]
        
        else:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[i][location_on_grid[0]-100+j]
    
    elif location[0] > 1100:
        if location[1] < 100:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[1000+i][j]
            
        elif location[1] > 1100:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[1000+i][1000+j]
        
        else:
            for i in range(0, 200):
                for j in range(0, 200):
                    result_w[i][j] = w[1000+i][location_on_grid[0]-100+j]
    
    else:
        if location[1] < 100:
            
            
        elif location[1] > 1100:
            
        
        else:
            
    
    return 
'''