# -*- coding: utf-8 -*-
"""
Fallstudie: Invertierung der Hilbert-Matrix
"""

import numpy as np


# We solve a linear equation system for the columns of Hinv
# Use the identiy matrix as right hand side
n = 7
rhs = np.identity(n)

computed_inv = np.linalg.solve(hilbert, rhs)
print('Result of the computation of the inverse using linalg.solve')
print(computed_inv)

print('Relative Error for computing the inverse of a Hilbert matrix')
print('n = ', n)
# relativer Fehler noch implementieren!
print(np.linalg.norm(hilbert_inv - computed_inv))
