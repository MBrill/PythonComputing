# -*- coding: utf-8 -*-
"""
Visualisierung einer Mandelbrot-Menge.

Original stammt von Tom Roelands. Kommentare und PEP8: Manfred Brill

https://tomroelandts.com/articles/how-to-compute-the-mandelbrot-set-using-numpy-array-operations
"""
import numpy as np
import matplotlib.pyplot as plt

# Auflösung in "Pixel" des Rechtsecks in der komplexen Zahlenebene
m = 480
n = 480
# Rechteck auf der reellen und der imaginären Achse
xmin = -2.0
xmax = 2.0
ymin = -2.0
ymax = 2.0

x = np.linspace(xmin, xmax, num=m).reshape((1, m))
y = np.linspace(ymin, ymax, num=n).reshape((n, 1))
# mxn Matrix aus x und y bauen mit tile
# np.tile multipliziert die Elemente so aus,
# dass auf der Matrix C der meshgrid steht
C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

# Iteration startet bei 0
Z = np.zeros((n, m), dtype=np.complex)

# Die Entscheidung, ob ein Punkt in der Mandelbrot-Menge liegt
# wird mit einer logischen Matrix durchgeführt, mit
# der wir auch indizieren können.
# Tritt während der Iteration Divergenz auf,
# wird das entsprechende Element in M False gesetzt
M = np.full((n, m), True, dtype=np.bool)
# Maximale Anzahl der Iterationen
n = 100
divBarrier = 2.0
for i in range(n):
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > divBarrier] = False

# Für invert == True verwenden wir schwarzen Hintergrund,
# für False ist der Hintergrund weiss und die Menge schwarz.
invert = False
if invert:
    color_map = plt.cm.get_cmap('gray')
else:
    color_map = plt.cm.get_cmap('gray').reversed()

plt.figure(figsize=(8.0, 4.0))
plt.imshow(M, cmap=color_map, origin='lower')
plt.xlabel('')
plt.ylabel('')
plt.xticks(np.arange(0.0, 481.0, 240.0), (xmin, 0.0, xmax))
plt.yticks(np.arange(0.0, 321.0, 160.0), (ymin, 0.0, ymax))
plt.title('Mandelbrot-Menge')

dpi = 150
plt.savefig('images/mandelbrot.png', dpi=dpi)
plt.show()
