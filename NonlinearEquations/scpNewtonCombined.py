# -*- coding: utf-8 -*-
"""
Beispiele für die numerische Nullstellensuche mit SciPy
"""
from scipy import optimize
import functions as ft


print('Numerische Nullstellensuche mit dem Newton-Algorithmus')
print('Ausgaben')
print('Nullstelle, Anzahl der Iterationen, Anzahl der Funktionsaufrufe')
print('')

sol = optimize.root_scalar(ft.f_p_pp,
                           x0=0.2,
                           fprime=True,
                           method='newton')
if sol.converged:
    print('Newton mit einer Funktion')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Fehler im Newton-Verfahren')
