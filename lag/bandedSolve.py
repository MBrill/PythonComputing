# -*- coding: utf-8 -*-
"""
Beispiel für die Verwendung von Band-Matrizen

Die Zahlenwerte stammen aus der SciPy-Dokumentation!
"""
import numpy as np
from scipy import linalg


l = 1
u = 2
ab = np.array([[0,  0, -1, -1, -1],
               [0,  2,  2,  2,  2],
               [5,  4,  3,  2,  1],
               [1,  1,  1,  1,  0]])

rhs = np.array([0, 1, 2, 2, 3])
x = linalg.solve_banded((l, u), ab, rhs)

print('Lösung', x)

# Eine Tridiagonalmatrix
l = 1
u = 1
a = np.array([0.0, 2.0, 2.0, 2.0, 2.0])
b = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
c = np.array([3.0, 3.0, 3.0, 3.0, 0.0])
ab = np.array([a, b, c])

# Alternatite Lösung für die Tridiagonalmatrix
# wie in der Kabelgleichung
l = 1
u = 1
upperElement = 1.0
diagElement = 2.0
lowerElement = 3.0
ab = np.zeros((3, 5))
ab[0, 1:] = upperElement
ab[1, :] = diagElement
ab[2, :-1] = lowerElement

# Probe für die Lösung des linearen Gleichungssystems
# Scheinbar gibt es keine Multiplikation, außer im
# Paket sparse. Aber da werden die Matrizen anders abgelegt.

# Wir vereinbaren A als "normale" Matrix
fullA = np.array([[5, 2, -1, 0, 0],
                 [1, 4, 2, -1, 0],
                 [0, 1, 3, 2, -1],
                 [0, 0, 1, 2, 2],
                 [0, 0, 0, 1, 1]])

if np.allclose(fullA @ x - rhs, np.zeros((5,))):
    print('Alles korrekt!')
