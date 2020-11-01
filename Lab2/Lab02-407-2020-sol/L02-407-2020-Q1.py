"""
Calculate finite difference approximations to exp(-x**2)
Authors: Paul Kushner & Nicolas Grisouard, University of Toronto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from pylab import plot, legend, show, figure, xscale, yscale, savefig


def f(x):
    """ Function to differentiate: Gaussian """
    return np.exp(-x**2)


font = {'family': 'normal',
        'size': 12}

rc('font', **font)


N = 17  # number of h's to test
x0 = 0.5  # point at which to evaluate everything
exact = -2 * x0 * f(x0)  # exact value of the derivative
error_forward = np.empty(N)   # initializing fwd errors
error_centred = np.empty(N)   # initializing ctr errors
h = np.empty(N)

# prepare table headers of on-screen printout
print('   h     |    fwd    |  cntrd    | fwd err  | cntrd err')

for jj in range(N):
    h[jj] = 10**(-jj)
    df = (f(x0+h[jj]) - f(x0)) / h[jj]  # forward d/dx
    dfc = (f(x0+h[jj]) - f(x0-h[jj])) * .5 / h[jj]  # cntr d/dx
    error_forward[jj] = abs((df - exact)/exact)
    error_centred[jj] = abs((dfc - exact)/exact)
    print('{0:3.2e} | {1:3.2e} | {2:3.2e} | {3:3.2e} | {4:3.2e}'
          .format(h[jj], df, dfc, error_forward[jj], error_centred[jj]))


plt.figure(1)
ax = plt.gca()
ax.loglog(h, error_forward, label='forward difference error')
ax.loglog(h, error_centred, '--', label='centred difference error')
ax.set_xlabel('$h$')
ax.set_ylabel('error')
ax.set_aspect('equal')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('Lab02-Q1.png')
plt.show()
