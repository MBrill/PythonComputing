# -*- coding: utf-8 -*-
"""
Tridiagonal nxn matrices

We solve tridiagonal linear equations using SciPy.
"""
import numpy as np
from scipy import linalg


def vectors_to_matrix(a, b, c):
    """
    convert the vectors a, b und c to a banded-matrix for SciPy.

    Parameters
    ----------
    a : ndarray
        Diagonal elements, size of a is n.
    b : ndarray
        Elements in the upper diagonal, size of b is n-1.
    c : ndarray
        Elements in the upper diagonal, size of c is n-1.

    Returns
    -------
    nxn ndarray ab and the pair (l, u) = (1,1) for linalg.solve_banded.
    """
    n = a.shape[0]
    lu = (1, 1)
    ab = np.zeros(shape=(3, n), dtype=np.float64)
    ab[0, 1:n] = b[:]
    ab[1, :] = a[:]
    ab[2, 0:n-1] = c[:]
    return lu, ab


def matrix_to_vectors(ab):
    """
    convert the ab-matrix for solve_banded to three vectors

    Parameters
    ----------
    A : ndarray
        Tridiagonal nxn matrix.

    Returns
    -------
    a : ndarray
        Diagonal elements, size of a is n.
    b : ndarray
        Elements in the upper diagonal, size of b is n-1.
    c : ndarray
        Elements in the upper diagonal, size of c is n-1.
    """
    n = ab.shape[1]
    a = ab[1, :]
    b = ab[0, 1:n]
    c = ab[2, 0:n-1]
    return a, b, c


def main():
    """
    Tidiagonal matrices and solve_banded in SciPy

    Returns
    -------
    None.
    """
    a = np.full(shape=(4, ), fill_value=2.0)
    a[0] = 1.0
    b = c = np.full(shape=(3, ), fill_value=-1.0)
    lu, ab = vectors_to_matrix(a, b, c)
    print(lu)
    print(ab)

    a, b, c = matrix_to_vectors(ab)
    print(b)
    print(a)
    print(c)

    # Linear Equations
    print('Elimination')
    rhs = np.zeros(shape=(4, ), dtype=np.float32)
    rhs[0] = 5.0
    rhs[2] = 1.0
    x = linalg.solve_banded(lu, ab, rhs)

    correct = np.array([22.0, 17.0, 12.0, 6.0])
    check = x == correct
    if check.all():
        print('Everything worked!')
    else:
        print('Something is wrong ')
        print('Here is the check:\n')


if __name__ == "__main__":
    main()
