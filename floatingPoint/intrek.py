# -*- coding: utf-8 -*-
"""
Integralberechnungen.
"""
import numpy as np


# Funktionen
def forward(n):
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


def backward(start, n, istart):
    """
    Berechnung des Integrals I_n aus einem Startwert I_(start) mit start>n.

    Parameters
    ----------
    start : int
        Index des Startwerts.
    n : int
        Index des Integrals, das berechnet werden soll.
    istart : float
        Wert des Integrals für den index start.

    Returns
    -------
    values : ndarray mit shape (start-n,)
        Berechnete Werte der Integrale von I_(start) bis I_n.
        I_(start) steht im Index 0 des Felds, der letzte berechnete
        Wert steht im Index start-n.
    """
    values = np.zeros(shape=(start-n,), dtype=np.float64)
    iterationValue = np.float64(istart)
    values[0] = np.float64(istart)
    for counter in range(start, n, -1):
        iterationValue = (1.0-iterationValue)/float(counter)
        values[start - counter] = iterationValue
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
    n = 4
    print('Berechnung von I_', n, 'mit beiden Iterationen')
    lower, upper = estimates(n)
    print('Das Integral liegt zwischen', lower, 'und', upper, '.')
    results = forward(n)
    print('Ergebnis der Berechnung ausgehend von I_0 ist', results[n])

    start = 10
    istart = np.float64(1.0)
    print('\nVerwendeter Startwert war', istart)
    results = backward(start, n, istart)
    print('Ergebnis der Berechnung ausgehend von I_', start, ' ist',
          results[start - n - 1])


if __name__ == "__main__":
    main()
