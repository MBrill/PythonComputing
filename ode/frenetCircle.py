# -*- coding: utf-8 -*-
"""
SciPy Beispiel für ein Anfangswertproblem für Parameterkurven
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

r = 2.0


def k(s):
    """
    Krümmung der gesuchten Kurve

    Parameters
    ----------
    s : float
        Paramterwerte.

    Returns
    -------
    Wert der Krümmung für den Parameterwert s.
    """
    return 1.0/r


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


a = 0.0
b = 4.0*np.pi
n = 100
points = np.linspace(a, b, n)

# Krümmung grafisch darstellen
kVec = np.vectorize(k)
kappaValues = kVec(points)

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
plt.title('Kurve mit konstanter Krümmung')
plt.xlabel('x')
plt.ylabel('y)')

# Plot abspeichern
#plt.savefig('images/ivp1.png', dpi=150)
plt.show()
