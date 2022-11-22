# -*- coding: utf-8 -*-
"""
Lineare Ausgleichsrechnung auf Basis der QR-Zerlegung
mit einem quadratischen Polynom.
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

data = np.genfromtxt('quadratic.csv',
                     delimiter=';', skip_header=False)

a = np.ones(shape=(data.shape[0], 3))
a[:, 0] = data[:, 0]*data[:, 0]
a[:, 1] = data[:, 0]
rhs = data[:, 1]
q, r = linalg.qr(a)
qrhs = np.transpose(q) @ rhs
coeff = linalg.solve_triangular(r[:3, :], qrhs[:3])
a2, a1, a0 = coeff
print('Regression mit einem quadratischen Polynom')
print('Die Koeffizienten des Polynoms \n', a2, a1, a0)

# Vorhersagen
xv = np.array([0.8, 1.25])
prediction = np.polyval(coeff, xv)
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
fig.savefig('images/quadraticScatter.png', dpi=300)

# Berechnung der Daten für die Ausgleichsparabel
xmin = np.min(data[:, 0])
xmax = np.max(data[:, 0])
xvals = np.linspace(xmin, xmax, num=50)
yvals = np.polyval(coeff, xvals)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Lineare Regression mit einem quadratischen Polynom',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)
plt.plot(xvals, yvals, '-r')

plt.show()
fig.savefig('images/quadratic.png', dpi=300)
