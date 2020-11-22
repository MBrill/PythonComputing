# -*- coding: utf-8 -*-
"""
Fit a ellipse or circle to a set of points.

Use non-linear least squares function in Scipy.
"""
import numpy as np
from scipy import optimize


def s(theta, t):
    """
    Taken from Elias Hernandis,
    "Three Examples of nonlinear least-squares fitting
    in Python with SciPy"

    Parameters
    ----------
    theta : ndarray of float
        Parameters of ellipse
    t: parameter value for ellipse

    Returns
    -------
    Point on ellipse.
    """
    x = theta[0] + theta[2]*np.cos(t)
    y = theta[1] + theta[2]*np.sin(t)
    return np.array([x, y])


# compute points on ellipse and add some noise
ts = np.linspace(0, 2.0*np.pi)
cx = 1.5
cy = 1.3
r = 0.75
noise = 0.05
ss = s([cx, cy, r], ts)
ss[0] += noise*np.random.rand(ts.shape[0])
ss[1] += noise*np.random.rand(ts.shape[0])


def fun(theta):
    return (s(theta, ts) - ss).flatten()


theta_0 = np.zeros(shape=(3,), dtype=np.float64)
res = optimize.least_squares(fun, theta_0)

# res is of Type OptimizeResult
if res.success:
    print('Fitting points to an ellipse')
    print('The exact solution is (1.5, 1.3, 0.75)')
    print('Minimizer ended successful')
    print('The computed x-value for the local minium')
    print(res.x)
    print('The function value at this point')
    print(res.cost)
    print('Number of function calls to the objective function: ',
          res.nfev)
    print('Optimality condition (norm of gradient): ', res.optimality)
    print('Mean Least Squares error is', (res.fun**2).mean())
