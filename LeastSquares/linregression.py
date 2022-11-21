# -*- coding: utf-8 -*-
"""
Lineare Ausgleichsrechnung im Modul stats

Daten stammen aus der csv-Datei wassergehalt.csv
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.genfromtxt('wassergehalt.csv',
                     delimiter=';', skip_header=True)

r = stats.linregress(data)

print('Korrekte Werte')
print('Die Steigung der Gerade ist 0.236')
print('Der Achsenabschnitt ist 2.665')
print(r.slope, r.intercept)

print('Berechnungsergebnisse')
print('Bestimmtheits1mass: ', r.rvalue)
print('p-Wert: ', r.pvalue)
print('Least-Squares Fehler: ', r.stderr)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'oc', label='data points')
plt.plot(data[:, 0], r.slope*data[:, 0] + r.intercept, '-g',
         label='data points')
plt.legend()

plt.show()

fig.savefig('images/wassergehalt.png', dpi=300)
