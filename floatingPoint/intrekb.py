# -*- coding: utf-8 -*-
"""
Berechnung von I_(30) ausgehend von I_(50)
"""
import numpy as np
import intrek as ir


def doit(n: int, start: int, istart: np.float64):
    results = ir.backward(start, n, istart)
    print('Startindex ist', start)
    print('Verwendeter Startwert war', istart)
    print('Index, Untere Grenze, Berechnter Wert, Obere Grenze')
    for i in range(start - n + 1):
        lower, upper = ir.estimates(start-i)
        print(start-i, lower, results[i], upper)


n = 30
start = 50

# Erster Startwert: 1.0
istart = np.float64(1.0)
print('\n')
doit(n, start, istart)

# Zweiter Startwert: 100000
istart = np.float64(100000.0)
print('\n')
doit(n, start, istart)

# Dritter Startwert: -100000
istart = np.float64(-100000.0)
print('\n')
doit(n, start, istart)
