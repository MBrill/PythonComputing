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


a = 0.0
b = 2.0
n = 9
h = (b-a)/(n-1)

t = np.linspace(a, b, num=n+1)
y = np.zeros(shape=(n+1,))

y[0] = 1.0
for i in np.arange(n):
    y[i+1] = y[i] + h*f(t[i], y[i])

print(y)

fig = plt.figure()
plt.grid(True)
plt.plot(t, y, 'g-', label='h=0.25')

n = 21
h = (b-a)/(n-1)
t = np.linspace(a, b, num=n+1)
y = np.zeros(shape=(n+1,))

y[0] = 1.0
for i in np.arange(n):
    y[i+1] = y[i] + h*f(t[i], y[i])

plt.plot(t, y, 'm-', label='h=0.1')

plt.title('Euler-Verfahren')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()

# Plot abspeichern
# plt.savefig('images/eulerdiff.png', dpi=120)
plt.show()
