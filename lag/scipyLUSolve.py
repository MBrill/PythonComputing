# -*- coding: utf-8 -*-
"""
LU-Zerlegung in SciPy und Auflösung des linearen Gleichungssystems
"""
import numpy as np
from scipy import linalg

A = np.array([[3, 1, 6],
              [2, 1, 3],
              [1, 1, 1]
              ])

lu, piv = linalg.lu_factor(A)

print('Die berechnete Permutationsmatrix\n')
print(piv)
print('\nDie Matrizen L und U in einer Matrix\n')
print(lu)

b = np.array([10, 6, 3])
x = linalg.lu_solve((lu, piv), b)
print('\nDie berechnete Lösung: ', x)

if np.allclose(A @ x - b, np.zeros((3,))):
    print('Alles korrekt berechnet')

# Noch eine rechte Seite
b = np.array([2, 1, 3])
x = linalg.lu_solve((lu, piv), b)
print('Die berechnete Lösung: ', x)
if np.allclose(A @ x - b, np.zeros((3,))):
    print('Alles korrekt berechnet')
