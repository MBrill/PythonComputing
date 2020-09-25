# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe num4.
"""
import numpy as np

arr = np.array([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

index = arr > 6
new1 = arr[index]
print(new1)

new2 = arr[~index]
print(new2)
