# -*- coding: utf-8 -*-
"""
Basisklasse für geometrische Objekte in einem Ray-Tracer System
"""
import numpy as np
import ray


class Shape:
    """
    Basisklasse für geometrische Objekte.

    Kein Konstruktor, virtuelle Funktion hit für Schnittberechnungen.

    Wir müssten die virtuelle Funktion hit nicht implementieren.
    Das gewählte Vorgehen entspricht den Empfehlungen in der
    Python3-Dokumentation.
    """

    def hit(self, r):
        raise NotImplementedError()

    """
    Ausgabe auf der Konsole
    """

    def print(self):
        print("Basisklasse Shape")


def main():
    """
    Beispiel-Code für die Verwendung der Klassen Shape und Plane

    Returns
    -------
    None.

    """
    shape = Shape()
    shape.print()

    rayPoint = np.zeros(shape=(3,))
    direction = np.array([1.0, 1.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    shape.hit(r)


if __name__ == "__main__":
    main()
