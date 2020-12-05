# -*- coding: utf-8 -*-
"""
Continous Distributions in SciPy and NumPy

Densities, cdfs, functions and samples
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# Normal distribution
# Mean: mean, variance: var, standard deviation: std
rv = stats.norm()

mean, var = rv.stats(moments='mv')
sdev = rv.std()
med = rv.median()
print('Parameters of a standardised normal variable')
print('Mean: ', mean, 'Variance: ', var)
print('Standard deviation: ', sdev)

# Plot of probablity mass function (density)
# .ppf: Quantiles
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), num=100)
plt.plot(x, rv.pdf(x), 'g-', ms=8)
plt.title('Dichte der Standardnormalverteilung')
plt.savefig('images/standard.png', dpi=150)
plt.show()

plt.plot(x, rv.cdf(x), 'g-', ms=8)
plt.title('Verteilungsfunktion der Standardnormalverteilung')
plt.savefig('images/standardDist.png', dpi=150)
plt.show()

x = rng.standard_normal(size=2)
print('Samples from a standardised normal variable: ', x)
x = rng.standard_normal(size=(2, 3))
print('We can give a shape for size!')
print('Samples from a standardised normal variable: \n', x)

# Normal distribution
mu = 1.0
sigma = 0.5
rv = stats.norm(mu, sigma)
mean, var = rv.stats(moments='mv')
sdev = rv.std()
med = rv.median()
print('Parameters of a normal variable with mu = ', mu, ' and sigma = ', sigma)
print('Mean: ', mean, 'Variance: ', var)
print('Standard deviation: ', sdev)

# Plot of probablity mass function (density)
# .ppf: Quantiles
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), num=100)
plt.plot(x, rv.pdf(x), 'g-', ms=8)
plt.title('Dichte der Normalverteilung (mu=1.0, sigma=0.5)')
plt.savefig('images/standardScaled.png', dpi=150)
plt.show()

x = rng.normal(mu, sigma, size=2)
print('Samples from a normal distributed variable: ', x)
