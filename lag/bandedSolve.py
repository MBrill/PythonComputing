# -*- coding: utf-8 -*-
"""
Banded matrices --- the Scipy example
"""
import numpy as np
from scipy import linalg

ab = np.array([[0,  0, -1, -1, -1],
               [0,  2,  2,  2,  2],
               [5,  4,  3,  2,  1],
               [1,  1,  1,  1,  0]])
b = np.array([0, 1, 2, 2, 3])
x = linalg.solve_banded((1, 2), ab, b)

print('Solution \n', x)
