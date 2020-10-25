# -*- coding: utf-8 -*-
"""
Berechnung von I_(30) ausgehend von I_(50)
"""
import numpy as np
import intrek as ir


def doit(n, start, istart):
    results = ir.backward(start, n, istart)
    print('Ausgehend von Startindex', start)
    print('Startwert', istart, '.')
    print('Ausgegeben werden immer:')
    print('Index, untere Grenze, berechnter Wert, obere Grenze')
    lower, upper = ir.estimates(start)
    print('i', start, lower, istart, upper)
    for i in range(start - n):
        lower, upper = ir.estimates(start-i-1)
        print('i', start-i-1, lower, results[i], upper)


n = 30
start = 50
istart = np.float64(1.0)
doit(n, start, istart)

# Nochmal die Berechnung, aber mit einem anderen Startwert
istart = np.float64(100000.0)
print('\n')
doit(n, start, istart)

# Nochmal die Berechnung, aber mit einem anderen Startwert
istart = np.float64(-100000.0)
print('\n')
doit(n, start, istart)
