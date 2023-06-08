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


a = 0.0
b = 2.0
n = 9

t = np.linspace(a, b, num=n+1)

y0 = 1.0
y = euler1D.euler1D(f, t, y0)

fig = plt.figure()
plt.grid(True)
plt.plot(t, y, 'g-', label='h=0.25')

n = 21
h = (b-a)/(n-1)
t = np.linspace(a, b, num=n+1)

y0 = 1.0
y = euler1D.euler1D(f, t, y0)

plt.plot(t, y, 'm-', label='h=0.1')

plt.title('Euler-Verfahren mit verschiedenen Schrittweiten')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()

# Plot abspeichern
plt.savefig('images/eulerdiff.png', dpi=120)
plt.show()
