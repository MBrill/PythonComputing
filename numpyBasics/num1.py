# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe num1.
"""
import numpy as np

h = lambda x: (1.0/np.sqrt(2.0*np.pi)) * np.exp(-0.5*x*x)

xlist = np.linspace(-4.0, 4.0, 41, dtype=np.float64)
hlist = h(xlist)

print(xlist.shape)
print(xlist)
print(hlist)
