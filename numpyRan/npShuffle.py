# -*- coding: utf-8 -*-
"""
Shuffle the cards
"""
import numpy as np

rng = np.random.default_rng(42)

deck = np.arange(1, 33)
print('Die Spielkarten vor dem Mischen')
print(deck)
rng.shuffle(deck)
print('Die Spielkarten nach dem Mischen')
print(deck)
