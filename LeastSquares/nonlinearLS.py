# -*- coding: utf-8 -*-
"""
Beispiele für ein nicht-lineares Ausgleichsproblem mit SciPy

Wir verwenden die Rosenbrock-Banane als Zielfunktion.
Dabei müssen wir sie als Summe von Fehlerquadraten formulieren.
"""
import numpy as np
from scipy import optimize


def fun_rosenbrock(x):
    """
    Rosenbrock-Funktion als Summe von Fehlerquadraten

    Parameters
    ----------
    x : 2D Vektor
        Punkt, an die Funktion ausgewertet wird..

    Returns
    -------
    np.float
        Vektor der Fehlerquadrate.
    """
    return np.array([10.0 * (x[1] - x[0]**2), (1.0 - x[0])])


print('Nicht-lineare Ausgleichsrechnung')
print('Ausgaben')
print('')

# Code wir im Hilfetext von scipy
# Startwert
x0 = np.array([2.0, 2.0])
result = optimize.least_squares(fun_rosenbrock, x0)

if result.success:
    print('Konvergenz!')
    print('Das berechnete Minimum: ', result.x)
    print('Wert der Zielfunktion an diesem Punkt: ', result.cost)
else:
    print('Fehler im Verfahren')
