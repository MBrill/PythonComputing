# -*- coding: utf-8 -*-
"""
Example for quadratic regression using qr-decomposition

we compute a = qr, q^T b and solve r x = q^T b
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

data = np.genfromtxt('quadratic.csv',
                     delimiter=';', skip_header=False)

# 3 columns for the quadratic polynomial
a = np.ones(shape=(data.shape[0], 3))
a[:, 0] = data[:, 0]*data[:, 0]
a[:, 1] = data[:, 0]
y = np.zeros(shape=(data.shape[0],))
y = data[:, 1]

q, r = linalg.qr(a)
yprime = np.transpose(q) @ y

x = linalg.solve_triangular(r[:3, :], yprime[:3])
print('Results of least squares computation using QR')
print('The coefficients of the quadratic polynomial \n', x[0], x[1], x[2])

xvals = np.linspace(0.0, 2.0, num=50)
yvals = np.polyval(x, xvals)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Quadratic Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'ob', markersize=10, label='data points')
plt.plot(xvals, yvals, '-g', label='quadratic polynomial')
plt.legend()

plt.show()

fig.savefig('images/quadratic.png', dpi=300)
