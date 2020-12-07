# -*- coding: utf-8 -*-
"""
Densities, Distributions and samples
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng()

# Bernoulli
p = 0.3
rv = stats.bernoulli(p)

mean, var = rv.stats(moments='mv')
sdev = rv.std()
med = rv.median()
print('Parameters of a Bernoulli variable with p = ', p)
print('Mean: ', mean, 'Variance: ', var)
print('Standard Deviation: ', sdev)
print('Median: ', med)

rng = np.random.default_rng()
x = rng.binomial(2, p, size=10)
print('10 samples of a Bernoulli distributed variable', x)

x = np.arange(0, 2)
plt.plot(x, rv.pmf(x), 'go', ms=8, label='Bernoulli pmf')
plt.vlines(x, 0, rv.pmf(x), colors='g', lw=5)
plt.title('Dichte einer Bernoulli-Variable mit p=0.3')
plt.savefig('images/bernoulli.png', dpi=150)
plt.show()

# Binomialverteilung
n = 5
p = 0.1
rv = stats.binom(n, p)
mean, var = rv.stats(moments='mv')
sdev = rv.std()
med = rv.median()
print('Parameters of a binomial distributed variable with n = ', n,
      'and p = ', p)
print('Mean: ', mean, 'Variance: ', var)
print('Standard Deviation: ', sdev)
print('Median: ', med)

x = rng.binomial(n, p, size=10)
print('10 samples of a binomial distributed variable', x)

x = np.arange(0, n+1)
plt.plot(x, rv.pmf(x), 'go', ms=8, label='Binomial pmf')
plt.vlines(x, 0, rv.pmf(x), colors='g', lw=5)
plt.title('Dichte einer binomail verteilten Variable mit n = 5 und p=0.1')
plt.savefig('images/binom.png', dpi=150)
plt.show()

# Hypergeometrische Verteilung
# M: total number of objects in urn
M = 30
# n: total number of objects of type 1
n = 7
# N: number of draws
N = 12

rv = stats.hypergeom(M, n, N)
mean, var = rv.stats(moments='mv')
sdev = rv.std()
med = rv.median()
print('Parameters of a hypergeometric distruted variable with M = ', M,
      'n = ', n, ' and N = ', N)
print('Mean: ', mean, 'Variance: ', var)
print('Standard Deviation: ', sdev)

# Samples
size = 10
x = rng.hypergeometric(N-n, n, N, size=size)
print('Samples of a hypergeometric distributed variable: ', x)
print('Results are the number of good parts drawn!')

x = np.arange(0, N+1)
plt.plot(x, rv.pmf(x), 'go', ms=8, label='Binomial pmf')
plt.vlines(x, 0, rv.pmf(x), colors='g', lw=5)
plt.title('Dichte einer hypergeometrisch verteilten Variable ((30,7,12)')
plt.savefig('images/hyper.png', dpi=150)
plt.show()

# Goodie: 6 aus 49
M = 49
n = 6
N = 6
prob = stats.hypergeom.pmf(6, M, n, N)
print('\n Probability of 6 correct guesses in Lotto', prob)
