# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:20:42 2020

@author: rundo
"""

import numpy as np
from matplotlib import pyplot as plt
from Lab07_Q3function import *



tsize = 10000
target = e/tsize
x = np.arange(h, L, h)
x_plot = x/a

##############################################################
n = 1
l = 0
print('For n=1, l=0, with stepsize = %fa,'%size, 'target size = e/%i'%tsize)
print('The calculated energy eigen value is:')
E1 = -15*e/n**2
E2 = -13*e/n**2

R2 = solve(E1, l)[0]

while abs(E1-E2)>target:
    R1, R2, p1 = R2, solve(E2, l)[0], solve(E2, l)[1]
    E1, E2 = E2, E2-R2*(E2-E1)/(R2-R1)
    



norm_simp1 = np.sqrt(normalize_simp(p1))
print(E2/e,'eV')
norm = np.sqrt(Simp(R_1_0, h, L, len(p1)))
print('----------------------------------')

plt.figure(1, figsize = (8,8))
plt.plot(x_plot, p1/norm_simp1, label = 'Simulated solution with RK4', color = 'k')
plt.plot(x_plot, R_1_0(x)*a**(1/2)/norm, label = 'Analytic solution', 
         linestyle = '-.', color = 'r', linewidth = 1)
plt.legend()
plt.title('Radial function $R(r)$, $n=1, l=0$', fontsize = 15)
plt.xlabel('Multiples of Bohr radius ($a_0 = 5.29*10^{-11}$m)', fontsize = 15)
plt.ylabel('Normalized wave function $R(r)/\int |R(r)|^2$', fontsize = 15)

plt.show()
###########################################################
n = 2
l = 0
print('For n=2, l=0, with stepsize = %fa,'%size, 'target size = e/%i'%tsize)
print('The calculated energy eigen value is:')
E1 = -15*e/n**2
E2 = -13*e/n**2

R2 = solve(E1, l)[0]

while abs(E1-E2)>target:
    R1, R2, p2 = R2, solve(E2, l)[0], solve(E2, l)[1]
    E1, E2 = E2, E2-R2*(E2-E1)/(R2-R1)
    

  

norm_simp2 = np.sqrt(normalize_simp(p2))
print(E2/e)

print('----------------------------------')

norm = np.sqrt(Simp(R_2_0, h, L, len(p2)))
plt.figure(2, figsize = (8,8))

plt.plot(x_plot, p2/norm_simp2, label = 'Simulated solution with RK4', color = 'k')
plt.plot(x_plot, R_2_0(x)*a**(1/2)/norm, label = 'Analytic solution', 
         linestyle = '-.', color = 'r', linewidth = 1)
plt.legend()
plt.title('Radial function $R(r)$, $n=2, l=0$', fontsize = 15)
plt.xlabel('Multiples of Bohr radius ($a_0 = 5.29*10^{-11}$m)', fontsize = 15)
plt.ylabel('Normalized wave function $R(r)/\int |R(r)|^2$', fontsize = 15)
plt.show()
##############################################################
n = 2
l = 1
print('For n=2, l=1, with stepsize = %fa,'%size, 'target size = e/%i'%tsize)
print('The calculated energy eigen value is:')
E1 = -15*e/n**2
E2 = -13*e/n**2

R2 = solve(E1, l)[0]

while abs(E1-E2)>target:
    R1, R2, p3 = R2, solve(E2, l)[0], solve(E2, l)[1]
    E1, E2 = E2, E2-R2*(E2-E1)/(R2-R1)
    



norm_simp3 = np.sqrt(normalize_simp(p3))
print(E2/e)
print('----------------------------------')
norm = np.sqrt(Simp(R_2_1, h, L, len(p3)))
plt.figure(3, figsize = (8,8))
plt.plot(x_plot, p3/norm_simp3, label = 'Simulated solution with RK4', color = 'k')
plt.plot(x_plot, R_2_1(x)*a**(1/2)/norm, label = 'Analytic solution', 
         linestyle = '-.', color = 'r', linewidth = 1)
plt.legend()
plt.title('Radial function $R(r)$, $n=2, l=1$', fontsize = 15)
plt.xlabel('Multiples of Bohr radius ($a_0 = 5.29*10^{-11}$m)', fontsize = 15)
plt.ylabel('Normalized wave function $R(r)/\int |R(r)|^2$', fontsize = 15)
plt.show()
###################################################
prob1 = normalize_simp(p1/norm_simp1)
prob2 = normalize_simp(p2/norm_simp2)
prob3 = normalize_simp(p3/norm_simp3)
print('Check normalization')
print(prob1)
print(prob2)
print(prob3)