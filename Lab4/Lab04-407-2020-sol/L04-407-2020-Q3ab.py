# Author: Nico Grisouard, University of Toronto Physics
# Answer to questions related to finding roots and extrema

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def f(x, c): return 1 - np.exp(-c*x)


font = {'family': 'normal', 'size': 14}  # font size
rc('font', **font)


# Q3a (omega=0), b -----------------------------------------------------------|
# list_of_cs = [2.]  # For Newman 6.10a and 6.11
list_of_cs = np.arange(0., 3., 0.01)  # For Newman 6.10b
omega = 0.7  # 0. for Newman 6.10, 0.5 to start Newman 6.11c; 0.7 is my answer
print('omega = ' + str(omega))

if len(list_of_cs) > 1:  # then we are solving Newman 6.10b
    solutions = []  # empty list, to which we will append the x solutions

for c in list_of_cs:
    # Do it once
    x0 = 0.5
    x1 = (1. + omega)*f(x0, c) - omega*x0

    # do it many times
    it = 0
    while abs(x1 - x0) > 1e-6:
        it += 1
        x0 = x1  # I multiply by one to copy the value instead of pointing it
        x1 = (1. + omega)*f(x0, c) - omega*x0

    if len(list_of_cs) > 1:  # then we are solving 6.10b
        solutions.append(x1)
    else:
        print("c = {0:.0f}, {1} iterations, x = {2:.7e}".format(c, it, x1))

if len(list_of_cs) > 1:
    plt.figure()
    plt.plot(list_of_cs, solutions)
    plt.xlabel('$c$')
    plt.ylabel(r'Solution of $x = 1-\exp(cx)$')
    plt.grid()
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.tight_layout()
    plt.savefig("Newman610b.png")
    plt.show()
