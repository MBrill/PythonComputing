# -*- coding: utf-8 -*-
"""
Example for cancelation errors.

The numbers are taken from Hanke-Bourgeois, p. 21
"""
import numpy as np


def compute(x: np.float64):
    eta1 = x/(x*x - 1.0)
    eta2 = 1.0/x
    eta3 = x*x*x
    eta4 = eta1 - eta2
    return eta3*eta4


def alt_compute(x: np.float64):
    x2 = x*x
    return x2/(x2-1.0)
    
# Test an den Stellen x=2, x=3 und x=4
print('Exakter Wert für x=2 ist 4/3 = ', 4/3)
print('Ergebnis der Berechnungsfunktion ist ', compute(2.0))
print('Exakter Wert für x=3 ist 9/8 = ', 9/8)
print('Ergebnis der Berechnungsfunktion ist ', compute(3.0))
print('Exakter Wert für x=4 ist 16/15 = ', 16/15)
print('Ergebnis der Berechnungsfunktion ist ', compute(4.0))

# Auswertung an der Stelle 1.2e7
x = np.float32(1.2e7)
print('Exakter Wert für x= ', x, ' ist 1 + 1.0e(-15) = ', 1.0+1.0e-15)
print('Ergebnis der Berechnungsfunktion ist ', compute(x))


# Auswertung mit der alternativen Funktion
print('Exakter Wert für x=2 ist 4/3 = ', 4/3)
print('Ergebnis der Berechnungsfunktion ist ', alt_compute(2.0))
print('Exakter Wert für x=3 ist 9/8 = ', 9/8)
print('Ergebnis der Berechnungsfunktion ist ', alt_compute(3.0))
print('Exakter Wert für x=4 ist 16/15 = ', 16/15)
print('Ergebnis der Berechnungsfunktion ist ', alt_compute(4.0))

# Auswertung an der Stelle 1.2e7
x = np.float32(1.2e7)
print('Exakter Wert für x= ', x, ' ist 1 + 1.0e(-15) = ', 1.0+1.0e-15)
print('Ergebnis der Berechnungsfunktion ist ', alt_compute(x))

