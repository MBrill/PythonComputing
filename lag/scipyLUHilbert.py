# -*- coding: utf-8 -*-
"""
Use lu_factor and lu_solve with the Hilbert matrix.
"""
import numpy as np
from scipy import linalg


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
    a = linalg.hilbert(n)
    b = np.zeros(shape=(n, ), dtype=np.float64)
    b[0] = np.float64(1.0)

    lu, piv = linalg.lu_factor(a)
    x = linalg.lu_solve((lu, piv), b)
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
    print('We use linalg.lu_factor and linalg.lu_solve')
    ind = np.array([3, 5, 7, 9], dtype=np.int)
    iterCompute(ind)

    # from n=11 to 20
    n = 11
    ind = np.arange(n, 20, 2)
    iterCompute(ind)


if __name__ == "__main__":
    main()
