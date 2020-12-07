# -*- coding: utf-8 -*-
"""
Werte für die quadratische Iteration als Vorbereitung der Mandelbrot-Menge.
"""

import numpy as np


def quadraticPoly(z: np.complex, c: np.complex):
    """
    Berechnung des quadratischen Polynoms für die Mandelbrot-Menge

    Parameters
    ----------
    z : np.complex
        Argument des Polynoms.
    c : np.complex
        Wert für c.

    Returns
    -------
    Funktionswert (np.complex).
    """
    return z*z + c


def iterate(c: np.complex, n=5):
    """
    Iteration für die Motivation der Mandelbrot-Menge

    Parameters
    ----------
    c : np.complex
        Wert für die Konstante im quadratischen Polynom.
    n : np.int
        Anzahl der Werte, die berechnet werden sollen.

    Returns
    -------
    Werte der Iteration als Numpy-Array von komplexen Zahlen.
    """
    z = np.zeros(shape=(n,), dtype=np.complex)
    for i in np.arange(1, n):
        z[i] = quadraticPoly(z[i-1], c)
    return z


def iterate_with_barrier(c: np.complex, n=10, barrier=2.0):
    """
    Iteration für die Motivation der Mandelbrot-Menge.

    Diese Funktion gibt nicht die Folgeglieder aus, sondern
    entscheidet mit Hilfe einer Konstante, ob die Zahl c
    in der Mandelbrot-Menge liegt oder nicht.

    Parameters
    ----------
    c : np.complex
        Wert für die Konstante im quadratischen Polynom.
    n : np.int
        Anzahl der Werte, die berechnet werden sollen.
    barrier : np.float64
        Konstante, mit der entschieden wird ob Divergenz vorliegt.
        Ohne diese Konstante erreichen wird relativ schnell NaN
        im Fall der Divergenz der Beträge!

    Returns
    -------
    True, falls c in der mandelbrot-menge liegt
    """
    z = np.zeros(shape=(n,), dtype=np.complex)
    for i in np.arange(1, n):
        z[i] = quadraticPoly(z[i-1], c)
        if np.abs(z[i]) > barrier:
            return False

    return True


def main():
    n = 5
    c = np.array([np.complex(0, 0),
                  np.complex(1, 0),
                  np.complex(0, 1),
                  np.complex(1, 1)])

    z = np.zeros(shape=(c.size, n), dtype=np.complex)
    for i in np.arange(c.size):
        z[i] = iterate(c[i])
    print(z)


if __name__ == "__main__":
    main()
   