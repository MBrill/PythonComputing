# -*- coding: utf-8 -*-
"""
Integralberechnungen.
"""
import numpy as np


# Funktionen
def forward(n: int):
    """
    Iterative Berechnung des Integrals I_n aus I_0.

    Parameters
    ----------
    n : int
        Index des Integrals, das berechnet werden soll.

    Returns
    -------
    values : numpy array mit shape (n+1,)
        Berechnete Werte der Integrale von I_0 bis I_n.
    """
    values = np.zeros(shape=(n+1,), dtype=np.float64)
    values[0] = np.float64(1.0 - 1.0/np.e)
    for counter in range(1, n+1):
        values[counter] = 1.0 - counter*values[counter-1]
    return values


def backward(start: int, n: int, istart: np.float64):
    """
    Berechnung des Integrals I_n aus einem Startwert I_(start)
    mit start>n.

    Parameters
    ----------
    start : int,  Index des Startwerts.
    n : int, Index des Integrals, das berechnet werden soll.
    istart : float, Wert des Integrals für den index start.

    Returns
    -------
    values : ndarray mit shape (start-n+1,)
        Startwert auf value[0],
        berechnete Werte der Integrale von I_(start-1) bis I_n.
        Der berechnete Wert steht im Index start-n, auf der letzten Stelle.
    """
    values = np.zeros(shape=(start-n+1,), dtype=np.float64)
    values[0] = istart
    for counter in range(start, n, -1):
        values[start-counter+1] = (1.0-values[start-counter])/float(counter)
    return values


def estimates(n):
    """
    Berechnen der Abschätzungen nach unten und oben für das Integral I_n.

    Parameter
    ---------
    n : int
        Index des Integrals.

    Returns
    -------
    Linke und rechte Grenze für I_n.
    """
    return 1.0/(3.0*(n+1)), 1.0/(n+1.0)


def main():
    """
    Berechnen eines Integrals mit einer Vorwärts- und eine Rückwärts-Tteration.

    Returns
    -------
    None.
    """

    print('Rekursive Berechnungen für ein Integral')
    print(' ')
    print('Berechnung mit der Funktion forward')
    n = 4
    lower, upper = estimates(n)
    results = forward(n)
    print(n, lower, results[n], upper)

    start = 10
    istart = np.float64(1.0)
    print('\nBerechnung mit der Funktion backward')
    print('Startindex ist', start)
    print('Verwendeter Startwert war', istart)
    results = backward(start, n, istart)
    print(n, lower, results[start - n], upper)


if __name__ == "__main__":
    main()
