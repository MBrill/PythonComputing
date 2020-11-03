# -*- coding: utf-8 -*-
"""
Back substitution and simple implementation of the Gauss algorithm.
"""

import numpy as np
import sys


def backSubstitution(a):
    """
    Back substitution for a simple Gauss algorithm. Call this
    function after eliminating the extended coefficient matrix.

    We expect all diagonal elements to be non-zero.
    This is not checked, if this happens we get a message
    computing the eliminated matrix.

    Parameters
    ----------
    a : ndarray with shape (n,n+1)
        Extended coefficient matrix of our linear equation system.

    Returns
    -------
    Solution of the linear equation system.
    """
    n = np.size(a, 0)
    x = np.zeros(n)
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in np.arange(n-2, -1, -1):
        x[i] = a[i][n]
        for j in np.arange(i+1, n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i] / a[i][i]
    return x


def gauss(a, eps=1.0e-10):
    """
    Gauss elimination of an extended coefficient matrix of a
    quadratic linear equation system. The algorithm is done in place,
    so if you need the original matrix A or the right hand side b,
    store them before calling this function.

    Parameters
    ----------
    a : ndarray of size (n, n+1)
        Extended coefficient matrix of the lineare equation system.
    eps: precision for the decision, if a diagonal element is zero.

    Returns
    -------
    Result of the Gauss elimination in place.
    """
    n = np.size(a, 0)
    for i in np.arange(n):
        if np.abs(a[i][i]) <= eps:
            sys.exit('Division by zero detected in function gauss')
        for j in np.arange(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in np.arange(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    return a


def cool():
    A = np.array([[3, 2, 1, 10], [2, 3, 2, 14], [1, 2, 3, 14]])
    A[1, :] = A[1, :] - A[0, :]*A[1, 0]/A[0, 0]
    A[2, :] = A[2, :] - A[0, :]*A[2, 0]/A[0, ]
    print(A)
    print('After transformation\n')
    A[2, :] = A[2, :] - A[1, :]*A[2, 1]/A[1, ]
    print(A)

    z = A[2, 3]/A[2, 2]
    y = (A[1, 3] - A[1, 2]*z)/A[1, 1]
    x = (A[0, 3] - A[0, 1]*y - A[0, 2]*z)/A[0, 0]
    print('x =', x)
    print('y =', y)
    print('z =', z)


def main():
    """
    Code to demonstrate gauss elimination and back substitution.

    Returns
    -------
    None.
    """
    # Example matrix from LAG class
    # solution:
    # x = [2/3, 1/6, 1/3]
    a = np.array([[1, 2, 0, 1],
                  [0, 2, 2, 1],
                  [0, 0, 3, 1]])
    print('Do the back substitution')
    print('The computed solution should be:')
    print(np.array([2/3, 1/6, 1/3]))
    x = backSubstitution(a)
    print('The computed solution')
    print(x)
    print('Testing the gauss elimination')
    # We use the first example for Gauss in the LAG class
    a = np.array([[1, -1, 0, 0, 5],
                  [-1, 2, -1, 0, 0],
                  [0, -1, 2, -1, 1],
                  [0, 0, -1, 2, 0]])

    correct = np.array([[1, -1, 0, 0, 5],
                        [0, 1, -1, 0, 5],
                        [0, 0, 1, -1, 6],
                        [0, 0, 0, 1, 6]])

    print('The correct solution would be')
    print(correct)

    gauss(a)
    print('Computed eliminated matrix')
    print(a)

    print('Back substitution for this example')
    x = np.array([22, 17, 12, 6])
    print('Correct solution')
    print(x)
    x = backSubstitution(a)
    print('Computed solution')
    print(x)


if __name__ == "__main__":
    main()
