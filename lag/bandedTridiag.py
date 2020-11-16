# -*- coding: utf-8 -*-
"""
Banded matrices --- our tridiagonal example
"""
import numpy as np
from scipy import linalg

ab = np.array([[0,  -1,   -1, -1],
               [1,   2,    2,  2],
               [-1,  -1,  -1,  0]])
b = np.zeros(shape=(4, ), dtype=np.float32)
b[0] = 5.0
b[2] = 1.0
x = linalg.solve_banded((1, 1), ab, b)

print('Solution \n', x)
