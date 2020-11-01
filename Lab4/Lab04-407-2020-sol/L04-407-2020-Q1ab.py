# Author: Nicolas Grisouard
# The script contains answers to Q1 of lab 04 about solving linear
# systems of equations

import numpy as np
from numpy.linalg import solve
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib import rc
import SolveLinear_sol as sl
from time import time


def check_x(A_in, v_in, x):
    """ This function checks the solution given by the three methods of
    resolution of linear systems """
    return np.mean(abs(v_in - np.dot(A_in, x)))


font = {'family': 'normal', 'size': 16}  # font size
rc('font', **font)


# %% Q1a - WAS NOT REQUIRED --------------------------------------------------|
A_62 = np.array([[2,  1,  4,  1],  # the matrix (6.2) in textbook
                 [3,  4, -1, -1],
                 [1, -4,  1,  5],
                 [2, -2,  1,  3]], float)
v_62 = np.array([-4, 3, 9, 7], float)  # the vector (6.2) in textbook

print(sl.PartialPivot(A_62, v_62))


# %% Q1b ---------------------------------------------------------------------|
# First, define N
list_of_N = [8, 16, 32, 64, 128, 256, 512]
list_of_A = []  # will be a list of n*n-shaped numpy arrays
list_of_v = []  # will be a list of n-shaped numpy arrays
list_of_tLU = []  # will be a list of execution times for the LU decomposition
list_of_tge = []  # will be a list of execution times for the Gauss. elim.
list_of_tpp = []  # will be a list of execution times for the partial pivot
list_of_errLU = []  # will be a list of errors for the LU decomposition
list_of_errge = []  # will be a list of errors for the gaussian elimination
list_of_errpp = []  # will be a list of errors for the partial pivot

for i, N in enumerate(list_of_N):  # for each size, I create an A and a v
    list_of_A.append(rand(N, N))
    list_of_v.append(rand(N))

for i, N in enumerate(list_of_N):
    A = list_of_A[i]
    v = list_of_v[i]

    # First, LU decomposition
    start = time()
    x = solve(A, v)
    end = time()
    list_of_tLU.append(end - start)
    list_of_errLU.append(check_x(A, v, x))

    # Second, Gaussian elimination
    start = time()
    x = sl.GaussElim(A, v)
    end = time()
    list_of_tge.append(end - start)
    list_of_errge.append(check_x(A, v, x))

    # Third, partial pivot
    start = time()
    x = sl.PartialPivot(A, v)
    end = time()
    list_of_tpp.append(end - start)
    list_of_errpp.append(check_x(A, v, x))

plt.figure()
plt.semilogy(list_of_N, list_of_tLU, '+-', label='LU decomposition')
plt.semilogy(list_of_N, list_of_tge, '+-', label='Gaussian elim.')
plt.semilogy(list_of_N, list_of_tpp, '+-', label='Partial pvt')
plt.xlabel('$N$')
plt.ylabel('Execution time (s)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Lab04-Q1b-time.png', dpi=100)

plt.figure()
plt.semilogy(list_of_N, list_of_errLU, '+-', label='LU decomposition')
plt.semilogy(list_of_N, list_of_errge, '+-', label='Gaussian elim.')
plt.semilogy(list_of_N, list_of_errpp, '+-', label='Partial pvt')
plt.xlabel('$N$')
plt.ylabel('Error')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Lab04-Q1b-err.png', dpi=100)

plt.show()
