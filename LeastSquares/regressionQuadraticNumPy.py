# -*- coding: utf-8 -*-
"""
Lineare Ausgleichsrechnung mit einer Parabel
auf der Basis der Funktion numpy.polyfit.
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('quadratic.csv',
                     delimiter=';', skip_header=False)

coeff = np.polyfit(data[:, 0], data[:, 1], deg=2)

print('Ergebnisse der Funktion np.polyfit')
print('Die Koeffizienten des quadratischen Polynoms: \n',
      coeff[0], coeff[1], coeff[2])

# Berechnung der Daten für die Ausgleichsparabel
xmin = np.min(data[:, 0])
xmax = np.max(data[:, 0])
xvals = np.linspace(xmin, xmax, num=50)
yvals = np.polyval(coeff, xvals)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Quadratisches Ausgleichspolynom mit numpy.polyfit',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)
plt.plot(xvals, yvals, '-r')

plt.show()
fig.savefig('images/quadraticNumPy.png', dpi=300)
