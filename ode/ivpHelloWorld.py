# -*- coding: utf-8 -*-
"""
SciPy Beispiel für ein Anfangswertproblem
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def F(t, y):
    """
    Exponentieller Zerfall

    Parameters
    ----------
    t : float
        Unabhängige Variable
    y : float
        Funktionswerte der gesuchten Lösung.

    Returns
    -------
    float.
    """
    return -0.5*y


t0 = 0.0
t1 = 10.0
n = 50
eval = np.linspace(t0, t1, n)

# Array mit Startwert
start = np.array([2])
sol = integrate.solve_ivp(fun=F,
                          t_span=[t0, t1],
                          y0=start,
                          t_eval=eval)
if sol.success:
    y = sol.y[0, :]

fig = plt.figure()
plt.grid(True)

plt.plot(t0, start[0], 'go')
plt.plot(eval, y, 'g-')
plt.title('Lösung des exponentiellen Zerfalls mit integrate.solve_ivp')
plt.xlabel('t')
plt.ylabel('y(t)')

# Plot abspeichern
plt.savefig('images/ivpHello.png', dpi=150)
plt.show()
