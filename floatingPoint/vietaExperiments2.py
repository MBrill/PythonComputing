# -*- coding: utf-8 -*-
"""
Lösungen für die quadratische Gleichung für den Auslöschungseffekt
"""
import numpy as np
import vieta

# Werte für p und q produzieren
# Dieses mal verwenden wir ein q, das p^2 immer näher kommt
n = 20
pvalue = 999.0
p = np.full(shape=(n, ), fill_value=pvalue, dtype=np.float64)
pp = np.full(shape=(n, ), fill_value=pvalue*pvalue, dtype=np.float64)
k = np.arange(1, n+1, 1)
qq = np.full(shape=(n,), fill_value=0.1, dtype=np.float64)
q = pp - np.power(qq, k)

print('Test der Funktionen numberOne und numberTwo')
print('Wir verwenden p=999.0 und')
print('die Werte q = 999^2 - 0.1, 999^2 - 0.01, ..., 999^2 -  10^(-20)!')

# Wir führen die Berechnung durch und speichern die Ergebnisse
# für eine übersichtliche Ausgabe
sol1 = vieta.numberOne(p, q)
sol2 = vieta.numberTwo(p, q)

for i in range(n):
    print('k =', i+1, '1:', sol1[i], '2:', sol2[i])

# Als Test setzen wir die Werte, die wir mit der alternativen
# Formel berechnet haben in das Polynom ein, mit fl.evaluate
print('Test mit den Ergebnissen aus Formel 2')
print('Wir setzen die Ergebnisse in das quadratische Polynom ein:')
print(vieta.evaluate(p, q, sol2))

print('Test mit den Ergebnissen aus Formel 1')
print('Wir setzen die Ergebnisse in das quadratische Polynom ein:')
print(vieta.evaluate(p, q, sol1))
