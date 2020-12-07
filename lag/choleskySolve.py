# -*- coding: utf-8 -*-
"""
Use Cholesky algorithm for a positive definite matrix
"""
import numpy as np
from scipy import linalg

# Hanke Faktorisierungs-Beispiel
A = np.array([[1, 2, 1],
             [2, 5, 2],
             [1, 2, 10]])

c, low = linalg.cho_factor(A)
correctL = np.array([[1, 2, 1],
                     [0, 1, 0],
                     [0, 0, 3]])

print('Solution of linalg.cho_factor')
print('Look at the upper matrix!')
print(c)

print('Correct L from Hanke-Bourgeois')
print(correctL)

# SciPy documentation example
A = np.array([[9, 3, 1, 5],
              [3, 7, 5, 1],
              [1, 5, 9, 2],
              [5, 1, 2, 6]])
c, low = linalg.cho_factor(A)
x = linalg.cho_solve((c, low), [1, 1, 1, 1])
if np.allclose(A @ x - [1, 1, 1, 1], np.zeros(4)):
    print('Test passed')

# Example from Schwarz, p. 41
A = np.array([[5, 7, 3],
              [7, 11, 2],
              [3, 2, 6]
              ])
b = np.array([0, 0, 1])
c, low = linalg.cho_factor(A)
x = linalg.cho_solve((c, low), b)
# Solution from Schwarz
xexact = np.array([-19.0, 11.0, 6.0])

if np.allclose(x, xexact):
    print('Ok')

if np.allclose(A @ x - b, np.zeros((3,))):
    print('Test passed')
