# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe num3.
"""
import numpy as np

v = np.array([2.0, 3.0, 1.0])
f = lambda v: v**3 + v * np.exp(v) + 1.0

print(f(v))
