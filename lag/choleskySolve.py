# -*- coding: utf-8 -*-
"""
Use Cholesky algorithm for a positive definite matrix

1. Beispiel: Hanke Faktorisierungs-Beispiel
2. Beispiel: SciPy Dokumentation
3. Beispiel: aus Schwarz, p. 41
"""
import numpy as np
from scipy import linalg


A = np.array([[1, 2, 1],
             [2, 5, 2],
             [1, 2, 10]])

c, low = linalg.cho_factor(A)
correctL = np.array([[1, 2, 1],
                     [0, 1, 0],
                     [0, 0, 3]])

print('Zerlegung mit linalg.cho_factor')
print(c)

print('Korrektes L aus Hanke-Bourgeois')
print(correctL)

# SciPy documentation example
A = np.array([[9, 3, 1, 5],
              [3, 7, 5, 1],
              [1, 5, 9, 2],
              [5, 1, 2, 6]])
c, low = linalg.cho_factor(A)
x = linalg.cho_solve((c, low), [1, 1, 1, 1])
print('SciPy Beispiel')
if np.allclose(A @ x - [1, 1, 1, 1], np.zeros(4)):
    print('Test passed')

# Drittes Beispiel aus Schwarz
print('Beispiel aus Schwarz')
A = np.array([[5, 7, 3],
              [7, 11, 2],
              [3, 2, 6]
              ])
b = np.array([0, 0, 1])
xexact = np.array([-19.0, 11.0, 6.0])
c, low = linalg.cho_factor(A)
x = linalg.cho_solve((c, low), b)

if np.allclose(x, xexact):
    print('Ok')

if np.allclose(A @ x - b, np.zeros((3,))):
    print('Ok')

# Das Beispiel von Schwarz mit linalg.solve
print('Mit linalg.solve')
x = linalg.solve(A, b, assume_a='sym')
if np.allclose(x, xexact):
    print('Ok')
