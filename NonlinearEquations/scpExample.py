# -*- coding: utf-8 -*-
"""
Examples for scalar root finding in SciPy
"""
from scipy import optimize


def f(x):
    return (x**3 - 1)


def fprime(x):
    return 3*x**2


def f_p_pp(x):
    return (x**3 - 1), 3*x**2, 6*x


print('Root finding for scalar functions')
print('Output: computed root, number of iterations, number of function calls')
print('')

# Bisection
sol = optimize.root_scalar(f, bracket=[0, 3],
                           method='bisect')
if sol.converged:
    print('Bisection')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Error using Bisection')
    
# Brent
sol = optimize.root_scalar(f, bracket=[0, 3],
                           method='brentq')
if sol.converged:
    print('Brent')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Error using Brent')

# Newton
sol = optimize.root_scalar(f, x0=0.2, fprime=fprime,
                           method='newton')
if sol.converged:
    print('Newton')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Error using Newton')

# combined
sol = optimize.root_scalar(f_p_pp, x0=0.2, fprime=True,
                           method='newton')
if sol.converged:
    print('Newton using a combined function')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Error using Newton')

# Use upto second derivative
sol = optimize.root_scalar(f_p_pp, x0=0.2, fprime=True, fprime2=True,
                           method='halley')
if sol.converged:
    print('Newton using second derivatives')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Error using Newton')
