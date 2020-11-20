# -*- coding: utf-8 -*-
"""
Example for linear regression using qr-decomposition

we compute a = qr, q^T b and solve r x = q^T b
"""
import numpy as np
from scipy import linalg

data = np.genfromtxt('wassergehalt.csv',
                     delimiter=';', skip_header=True)

a = np.ones(shape=(data.shape[0], 2))
a[:, 0] = data[:, 0]
b = np.zeros(shape=(data.shape[0],))
b = data[:, 1]

q, r = linalg.qr(a)
bprime = np.transpose(q) @ b

x = linalg.solve_triangular(r[:2, :], bprime[:2])
print('Results least squares computation using QR')
print('The slope of the line is ', x[0])
print('The intercept of the line is ', x[1])
