"""
PHY407@UofT
Author: Nicolas Grisouard, University of Toronto
"""

import intfuncs as fi  # my own functions for integrals
import numpy as np
from scipy.special import dawsn
from timeit import timeit  # function timeit.timeit


def integrand(x, t):
    """ The integrand in the definition of Dawson function (Q2a) """
    return np.exp(t**2 - x**2)


def integration_error(exponent, s_or_t, x_value, int_true):
    """ For Q2a
    This function computes the integral with a given method (Trapz or Simpson)
    and a given number of slices, computes and prints the difference with
    scipy's function
    IN:
    exponent [int]: the number of slices will be 10**exponent
    s_or_t [string]: If 's', Simpson, if 't', Trapezoidal
    x_value [float]: the upper bound of integration
    OUT:
    prints out a statement
    IntErr [float]: the error compared with int_true (abs value)
    """
    if s_or_t == 't':
        ID = 'Trapezoidal'  # for formatting the printed output
        DaFunc = fi.trapz_int  # method selection
    elif s_or_t == 's':
        ID = 'Simpson'  # for formatting the printed output
        DaFunc = fi.simps_int  # method selection
    else:  # test if we made a mistake
        raise NameError("Need to specify which method: 's' or 't'")

    N_slices = 2**exponent  # number of slices
    int_comp = DaFunc(0., x_value, N_slices, lambda t: integrand(x, t))
    IntErr = int_comp - int_true  # the error
    print("  {0}, with N = {1}: error = {2}".format(ID, N_slices, IntErr))
    return IntErr


# The parameters below will be used throughout Q2a
x = 4.
spVal = dawsn(x)  # I store it because I do not want to compute it every time
print("According to scipy,        D({0}) = {1}".format(x, dawsn(x)))


def integrand_for_x(t): return integrand(x, t)  # not-so-anonymous function


# i. Test with N=8
N = 8
print("\nTest with N={0} slices".format(N))
int_t = fi.trapz_int(0., x, N, integrand_for_x)
print("With the Trapezoidal rule, D({0}) = {1}".format(x, int_t))
int_s = fi.simps_int(0., x, N, integrand_for_x)
print("With Simpson's rule,       D({0}) = {1}".format(x, int_s))


# ii. How many slices until reaching an error of 1e-10?
IE_target = 1e-9  # the error we want to reach
for method in ['s', 't']:  # we loop over both methods
    print(' ')
    # First, we try with 10 slices
    nexp = 3  # first order of magnitude
    # Below: wrapping the computation in a function allows modularity and
    # profiling
    IE = integration_error(nexp, method, x, spVal)
    while (IE > IE_target):  # we increase until we hit it
        nexp += 1  # increase the order of magnitude until we hit it
        IE = integration_error(nexp, method, x, spVal)
    if method == 's':
        N_s_final = 2**nexp
    elif method == 't':
        N_t_final = 2**nexp


# Below is an alternative method to time a python statement.
# The method, exposed in the 1st lab is perfectly OK to use.
num_reps = 10  # the functions below will compute the same thing num_reps time

print('\nLet us time it.')
a = timeit("fi.simps_int(0., x, N_s_final, integrand_for_x)",
           "from __main__ import integrand_for_x, fi, x, N_s_final",
           number=num_reps)
print("Integrating with an error of {0} with Simpson's rule takes {1:.3e} s."
      .format(IE_target, a/num_reps))

a = timeit("fi.trapz_int(0., x, N_t_final, integrand_for_x)",
           "from __main__ import integrand_for_x, fi, x, N_t_final",
           number=num_reps)
print("Integrating with an error of {0} with trapezoidal rule takes {1:.3e} s."
      .format(IE_target, a/num_reps))

a = timeit("dawsn(x)", "from __main__ import dawsn, x", number=num_reps)
print("It takes {0:.3e} s for scipy to compute D({1}).".format(a/num_reps, x))


# iii. Practical estimate of the error: doubling and comparing.**
N1 = 32
h1 = x/N1
h2 = h1/2.

I1_trapz = fi.trapz_int(0., x, N1, integrand_for_x)
I2_trapz = fi.trapz_int(0., x, 2*N1, integrand_for_x)

epsilon_trapz = (I2_trapz - I1_trapz)/3.
print('\nPractical estimation of epsilon for trapz = ', epsilon_trapz)

I1_simps = fi.simps_int(0., x, N1, integrand_for_x)
I2_simps = fi.simps_int(0., x, 2*N1, integrand_for_x)

epsilon_simps = (I2_simps - I1_simps)/15.
print('Practical estimation of epsilon for Simpson = ', epsilon_simps)
