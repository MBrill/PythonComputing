# -*- coding: utf-8 -*-
"""
Lineare Ausgleichsrechnung mit nichtlinearen Ansatzfunktionen
für eine Kennlinie
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def f1(x):
    """
    Erste Ansatzfunktion

    Parameters
    ----------
    x : float
        x-Wert.

    Returns
    -------
    Funktionswert.
    """
    return x/(1.0+x)


def f2(x):
    """
    Zweite Ansatzfunktion

    Parameters
    ----------
    x : float
        x-Wert.

    Returns
    -------
    Funktionswert.
    """
    return 1.0-np.exp(-x)


data = np.genfromtxt('kennlinie.csv',
                     delimiter=';', skip_header=False)

# Zwei Spalten für zwei Ansatzfunktionen
a = np.ones(shape=(data.shape[0], 2))
a[:, 0] = f1(data[:, 0])
a[:, 1] = f2(data[:, 0])
rhs = data[:, 1]
q, r = linalg.qr(a)
qrhs = np.transpose(q) @ rhs
x = linalg.solve_triangular(r[:2, :], qrhs[:2])

print('Regression mit nicht-linearen Ansatzfunktionen')
print('Die Koeffizienten für die Ansatzfunktion: \n', x[0], x[1])

# Vorhersagen
xv = np.array([0.8, 1.25])
prediction = x[0] * f1(xv) + x[1] * f2(xv)
print('Vorhersagen')
print(xv)
print(prediction)

# Streuungsdiagramm ohne Ausgleichsparabel
fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Streuungsdiagramm',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)

plt.show()
fig.savefig('images/kennlinieScatter.png', dpi=300)

xmin = np.min(data[:, 0])
xmax = np.max(data[:, 0])
xvals = np.linspace(xmin, xmax, num=50)
yvals = x[0] * f1(xvals) + x[1] * f2(xvals)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Regression einer Kennlinie',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)
plt.plot(xvals, yvals, '-r')

plt.show()
fig.savefig('images/kennlinie.png', dpi=300)
