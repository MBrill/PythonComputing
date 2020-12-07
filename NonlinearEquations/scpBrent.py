# -*- coding: utf-8 -*-
"""
Beispiele für die numerische Nullstellensuche mit SciPy
"""
from scipy import optimize
import functions as ft


print('Numerische Nullstellensuche mit dem Brent-Algorithmus')
print('Ausgaben')
print('Nullstelle, Anzahl der Iterationen, Anzahl der Funktionsaufrufe')
print('')


sol = optimize.root_scalar(ft.f,
                           bracket=[0, 3],
                           method='brentq')
if sol.converged:
    print('Brent-Algorithmus')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Fehler im Brent-Algorithmus')
