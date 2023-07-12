# -*- coding: utf-8 -*-
"""
SciPy Beispiel für ein Anfangswertproblem für Parameterkurven
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def k(s, r=1.0):
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
b = 2.0*np.pi
n = 50
eval = np.linspace(a, b, n)

# Array mit 2 Startwerten
r = 1.0
ivs = np.array([r, 0.0, k(a, r)])
sol = integrate.solve_ivp(fun=func,
                          t_span=[a, b],
                          y0=ivs,
                          t_eval=eval)

if sol.success:
    y1 = sol.y[0, :]
    y2 = sol.y[1, :]
    y3 = sol.y[1, :]

fig, axs = plt.subplots(1, 1)
axs.axis('equal')
plt.grid(True)

plt.plot(y1, y2, 'g-')
plt.title('Lösung mit integrate.solve_ivp (Runge-Kutta45 ')
plt.xlabel('s')
plt.ylabel('K(s)')

# Plot abspeichern
#plt.savefig('images/ivp1.png', dpi=150)
plt.show()
