"""
Testing the logistic map
2020, Nicolas Grisouard, University of Toronto
"""

import numpy as np
import matplotlib.pyplot as plt
from random import random


def evolution(pop0, r, ny):
    """ Given:
    pop0 the initial population
    r the reproduction rate
    ny how many times we iterate the logistic map (# of years),
    compute the population over ny years (list pop).
    """
    pop = [pop0]  # list of one element to which we will append
    for p in range(1, ny):  # computing the insect population recursively
        last_pop = pop[-1]
        pop.append(r*(1 - last_pop)*last_pop)

    return pop


# A few parameters that I will use throughout --------------------------------|
dpi = 300   # dopts per inch for printing figures
ftsz = 14  # font size on plots
mksz = 0.1  # marker size for the bifurcation plots


# A few population evolutions ------------------------------------------------|
plt.figure(0)  # initializing the figure

x0 = 0.1  # we will reuse this initial population a few times

for r in [2., 2.5, 3.1, 3.5, 4.]:  # reproduction rates
    x = evolution(x0, r, 51)
    plt.plot(x, label='$r = {0}$'.format(r))

plt.title("Population evolution for different $r$'s", fontsize=ftsz)
plt.xlabel('$p$', fontsize=ftsz)
plt.ylabel('$x_p$', fontsize=ftsz)
plt.legend()
plt.grid()

# saving the figure as png
plt.savefig('L01-407-logistic-evol.png', dpi=dpi)  # dpi=dots/inch

# Bifurcation plot -----------------------------------------------------------|
plt.figure(1)  # initializing the figure

for r in np.arange(2., 4., 0.005):  # reproduction rate

    x = evolution(x0, r, 2001)
    rs = [r] * 2001  # create a list of 2001 times r

    if r < 3:
        plt.plot(rs[-100:], x[-100:], 'k.', markersize=mksz)
    else:
        plt.plot(rs[-1000:], x[-1000:], 'k.', markersize=mksz)

plt.title('Bifurcation diagram', fontsize=ftsz)
plt.xlabel('$r$', fontsize=ftsz)
plt.ylabel("$x_p$'s", fontsize=ftsz)
# plt.legend()
plt.grid()

# saving the figure as png
plt.savefig('L01-407-logistic-bifurc.png', dpi=dpi)  # dpi=dots/inch


# Bifurcation plot (narrower set of r's) -------------------------------------|
plt.figure(2)  # initializing the figure

for r in np.arange(3.737, 3.745, 0.00001):  # reproduction rate
    x = evolution(x0, r, 2001)
    rs = [r] * 2001

    if r < 3:
        plt.plot(rs[-100:], x[-100:], 'k.', markersize=mksz)
    else:
        plt.plot(rs[-1000:], x[-1000:], 'k.', markersize=mksz)

plt.title('Bifurcation diagram', fontsize=ftsz)
plt.xlabel('$r$', fontsize=ftsz)
plt.ylabel("$x_p$'s", fontsize=ftsz)
plt.grid()

# saving the figure as png  (NOT REQUIRED IN THE REPORT)
plt.savefig('L01-407-logistic-bifurc-zoom.png', dpi=dpi)  # dpi=dots/inch


# Sensitivity to initial conditions ------------------------------------------|
r = 3.75  # other values are possible; this one seems to be chaotic
lyapunov = 0.33

plt.figure(3)  # two different trajectories

ny = 71  # number of years
epsilon = 2e-7*(random()-0.5)  # draw random number in [-1e-7, 1e-7)
x1 = evolution(x0, r, ny)
x2 = evolution(x0 + epsilon, r, ny)

plt.plot(x1, label='$x_0 = {0}$'.format(x0))
plt.plot(x2, '--', label='$x_0 = {0}$'.format(x0+epsilon))

plt.title('Population evolution for different initial conditions',
          fontsize=ftsz)
plt.xlabel('$p$', fontsize=ftsz)
plt.ylabel('$x_p$', fontsize=ftsz)
plt.legend()
plt.grid()

# saving the figure as png
plt.savefig('L01-407-logistic-divergence.png', dpi=dpi)  # dpi=dots/inch

plt.figure(4)  # distance between trajectories
delta = []  # divergence
ps = []  # list of (l*p)'s for plotting
for p in range(ny):  # numpy arrays would have been more convenient
    delta.append(abs(x2[p] - x1[p]))
    ps.append(lyapunov*p)

plt.semilogy(delta, label='$|x_p^{(2)}-x_p^{(1)}|$')
plt.semilogy(abs(epsilon) * np.exp(ps), '--',
             label='$|\epsilon|\exp({0}p)$'.format(lyapunov))

plt.title('Population divergence between two different initial conditions',
          fontsize=ftsz)
plt.xlabel('$p$', fontsize=ftsz)
# plt.ylabel('$|x_p^{(2)} - x_p^{(1)}|$', fontsize=ftsz)
plt.legend()
plt.grid()

# saving the figure as png
plt.savefig('L01-407-logistic-lyapunov.png', dpi=dpi)  # dpi=dots/inch


plt.show()
