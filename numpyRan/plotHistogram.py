# -*- coding: utf-8 -*-
"""
Sample a normal distribution and plot the histogram
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
mu = 0.0
sigma = 0.1
s = rng.normal(mu, sigma, size=1000)

count, bins, ignored = plt.hist(s, bins=30, density=True, color='g')
plt.plot(bins,
         1/(np.sqrt(2.0*np.pi*sigma*sigma))
         * np.exp(-(bins-mu)**2/(2.0*sigma*sigma)),
         linewidth=2, color='r')
plt.title('Histogramm mit 1000 Samples einer Normalverteilung')

plt.savefig('images/histosamples.png', dpi=150)
plt.show()
