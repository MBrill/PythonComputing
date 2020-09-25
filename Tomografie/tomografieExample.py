# -*- coding: utf-8 -*-
"""
Solving a small example for computer tomography using NumPy and SciPy.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Setup the matrix
a = np.array([[1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
             [0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
             [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
             [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0],
             [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0]])

# setup the right hand side
b = np.array([18.0, 14.0, 18.0, 17.0, 15.0, 12.0, 12.0, 13.0, 14.0])


# use numpy to solve the linear equation system
x = np.linalg.solve(a, b)

print("Die berechnete Lösung: ", x)

# convert the nine values to a 3x3 matrix for the heatmap
grid = np.split(x, 3)

# Vis
fig = plt.figure()
plt.figure(dpi=2400)
ax = plt.imshow(grid, cmap=cm.gray)

plt.title('Gewebedichten')
plt.xticks([])
plt.yticks([])
plt.colorbar()

plt.show()
