# Answer to Q2, Lab 01, PHY407, 2020
# Author: Nicolas Grisouard, University of Toronto
# Quantum uncertainty

import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from math import factorial
import intfuncs as fi


# %% Q2a: the pre-factor will the factorials ---------------------------------|
def PreFac(n):
    """Computes the wavefunction for a particle in its nth energy level
    IN: n [int>=0]: the order
    """
    return (float(2**n)*float(factorial(n))*(np.pi**.5))**-0.5


# %% Q2a: the function that computes the Hermite polynomials -----------------|
def H(n, x):
    """ Computes nth-order Hermite Polynomial
    IN:
    n [int>=0]: the order
    x [float or np.array]: the point(s) at which it is evaluated
    OUT:
    the function evaluated at x
    """
    if n == 0:
        H1 = np.ones(x.shape)
    elif n == 1:
        H1 = 2*x
    elif n > 1:
        H0 = 1
        H1 = 2*x
        for k in range(1, n):
            H1, H0 = 2.*x*H1 - 2*k*H0, H1  # replace H0 by old H1, N1 by new H1
    else:
        raise NameError('n = {} < 0!'.format(n))
    return H1  # the last H1


# %% Q2a: the function that computes the wave function -----------------------|
def psin(n, x):
    """Computes the wavefunction for a particle in its nth energy level
    IN:
    n [int>=0]: the order
    x [float or np.array]: the point(s) at which it is evaluated
    OUT:
    the function evaluated at x
    """
    return PreFac(n) * H(n, x) * np.exp(-.5*x**2)


# %% Q2c: the function that computes the RMS of position with GQ -------------|
def RMS_pos(n):
    """
    IN:
    n [int>=0]: the energy level of the particle
    x [float or np.array]: the point(s) at which it is evaluated
    OUT:
    the function evaluated at x
    """
    def inner_fct(z):  # with an inner function, n is part of the outer scope
        """the sole purpose of this function is to turn a bivariate fct into a
        univariate function"""
        x = np.tan(z)
        # below, the cos() is the change of variables for indefinite integrals
        # also, the abs() is somewhat useless bc psi is real
        return x**2 * abs(psin(n, x))**2 / np.cos(z)**2

    return np.sqrt(fi.gauss_int(-.5*np.pi, .5*np.pi, 100, inner_fct))


# %% Q2c: the function that computes the RMS of momentum with GQ -------------|
def RMS_mom(n):
    """
    IN:
    n [int>=0]: the energy level of the particle
    x [float or np.array]: the point(s) at which it is evaluated
    OUT:
    the function evaluated at x
    """
    def inner_fct(z):  # with an inner function, n is part of the outer scope
        """the sole purpose of this function is to turn a bivariate fct into a
        univariate function"""
        x = np.tan(z)
        if n == 0:
            intermediate_result = -PreFac(n) * x
        else:
            intermediate_result = PreFac(n) * (-x*H(n, x) + 2*n*H(n-1, x))
        # below, the cos() is the change of variables for indefinite integrals
        # also, the abs() is somewhat useless bc psi is real
        return abs(np.exp(-.5*x**2) * intermediate_result)**2 / np.cos(z)**2

    return np.sqrt(fi.gauss_int(-.5*np.pi, .5*np.pi, 100, inner_fct))


font = {'family': 'normal', 'size': 16}  # font size
rc('font', **font)


# %% Q2a: the Hermite plots --------------------------------------------------|
x_ar = np.linspace(-4., 4., 128)

plt.figure()
for (nn, line) in zip(range(4), ('-', '--', '-.', ':')):
    plt.plot(x_ar, psin(nn, x_ar), linestyle=line, label="$n = {}$".format(nn))
plt.grid()
plt.legend()
plt.xlim([x_ar.min(), x_ar.max()])
# plt.ylim([-20., 20.])
plt.xlabel('$x$')  # , fontsize=ftsz)
plt.ylabel('$\psi_n(x)$')  # , fontsize=ftsz)
plt.tight_layout()
plt.savefig('psins_Q2a.png', dpi=150)
# plt.show()


# %% Q2b: wave function for n=30 ---------------------------------------------|
x_ar = np.linspace(-10., 10., 512)

nn = 30
plt.figure()
ZehErmitt = H(nn, x_ar)  # the Hermite polynomial we need
ZehFactor = (float(2**nn)*float(factorial(nn))*(np.pi**.5))**-0.5
ZehPsee = ZehFactor * ZehErmitt * np.exp(-0.5*x_ar**2)
plt.plot(x_ar, ZehPsee)
# Hermites[nn] = H(nn, x_ar)
plt.grid()
plt.xlim([x_ar.min(), x_ar.max()])
plt.ylim([ZehPsee.min(), ZehPsee.max()])
plt.xlabel('$x$')  # , fontsize=ftsz)
plt.ylabel(r'$\psi_{30}(x)$')  # , fontsize=ftsz)
plt.tight_layout()
plt.savefig('psi_Q2b.png', dpi=200)
# plt.show()


# %% Q2c: RMS of position ----------------------------------------------------|
print("Let's verify that for n=5, sqrt(<x**2>) = " + str(RMS_pos(5)))
print('')
print(" n    sqrt(<x^2>)    sqrt(<p^2>)        E")
print("---------------------------------------------")
for nn in range(16):
    E = 0.5*(RMS_pos(nn)**2 + RMS_mom(nn)**2)
    # below: the '>2d' means integer, 2 slots reserved, right align
    # .2e means exponential format, 3 digits after point
    print("{0:>2d}     {1:.3e}      {2:.3e}      {3:.2e}".format(
        nn, RMS_pos(nn), RMS_mom(nn), E))
