# -*- coding: utf-8 -*-
"""
Solving the wire equation using NumPy and SciPy.

We could use our own tridiagonal LU solver,
or just solve from numpy.linalg.

Here we use the solve_banded from scipy. N
Note we do not use the symmetry of the matrix.
"""
import numpy as np
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

# our system and the parametersof the wire equation
# boundary condition
ya = -1.0
yb = 1.0
# constant force (don't forget the minus sign!)
f = -10.0
# length of our wire
length = 1.0
# discretization parameters
n = 50
h = length/n

# set the tridiagonal matrix of our system
diag = 2.0
offdiag = -1.0
aa = np.zeros((3, n))
aa[0, 1:] = offdiag
aa[1, :] = diag
aa[2, :-1] = offdiag
# right-hand side
b = np.zeros((n, 1))
b[:] = h*h*f
# boundary values
b[0] += ya
b[-1] += yb
# Call SciPy solver
x = solve_banded((1, 1), aa, b)

# Vis
# We add the boundary points using a and b for the y-values
# and Matplotlib.
wireX = np.linspace(0.0, length, n+2)
wireY = np.linspace(0.0, length, n+2)

wireY[0] = ya
wireY[1: -2] = x[:-1, 0]
wireY[n] = x[-1, 0]
wireY[n+1] = yb

fig = plt.figure(figsize=(16.0, 9.0))
plt.figure(dpi=600)
plt.grid(True)
plt.axis([0.0, length, np.floor(wireY.min()), max(ya, yb)+1.0])
plt.xticks([])
# plt.yticks([])
plt.plot(wireX, wireY, 'g-')
plt.title('Lösung der Kabelgleichung')

# plt.savefig('images/lambdaExample.png')
plt.show()
