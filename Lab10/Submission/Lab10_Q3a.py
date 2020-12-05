# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:41:21 2020

@author: rundo
"""
import numpy as np
from numpy import random
from matplotlib import pyplot as plt
from Lab10_Q3a_functions import *


N = 10000           # number of sampling points

I_mean = np.empty(0)
I_impo = np.empty(0)

n = 100             # time of iterations

for i in range(n):
    
    I_mean = np.append(I_mean, mean(N))
    I_impo = np.append(I_impo, importance(N))
    
#%% Plots
fig, (mean_plot, impo_plot) = plt.subplots(2, figsize = (8, 10))

mean_plot.hist(I_mean, 10, range=[0.8, 0.88])
impo_plot.hist(I_impo, 10, range=[0.8, 0.88])

mean_plot.set_title('Mean value method')
impo_plot.set_title('Importance sampling method')

mean_plot.set(xlabel = '$I$ values', ylabel = 'Counts')
impo_plot.set(xlabel = '$I$ values', ylabel = 'Counts')

print('Standard deviation for Mean value method is:', np.std(I_mean))
print('Standard deviation for Importance sampling method is:', np.std(I_impo))









