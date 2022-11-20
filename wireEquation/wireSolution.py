# -*- coding: utf-8 -*-
"""
Lösung der diskretisierten Kabelgleichung mit
Bandmatrizen in SciPy.
"""
import numpy as np
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

# Wie hoch ist das Kabel an den beiden Enden in y?
ya = 5.0
yb = 3.0
# Wo ist der rechte Punkt des Kabels auf der x-Achse?
length = 3.0
# Krafvektor mit konstantem Wert - der Wert muss negativ sein!
f = -30.0

# Wie fein ist die Diskretisierung?
n = 50
h = length/n

# Tridiagonalmatrix als SciPy Bandmatrix
diagElement = 2.0
offdiagElement = -1.0
upperCount = 1
lowerCount = 1
aa = np.zeros((3, n))
aa[0, 1:] = offdiagElement
aa[1, :] = diagElement
aa[2, :-1] = offdiagElement
# rechte Seite
b = np.full((n, 1), fill_value=h*h*f)
# Randbedingungen in die rechte Seite einpflegen
b[0] += ya
b[-1] += yb

# SciPy Solver aufrufen.
x = solve_banded((upperCount, lowerCount), aa, b)

# Der Polygonzug für die Visualisierung liegt auf wireX, wireY
# Wir fügen die Randpunkte mit Hilfe von ya und yb hinzu.
wireX = np.linspace(0.0, length, n+2)
wireY = np.linspace(0.0, length, n+2)
wireY[0] = ya
wireY[1: -2] = x[:-1, 0]
wireY[n] = x[-1, 0]
wireY[n+1] = yb

fig = plt.figure(figsize=(16.0, 9.0))
plt.figure(dpi=600)
plt.grid(True)
plt.axis([0.0, length, np.floor(wireY.min())-1.0, max(ya, yb)+1.0])
plt.plot(wireX, wireY, 'g-')
# Randpunkte ausgeben
plt.plot(0.0, wireY[0], 'ks')
plt.plot(length, wireY[n+1], 'ks')
plt.title('Lösung der Kabelgleichung')

plt.savefig('images/wiren50a5b3.png')
plt.show()
