# -*- coding: utf-8 -*-
"""
Samples from distributions
"""
import numpy as np

rng = np.random.default_rng()

# Standardnormalverteilung
x = rng.standard_normal(size=2)
print('Standardnormalverteilung: ', x)
x = rng.standard_normal(size=(2, 3))
print('Standardnormalverteilung: \n', x)

# Normalverteilung
mu = 1.0
sigma = 0.5
x = rng.normal(mu, sigma, size=2)
print('Normalverteilung (mu=1, s=0.5) ', x)

# Binomialverteilung
n = 2
p = 0.1
x = rng.binomial(n, p, size=10)
print('Binomialverteilung mit n=2 und p=0.5 ', x)

# Hypergeometrische Verteilung
ngood = 10
nbad = 10
nsample = 6
size = 6
x = rng.hypergeometric(ngood, nbad, nsample, size)
print('Sample mit einer hypergeometrischen Verteilung: ', x)

# Geometrische Verteilung
x = rng.geometric(0.4, 5)
print('Sample mit einer geometrischen Verteilung: ', x)