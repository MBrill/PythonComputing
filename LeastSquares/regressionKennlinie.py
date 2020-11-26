# -*- coding: utf-8 -*-
"""
Example for a linear regression using qr-decomposition

we compute a = qr, q^T b and solve r x = q^T b
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def f1(x):
    """
    First part of the function

    Parameters
    ----------
    x : float
        x-value.

    Returns
    -------
    function value.
    """
    return x/(1.0+x)


def f2(x):
    """
    Second part of the function

    Parameters
    ----------
    x : float
        x-value.

    Returns
    -------
    function value.
    """
    return 1.0-np.exp(-x)


data = np.genfromtxt('kennlinie.csv',
                     delimiter=';', skip_header=False)

# 3 columns for the quadratic polynomial
a = np.ones(shape=(data.shape[0], 2))
a[:, 0] = f1(data[:, 0])
a[:, 1] = f2(data[:, 0])

y = np.zeros(shape=(data.shape[0],))
y = data[:, 1]

q, r = linalg.qr(a)
yprime = np.transpose(q) @ y

x = linalg.solve_triangular(r[:2, :], yprime[:2])
print('Results of least squares computation using QR')
print('The coefficients of the functions \n', x[0], x[1])

xvals = np.linspace(0.0, 3.0, num=50)
yvals = x[0]*f1(xvals) + x[1]*f2(xvals)


fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'ob', markersize=10, label='data points')
plt.plot(xvals, yvals, '-g', label='fitting function')
plt.legend()

plt.show()

fig.savefig('images/kennlinie.png', dpi=300)