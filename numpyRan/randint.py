# -*- coding: utf-8 -*-
"""
Generate random integers using randint
"""
import random

random.seed(42)

i = random.randint(0, 10)
print('Random number between 0 and 10: ', i)

j = random.randint(1, 6)
print('Random number between 1 and 6: ', j)

k = random.randrange(1, 6)
print('Random number between 1 and 5: ', k)

l = random.randrange(1, 7)
print('Random number between 1 and 6: ', l)