# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:11:33 2020

@author: rundo
"""
#%%
# SolveLinear.py
# Python module for PHY407
# Paul Kushner, 2015-09-26
# Modifications by Nicolas Grisouard, 2018-09-26
# This module contains useful routines for solving linear systems of equations.
# Based on gausselim.py from Newman
from numpy import empty
from numpy import copy
# The following will be useful for partial pivoting
# from numpy import empty, copy

#


def GaussElim(A_in, v_in):
    """Implement Gaussian Elimination. This should be non-destructive for input
    arrays, so we will copy A and v to
    temporary variables
    IN:
    A_in, the matrix to pivot and triangularize
    v_in, the RHS vector
    OUT:
    x, the vector solution of A_in x = v_in """
    # copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    
    
    N = len(v)

    for m in range(N):
        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult*A[m, :]
            v[i] -= mult*v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i]*x[i]
    return x

#%%
def PartialPivot(A_in, v_in):
    """ In this function, code the partial pivot (see Newman p. 222) """
    
    A = copy(A_in)
    v = copy(v_in)

    
    N = len(v)

    for m in range(N):
        
        ###### Partial pivoting starts here #############
        maxi = A[m, m]
        swap_index = m
        for i in range(m, N):
            if abs(A[i][m]) > abs(maxi):
                swap_index = i
                maxi = A[i][m]
        
        if swap_index != m:
            temp_A = copy(A[swap_index][:])
            temp_v = copy(v[swap_index])
        
            A[swap_index][:] = A[m][:]
            v[swap_index] = v[m]
        
            A[m][:] = temp_A
            v[m] = temp_v
        ##################################################
        
        # Divide by the diagonal element
        div = A[m][m]
        
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult*A[m, :]
            v[i] -= mult*v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i]*x[i]
    return x






