# -*- coding: utf-8 -*-
"""
Example for cancelation errors.

The numbers are taken from Hanke-Bourgeois, p. 21
"""
import numpy as np


x = np.float32(1.2e7)
eta1 = np.float32(x/(x*x-1.0))
eta2 = np.float32(1.0/x)
eta3 = np.float32(x*x*x)
print(eta1, eta2, eta3)

eta4 = eta1 - eta2
print(eta4)

result = eta3*eta4
print('Naiv mit float32: ', result)

result = 1.0/(1.0-1.0/(x*x))
print('Alternativ mit float32: ', result)

x = np.float64(1.2e7)
eta1 = np.float64(x/(x*x-1.0))
eta2 = np.float64(1.0/x)
eta3 = np.float64(x*x*x)
print(eta1, eta2, eta3)

eta4 = eta1 - eta2
print(eta4)

result = eta3*eta4
print('Naiv mit float64: ', result)

result = 1.0/(1.0-1.0/(x*x))
print('Alternativ mit float64: ', result)
