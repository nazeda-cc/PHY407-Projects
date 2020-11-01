# Author: Nicolas Grisouard, University of Toronto
# The script contains answers to Q1 of lab 04 about solving linear
# systems of equations for an electric circuit

import numpy as np
from cmath import polar, phase
import matplotlib.pyplot as plt
import SolveLinear_sol as sl
from matplotlib import rc


def ZeMatrix(element, R_, C_):
    """ I define the matrix A as a function of the one element we turn from a
    resistor to an inductor
    IN: element [complex]: the resistor or inductor
    R_ [float]: list of resistors R1 to R5
    C_ [complex]: list of capacitances C1 and C2
    """
    A = np.empty((3, 3), complex)

    # 1st line of matrix
    A[0, 0] = 1./R[1] + 1./R[4] + C[1]
    A[0, 1] = -C[1]
    A[0, 2] = 0.

    # 2nd line of matrix
    A[1, 0] = -C[1]
    A[1, 1] = 1./R[2] + 1./R[5] + C[1] + C[2]
    A[1, 2] = -C[2]

    # 3rd line of matrix
    A[2, 0] = 0.
    A[2, 1] = -C[2]
    A[2, 2] = 1./R[3] + 1./element + C[2]

    return A


font = {'family': 'normal', 'size': 16}  # font size
rc('font', **font)


# %% Values that will not change ---------------------------------------------|
# 1st elements of each list are empty to have indexing be like in Newman's book
R = ['', 1e3, 2e3, 1e3, 2e3, 1e3]  # list of resistance values

omega = 1e3  # [rad/s]
C = ['', 1e-6 * omega * 1j, 5e-7 * omega * 1j]  # [F*rad/s]
# Capacitance is always multiplied by iw

xplus = 3.  # [V]


# %% Q1c - when resistors are resistors --------------------------------------|
R6 = 2e3  # [ohms]
v = xplus*np.array([1./R[1], 1./R[2], 1./R[3]], complex)  # the RHS

# the time array for plotting
duration = 1.5*2.*np.pi/omega
t = np.linspace(0., duration, 256)

X = sl.PartialPivot(ZeMatrix(R6, R, C), v)  # [x1, x2, x3]
V1 = X[0] * np.exp(1j*omega*t)
V2 = X[1] * np.exp(1j*omega*t)
V3 = X[2] * np.exp(1j*omega*t)

print("Amplitudes and phases of voltages with resistor R6:")
for i in range(3):
    print("  |V{0}| = {1:.2e} V, phi{0}(t=0) = {2} degrees".format(
        i+1, abs(X[i]), int(np.angle(X[i], deg=True))))

plt.figure()
plt.plot(t, np.real(V1), label='$V_1$')
plt.plot(t, np.real(V2), label='$V_2$')
plt.plot(t, np.real(V3), label='$V_3$')
plt.xlabel('time (s)')
plt.ylabel(r'Real parts of $V_i$, in V')
plt.title(r'When the resistor is $R_6 = 2000$ $\Omega$.')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Lab04-Q1c-R6.png', dpi=100)


# %% Q1c - replacing with inductor -------------------------------------------|
L = R6/omega  # [H] the inductance

X = sl.PartialPivot(ZeMatrix(1j*omega*L, R, C), v)  # [x1, x2, x3]
V1 = X[0] * np.exp(1j*omega*t)
V2 = X[1] * np.exp(1j*omega*t)
V3 = X[2] * np.exp(1j*omega*t)

print("Amplitudes and phases of voltages with inductor:")
for i in range(3):
    print("  |V{0}| = {1:.2e} V, phi{0}(t=0) = {2} degrees".format(
        i+1, abs(X[i]), int(np.angle(X[i], deg=True))))

plt.figure()
plt.plot(t, np.real(V1), label='$V_1$')
plt.plot(t, np.real(V2), label='$V_2$')
plt.plot(t, np.real(V3), label='$V_3$')
plt.xlabel('time (s)')
plt.ylabel('Real parts of $V_i$, in V')
plt.title('When the inductor is $L = 2$ H.')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Lab04-Q1c-L.png', dpi=100)

plt.show()
