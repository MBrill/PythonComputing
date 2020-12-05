# -*- coding: utf-8 -*-
"""
Beispiele für die numerische Nullstellensuche mit SciPy - komplexe Gleichung.
"""
import numpy as np
from scipy import optimize


def f(z: np.complex):
    """
    Beispiel einer Funktion.

    Parameters
    ----------
    x : np.complex
        Auswertungsstelle.

    Returns
    -------
    float
        Funktionswert.
    """
    return (z**3 - np.complex(1.0, 0.0))


def fprime(z: np.complex):
    """
    Ableitung der Beispielfunktion.

    Parameters
    ----------
    x : float
        Auswertungsstelle.

    Returns
    -------
    float
        Wert der Ableitung.
    """
    return 3.0*z**2


z1 = np.complex(1.0, 0.0)
z2 = np.complex(-0.5, 0.5*np.sqrt(3.0))
z3 = np.complex(-0.5, -0.5*np.sqrt(3.0))


def decision(z: np.complex, epsilon=0.00001):
    """
    Entscheidung welche der drei Einheitswurzeln als
    Grenzwert berechnet wurden.

    Parameters
    ----------
    z : np.complex
        Berechnete Lösung.
    z : np.float64
        Tolerenz für die Entscheidung (Default ist 0.00001.

    Returns
    -------
    int
        Entscheidung (1 = z1, 2 = z2, 3 = z3, 0 keine Konvergenz).

    """
    dec = 0
    if (np.linalg.norm(z-z1) < epsilon):
        dec = 1
    if (np.linalg.norm(z-z2) < epsilon):
        dec = 2
    if (np.linalg.norm(z-z3) < epsilon):
        dec = 3
    return dec


print('Numerische Nullstellensuche mit dem Newton-Algorithmus')
print('Ausgaben')
print('Nullstelle, Anzahl der Iterationen, Anzahl der Funktionsaufrufe')
print('')

z_0 = np.complex(0.0, 1.0)
maxN = 100
epsilon = 0.001
sol = optimize.root_scalar(f,
                           fprime=fprime,
                           x0=z_0,
                           maxiter=maxN,
                           rtol=epsilon,
                           method='newton')
if sol.converged:
    print('Newton-Algorithmus in den komplexen Zahlen')
    print(sol.root)
    if decision(sol.root) == 1:
        print('Konvergenz gegen z1')
    if decision(sol.root) == 2:
        print('Konvergenz gegen z2')
    if decision(sol.root) == 3:
        print('Konvergenz gegen z3')
    if decision(sol.root) == 0:
        print('Keine Konvergenz')
else:
    print('Fehler im Newton-Verfahren')
