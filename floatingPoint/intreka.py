# -*- coding: utf-8 -*-
"""
Berechnung von I_(30) ausgehend von I_0
"""
import intrek as ir

n = 30
values = ir.forward(n)
print('Index, untere Grenze, berechneter Wert, obere Grenze')
for i in range(n+1):
    lower, upper = ir.estimates(i)
    print('i', i, lower, values[i], upper)
