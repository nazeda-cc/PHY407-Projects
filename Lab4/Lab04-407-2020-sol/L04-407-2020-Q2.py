# Author: Nicolas Grisouard, Univ. of Toronto
# solution to asymmetric quantum  well
import numpy as np
from numpy.linalg import eigh  # As mentioned in the text, the matrix is symm.
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.constants as pc  # physical constants


def Hmatrix(m, n):
    """ Q1b: computing the Hamiltonian operator matrix. """

    if not isinstance(m, int) and not isinstance(n, int):
        raise NameError('m, n indices have to be integers')

    a = 10*pc.electron_volt  # [J]  the coefficient for the well potential
    # Note how converting to SI units will avoid problems later

    if m == n:
        res = .5*(a + (np.pi*pc.hbar*m/L)**2/pc.electron_mass)
    elif (m+n) % 2 == 1:  # one is even, one is odd
        res = -8*m*n*a/(np.pi*(m**2 - n**2))**2
    else:
        res = 0.

    return res


def simpson(a, b, vec):
    """ Adapted from infuncs.simps_int to accomodate for the fact that the
    function is now like a data array """
    # 1. test if N is odd or even, and throw an error if odd
    N = len(vec)
    if N % 2 == 1:  # if True, the number is even
        # this aborts the calculation
        raise NameError("Simpson's rule needs an even number of slices!")

    # 2.: from a, b and N, compute h
    h = (b-a)/N

    # 3.: the beginning and end
    result = vec[0] + vec[-1]

    # 4. loop over the odd k's to sum f(a+kh) from 1 to N-1
    odds = 0.
    for k in range(1, N, 2):
        odds += vec[k]
    result += 4.*odds  # 5. add 4*(sum above) to the result

    # 6. loop over the even k's to sum f(a+kh) from 2 to N-2
    evens = 0.
    for k in range(2, N, 2):
        evens += vec[k]
    result += 2*evens  # 7. add 2*(sum above) to the result

    return h*result/3  # 8. multiply the result by h/3 to create final result


font = {'family': 'normal', 'size': 14}  # font size
rc('font', **font)


# %% Q2c, d: first ten elements ----------------------------------------------|
N = 100  # we will never use non-square matrices anyway
L = 5e-10  # [m] width of the well
H = np.empty((N, N))
for m in range(1, N+1):
    for n in range(1, N+1):
        H[m-1, n-1] = Hmatrix(m, n)

# %% Q2c: first ten energy levels
Energies, eigvecs = eigh(H)

print('First 10 energy levels:')
for i, E in enumerate(Energies[:10]):
    print("E{0} = {1:.5e} eV".format(i+1, E/pc.electron_volt))


font = {'family': 'normal', 'size': 14}  # font size
rc('font', **font)


# Q2e : first three psis -----------------------------------------------------|
nx = 128
x = np.linspace(0., L, nx)

plt.figure()

for n in range(3):  # ground + 1st 2 excited states
    psi = 0.*x
    for j in range(N):  # sum over all components of the eigenvectors
        psi += eigvecs[j, n]*np.sin(np.pi*(j+1)*x/L)  # i-th energy level
    A = simpson(0., L, abs(psi)**2)
    print(A)
    psi /= np.sqrt(A)
    print("Integral of |psi_{0}|**2 = {1}".format(
        n+1, simpson(0., L, abs(psi)**2)))
    plt.plot(x, abs(psi)**2, label='$n$ = '+str(n+1))

plt.xlabel('$x$ (m)')
plt.ylabel('$|\psi_n(x)|^2$ (m$^{-1}$)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('ExcitedStates.png')
plt.show()
