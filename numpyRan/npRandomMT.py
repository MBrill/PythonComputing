# -*- coding: utf-8 -*-
"""
Generate random numbers using NumPy
"""
import numpy as np
from numpy.random import MT19937

mt = np.random.Generator(MT19937(42))
x = mt.random()
print('NumPy und dem Mersenne Twister: ', x)
y = mt.random()
print('NumPy und dem Mersenne Twister: ', y)

