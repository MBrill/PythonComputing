# -*- coding: utf-8 -*-
"""
Lösung der diskretisierten Kabelgleichung mit
Bandmatrizen in SciPy.
"""
import numpy as np
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

# our system and the parameters of the wire equation
# boundary condition
ya = -1.0
yb = 2.0
# constant force (don't forget the minus sign!)
f = -20.0
# length of our wire
length = 1.0
# discretization parameters
n = 50
h = length/n

# Tridiagolmatrix als SciPy Bandmatrix
lowerDiag = 1
upperDiag = 1
diag = 2.0
offdiag = -1.0
aa = np.zeros((3, n))
aa[0, 1:] = offdiag
aa[1, :] = diag
aa[2, :-1] = offdiag
# rechte Seite
b = np.zeros((n, 1))
b[:] = h*h*f
# Randbedingungen in die rechte Seite einpflegen
b[0] += ya
b[-1] += yb
# SciPy aufrufen. Die Bandmatrix
# ist durch (lowerDiag, upperDiag), aa gegeben.
x = solve_banded((1, 1), aa, b)

# Vis
# Wir fügen die Randpunkten mit Hilfe von a und b hinzu.
# und verwenden Matplotlib.
wireX = np.linspace(0.0, length, n+2)
wireY = np.linspace(0.0, length, n+2)

wireY[0] = ya
wireY[1: -2] = x[:-1, 0]
wireY[n] = x[-1, 0]
wireY[n+1] = yb

fig = plt.figure(figsize=(16.0, 9.0))
plt.figure(dpi=600)
plt.grid(True)
plt.axis([0.0, length, np.floor(wireY.min()), max(ya, yb)+1.0])
plt.xticks([])
# plt.yticks([])
plt.plot(wireX, wireY, 'g-')
plt.title('Lösung der Kabelgleichung')

# plt.savefig('images/pdf2.png')
plt.show()
