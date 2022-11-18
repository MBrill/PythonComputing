# -*- coding: utf-8 -*-
"""
LU-Zerlegung für ein kleines Blur-Beispiel
"""
import numpy as np
from scipy import linalg

A = np.array([[1.0, 1.0, 0.0, 0.0, 0.0],
              [1.0, 1.0, 1.0, 0.0, 0.0],
              [0.0, 1.0, 1.0, 1.0, 0.0],
              [0.0, 0.0, 1.0, 1.0, 1.0],
              [0.0, 0.0, 0.0, 1.0, 1.0]
              ])

correct = np.ones(shape=(5,))

b = A@correct
print(b)

# Die Tridiganolmatrix als Bandmatrix
ldiag = 1
udiag = 1
a = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
b = np.array([0.0, 1.0, 1.0, 1.0, 1.0])
c = np.array([1.0, 1.0, 1.0, 1.0, 0.0])
ab = np.array([b, a, c])
print(ab)

x = linalg.solve_banded((ldiag, udiag), ab, b)

#b = np.array([12.0, 3.0, 3.0, 3.0, 2.0])
#x = linalg.lu_solve((lu, piv), b)
#print('\nDie berechnete Lösung: ', x)

# if np.allclose(A @ x - b, np.zeros((5,))):
#print('Alles korrekt berechnet')
