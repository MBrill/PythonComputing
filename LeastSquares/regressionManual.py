# -*- coding: utf-8 -*-
"""
Lineare Ausgleichsrechnung mit der QR-Zerlegung
für den Datensatz Wassergehalt

Wir berechnen a = qr, q^T b und lösen r x = q^T b.
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# Daten einlesen
data = np.genfromtxt('wassergehalt.csv',
                     delimiter=';', skip_header=True)

a = np.ones(shape=(data.shape[0], 2))
a[:, 0] = data[:, 0]
rhs = data[:, 1]

q, r = linalg.qr(a)

qrhs = np.transpose(q) @ rhs
x = linalg.solve_triangular(r[:2, :], qrhs[:2])
m = x[0]
b = x[1]

print('Ergebnisse der lineare Ausgleichnungsrechnung mit QR-Zerlegung')
print('Steigung der Geraden: ', m)
print('Der Achsenabschnitt der Gerade: ', b)

# Vorhersagen
rL = np.array([30.0, 60.0])
Wg = m*rL + np.full(shape=(2, ), fill_value=b)
print('Vorhersagen')
print(rL)
print(Wg)

# Koordinaten für die Ausgleichsgerade
xmin = np.min(data[:, 0])
xmax = np.max(data[:, 0])
xvals = np.linspace(xmin, xmax, num=2)
yvals = m*xvals + b

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Streuungsdiagramm und Ausgleichsgerade für den Datensatz Wassergehalt',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('Luftfeuchtigkeit in Prozent')
plt.ylabel('Wassergehalt in Prozent')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)
plt.plot(xvals, yvals, '-r')
plt.legend()

plt.show()
fig.savefig('images/wasserQR.png', dpi=300)
