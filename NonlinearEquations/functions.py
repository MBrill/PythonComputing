# -*- coding: utf-8 -*-
"""
Beispielfunktion und Ableitung für die Nullstellensuche mit Scipy
"""


def f(x):
    """
    Beispiel einer Funktion.

    Parameters
    ----------
    x : float
        Auswertungsstelle.

    Returns
    -------
    float
        Funktionswert.
    """
    return (x**3 - 1.0)


def fprime(x):
    """
    Ableitung der Beispielfunktion

    Parameters
    ----------
    x : float
        Auswertungsstelle.

    Returns
    -------
    float
        Wert der Ableitung.
    """
    return 3.0*x**2.0


def f_p_pp(x):
    """
    Auswertung der Funktion und der 1. Ableitung in einem Aufruf.

    Parameters
    ----------
    x : float
        Auswertungsstelle.

    Returns
    -------
    float
        Wert der Funktion, der ersten und der zweiten Ableitung.
    """
    return (x**3 - 1.0), 3.0*x**2


def f_p_pp_ppp(x):
    """
    Auswertung der Funktion und der 1. und 2. Ableitung in einem Aufruf.

    Parameters
    ----------
    x : float
        Auswertungsstelle.

    Returns
    -------
    float
        Wert der Funktion, der ersten und der zweiten Ableitung.
    """
    return (x**3 - 1.0), 3*x**2, 6.0*x


def main():
    x = 2.0
    print('Beispielfunktion für die numerische Nullstellensuche')
    print('Auswertungsstelle x = ', x)
    print('Funktionswert f(x) = ', f(x))
    print('Wert der Ableitung f\'(x) = ', fprime(x))
    print('auswertung von FUnktion, 1. und 2. Ableitung: ', f_p_pp_ppp(x))


if __name__ == "__main__":
    main()
