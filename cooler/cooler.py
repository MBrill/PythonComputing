# -*- coding: utf-8 -*-
"""
Simulation einer Kühlrippe mit Hilfe der Wärmeleitungsgleichung
mit Bandmatrizen in SciPy.

Die Kühlrippe ist aktuell durch das Einheitsquadrat
gegeben. Links kommt eine konstante Temperatur an,
alle anderen Randwerte sind 0.
"""
import numpy as np
from scipy.linalg import solve_banded
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
from matplotlib import cm

# Wir gehen von einer konstanten Temperatur am linken Rand aus
C = 2.0
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

# Koeffizientenmatri als SciPy Band-Matrix
diagElement = 4.0
offdiagElement = -1.0
zeroElement = 0.0
upperCount = n
lowerCount = n

aa = np.zeros(shape=(2*n+1, n2))
aa[0, n:] = offdiagElement
aa[n-1, 1:] = offdiagElement
aa[n, :] = diagElement
aa[n+1, :-1] = offdiagElement
aa[2*n, :-n] = offdiagElement

# SciPy Solver aufrufen.
x = solve_banded((upperCount, lowerCount), aa, rhs)

# Jetzt x wieder zu einem zweidimensionalen Feld machen
# und die Werte mit Hilfe einer Heatmap darstellen
x2d = np.reshape(x, (n, n), order='F')
print(x2d)

A = (upperCount, lowerCount), aa
x, exitCode = spla.gmres(A, rhs)
if exitCode == 0:
    x2d = np.reshape(x, (n, n), order='F')
    print(x2d)

boundary = np.full(shape=(n, 1), fill_value=C)
cooler = np.zeros(shape=(n, n+1))
cooler[:, 0] = C
cooler[:, 1:n+1] = x2d[:, 0:n]

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
