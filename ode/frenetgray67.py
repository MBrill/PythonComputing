# -*- coding: utf-8 -*-
"""
SciPy Beispiel für ein Anfangswertproblem für Parameterkurven.
in Anhehnung an Gray.
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def k(s):
    """
    Krümmung der gesuchten Kurve: s + sin(s)

    Parameters
    ----------
    s : float
        Paramterwerte.

    Returns
    -------
    Wert der Krümmung für den Parameterwert s.
    """
    return (s * s * np.sin(s))


def func(s, y):
    """
    Rechte Seite aus Gray, p. 103

    Parameters
    ----------
    s : float
        Unabhängige Variable
    y : float
        Funktionswerte der gesuchten Lösung.

    Returns
    -------
    float.
    """
    return [np.cos(y[2]), np.sin(y[2]), k(s)]


a = -10.0
b = 10.0
n = 500
points = np.linspace(a, b, n)

# Krümmung grafisch darstellen
kappaValues = k(points)

fig = plt.figure()
plt.grid(True)

plt.plot(points, kappaValues, 'g-')
plt.title('Vorgegebene Krümmung')
plt.ylabel('kappa')

# ODE lösen und visualisieren
ivs = np.array([0, 0, k(a)])
sol = integrate.solve_ivp(fun=func,
                          t_span=[a, b],
                          y0=ivs,
                          t_eval=points)

if sol.success:
    y1 = sol.y[0, :]
    y2 = sol.y[1, :]
    y3 = sol.y[2, :]

fig, axs = plt.subplots(1, 1)
axs.axis('equal')
plt.grid(True)

plt.plot(y1, y2, 'g-')
plt.title('Kurve mit der vorgegebenen Krümmung')
plt.xlabel('x')
plt.ylabel('y)')

# Plot abspeichern
#plt.savefig('images/ivp1.png', dpi=150)
plt.show()
