# -*- coding: utf-8 -*-
"""
Testing our implementation of our implementation of Gauss
with the Hilbert matrix
"""
import numpy as np
from scipy import linalg
import gauss as gs


def compute(n: int):
    """
    Compute the first column of the inverse of the Hilbert matrix

    Parameters
    ----------
    n : int
        Dimension of Hilbert matrix.

    Returns
    -------
    float
        euclidean absolute and relative errors.
    """
    h = linalg.hilbert(n)
    b = np.zeros(shape=(n, ), dtype=np.float64)
    b[0] = np.float64(1.0)
    a = np.zeros(shape=(n, n+1))
    a[:n, :n] = h[0:n, 0:n]
    a[:, n] = b
    gs.gauss(a)
    x = gs.backSubstitution(a)
    y = linalg.invhilbert(n)[:, 0]
    abseps = linalg.norm(x-y)
    releps = abseps/linalg.norm(y)
    return abseps, releps


def iterCompute(ind):
    """
    Compute the tests for a set of values for n

    Parameters
    ----------
    ind : ndarray of int
        dimensions for the hilbert matrix.

    Returns
    -------
    None.
    """
    for n in ind:
        abs, rel = compute(n)
        print('Inverting the Hilbert matrix')
        print('Dimension ', n)
        print('Absolute Error', abs)
        print('Relative Error', rel)


def main():
    """
    Main program for the tests using the hilbert matrix

    Returns
    -------
    None.
    """
    ind = np.array([3, 5, 7, 9], dtype=np.int)
    iterCompute(ind)

    # Last time n=10
    ind = np.array([10], dtype=np.int)
    print('Test with n = ', ind[0])
    iterCompute(ind)


if __name__ == "__main__":
    main()
