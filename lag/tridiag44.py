# -*- coding: utf-8 -*-
"""
Tridiagonal 4x4 matrices

We implement Gauss-Elimination for 4x4 tridiagonal matrices.

We implement the elimination using vectors a for the diagonal,
b for the upper off-diagonal and c for the lower off-diagonal.

We implement helper functions to convert betweet a 4x4 matrix
and these vectors!
"""
import numpy as np


def vectors_to_matrix(a, b, c):
    """
    convert the vectors a, b und c to a 4x4-matrix.

    Parameters
    ----------
    a : ndarray
        Diagonal elements, size of a is 4.
    b : ndarray
        Elements in the upper diagonal, size of b is 3.
    c : ndarray
        Elements in the upper diagonal, size of c is 3.

    Returns
    -------
    4x4 ndarray.
    """
    A = np.zeros(shape=(4, 4))
    A.flat[::5] = a
    A.flat[1::5] = b
    A.flat[4::5] = c
    return A


def matrix_to_vectors(A):
    """
    convert the vectors a, b und c to a 4x4-matrix.

    Parameters
    ----------
    A : ndarray
        Tridiagonal 4x4 matrix.

    Returns
    -------
    a : ndarray
        Diagonal elements, size of a is 4.
    b : ndarray
        Elements in the upper diagonal, size of b is 3.
    c : ndarray
        Elements in the upper diagonal, size of c is 3.
    """
    a = np.zeros(shape=(4,))
    b = c = np.zeros(shape=(3,))
    a = A.flat[::5]
    b = A.flat[1::5]
    c = A.flat[4::5]
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
    for i in np.arange(1, 4):
        factor = c[i-1]/a[i-1]
        a[i] -= factor*b[i-1]
        rhs[i] -= factor*rhs[i-1]
    A.flat[::5] = a


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
    x = np.zeros(shape=(4,), dtype=np.float64)
    a, b, c = matrix_to_vectors(A)
    x[3] = rhs[3]/a[3]
    for i in np.arange(2, -1, -1):
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
