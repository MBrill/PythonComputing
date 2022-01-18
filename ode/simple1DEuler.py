# -*- coding: utf-8 -*-
"""
Example for a simple one-dimensionale Euler
"""
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    """
    Function in the ode,

    Parameters
    ----------
    t : float
        Independent variable.
    y : float
        solution we look for.

    Returns
    -------
    float.
    """
    return (t + y)


n = 9
a = 0.0
b = 2.0
h = (b-a)/(n-1)

t = np.linspace(a, b, num=n+1)
y = np.zeros(shape=(n+1,))

y[0] = 1.0
for i in np.arange(n):
    y[i+1] = y[i] + h*f(t[i], y[i])

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
