# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe float1.
"""
import numpy as np


def computeE16(x: np.float16):
    return np.float16((1.0+1.0/x)**x)


def computeE32(x: np.float32):
    return np.float32((1.0+1.0/x)**x)


def computeE64(x: np.float64):
    return np.float64((1.0+1.0/x)**x)


values = np.arange(1, 7, 1)
xvalues = 10.0**values

# Mit np.float16
yvalues = computeE16(np.float16(xvalues))
abs = np.abs(yvalues - np.e)

print('Ergebnisse mit np.float16')
print('Die berechneten Näherungen')
print(yvalues)
print('Die absoluten Fehler')
print(abs)

# Mit np.float32
values = np.arange(1, 17, 1)
xvalues = 10.0**values
yvalues = computeE32(np.float32(xvalues))
abs = np.abs(yvalues - np.e)

print('\nErgebnisse mit np.float32')
print('Die berechneten Näherungen')
print(yvalues)
print('Die absoluten Fehler')
print(abs)

# Mit np.float64
values = np.arange(1, 17, 1)
xvalues = 10.0**values
yvalues = computeE64(np.float64(xvalues))
abs = np.abs(yvalues - np.e)

print('\nErgebnisse mit np.float64')
print('Die berechneten Näherungen')
print(yvalues)
print('Die absoluten Fehler')
print(abs)
