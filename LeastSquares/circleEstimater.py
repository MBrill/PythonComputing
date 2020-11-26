# -*- coding: utf-8 -*-
"""
Fit a circle to a set of points.

Use non-linear least squares function in Scipy.
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def circle(theta, t):
    """
    Taken from Elias Hernandis,
    "Three Examples of nonlinear least-squares fitting
    in Python with SciPy"

    Parameters
    ----------
    theta : ndarray of float
        Parameters of circle
    t: float
       Parameter value for circle

    Returns
    -------
    Point on circle.
    """
    x = theta[0] + theta[2]*np.cos(2.0*np.pi*t)
    y = theta[1] + theta[2]*np.sin(2.0*np.pi*t)
    return np.array([x, y])


def resFun(theta, x, y):
    Ri = np.sqrt((x-theta[0])**2 + (y - theta[1])**2)
    return Ri - theta[2]


data = np.genfromtxt('kreis.csv',
                     delimiter=';', skip_header=True)


def fun(theta):
    return resFun(theta, data[:, 0], data[:, 1]).flatten()


x_0 = np.zeros(shape=(3,), dtype=np.float64)
res = optimize.least_squares(fun, x_0)

# res is of Type OptimizeResult
if res.success:
    print('Fitting points to a circle')
    print('Minimizer ended successful')
    print('The computed values (centerx, centery, radius)')
    print(res.x)
    print('Number of function calls to the objective function: ',
          res.nfev)
    print('Optimality condition (norm of gradient): ', res.optimality)
    print('Mean Least Squares error is', (res.fun**2).mean())


t = np.linspace(0.0, 1.0, num=256)
xc, yc = circle(res.x, t)

fig = plt.figure(figsize=(16.0, 16.0))
plt.title('Circle Estimation')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'ob', markersize=10, label='data points')
plt.plot(res.x[0], res.x[1], 'or', markersize=20)
plt.plot(xc, yc, '-g', label='circle')
plt.legend()

plt.show()

fig.savefig('images/circleEstimator.png', dpi=300)
