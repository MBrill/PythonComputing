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


def cool3(a):
    # n=3
    # Schritt 1
    a[1, 1:] = a[1, 1:] - (a[1, 0]/a[0, 0]) * a[0, 1:]
    a[2, 1:] = a[2, 1:] - (a[2, 0]/a[0, 0]) * a[0, 1:]
    # Schritt 2
    a[2, 2:] = a[2, 2:] - (a[2, 1]/a[1, 1]) * a[1, 2:]


def gauss(a):
    """
    Gauss-Elimation using slicing

    Parameters
    ----------
    a : float ndarray
        coefficent matrix with right hand side in last column.

    Returns
    -------
    Eliminated matrix in the upper triangle of a.

    """
    # Schritt 1
    n = a.shape[0]
    for k in np.arange(1, n):
        for i in np.arange(k, n):
            a[i, k:] = a[i, k:] - (a[i, k-1]/a[k-1, k-1]) * a[k-1, k:]


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
    a = np.array([[1, 3, 4, 1], [2, 1, 3, 2], [4, 7, 2, 3]])
    print('n=3')
    print('Matrix A\n', a)
    gauss(a)
    print('After elimination\n', a)
    x = backSubstitution(a)
    print('The computed solution (exact would be (8/9, -1/9, 1/9)')
    print(x)

    print('n=4')
    a = np.array([[1, -1, 0, 0, 5],
                  [-1, 2, -1, 0, 0],
                  [0, -1, 2, -1, 1],
                  [0, 0, -1, 2, 0]])
    print('Coefficient matrix\n', a)

    correct = np.array([[1, -1, 0, 0, 5],
                        [0, 1, -1, 0, 5],
                        [0, 0, 1, -1, 6],
                        [0, 0, 0, 1, 6]])
    print('The correct eliminated matrix is')
    print(correct)

    gauss(a)
    print('Computed eliminated matrix')
    print(a)
    x = np.array([22, 17, 12, 6])
    print('Correct solution')
    print(x)
    x = backSubstitution(a)
    print('Computed solution')
    print(x)


if __name__ == "__main__":
    main()
