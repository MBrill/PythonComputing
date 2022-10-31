# -*- coding: utf-8 -*-
"""
Beispiel für die Verwendung von Band-Matrizen

Die Zahlenwerte stammen aus der SciPy-Dokumentation!
"""
import numpy as np
from scipy import linalg


l=1
u=2
ab = np.array([[0,  0, -1, -1, -1],
               [0,  2,  2,  2,  2],
               [5,  4,  3,  2,  1],
               [1,  1,  1,  1,  0]])

b = np.array([0, 1, 2, 2, 3])
x = linalg.solve_banded((l, u), ab, b)

print('Lösung', x)

# Eine Tridiagonalmatrix
l = 1
u = 1
a = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
b = np.array([0.0, 2.0, 2.0, 2.0, 2.0])
c = np.array([3.0, 3.0, 3.0, 3.0, 0.0])
ab = np.array([b, a, c])
print(ab)
