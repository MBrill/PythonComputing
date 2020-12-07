# -*- coding: utf-8 -*-
"""
Beispiele für die numerische Nullstellensuche mit SciPy
"""
from scipy import optimize
import functions as ft


print('Numerische Nullstellensuche mit Bisektion')
print('Ausgaben')
print('Nullstelle, Anzahl der Iterationen, Anzahl der Funktionsaufrufe')
print('')

sol = optimize.root_scalar(ft.f,
                           bracket=[0, 3],
                           method='bisect')
if sol.converged:
    print('Bisektion')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Fehler bei der Bisektion')
