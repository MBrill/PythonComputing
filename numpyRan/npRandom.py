# -*- coding: utf-8 -*-
"""
Generate random numbers using NumPy
"""
import numpy as np

rng = np.random.default_rng()

x = rng.random()
print('Meine erste Zufallszahl mit NumPy: ', x)
y = rng.random()
print('Meine zweite Zufallszahl mit NumPy: ', y)
