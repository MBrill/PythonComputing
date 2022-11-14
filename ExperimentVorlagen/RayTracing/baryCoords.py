# -*- coding: utf-8 -*-
"""
Berechnung von baryzentrischen Koordinaten von Punkten
mit unserer Implementierung der Gauß-Elimination in lgs33.
"""
import numpy as np
import lgs33


point1 = np.array([-1.0, 1.0, 1.0])
point2 = np.array([1.0, 1.0, 1.0])
point3 = np.array([0.0, 2.0, 1.0])

p = np.array([0.0, 4.0/3.0, 1.0])

A = np.zeros(shape=(3, 4), dtype=np.float64)
A[0:, 0] = point1
A[0:, 1] = point2
A[0:, 2] = point3
A[0:, 3] = p

ok, solution = lgs33.solve(A)
if ok:
    print('Berechnete Koordinaten des Punkts P: ', solution)
else:
    print('Fehler in der Berechnung der Koordinaten')

# ein weiteres Beispiel
point1 = np.array([-1.0, 0.0, 1.0])
point2 = np.array([1.0, 0.0, 1.0])
point3 = np.array([0.0, 2.0, 1.0])

p = np.array([1.0, 2.0, 1.0])

A[0:, 0] = point1
A[0:, 1] = point2
A[0:, 2] = point3
A[0:, 3] = p
print(A)

ok, solution = lgs33.solve(A)
if ok:
    print('Berechnete Koordinaten des Punkts P: ', solution)
else:
    print('Fehler in der Berechnung der Koordinaten')
