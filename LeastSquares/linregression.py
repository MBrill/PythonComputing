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

result = stats.linregress(data)
print(result.slope, result.intercept)

print('Weitere Ausgaben der Funktion stats.linregression')
print('Bestimmtheits1mass: ', result.rvalue)
print('p-Wert: ', result.pvalue)
print('Least-Squares Fehler: ', result.stderr)

# Koordinaten für die Ausgleichsgerade
xmin = np.min(data[:, 0])
xmax = np.max(data[:, 0])
xvals = np.linspace(xmin, xmax, num=2)
yvals = result.slope*xvals + result.intercept

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Lineare Regression mit scipy.stats',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'og')
plt.plot(xvals, yvals, '-r')

plt.show()
fig.savefig('images/wassergehaltscp.png', dpi=300)
