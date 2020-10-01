# -*- coding: utf-8 -*-
"""
Computing some examples for the Mandelbrot set.
"""
import numpy as np

c = np.complex(0.0, 0.0)


def quadraticPoly(z, c):
    """
    Compute a value for the quadratic polynomial
    for the Mandelbrot set.

    Parameters
    ----------
    z : np.complex
        Argument of the polynomial.
    c : np.complex
        Value for c.

    Returns
    -------
    Function value as a complex number (np.complex).
    """
    return z*z + c


def iterate(c, n, divBarrier=2.0):
    """
    The first n iterations for the Mandelbrot set.
    The results are printed on the console.

    Parameters
    ----------
    c : np.complex
        Value of c in the polynomial.
    n : np.int
        Number of iterations to be computed.
    divBarrier : np.float
        Barrier for the decision of divergence.
        If abs(z) ist getting bigger than that number we
        assume the sequence is diverging.
        If we do not use such a number wie get Nan quite fast!

    Returns
    -------
    None.
    """
    z = np.complex(0.0, 0.0)
    absz = np.abs(z)
    print('Value of c: ', c)
    print('z = ', z)
    print('abs(z) = ', absz)
    for i in range(n):
        print('Iteration', i)
        z = quadraticPoly(z, c)
        absz = np.abs(z)
        print('z = ', z)
        print('abs(z) = ', absz)
        if (absz > divBarrier):
            break

n=4
c = np.complex(1.0, 0.0)
iterate(c, 4, 1000.0)

print('\n')
c = np.complex(0.0, 1.0)
iterate(c, 4, 1000.0)

print('\n')
c = np.complex(1.0, 1.0)
iterate(c, 4, 1000.0)

print('\n')
c = np.complex(0.1, 0.1)
iterate(c, 4, 1000.0)

print('\n')
c = np.complex(0.0, 0.5)
iterate(c, 4, 1000.0)