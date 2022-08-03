# -*- coding: utf-8 -*-
"""
Backsubstitution and simple implementation of the Gauss algorithm.
"""
import numpy as np
import sys


def backSubstitution(a: np.float64):
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
    n = a.shape[0]
    x = np.zeros(n, dtype=np.float64)
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in np.arange(n-2, -1, -1):
        res = a[i][n]
        for j in np.arange(i+1, n):
            res = res - a[i][j]*x[j]
        x[i] = res / a[i][i]
    return x


def gauss(a: np.float64, eps=np.float64(1.0e-10)):
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
    n = a.shape[0]
    for k in np.arange(n):
        if np.abs(a[k][k]) <= eps:
            sys.exit('Division by zero detected in function gauss')
        for i in np.arange(k+1, n):
            factor = a[i][k]/a[k][k]
            for j in np.arange(n+1):
                a[i][j] = a[i][j] - factor * a[k][j]
    return a


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
    print('The coefficient matrix')
    print(a)
    print('The computed solution should be:')
    print(np.array([2/3, 1/6, 1/3]))
    x = backSubstitution(a)
    print('The computed solution')
    print(x)
    print('Testing the gauss elimination')
    a = np.array([[1, -1, 0, 0, 5],
                  [-1, 2, -1, 0, 0],
                  [0, -1, 2, -1, 1],
                  [0, 0, -1, 2, 0]])

    correct = np.array([[1, -1, 0, 0, 5],
                        [0, 1, -1, 0, 5],
                        [0, 0, 1, -1, 6],
                        [0, 0, 0, 1, 6]])

    print('The correct eliminated matrix is')
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
