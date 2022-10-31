# -*- coding: utf-8 -*-
"""
Eine Ebene im Raum für einen Ray-Tracer
"""
import numpy as np
import shape
import ray


"""
Repräsentation einer Ebene im 3D-Raum.
"""


class Plane(shape.Shape):
    """
    Konstruktor
    """

    def __init__(self,
                 point: np.ndarray,
                 normal: np.ndarray):
        self.p = point
        self.n = normal

    """
    Berechnung eines Schnittpunkt mit einem Strahl

    Returns
    True: falls es einen Schnittpunkt gibt. Dieser liegt dann
          auf dem Parameter intersect.
    False: es gibt keinen Schnittpunkt, intersect enthält den Nullvektor
    """

    def hit(self, r):
        nom = np.dot(self.p - r.p, self.n)
        denom = np.dot(r.d, self.n)

        if denom != 0.0:
            t = nom/denom
            intersect = r.point(t)
            return True, intersect
        else:
            return False, np.zeros(shape=(3,))

    """
    Liegt ein Punkt in der Ebene?

    Returns
    -------
    TRUE falls der Punkt in der ebene liegt,
    FALSE sonst
    """

    def inPlane(self, point):
        value = np.dot(self.p - point, self.n)
        if np.abs(value) <= np.finfo(float).eps:
            return True
        else:
            return False
    """
    Ausgabe der Ebene auf der Konsole
    """

    def print(self):
        print("Ebene")
        print("Punkt:", self.p)
        print("Normalenvektor", self.n)


def main():
    """
    Beispiel-Code für die Verwendung der Klassen Shape und Plane

    Returns
    -------
    None.

    """
    point = np.ones(shape=(3,))
    normal = np.array([0.0, 0.0, 1.0])
    plane = Plane(point, normal)

    plane.print()

    x1 = np.array([2.0, 2.0, 1.0])
    x2 = np.array([2.0, 2.0, 3.0])

    if plane.inPlane(x1):
        print("Der Punkt ", x1, " liegt in der Ebene")
    else:
        print("Der Punkt ", x1, " liegt nicht in der Ebene")

    if plane.inPlane(x2):
        print("Der Punkt ", x2, " liegt in der Ebene")
    else:
        print("Der Punkt ", x2, " liegt nicht in der Ebene")

    rayPoint = np.zeros(shape=(3,))
    r = ray.Ray(rayPoint, normal)
    r.print()

    hit, intersect = plane.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")

    rayPoint = np.zeros(shape=(3,))
    d = np.array([1.0, 0.0, 0.0])
    r = ray.Ray(rayPoint, d)
    r.print()

    hit, intersect = plane.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")


if __name__ == "__main__":
    main()
