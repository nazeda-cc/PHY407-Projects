"""
Diffraction limit of a telescope
Author: Nicolas Grisouard, University of Toronto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.special import jv
import intfuncs as fi  # my own functions for integrals


def integrand(order, theta, x_eval):
    """ The integrand in the definition of Bessel function (Q2b)
    IN:
    order [int]: the order of the Bessel function
    theta [float]: the integration variable
    x_eval [float]: the point at which the Bessel function is evaluated
    OUT [float]: cos(m*theta - x*sin(theta))/pi
    """
    return np.cos(order*theta - x_eval*np.sin(theta))/np.pi


def J(m, x):
    """Computes the m-th-order Bessel function of the
    1st kind evaluated at x"""
    N_slices = 1000  # question asks for a function for which N is not a var
    def temp_integrand(t): return integrand(order=m, theta=t, x_eval=x)
    Jmx = fi.simps_int(0., np.pi, N_slices, temp_integrand)
    return Jmx


# Some parameters that will apply everywhere
cmap = "viridis"
low_bnd, up_bnd = 0., 20.  # lower and upper bounds for plotting
N_pts = 256  # number of points at which to evaluate and plot J(m, x)
x_array = np.linspace(low_bnd, up_bnd, N_pts)
dpi = 100  # dots per inch for the figures
vmax = 0.01  # level at which colourmaps will saturate
font = {'family': 'normal',
        'size': 14}
rc('font', **font)


# plotting the Bessel functions
plt.figure(dpi=dpi)  # increasing the dots per inch for niceness
for mm in range(3):  # overkill?
    plt.plot(x_array, J(mm, x_array), label='$J_{0}(x)$'.format(mm))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$J_m(x)$')
plt.axis([low_bnd, up_bnd, min(J(0, x_array)), max(J(0, x_array))])
plt.axhline(0., color='k')  # marks the y = 0 line
plt.legend()
plt.savefig('Bessel_funcs.png')


# Comparing with SciPy's jv
plt.figure(dpi=dpi)  # increasing the dots per inch for niceness
for mm in range(3):  # overkill?
    to_plot = (J(mm, x_array) - jv(mm, x_array))/max(jv(mm, x_array))
    plt.plot(x_array, to_plot, label='$m$ = {}'.format(mm))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$J_m(x)$')
# The legend being less explicit, I am adding a title
plt.title(r"        $\neq$ between mine and scipy's $J_m(x)$")  # r"" for LaTeX
#plt.axis([low_bnd, up_bnd, min(J(0, x_array)), max(J(0, x_array))])
plt.axhline(0., color='k')  # marks the y = 0 line
plt.legend()
plt.savefig('Bessel_diffs.png')


# Intensity of the circular diffraction spot, 1st on a polar grid
lmbda = 500e-9  # 500 nm, the wavelength
k = 2.*np.pi/lmbda  # the wave number
r_max = 1e-6  # the maximum radius to plot

r = np.linspace(0., r_max, 256)  # the radius array
t = np.linspace(0., 2.*np.pi, 128)  # the azimuth array

R, T = np.meshgrid(r, t)  # the grids

I = (J(1, k*R)/(k*R))**2  # the intensity
# We now want to replaced the division by zero with its limit, 0.25
# this statement is useful if you want to know along which direction is r
print("Shape of I is", I.shape)
I[:, 0] = 0.5**2  # replacing the division by zero with the limit

plt.figure(dpi=dpi)
# making plt aware that we are plotting in polar
ax1 = plt.subplot(projection="polar")
# imshow does not like polar
cbax = ax1.pcolormesh(T, R, I, cmap=cmap, vmax=0.01)
plt.colorbar(cbax)
plt.title('Diffraction pattern')
plt.tight_layout()
plt.savefig('Diffraction_polar.png')


# Alternative on a Cartesian grid (what most will probably do)
x = np.linspace(-r_max, r_max, N_pts)
y = 1.*x

Y, X = np.meshgrid(y, x)
RR = np.sqrt(X**2 + Y**2)
I_Cart = (J(1, k*RR)/(k*RR))**2

plt.figure(dpi=dpi)
# imshow is a silly method, I am commenting it out
# plt.imshow(I_Cart, vmax=0.01)
# plt.hot()
plt.pcolormesh(X*1e6, Y*1e6, I_Cart, cmap=cmap, vmax=0.01)  # better
# note that I converted in micrometers above
plt.colorbar()
plt.axis('image')  # see lab01
plt.xlabel(r'$x$ ($\mu$m)')
plt.ylabel(r'$y$ ($\mu$m)')
plt.title('Diffraction pattern')
plt.savefig('Diffraction_Cartesian.png')
# plt.show()
