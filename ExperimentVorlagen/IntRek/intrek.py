# -*- coding: utf-8 -*-
"""
Implementierung von iterativen Berechnungen für ein Integral.
"""
import numpy as np


# Funktionen
def forward(n: int):
    """
    Iterative Berechnung des Integrals I_n augehend von I_0.

    Parameters
    ----------
    n : int
        Index des Integrals, das berechnet werden soll.

    Returns
    -------
    values : numpy array mit shape (n+1,)
        Berechnete Werte der Integrale von I_0 bis I_n.
    """
    raise NotImplementedError()


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
             Der berechnete Wert steht im Index start-n,
             auf der letzten Stelle.
    """
    raise NotImplementedError()


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
    raise NotImplementedError()


def main():
    """
    Berechnen eines Integrals mit einer Vorwärts- und eine Rückwärts-Tteration.

    Returns
    -------
    None.
    """

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
