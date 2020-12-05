# -*- coding: utf-8 -*-
"""
Example for quadratic regression using numpy.polyfit
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('quadratic.csv',
                     delimiter=';', skip_header=False)

p = np.polyfit(data[:, 0], data[:, 1], deg=2)

print('Results least squares computation using np.polyfit')
print('The coefficients of the quadratic polynomial: \n',
      p[0], p[1], p[2])

xvals = np.linspace(0.0, 2.0, num=50)
yvals = np.polyval(p, xvals)


fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Quadratic Regression using numpy.polyfit')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'ob', markersize=10, label='data points')
plt.plot(xvals, yvals, '-g', label='quadratic polynomial')
plt.legend()

plt.show()

fig.savefig('images/quadraticScp.png', dpi=300)
