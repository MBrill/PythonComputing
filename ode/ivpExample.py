# -*- coding: utf-8 -*-
"""
SciPy example for initial value problems
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def f(t, y):
    """
    Exponentieller Zerfall

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
    return -0.5*y


a = 0.0
b = 10.0
n = 50
eval = np.linspace(a, b, n)
# Array mit Startwerten
ivs = np.array([2, 4])
sol = integrate.solve_ivp(fun=f, t_span=[a, b], y0=ivs,
                          t_eval=eval)
if sol.success:
    y1 = sol.y[0, :]
    y2 = sol.y[1, :]

fig = plt.figure()
plt.grid(True)

plt.plot(a, ivs[0], 'go')
plt.plot(eval, y1, 'g-')
plt.plot(a, ivs[1], 'mo')
plt.plot(eval, y2, 'm-')
plt.title('Lösung mit integrate.solve_ivp (Runge-Kutta45')
plt.xlabel('t')
plt.ylabel('y(t)')

# Plot abspeichern
plt.savefig('images/ivp1.png', dpi=150)
plt.show()
