# -*- coding: utf-8 -*-
"""
Berechnung von I_(30) ausgehend von I_(50)
"""
import numpy as np
import intrek as ir


def doit(n: int, start: int, istart: np.float64):
    """
    Durchführung des Experiments für die Rückwärts-Iteration

    Parameters
    ----------
    n : int
        Welches Integral soll berechnet werden?.
    start : int
        Mit welchem Index (start > n) möchten wir beginnen?.
    istart : np.float64
        Welchen Startwert verwenden wir?.
    """
    results = ir.backward(start, n, istart)
    print('Startindex ist', start)
    print('Verwendeter Startwert war', istart)
    print('Index, Untere Grenze, Berechnter Wert, Obere Grenze')
    for i in range(start - n + 1):
        lower, upper = ir.estimates(start-i)
        print(start-i, lower, results[i], upper)


def main():
    n = 30
    start = 50

    # Erster Startwert: 1.0
    istart = np.float64(1.0)
    print('\n')
    doit(n, start, istart)

    # Zweiter Startwert: 100000
    istart = np.float64(100000.0)
    print('\n')
    doit(n, start, istart)

    # Dritter Startwert: -100000
    istart = np.float64(-100000.0)
    print('\n')
    doit(n, start, istart)


if __name__ == "__main__":
    main()
