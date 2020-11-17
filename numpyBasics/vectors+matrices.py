# -*- coding: utf-8 -*-
"""
Reshape and ravel for numpy arrays.
"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
x = np.ravel(A, order='c')

B = np.reshape(x, newshape=(2, 2), order='C')
print(B)
B = np.reshape(x, newshape=(2, 2), order='F')
print(B)
