# -*- coding: utf-8 -*-
"""
Einfache Implementierung des Euler-Verfahrens 
für eindimensionale gewöhnliche Differentialgleichungen.
"""
import numpy as np


def euler1D(f, t, y0):
    """
    Einfaches Euler-Verfahren für eine
    eindimensionale gewöhnlichte Differentialgleichung


    Parameters
    ----------
    t : float array
        Variablen, an denen wir die Funktionswerte berechnen..
    y0 : float
        Funktionswert an der Stelle t[0].

    Returns
    -------
    Array y mit den berechnen Funktionswerten.

    """
    n = t.size - 1
    h = (t[-1]-t[0])/(n-1)
    y = np.zeros(shape=(n+1,))

    y[0] = y0
    for i in np.arange(n):
        y[i+1] = y[i] + h*f(t[i], y[i])

    return y


# Beispielfunktion
def f(t, y):
    """
    Funktion in der Differentialgleichung

    Parameters
    ----------
    t : float
        Variable
    y : float
        Funktionswerte der gesuchten Lösung

    Returns
    -------
    float.
    """
    return (t + y)


def main():
    n = 9
    a = 0.0
    b = 2.0
    t = np.linspace(a, b, num=n+1)
    print(n)
    print(t.size)

    y0 = 1.0
    y = euler1D(f, t, y0)
    print(y)


if __name__ == "__main__":
    main()
