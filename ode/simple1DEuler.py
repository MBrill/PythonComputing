# -*- coding: utf-8 -*-
"""
Einfaches Beispiel für ein eindimensionales Euler-Verfahren
"""
import numpy as np
import euler1D
import matplotlib.pyplot as plt


def f(t, y):
    """
    Funktion in der Differentialgleichung

    Parameters
    ----------
    t : float
        Variable
    y : float
        Funktionswerte der gesuchten Lösung

    Returns
    -------
    float.
    """
    return (t + y)


n = 9
a = 0.0
b = 2.0

t = np.linspace(a, b, num=n+1)
y = np.zeros(shape=(n+1,))

y0 = 1.0
y = euler1D.euler1D(f, t, y0)

fig = plt.figure()
plt.grid(True)

# Grafische Ausgabe
plt.plot(t, y, 'g-')
plt.title('Lösung mit dem Eulerverfahren mit $h=0.25$')
plt.xlabel('t')
plt.ylabel('y(t)')

# Plot abspeichern
plt.savefig('images/euler2.png', dpi=120)
plt.show()
