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
a = 0.0
b = 0.0
# constant force (don't forget the minus sign!)
f = -0.5
# length of our wire
length = 1.0
# discretization parameters
n = 20
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
# Hier noch etwas machen: die rechte Seite hängt von n ab!
# sonst werden die Bilder für variables n falsch!
# für n=10 ist das Ergebnis korrekt1
b[:] = f

# Call SciPy solver
x = solve_banded((1, 1), aa, b)

# Vis
# We add the boundary points using a and b for the y-values
# and Matplotlib.
wireX = np.linspace(0.0, n+1, n+2)
wireY = np.zeros((n+2, 1))
wireY[1:n+1] = x[0:n]

fig = plt.figure(figsize=(16.0, 9.0))
plt.figure(dpi=600)
plt.grid(True)
plt.axis([0.0, np.ceil(wireX[n+1]), np.floor(x.min()), 0.5])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
plt.plot(wireX, wireY, 'g-')

plt.title('Kabelgleichung für a=b=0')

# plt.savefig('images/lambdaExample.png')
plt.show()
