# Author: Nicolas Grisouard, University of Toronto
# Timing the mulitiplication of two matrices with two different methods

import matplotlib.pyplot as plt
import numpy as np
from time import time
import numpy.random as npr  # because why not

n_repeat = 10  # we will repeat every multiplication n_repeat times
# the above was not explicitely asked.
ftsz = 12  # font size for the figures

size_max = 100  # the side size of the largest matrices we will multiply
duration_silly = np.empty(size_max)  # this array will contain durations for
# the text method
duration_dot = np.empty(size_max)  # same, but for the dot method

duration_silly[0:1] = 0.  # no 0x0 nor 1x1 matrices
duration_dot[0:1] = 0.  # no 0x0 nor 1x1 matrices

N_array = np.arange(100)  # numpy range

for N in range(2, size_max):
    print('Size of matrices: ' + str(N))
    A = npr.random((N, N))  # because why not
    B = npr.random((N, N))  # idem
    C = np.empty((N, N))  # slightly faster than zeros

    start = time()  # initializing timer for silly
    for n in range(n_repeat):  # repeating the same thing for better stats
        for i in range(N):  # as in Example 4.3 of the book
            for j in range(N):
                for k in range(N):
                    C[i, j] = A[i, k] * B[k, j]
    end = time()
    duration_silly[N] = (end - start)/n_repeat  # the duration for this method

    start = time()  # initializing timer for dot product method
    for n in range(n_repeat):
        C = np.dot(A, B)
    end = time()
    duration_dot[N] = (end - start)/n_repeat  # the duration for this method


plt.figure()  # this figure is for the slow ("silly") method -----------------|

plt.subplot(211)  # durations as a function of N
plt.plot(N_array, duration_silly)
plt.xlabel('$N$, the size of the matrix', fontsize=ftsz)
plt.title('avg time it takes to multiply [s]', fontsize=ftsz)
plt.grid()

plt.subplot(212)  # durations as a function of N**3
plt.plot(N_array**3, duration_silly)
plt.xlabel('$N^3$', fontsize=ftsz)
plt.title('avg time it takes to multiply [s]', fontsize=ftsz)
plt.grid()
plt.tight_layout()  # otherwise, there are overlaps and crops

plt.savefig('L01-Q3-slow.png', dpi=300)  # dpi is for dots per inch


plt.figure()  # this figure is for the fast ("dot") method -------------------|

plt.subplot(211)  # durations as a function of N
plt.plot(N_array, duration_dot)
plt.xlabel('$N$, the size of the matrix', fontsize=ftsz)
plt.title('avg time it takes to multiply [s]', fontsize=ftsz)
plt.grid()

plt.subplot(212)  # durations as a function of N**3
plt.plot(N_array**3, duration_dot)
plt.xlabel('$N^3$', fontsize=ftsz)
plt.title('avg time it takes to multiply [s]', fontsize=ftsz)
plt.grid()
plt.tight_layout()  # otherwise, there are overlaps and crops

plt.savefig('L01-Q3-fast.png', dpi=300)  # dpi is for dots per inch
