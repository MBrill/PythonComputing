# -*- coding: utf-8 -*-
"""
Tridiagonal nxn matrices

We implement Gauss-Elimination for nxn tridiagonal matrices.

We implement the elimination using vectors a for the diagonal,
b for the upper off-diagonal and c for the lower off-diagonal.

We implement helper functions to convert betweet a nxn matrix
and these vectors!

This module is based on the 4x4 examples in tridiag44.py!
"""
import numpy as np


def vectors_to_matrix(a, b, c):
    """
    convert the vectors a, b und c to a nxn-matrix.

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
    nxn ndarray.
    """
    n = a.shape[0]
    A = np.zeros(shape=(n, n), dtype=np.float64)
    A.flat[::n+1] = a
    A.flat[1::n+1] = b
    A.flat[n::n+1] = c
    return A


def matrix_to_vectors(A):
    """
    convert a nxn-matrix to vectors a, b und c.

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
    n = A.shape[0]
    a = np.zeros(shape=(n,), dtype=np.float64)
    b = c = np.zeros(shape=(n-1,), dtype=np.float64)
    a = A.flat[::n+1]
    b = A.flat[1::n+1]
    c = A.flat[n::n+1]
    return a, b, c


def elimination(A, rhs):
    """
    Gauss-Elimination for a 4x4 tridiagonal matrix.

    If you need the original matrix or the right hand side save it
    before calling this function using np.copy()!

    Parameters
    ----------
    A : ndarray
        Matrix with shape (4,4), tridiagonal.
    rhs : ndarray
        Right hand side with shape (4,).

    Returns
    -------
    Eliminated upper matrix, the lower part is unchanged and eliminated
    right hand side.
    """
    a, b, c = matrix_to_vectors(A)
    n= A.shape[0]
    for i in np.arange(1, n):
        factor = c[i-1]/a[i-1]
        a[i] -= factor*b[i-1]
        rhs[i] -= factor*rhs[i-1]
    A.flat[::n+1] = a


def backsubstitution(A, rhs):
    """
    Solving the tridiagonal system Ax = rhs.

    We expect A and rhs to be the result of the function elimination.

    Parameters
    ----------
    A : ndarray
        Eliminated coefficient matrix, shape is (4,4).
    rhs : ndarray
        Eliminated right hand side, shape is (4,).

    Returns
    -------
    Solution vector x, shape is (4,).
    """
    n = rhs.shape[0]
    x = np.zeros(shape=(n,), dtype=np.float64)
    a, b, c = matrix_to_vectors(A)
    x[n-1] = rhs[n-1]/a[n-1]
    for i in np.arange(n-2, -1, -1):
        x[i] = (1.0/a[i])*(rhs[i] - b[i]*x[i+1])
    return x


def main():
    """
    Gauss elimination and back substitution for tridiagonal matrices.

    Returns
    -------
    None.
    """
    a = np.full(shape=(4, ), fill_value=2.0)
    a[0] = 1.0
    b = c = np.full(shape=(3, ), fill_value=-1.0)
    A = vectors_to_matrix(a, b, c)
    print('The matrix')
    print(A)

    print('Elimination')
    print('Note that the elements in the lower triangle are unchanged!')
    rhs = np.zeros(shape=(4, ), dtype=np.float32)
    rhs[0] = 5.0
    rhs[2] = 1.0
    elimination(A, rhs)
    print('Eliminated matrix')
    print(A)
    print('Eliminated right hand side')
    print(rhs)

    print('The solution')
    x = backsubstitution(A, rhs)
    print(x)


if __name__ == "__main__":
    main()
