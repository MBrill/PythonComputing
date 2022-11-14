# -*- coding: utf-8 -*-
"""
 und Eine Implementierung des Gauß-Algorithmus
und der Rückwärtssubstitution für das Ray-Tracing von Dreiecken.
"""
import numpy as np

# Genauigkeit für die Überprüfung auf zu kleine Werte bei Divisionen
epsilon33 = np.float64(1.0e-10)


def backSubstitution(A):
    """
    Rückwärtssubstitution für eine 3x3 obere Dreiecksmatrix.

    Diese Funktion wird typischer Weise aufgerufen nachdem wir
    eine Elimination durchgeführt haben.

    Es wird erwartet, dass alle drei Diagonalelemente ungleich Null
    sind. Dies wird zu Beginn der Funktion überprüft. Ist die Voraussetzung
    verletzt wird eine Exception erzeugt.

    Es wid nicht überprüft, ob es sich
    um einen obere Dreiecksmatrix handelt, es werden nur die Elemente auf
    der Diagonale und oberhalb verwendet. Es wird nicht überprüft ob die
    übergebene Matrix eine 3x4-Matrix ist.

    Die Implementierung ist so angelegt, dass wir sie einfach
    auf den nx(n+1)-Fall übertage können.

    Parameter
    ----------
    A : ndarray mit shape (3,4)
        Erweiterte Koeffizientenmatrix mit der rechten Seite als letzte Spalte.

    Returns
    -------
    Berechnete Lösung des 3x3 Systems.
    """
    if np.abs(A[0][0]*A[1][1]*A[2][2]) < epsilon33:
        raise ZeroDivisionError

    x = np.zeros(3, dtype=np.float64)
    x[2] = A[2, 3]/A[2, 2]
    x[1] = (A[1, 3] - A[1, 2]*x[2])/A[1, 1]
    x[0] = (A[0, 3] - A[0, 1]*x[1] - A[0, 2]*x[2])/A[0, 0]

    return x


def gauss(A):
    """
    Gauss-Elimination für die erweiterte Koeffizientenmatrix
    eines 3x3 linearen Gleichungssystems. Das Verfahren wir
    'in place' implementiert. Damit bezeichnet man den Fall,
    dass wir nicht mit einer Kopie der übergebenen Matrix arbeiten.

    Ist im Verlauf des Verfahrens ein Diagonalelement zu klein
    wird eine entsprechende Exception erzeugt.

    Nach der Elimination wird die Rückwärtssubstitution
    mit Hilfe der Funktion backsubstitution ausgeführt.

    Es wird nicht überprüft ob die Dimension der übergebenen Matrix
    3x4 ist!

    Parameter
    ----------
    A : ndarray mit shape (3, 4)
        Erweiterte Koeffizientenmatrix

    Returns
    -------
    Lösung des linearen Gleichungssystems
    """
    # Schritt 1
    if np.abs(A[0, 0]) <= epsilon33:
        raise ZeroDivisionError
    A[1, 1:] = A[1, 1:] - (A[1, 0]/A[0, 0]) * A[0, 1:]
    A[2, 1:] = A[2, 1:] - (A[2, 0]/A[0, 0]) * A[0, 1:]
    # Schritt 2
    if np.abs(A[1][1]) <= epsilon33:
        raise ZeroDivisionError
    A[2, 2:] = A[2, 2:] - (A[2, 1]/A[1, 1]) * A[1, 2:]


def solve(A):
    """
    Zusammenfassung der Elimination und der Rückwärtssubstitution
    in einer Funktion zum einfacheren Anwenden der Implementierung.

    Wir überprüfen die Lösbarkeit des Systems nach der Elimination
    und geben True plus eine Lösung zurück, falls eine eindeutige Lösung
    gibt. Gibt es keine Lösungen wird False zurückgegeben, und
    ein Lösungesvektor mit NaN. Gibt es unendlich viele Lösungen wird ebenfalls
    False zurückgegeben und der Nullvektor.


    Parameter
    ----------
    A : ndarray mit shape (3, 4)
        Erweiterte Koeffizientenmatrix

    Returns
    -------
    Lösung des linearen Gleichungssystems
    """
    gauss(A)
    # Falls wir noch keine Exception erhalten haben,
    # sind die beiden ersten Pivot-Elemente ok.
    # Jetzt überprüfen wir noch, ob es eine eindeutige Lösung gibt.
    if np.abs(A[2, 2]) < epsilon33:
        if np.abs(A[2, 3]) < epsilon33:
            return False, np.zeros(shape=(3, ))
        else:
            return False, np.array([np.NAN, np.NAN, np.NAN])
    # Eindeutige Lösung
    return True, backSubstitution(A)


def main():
    """
    Aufruf der Elimination und der Rückwärtssubstitution.

    Returns
    -------
    None.
    """
    # Beispiel für eine obere Dreiecksmatrix aus der Vorlesung
    # solution:
    # x = [-1/2, 1, 1]
    a = np.array([[2.0, 3.0, -1.0, 1.0],
                  [0.0, 4.0, -3.0, 1.0],
                  [0.0, 0.0,  1.0, 1.0]])

    print('Die verwendete erweiterte obere Dreiecksmatrix')
    print(a)
    print('Die korrekte Lösung ist')
    print(np.array([-0.5, 1.0, 1-0]))
    x = backSubstitution(a)
    print('Die berechnete Lösung ist')
    print(x)

    print('Gauß-Elimination')
    # Beispiel für eine 34atrix aus der Vorlesung
    # solution:
    # x = [16, 11, 6]
    a = np.array([[1.0, -1.0, 0.0,  5.0],
                  [-1.0, 2.0, -1.0, 0.0],
                  [0.0, -1.0,  2.0, 1.0]])

    # Korrektes Ergebnis der Elimination
    ac = np.array([[1.0, -1.0, 0.0,  5.0],
                   [0.0, 1.0, -1.0, 5.0],
                   [0.0, -0.0,  1.0, 6.0]])

    print('Das korrekte Ergebnis der Elimination:')
    print(ac)
    print('Achtung: die eliminierte Matrix wird unterhalb der Diagonale nicht verändert!')
    gauss(a)
    print('Das Ergebnis der Elimination:')
    print(a)

    print('Rückwärtssubstitution')

    x = backSubstitution(a)

    xc = np.array([16.0, 11.0, 6.0])
    print('Korrekte Lösung:')
    print(xc)

    print('Berechnete Lösung:')
    print(x)

    print('Gauß-Elimination mit der Funktion solve')
    # Beispiel für eine 34atrix aus der Vorlesung
    # solution:
    # x = [16, 11, 6]
    # Wir müssen die Matrix neu besetzen
    a = np.array([[1.0, -1.0, 0.0,  5.0],
                  [-1.0, 2.0, -1.0, 0.0],
                  [0.0, -1.0,  2.0, 1.0]])

    ok, x = solve(a)
    if ok:
        print('Es gibt eine eindeutige Lösung!')
        print('Berechnete Lösung mit der Funktion solve:')
        print(x)
    else:
        print('Keine Lösung oder unendlich viele Lösungen')


if __name__ == "__main__":
    main()
