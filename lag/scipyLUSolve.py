# -*- coding: utf-8 -*-
"""
Use lu_factor and lu_solve for solving a linear equation system
"""
import numpy as np
from scipy import linalg

a = np.array([[2, 5, 8, 7],
              [5, 2, 2, 8],
              [7, 5, 6, 6],
              [5, 4, 4, 8]
              ])
b = np.array([1, 1, 1, 1])

lu, piv = linalg.lu_factor(a)

print('LU factorization')
print('Permutation matrix after the LU factorization\n')
print(piv)
print('The matrix L and U\n')
print(lu)

x = linalg.lu_solve((lu, piv), b)
print('Computed solution', x)

if np.allclose(a @ x - b, np.zeros((4,))):
    print('Everything worked')
