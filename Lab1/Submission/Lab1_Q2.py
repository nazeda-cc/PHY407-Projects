# -*- coding: utf-8 -*-
"""
@author: Zirui Wan
"""

import matplotlib.pyplot as plt
import numpy as np

def calculate_x(x0, r, pmax):
    """This function calculates the array of x
    INPUT:
    x0[float]: the initial normalized population x0
    r[float]: the maximum reproduction rate r
    pmax[int]: the total number of years

    OUTPUT:
    x[float]: an array of values xp for each year p
    """
    x = np.zeros((pmax))
    x[0] = x0
    for p in range(1, pmax):
        x[p] = r*(1 - x[p-1])*x[p-1]

    return x


###########################################################################
######                         Part c                                ######
###########################################################################

# define array of years
years = np.arange(0, 50, 1)

# calculate x for a number of values of r
x1 = calculate_x(x0=0.1, r=2,   pmax=50)
x2 = calculate_x(x0=0.1, r=3,   pmax=50)
x3 = calculate_x(x0=0.1, r=3.5, pmax=50)
x4 = calculate_x(x0=0.1, r=4,   pmax=50)

# define first figure
plt.figure(figsize=(10, 10))

# plot these curves of x's in different subplots
plt.subplot(2, 2, 1)
plt.plot(years, x1)
plt.title('r = 2')
plt.grid()
plt.xlabel('year p')
plt.ylabel(r'$x_p$')

plt.subplot(2, 2, 2)
plt.plot(years, x2)
plt.title('r = 3')
plt.grid()
plt.xlabel('year p')
plt.ylabel(r'$x_p$')

plt.subplot(2, 2, 3)
plt.plot(years, x3)
plt.title('r = 3.5')
plt.grid()
plt.xlabel('year p')
plt.ylabel(r'$x_p$')

plt.subplot(2, 2, 4)
plt.plot(years, x4)
plt.title('r = 4')
plt.grid()
plt.xlabel('year p')
plt.ylabel(r'$x_p$')

plt.tight_layout()
plt.show()



###########################################################################
######                         Part d                                ######
###########################################################################

# define array of r
rs = np.arange(2, 4, 0.005)
# prepare a fugure
plt.figure(figsize=(8, 8))
# loop over r's
for r in rs:
    # calculate xp for current r
    xnow = calculate_x(x0=0.1, r=r, pmax=2000)
    # select data points
    if r < 3:
        rnow = np.zeros((100))
        rnow[:] = r
        plt.scatter(rnow, xnow[-100:], s=0.05, c='k')
    else:
        rnow = np.zeros((1000))
        rnow[:] = r
        plt.scatter(rnow, xnow[-1000:], s=0.05, c='k')

# plot figures
plt.title('Logistic map')
plt.xlabel('maximum reproduction rate, r')
plt.ylabel('Population x')
plt.grid()
plt.show()


###########################################################################
######                         Part e                                ######
###########################################################################

# define array of r now:
rs = np.arange(3.738, 3.745, 1e-5)
# prepare a fugure
plt.figure(figsize=(8, 32))
# loop over r's
for r in rs:
    # calculate xp for current r
    xnow = calculate_x(x0=0.1, r=r, pmax=2000)

    # select data points
    if r < 3:
        rnow = np.zeros((100))
        rnow[:] = r
        plt.scatter(rnow, xnow[-100:], s=0.05, c='k')
    else:
        rnow = np.zeros((1000))
        rnow[:] = r
        plt.scatter(rnow, xnow[-1000:], s=0.05, c='k')
        
# plot figures
plt.title(r'Logistic map with 3.738 $\leq$ r $\leq$ 3.745')
plt.xlabel('maximum reproduction rate, r')
plt.ylabel('Population x')
plt.grid()
plt.show()

###########################################################################
######                         Part f                                ######
###########################################################################

# prepare a fugure for part (f)
plt.figure(figsize=(8, 4))

# define array of years
years = np.arange(0, 20, 1)

# calculate and plot x for a number of values of r
x1 = calculate_x(x0=0.1, r=4, pmax=20)
x2 = calculate_x(x0=0.1 + np.random.uniform(-0.005, 0.005), r=4, pmax=20)
plt.plot(years, x1, label=r'with $x0$')
plt.plot(years, x2, label=r'with $x0$ + $\epsilon$')

# plot figures
plt.title(r'History of evolution of $x_p$')
plt.xlabel('p')
plt.ylabel(r'$x_p$')
plt.grid()
plt.legend()
plt.show()



###########################################################################
######                         Part g                                ######
###########################################################################

# prepare a fugure for part (f)
plt.figure(figsize=(8, 4))

# define array of years
years = np.arange(0, 20, 1)

# calculate x for a number of values of r
x1 = calculate_x(x0=0.1, r=4, pmax=20)
x2 = calculate_x(x0=0.1 + np.random.uniform(-0.001, 0.001), r=4, pmax=20)
# plot the aboslute differences on semi-log plot
plt.semilogy(years, np.abs(x1 - x2), label='Simulated $\delta$')

# do the exp fit now
popt = np.polyfit(years[:11], np.log(np.abs(x1 - x2))[:11], 1)
a = np.exp(popt[1])
lamb = popt[0]
plt.semilogy(years[:11], a*np.exp(lamb*years)[:11], 
             label='Fitted $\delta$ with: a=%.2e, $\lambda=%.2f$' % (a, lamb))

# plot figures
plt.title(r'History of evolution of $\delta = | x^{1}_p - x^{2}_p |$')
plt.xlabel('p')
plt.ylabel(r'$\delta = | x^{1}_p - x^{2}_p |$')
plt.grid()
plt.legend()
plt.show()



### Extral practice: try to plot diagram of Lyapunov exponent now

# prepare a fugure for part (f)
plt.figure(figsize=(8, 4))
# define array of r
rs = np.arange(2, 4, 0.005)
# define array of years
years = np.arange(0, 10, 1)
# define array of the Lyapunov exponents
lyap = np.zeros((rs.shape[0]))

# loop over different r's to find Lyapunov exponent
for i in range(rs.shape[0]):
    # calculate x for a number of values of r
    x1 = calculate_x(x0=0.1, r=rs[i], pmax=10)
    x2 = calculate_x(x0=0.1 + np.random.uniform(-0.001, 0.001), r=rs[i], pmax=10)
    # do the exp fit now
    popt = np.polyfit(years, np.log(np.abs(x1 - x2)), 1)
    a = np.exp(popt[1])
    lamb = popt[0]
    lyap[i] = lamb


# plot figures
plt.plot(rs, lyap)
plt.title(r'Diagram of Lyapunov exponent')
plt.xlabel('r')
plt.ylabel(r'$\lambda$')
plt.grid()
plt.legend()
plt.show()