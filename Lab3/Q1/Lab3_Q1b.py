# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:44:20 2020

@author: rundo
"""
import numpy as np
import scipy as sp
from scipy import special
from pylab import *
from Lab3_Q1b_function import *
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt



clf()
u = [6, 8, 10]
colours = ('r', 'g', 'b')
t = [24, 48, 72]
lines = (':', '-', '-.')

#method from comupational background
T = np.arange(-60, 30, 1)
plt.figure(figsize = (8, 8))
for (i, colour) in zip(u, colours):
    for (j, line) in zip(t, lines):
        plot_str = colour + line
        plt.plot(T, P(i, T, j), plot_str, linewidth = 1)

#Try to make some nice legends :D
line1 = Line2D([0,1],[0,1],linestyle='-', color='r')
line2 = Line2D([0,1],[0,1],linestyle='-', color='g')
line3 = Line2D([0,1],[0,1],linestyle='-', color='b')

line4 = Line2D([0,1],[0,1],linestyle=':', color='k')
line5 = Line2D([0,1],[0,1],linestyle='-', color='k')
line6 = Line2D([0,1],[0,1],linestyle='-.', color='k')

plt.legend([line1,line2,line3,line4,line5,line6], 
           ['$u_{10}=6$', '$\qquad\ \ \; 8$', '$\qquad\ \ \; 10$', '$t_h=24$', 
            '$\qquad\: 48$', '$\qquad\: 72$'])
plt.xlabel('$T_a (^{\circ} C)$', fontsize = 15)
plt.ylabel('Probability of Blowing snow, $P(T_a)$', fontsize = 15)
plt.title('Q1b, Probability of Blowing snow', fontsize = 15)

plt.show()