# -*- coding: utf-8 -*-
"""
We throw two dices and sum the results
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

rolls = 100000000
samples = rng.integers(1, 6, size=(rolls, 2), endpoint=True)
result = samples[:, 0] + samples[:, 1]

number_of_results = 11
frequencies = np.zeros(shape=(number_of_results,), dtype=np.float32)
frequencies = np.bincount(result)[2:]/rolls

correct = np.array([1.0/36.0, 1.0/18.0, 1.0/12.0, 1.0/9.0,
                    5.0/36.0, 1.0/6.0, 5.0/36.0, 1.0/9.0,
                    1.0/12.0, 1.0/18.0, 1.0/36.0])

diff = np.abs(correct - frequencies)
print('Maximale Abweichung ist ', np.max(diff))

plt.xticks(np.arange(2, 13), ('2', '3', '4', '5', '6',
                              '7', '8', '9', '10', '11', '12'))
plt.bar(np.arange(2, 13), frequencies, color='g')
plt.title('Relative Häufigkeiten für die Summe von zwei Würfeln')

dpi = 150
plt.savefig('images/sumOfDice.png', dpi=dpi)
plt.show()

plt.xticks(np.arange(2, 13), ('2', '3', '4', '5', '6',
                              '7', '8', '9', '10', '11', '12'))
plt.bar(np.arange(2, 13), correct, color='y')
plt.title('Die Wahrscheinlichkeiten für die Summe von zwei Würfeln')

dpi = 150
plt.savefig('images/sumOfDiceProb.png', dpi=dpi)
