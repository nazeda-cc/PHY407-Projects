# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:21:53 2020

@author: rundo
"""
#%%
import numpy as np
import time
from numpy.linalg import solve
from numpy.random import rand
import scipy as sp
from Lab04_Q1_function import *
from matplotlib import pyplot as plt

########### test pivot ##############
A_in = np.array([[2, 1, 4, 1], 
                 [3, 4, -1, -1], 
                 [1, -4, 1, 5], 
                 [2, -2, 1, 3]], dtype = float)

v_in = [-4., 3., 9., 7.]



x = GaussElim(A_in, v_in)

xp = PartialPivot(A_in, v_in)




print(x)
print(xp)
#########################################
#%%
################## Q1b ###########################

N = 300

error_gau = []
error_par = []
error_lu = []

t_gau = []
t_par = []
t_lu = []

for i in range(5, N):
    A = rand(i,i)*10
    v = rand(i)*10

    t = time.time()
    x_gau = GaussElim(A, v)
    t_gau.append(time.time() - t)
    
    t = time.time()
    x_par = PartialPivot(A, v)
    t_par.append(time.time() - t)
    
    t = time.time()
    for i in range(50):
        x_lu = solve(A, v)
    t_lu.append((time.time() - t)/50)
    
    
    v_sol_gau = np.dot(A, x_gau)
    v_sol_par = np.dot(A, x_par)
    v_sol_lu = np.dot(A, x_lu)
    
    error_gau.append(np.mean(abs(v - v_sol_gau)))
    error_par.append(np.mean(abs(v - v_sol_par)))
    error_lu.append(np.mean(abs(v - v_sol_lu)))

n = np.arange(5, N)
plt.figure(1, figsize = (10, 6))
plt.plot(n, error_gau, linewidth = 0.5, label = 'GaussElim')
plt.plot(n, error_par, linewidth = 0.5, label = 'PartialPivot')
plt.plot(n, error_lu, linewidth = 0.5, label = 'LU')
plt.semilogy()
plt.xlabel('$N$, dimension of the matrix')
plt.ylabel('Errors')
plt.title('Q1b, Error plot for three methods')
plt.legend()
plt.show()

plt.figure(2, figsize = (10, 6))
plt.plot(n, t_gau, linewidth = 0.5, label = 'GaussElim')
plt.plot(n, t_par, linewidth = 0.5, label = 'PartialPivot')
plt.plot(n, t_lu, linewidth = 0.5, label = 'LU')
plt.xlabel('$N$, dimension of the matrix')
plt.ylabel('Runtime (s)')
plt.title('Q1b, Runtime plot for three methods')
plt.legend()
plt.semilogy()
plt.show()
