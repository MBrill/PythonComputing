# -*- coding: utf-8 -*-
"""
Simulating a fair dice to show connections between frequency and probability
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

rolls = 60000
samples = rng.integers(1, 6, size=rolls, endpoint=True)

# count the frequencies
result = np.bincount(samples)
# relative frequencies
frequencies = result[1:]/rolls
print(frequencies)

# Cumulate the appearance of 1
# do not use this code, the random generator is just to good ...
cumulative_counts = np.zeros(shape=(rolls,))
count = 0
for i in np.arange(rolls):
    if samples[i] == 1:
        count = count + 1
    cumulative_counts[i] = count

cumulative_counts /= rolls

x = np.arange(0, rolls)
plt.ylim(0.0, 0.18)
plt.plot(x, cumulative_counts, 'g-')
plt.title('Kumulierte relative Häufigkeiten für die Augenzahl 1')
plt.savefig('images/relFreq1.png', dpi=150)
plt.show()
