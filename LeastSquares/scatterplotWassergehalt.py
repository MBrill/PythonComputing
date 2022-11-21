# -*- coding: utf-8 -*-
"""
Ausgabe eines Scatter Plot für den Datensatz Wassergehalt
"""
import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('wassergehalt.csv',
                     delimiter=';', skip_header=True)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Streuungsdiagramm für den Datensatz Wassergehalt',
          y=1.05, fontsize=24)
plt.grid()
plt.xlabel('Luftfeuchtigkeit in Prozent')
plt.ylabel('Wassergehalt in Prozent')
plt.plot(data[:, 0], data[:, 1], 'og', markersize=10)
plt.legend()

plt.show()
fig.savefig('images/scatterWasser.png', dpi=300)
