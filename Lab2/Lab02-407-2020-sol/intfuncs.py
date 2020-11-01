"""
This module contains one function for trapezoid rule, and one
for Simpson's rule
Author: Nicolas Grisouard
"""
import numpy as np


def trapz_int(a, b, N, f):
    """Trapezoid rule of integration
    IN:
    a, b: [floats] lower and upper bounds of integration
    N: [int] number of slices
    f: [function] a function to integrate
    OUT:
    [float] the integral

    PSEUDO-CODE:
    1. from a, b and N, compute h the int step
    2. initialize the result by adding (beginning + end)/2.
    3. loop to add the other terms f(a+kh)
    4. multiply the result by h to create final result
    """
    # 1.: from a, b and N, compute h
    h = (b-a)/N

    # 2.: the beginning and end
    result = 0.5*(f(a) + f(b))

    # 3. Then, loop over interior points
    for k in range(1, N):
        result += f(a + k*h)

    return h*result  # 4.


def simps_int(a, b, N, f):
    """Simpson's rule of integration
    IN:
    a, b: [floats] lower and upper bounds of integration
    N: [int] number of slices, HAS TO BE EVEN
    f: [function] a function to integrate
    OUT:
    [float] the integral

    PSEUDO-CODE:
    1. test if N is odd or even, and throw an error if odd
    2. from a, b and N, compute h the int step
    3. initialize the result by adding (beginning + end).
    4. loop over the odd k's to sum f(a+kh) from 1 to N-1
    5. add 4*(sum above) to the result
    6. loop over the even k's to sum f(a+kh) from 2 to N-2
    7. add 2*(sum above) to the result
    8. multiply the result by h/3 to create final result
    """

    # 1. test if N is odd or even, and throw an error if odd
    if N % 2 == 1:  # if True, the number is even
        # this aborts the calculation
        raise NameError("Simpson's rule needs an even nunmber of slices!")

    # 2.: from a, b and N, compute h
    h = (b-a)/N

    # 3.: the beginning and end
    result = f(a) + f(b)

    # 4. loop over the odd k's to sum f(a+kh) from 1 to N-1
    odds = 0.
    for k in range(1, N, 2):
        odds += f(a + k*h)
    result += 4.*odds  # 5. add 4*(sum above) to the result

    # 6. loop over the even k's to sum f(a+kh) from 2 to N-2
    evens = 0.
    for k in range(2, N, 2):
        evens += f(a + k*h)
    result += 2*evens  # 7. add 2*(sum above) to the result

    return h*result/3  # 8. multiply the result by h/3 to create final result
