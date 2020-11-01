# Answer to Q1a and b, Lab 03, PHY407, 2020
# Author: Nicolas Grisouard, University of Toronto
# Error on Dawson function estimates

import numpy as np
import matplotlib.pyplot as plt
import intfuncs as fi  # I added the Gaussian Q in there
# from scipy.special import dawsn


def D_integrand(t):
    """ The integrand in the definition of Dawson function (from Lab02) """
    return np.exp(t**2 - x**2)


ftsz = 16  # font size for figures


# %% Q1a: we can actually use gaussxwab because the bounds of integration ----|
# don't change
x = 4.
print(' ')
print("According to scipy, D({0}) = {1}".format(x, dawsn(x)))
print(' ')

list_of_N = [2**nn for nn in range(3, 12)]  # the Ns we will use
# Any set of N's would have worked, but using 2**n speeds up practical error
# estimations

nN = len(list_of_N)  # this to initialize the arrays containing the integrals
res_t = np.empty(nN)  # this array will contain the trapezoidal integrals
res_s = np.empty(nN)  # this array will contain the Simpson integrals
res_g = np.empty(nN)  # this array will contain the GQ integrals

for i, N in enumerate(list_of_N):
    print('For N = {} slices/sample points:'.format(N))
    res_t[i] = fi.trapz_int(0., x, N, D_integrand)
    print('  Trapezoidal says {}'.format(res_t[i]))
    res_s[i] = fi.simps_int(0., x, N, D_integrand)
    print('      Simpson says {}'.format(res_s[i]))
    res_g[i] = fi.gauss_int(0., x, N, D_integrand)
    print('        Gauss says {}'.format(res_g[i]))
    print(' ')

# %% Q1b: now we use some of the values above to compute some errors ---------|
eps_t = np.empty(nN)
eps_s = np.empty(nN)
eps_g = np.empty(nN)

j = 0  # I will fill up arrays of errors, and this will be the index
for i, N in enumerate(list_of_N):

    I2_t = res_t[i]
    I2_s = res_s[i]
    I2_g = res_g[i]
    # do we need to compute new integral with N/2, or did we compute it
    # already?
    if i == 0:  # we need to integrate with N=8 for the first error
        I1_t = fi.trapz_int(0., x, N//2, D_integrand)
        I1_s = fi.simps_int(0., x, N//2, D_integrand)
        I1_g = fi.gauss_int(0., x, N//2, D_integrand)
    else:  # we just need the previous element for all other N's
        I1_t = res_t[i-1]  # the previous item in the array
        I1_s = res_s[i-1]  # the previous item in the array
        I1_g = res_g[i-1]  # the previous item in the array

    # we now have all integrals. Let's compute the errors
    eps_t[j] = (I2_t - I1_t)/3
    eps_s[j] = (I2_s - I1_s)/15
    eps_g[j] = I2_g - I1_g

    j += 1  # on to the next N

# We now have computed the errors, let's plot
plt.figure()
plt.loglog(list_of_N, abs(eps_t), label='Trapezoidal')
# Always a good idea to add a pattern or shade to curves for e.g. colourblinds
plt.loglog(list_of_N, abs(eps_s), '--', label='Simpson')
plt.loglog(list_of_N, abs(eps_g), '-.', label='Gaussian')
plt.xlabel(r'Number of slices/sample points $N$ (log scale)', fontsize=ftsz)
plt.ylabel(r'Error $|\epsilon|$ (log scale)', fontsize=ftsz)
plt.grid()
plt.legend(fontsize=ftsz)
plt.tight_layout()
plt.savefig('epsilons_Q1a-ii.png', dpi=150)
# plt.show()
