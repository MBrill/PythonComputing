# -*- coding: utf-8 -*-
"""
Using scipy.linalg.solve for linear equations
"""
import numpy as np
from scipy import linalg

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = linalg.solve(a, b)
print('Computed solution:\n', x)

# Check, if the solution is correct
np.array([2.0, -2.0,  9.0])
check = np.dot(a, x) == b
if (check.all()):
    print('Everything worked!')
else:
    print('Something is wrong ')
    print('Here is the check:\n')
    print(check)
