# -*- coding: utf-8 -*-
"""
Fit a elliptic paraboloid to a set of points in space.

Use non-linear least squares function in Scipy.
"""
import numpy as np
from scipy import optimize


def h(theta, x, y):
    """
    Taken from Elias Hernandis,
    "Three Examples of nonlinear least-squares fitting
    in Python with SciPy"

    Parameters
    ----------
    theta : ndarray of float
            Parameters of elliptic paraboloid
    x: float
       x value of point where we evaluate the scalar field
    y: float
       y value of point where we evaluate the scalar field

    Returns
    -------
    Point on elliptic paraboloid.
    """
    return theta[2]*(x - theta[0])**2 + theta[3]*(y - theta[1])**2


# compute points on elliptic paraboloid and add some noise
xs = np.linspace(-1.0, 1.0, 20)
ys = np.linspace(-1.0, 1.0, 20)
gridx, gridy = np.meshgrid(xs, ys)
x0 = 0.1
y0 = -0.15
a = 1
b = 2
noise = 0.1
hs = h([x0, y0, a, b], gridx, gridy)
hs += noise*np.random.default_rng().random(hs.shape)

def fun(theta):
    return (h(theta, gridx, gridy) - hs).flatten()


theta_0 = np.zeros(shape=(4,), dtype=np.float64)
theta_0[2] = 1.0
theta_0[3] = 2.0

res = optimize.least_squares(fun, theta_0)

# res is of Type OptimizeResult
if res.success:
    print('Fitting points to an elliptic paraboloid')
    print('The exact solution is (0.1, -0.15, 1, 2)')
    print('Minimizer ended successful')
    print('The computed x-value for the local minium')
    print(res.x)
    print('The function value at this point')
    print(res.cost)
    print('Number of function calls to the objective function: ',
          res.nfev)
    print('Optimality condition (norm of gradient): ', res.optimality)
    print('Mean Least Squares error is', (res.fun**2).mean())
