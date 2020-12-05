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
ones = samples == 1
twos = samples == 2
threes = samples == 3
fours = samples == 4
fives = samples == 5
sixs = samples == 6

# relative frequencies
oneF = samples[ones].size/rolls
print(oneF)
twoF = samples[twos].size/rolls
print(twoF)
threeF = samples[threes].size/rolls
print(threeF)
fourF = samples[fours].size/rolls
print(fourF)
fiveF = samples[fives].size/rolls
print(fiveF)
sixF = samples[sixs].size/rolls
print(sixF)

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
plt.plot(x, cumulative_counts, 'g-')
plt.title('Kumulierte relative Häufigkeiten für die Augenzahl 1')
plt.savefig('images/relFreq1.png', dpi=150)
plt.show()
