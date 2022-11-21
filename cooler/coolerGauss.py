# -*- coding: utf-8 -*-
"""
Simulation einer Kühlrippe mit Hilfe der Wärmeleitungsgleichung
mit einer Blockmatrix und Gauss in SciPy.

Die Kühlrippe ist aktuell durch das Einheitsquadrat
gegeben. Links kommt eine konstante Temperatur an,
alle anderen Randwerte sind 0.
"""
import numpy as np
from scipy import linalg
import scipy.sparse as sparse
import scipy.sparse.linalg as spla
# import matplotlib.pyplot as plt

# Wir gehen von einer konstanten Temperatur am linken Rand aus
C = 1.0
# Der linke untere Rand wird als Ursprung angenommen
# Wie groß ist die Kühlrippe?
length = 1.0

# Funktionswert, als konstant angenommen
f = -0.5

# Wie fein ist die Diskretisierung?
# Wir verwenden eine n^2 x n^2 Matrix
n = 5
h = length/(n+1)
n2 = n*n

# Rechte Seite
# Die ersten n Elemente der insgesamt n^2 Element
# enthalten den Randwert C
# rechte Seite
rhs = np.full((n2, 1), fill_value=-h*h*f)
# Randbedingungen in die rechte Seite einpflegen
rhs[0:n] += C

# Diagonalblock B
diagElement = 4.0
offdiagElement = -1.0
E = np.eye(n)
E = diagElement*E
F = offdiagElement*np.eye(len(E), k=1)
G = offdiagElement*np.eye(len(E), k=-1)
B = E+F+G
MinusI = -E

# Block-Matrix bauen
A = np.block([
    [B, MinusI, np.zeros((n, 3*n))],
    [np.zeros((n, n)), B, MinusI, np.zeros((n, 2*n))],
    [np.zeros((n, 2*n)), B, MinusI, np.zeros((n, n))],
    [np.zeros((n, 3*n)), B, MinusI],
    [np.zeros((n, 4*n)), B]
])

# SciPy Solver aufrufen.
x = linalg.solve(A, rhs)
# = solve_banded((upperCount, lowerCount), aa, rhs)

# Jetzt x wieder zu einem zweidimensionalen Feld machen
# und die Werte mit Hilfe einer Heatmap darstellen
x2d = np.reshape(x, (n, n), order='F')
print(x2d)
