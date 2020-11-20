# -*- coding: utf-8 -*-
"""
Example for Eigenvalues and Eigenvectors
"""
import numpy as np
from scipy import linalg

a = np.array([[1.0, 2.0], [2.0, 1.0]])

print('Eigenvalues ')
evalues = linalg.eigvals(a)
print('Correct Eigenvalues are 3 and -1')
print('Computed Eigenvalues ', evalues)

evectors = linalg.eig(a)[1]
print('Orthonormalized Eigenvectors are\n', evectors)
print('Correct vectors are (1, -1), (1,1) (unnormalized)')

# Mit Hilfe von eigh
evalues, evectors = linalg.eigh(a)
print('Correct Eigenvalues are 3 and -1')
print('Computed Eigenvalues ', evalues)
print('Orthonormalized Eigenvectors are\n', evectors)
print('Correct vectors are (1, -1), (1,1) (unnormalized)')
