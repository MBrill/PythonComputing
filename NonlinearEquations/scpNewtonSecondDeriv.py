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

# Funktion, 1. und 2. Ableitung verwenden
sol = optimize.root_scalar(ft.f_p_pp_ppp,
                           x0=0.2,
                           fprime=True,
                           fprime2=True,
                           method='halley')
if sol.converged:
    print('Newton-Algorithmus mit zweiter Ableitung')
    print(sol.root, sol.iterations, sol.function_calls)
else:
    print('Fehler im Newton-Verfahren')
