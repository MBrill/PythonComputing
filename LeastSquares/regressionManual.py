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
y = np.zeros(shape=(data.shape[0],))
y = data[:, 1]

q, r = linalg.qr(a)
yprime = np.transpose(q) @ y

x = linalg.solve_triangular(r[:2, :], yprime[:2])
print('Results of least squares computation using QR')
print('The slope of the line is ', x[0])
print('The intercept of the line is ', x[1])
