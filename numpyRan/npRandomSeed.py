# -*- coding: utf-8 -*-
"""
Generate random numbers using NumPy and a seed value
"""
import numpy as np

rng = np.random.default_rng(42)

x = rng.integers(1, 6, size=2, endpoint=True)
print('Zwei Zahlen aus {1, 2, 3, 4, 5, 6}: ', x)

x = rng.random(size=3, dtype=np.float64)
print('Drei gleichverteilte Zahlen in [0, 1): ', x)
