# -*- coding: utf-8 -*-
"""
Implementieren Sie die Funktionen numberOne und numberTwo
für die Lösung einer quadratischen Gleichung.

Implementieren Sie zusätzlich die Funktion evaluate für das
Auswerte eines quadratischen Polynoms an einer gegebenen
x-Stelle.
"""
import numpy as np


def numberOne(p, q):
    """
    Berechnung der Lösung der quadratischen Gleichung x**2+2px+q=0 mit
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
    raise NotImplementedError()


def numberTwo(p, q):
    """
    Berechnung der Lösung der quadratischen Gleichung x**2+2px+q=0 mit
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
    raise NotImplementedError()


def evaluate(p, q, x):
    """
    Auswertung des quadratischen Polynoms x**2+2px+q an der Stelle x.

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
    raise NotImplementedError()


def main():
    """
    Die Vieta'sche Formel in verschiedenen Variationen

    Returns
    -------
    None.
    """

    # Drei Werte für p und q
    p = np.array([3.0, 4.0, 5.0])
    q = np.array([8.0, 7.0, 9.0])
    # Die exakte Lösung der drei Gleichungen
    correct = np.array([-2.0, -1.0, -1.0])
    # Lösungen berechnen mit Variante 1
    x = numberOne(p, q)
    print('Test der Funktion numberOne')
    for i in range(3):
        print('Das korrekte Ergebnis für p = ',
              p[i], ' und q = ', q[i], ' ist ', correct[i])
        print('Lösung mit Hilfe der Funktion: x = ', x[i])

    # Lösungen berechnen mit Variante 2
    x = numberTwo(p, q)
    print('\nTest der Funktion numberTwo')
    for i in range(3):
        print('Das korrekte Ergebnis für p = ',
              p[i], ' und q = ', q[i], ' ist ', correct[i])
        print('Lösung mit Hilfe der Funktion: x = ', x[i])


if __name__ == "__main__":
    main()
