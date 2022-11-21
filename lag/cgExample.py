# -*- coding: utf-8 -*-
"""
Beispiel für den CG-Algorithmus in SciPy
"""
import numpy as np
import scipy.sparse.linalg as spla
import scipy.sparse as sparse

A = sparse.csc_matrix([[3, 2, 0], [1, -1, 0], [0, 5, 1]], dtype=float)
b = np.array([2, 4, -1], dtype=float)

print('SciPy documentation example')
x, exitCode = spla.gmres(A, b)
if exitCode == 0:
    print('Ok')

if np.allclose(A.dot(x), b):
    print('Test passed')

# Example from Schwarz, p. 41
A = np.array([[5, 7, 3],
              [7, 11, 2],
              [3, 2, 6]
              ])
b = np.array([0, 0, 1])
x, exitCode = spla.gmres(A, b)

# Solution from Schwarz
xexact = np.array([-19.0, 11.0, 6.0])

print('Example from Schwarz')
if np.allclose(x, xexact):
    print('Ok')

if np.allclose(A @ x - b, np.zeros((3,))):
    print('Test passed')
