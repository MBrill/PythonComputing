# -*- coding: utf-8 -*-
"""
The Hilbert matrix.
"""

import numpy as np
from scipy import linalg

# Output the Hilbert matrix
n = 9
hilbert = linalg.hilbert(n)
print('Hilbert Matrix for n=', n)
print(hilbert)

# The inverse of the Hilbert matrix is known exactly
# and contains (in theory) only integer values.
# For values of n bigger than 14 the integers in the
# inverse Hilbert matrix are bigger than the integers
# we can work with.
# use invhilbert(n, exact = False) from n>=15 on.
# from scipy docs:
# invhilbert(16)[7,7]
# 4.2475099528537506e+19
# invhilbert(16, exact=True)[7,7]
# 42475099528537378560
hilbert_inv = linalg.invhilbert(n)
print('Inverse of Hilbert Matrix for n=', n)
print(hilbert_inv)

# H * Hinv should be the identity matrix
print('The product of H and the inverse should be the identy matrix')
print(np.matmul(hilbert, hilbert_inv))

# We solve a linear equation system for the columns of Hinv
# Use the identiy matrix as right hand side
rhs = np.identity(n)

computed_inv = np.linalg.solve(hilbert, rhs)
print('Result of the computation of the inverse using linalg.solve')
print(computed_inv)

print('Relative Error for computing the inverse of a Hilbert matrix')
print('n = ', n)
# relativer Fehler noch implementieren!
print(np.linalg.norm(hilbert_inv - computed_inv))
