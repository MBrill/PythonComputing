# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe num2.
"""
import numpy as np

x = np.array([0.0, 2.0])
t = np.array([1.0, 1.5])

f = lambda x, t: np.cos(np.sin(x)) + np.exp(1.0/t)

print(f(x,t))