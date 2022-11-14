# -*- coding: utf-8 -*-
"""
Berechnung von I_(30) ausgehend von I_0
"""
import intrek as ir

n = 30
values = ir.forward(n)
print('Index, Untere Grenze, Berechneter Wert, Obere Grenze')

for i in range(n+1):
    lower, upper = ir.estimates(i)
    print(i, lower, values[i], upper)
