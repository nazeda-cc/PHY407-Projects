# Answer to Q1c, Lab 03, PHY407, 2020
# Author: Nicolas Grisouard, University of Toronto
# Blowing snow

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import intfuncs as fi  # I added the Gaussian Q in there


def P_integrand(t):
    """ The integrand in the definition of Probability of blowing snow
    after the change of variable t = (u-ubar)/(delta*sqrt(2)) """
    return np.exp(-t**2)/np.sqrt(np.pi)


def ubar(Ta, th):
    """Mean wind speed (m/s)"""
    return 11.2 + 0.365*Ta + 0.00706*Ta**2 + 0.9*np.log(th)


def delta(Ta):
    """Wind speed standard deviation (m/s)"""
    return 4.3 + 0.145*Ta + 0.00196*Ta**2


font = {'family': 'normal', 'size': 10}  # font size
rc('font', **font)


# res_g[i] = fi.gauss_int(0., x, N, P_integrand)

N = 100  # N sample points
N_Ta = 64  # N_Ta values for the temperature
Ta_ar = np.linspace(-60., 0., N_Ta)  # (Canadian) temperatures in C

th_ar = np.array([24., 48., 72.])  # hours
u10_ar = np.array([6., 8., 10.])  # avg wind speed 10 m above ground

colours = ('r', 'g', 'b')  # u10's will be distinguishable with colours
lines = ('-', '.', ':')  # th's will be distinguishable with line styles

plt.figure()
for (u10, colour) in zip(u10_ar, colours):
    for (th, line) in zip(th_ar, lines):
        plot_str = colour + line
        legend_str = r'$t_h =$ ' + str(th) + r', $u_{10}$ = ' + str(u10)
        P = 0*Ta_ar
        for ii, TT in enumerate(Ta_ar):
            P[ii] = fi.gauss_int(- ubar(TT, th) / (2**0.5*delta(TT)),
                                 (u10 - ubar(TT, th)) / (2**0.5*delta(TT)),
                                 N, P_integrand)
        plt.plot(Ta_ar, P, plot_str, label=legend_str)

plt.xlabel('Temperature $T_a$ ($^\circ$C)')  # , fontsize=ftsz)
plt.ylabel('Probability of blowing snow $P$')  # , fontsize=ftsz)
plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig('P_Q1b.png', dpi=200)
# plt.show()
