# -*- coding: utf-8 -*-
"""
Example for linear regression

Data are taken from dataset wassergehalt.csv
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.genfromtxt('wassergehalt.csv',
                     delimiter=';', skip_header=True)

r = stats.linregress(data)

print('Correct values')
print('Slope of line is 0.236')
print('Intercept of line is 2.665')
print(r.slope, r.intercept)

print('Computed parameters')
print('Coefficient of determination is ', r.rvalue)
print('p-value is ', r.pvalue)
print('least squares error is ', r.stderr)

fig = plt.figure(figsize=(16.0, 9.0))
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(data[:, 0], data[:, 1], 'oc', label='data points')
plt.plot(data[:, 0], r.slope*data[:, 0] + r.intercept, '-g',
         label='data points')
plt.legend()

plt.show()

fig.savefig('images/wassergehalt.png', dpi=300)
