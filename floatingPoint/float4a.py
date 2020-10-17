# -*- coding: utf-8 -*-
"""
Verschiedene Alternativen für die Vieta'sche Formel.

Lösung der Aufgabe float4a.
"""
import numpy as np


def numberOne(p, q):
    """
    Berechnung der Lösung der quadratischen Gleichung x*+2+2px+q=0 mit
    kleinerem Absolutbetrag.
    
    Wir verwenden die Standard Formulierung x = -p + sqrt(p**2-q)

    Parameter
    ----------
    p : float
        Linear Term.
    q : float
        Constant Term.

    Returns
    -------
    float
        Lösung der quadratischen Gleichung mit kleinerem Absolutbetrag.

    """
    return -p + np.sqrt(p*p-q)


def numberTwo(p, q):
    """
    Berechnung der Lösung der quadratischen Gleichung x*+2+2px+q=0 mit
    kleinerem Absolutbetrag.
    
    Wir verwenden die alternative Formulierung x = -q/(p+ sqrt(p**2-q))

    Parameter
    ----------
    p : float
        Linearer Term.
    q : float
        Konstanter Term.

    Returns
    -------
    float
        Lösung der quadratischen Gleichung mit kleinerem Absolutbetrag.

    """    
    return (-q)/(p + np.sqrt(p*p-q))


def evaluate(p, q, x):
    """
    Auswertung des quadratischen Polynoms x*+2+2px+q an der Stelle x.

    Parameters
    ----------
    p : float
        Linearer Term des Polynoms.
    q : float
        Konstanter Term des Polynoms.
    x : float
        x-Wert, an der ausgewertet werden soll.

    Returns
    -------
    Ergebnis der Auswertung als float-Wert.
    """
    return x*x + 2.0*p*x + q


def main():
    """
    Implementing Vieta's formula

    Returns
    -------
    None.
    """
    p = np.array([3.0, 4.0, 5.0])
    q = np.array([8.0, 7.0, 9.0])
    correct = np.array([-2.0, -1.0, -1.0])
    x = numberOne(p, q)
    print('Test der Funktion numberOne')
    for i in range(3):
        print('Das korrekte Ergebnis für p = ',
              p[i], ' und q = ', q[i], ' ist ', correct[i])
        print('Lösung mit Hilfe der Funktion: x = ', x[i])

    x = numberTwo(p, q)
    print('\nTest der Funktion numberTwo')
    for i in range(3):
        print('Das korrekte Ergebnis für p = ',
              p[i], ' und q = ', q[i], ' ist ', correct[i])
        print('Lösung mit Hilfe der Funktion: x = ', x[i])


if __name__ == "__main__":
    main()
