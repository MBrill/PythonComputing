# -*- coding: utf-8 -*-
"""
Simulation einer Kühlrippe mit Hilfe der Wärmeleitungsgleichung
mit einer Blockmatrix dem cg-Algorithmus in SciPy.

Die Kühlrippe ist aktuell durch das Einheitsquadrat
gegeben. Links kommt eine konstante Temperatur an,
alle anderen Randwerte sind 0.

Wir beschränken uns auf den Fall n=5.
"""
import numpy as np
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
from matplotlib import cm

# Wir gehen von einer konstanten Temperatur am linken Rand aus
C = 2.0
# Der linke untere Rand wird als Ursprung angenommen
# Wie groß ist die Kühlrippe?
length = 1.0

# Funktionswert, als konstant angenommen
f = -0.1

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


x, exitCode = spla.gmres(A, rhs)
if exitCode == 0:
    x2d = np.reshape(x, (n, n), order='F')
    print(x2d)

boundary = np.full(shape=(n, 1), fill_value=C)
cooler = np.zeros(shape=(5, 6))
cooler[:, 0] = C
cooler[:, 1:6] = x2d[:, 0:5]

fig = plt.figure(figsize=(16.0, 16.0))

ax = plt.imshow(cooler, cmap=cm.Oranges, origin='lower')
plt.xticks([])
plt.yticks([])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lösung der Kühlrippe',
          y=1.05, fontsize=24)
cbar = fig.colorbar(ax)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('Temperaturen', rotation=270)
