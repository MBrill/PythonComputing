# -*- coding: utf-8 -*-
"""
Visualisierung einer Julia-Menge mit den Attraktoren für z^3-1 = 0
"""
import numpy as np
import matplotlib.pyplot as plt


def iterate(xy: np.complex, n=100, epsilon=0.0001):
    """
    Durchführung des Newton-Verfahrens für z^3-1=0 in der reellen Formulierung.
    Wir überprüfen nur, ob Konvergenz stattgefunden hat
    Parameters
    ----------
    xy: np.complex ndarray
        x- und y-Werte des Startwerts.
    n : np.int
        Maximale Anzahl der Iterationen.
    epsilon : np.float64
        Abbruchgenauigkeit für die Entscheidung, ob der Algorithmus
        gegen eine der Nullstellen konvergiert.

    Returns
    -------
    i : np.int
        Wert mit der Entscheidung.
        0 bedeutet keine Konvergenz,
        1, 2, 3 bedeutet KOnvergenz gegen eine der Einheitswurzeln.
    """
    # Die drei Einheitswurzeln
    x0 = np.complex(1.0, 0.0)
    x1 = np.complex(-0.5, 0.5*np.sqrt(3.0))
    x2 = np.complex(-0.5, -0.5*np.sqrt(3.0))
    # Anfangswerte kopieren und auf Kopien die Iteration durchführen
    s = xy
    s1 = np.zeros(shape=(2,), dtype=np.complex)
    for i in np.arange(n+1):
        s1 = s - (s**3-1.0)/(3.0*s**2)
        # Entscheidung
        if (np.linalg.norm(s1-x0) < epsilon):
            return 1
        if (np.linalg.norm(s1-x1) < epsilon):
            return 2
        if (np.linalg.norm(s1-x2) < epsilon):
            return 3
        s = s1

    return 0


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
xy = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

M = np.zeros(shape=(n, m), dtype=np.int)
for i in np.arange(n):
    for j in np.arange(m):
        M[i, j] = iterate(xy[i, j])


print('Computation done!')

fig = plt.figure(figsize=(8.0, 8.0))
color_map = plt.cm.get_cmap('jet', 4)
ax = plt.imshow(M,
                cmap=color_map,
                interpolation='nearest',
                origin='lower')

plt.xlabel('')
plt.ylabel('')
plt.xticks(np.arange(0.0, 481.0, 240.0), (xmin, 0.0, xmax))
plt.yticks(np.arange(0.0, 481.0, 240.0), (ymin, 0.0, ymax))
plt.title('Julia-Menge für $x^3-1$')


dpi = 150
plt.savefig('images/julia.png', dpi=dpi)
plt.show()
