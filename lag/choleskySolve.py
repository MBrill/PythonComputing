# -*- coding: utf-8 -*-
"""
Use Cholesky algorithm for a positive definite matrix
"""
import numpy as np
from scipy import linalg

# Example from Schwarz, p. 41
a = np.array([[5, 7, 3],
              [7, 11, 2],
              [3, 2, 6]
              ])
b = np.array([0, 0, 1])
# Solution from Schwarz
xexact = np.array([-19.0, 11.0, 6.0])

x = linalg.solve(a, b, assume_a='pos')
print('Solution \n')
print(x)

if np.allclose(a @ x - b, np.zeros((3,))):
    print('Everything worked')
