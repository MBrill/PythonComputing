# -*- coding: utf-8 -*-
"""
Eine Kugel im Raum für einen Ray-Tracer

Quellen: Suffern, Ray-Tracing from the Ground up, A.K. Peters
         Shirley, Morley: Realistic Ray Tracing, A.K. Peters
"""
import numpy as np
import shape
import ray


class Sphere(shape.Shape):
    """
    Repräsentation einer Kugel im 3D-Raum.
    """

    def __init__(self,
                 midpoint: np.ndarray,
                 radius: np.float64):
        """
        Konstruktor
        """
        self.m = midpoint
        self.r = radius

    def hit(self, r):
        """
        Berechnung eines Schnittpunkt mit einem Strahl.

        Nur der Fall, dass der Strahl die Kugel durchläuft, also nicht streift,
        wird als Schnitt zurückgegeben!

        Returns
        True: falls es einen Schnittpunkt gibt. Dieser liegt dann
              auf dem Parameter intersect.
        False: es gibt keinen Schnittpunkt, intersect enthält den Nullvektor
        """
        raise NotImplementedError()

    def onSphere(self, point: np.ndarray):
        """
        Liegt ein Punkt auf der Kugel?

        Returns
        -------
        True falls der Punkt auf der Kugel liegt,
        False sonst
        """
        diff = np.array(self.m - point)
        value = np.dot(diff, diff) - self.r**2
        if np.abs(value) <= np.finfo(float).eps:
            return True
        else:
            return False

    def print(self):
        """
        Ausgabe der Ebene auf der Konsole
        """
        print("Kugel")
        print("Mittelpunkt:", self.m)
        print("Radius", self.r)


def main():
    """
    Beispiel-Code für die Verwendung der Klassen Shape und Plane

    Returns
    -------
    None.

    """
    point = np.ones(shape=(3,))
    radius = 1.0
    sphere = Sphere(point, radius)

    sphere.print()

    x1 = np.array([1.0, 1.0, 0.0])
    x2 = np.array([2.0, 2.0, 3.0])

    if sphere.onSphere(x1):
        print("Der Punkt ", x1, " liegt auf der Kugel")
    else:
        print("Der Punkt ", x1, " liegt nicht auf der Kugel")

    if sphere.onSphere(x2):
        print("Der Punkt ", x2, " liegt auf der Kugel")
    else:
        print("Der Punkt ", x2, " liegt nicht auf der Kugel")

    rayPoint = np.array([1.0, 1.0, 0.0])
    direction = np.array([0.0, 0.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()

    hit, intersect = sphere.hit(r)
    if hit:
        print("Korrekter Schnittpunkt ist", np.array([1.0, 1.0, 0.0]))
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")

    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([0.0, 0.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()

    hit, intersect = sphere.hit(r)
    if hit:
        print("Korrekter Schnittpunkt ist", np.array([1.0, 1.0, 0.0]))
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")

    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([1.0, 0.0, 0.0])
    r = ray.Ray(rayPoint, direction)
    r.print()

    hit, intersect = sphere.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")

    # Beispiel für einen Strahl, der von der Kugel wegzeigt
    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([0.0, 0.0, -1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()

    hit, intersect = sphere.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")

    # Beispiel für einen Berührpunkt
    # Radius ist jetzt sqrt(2)
    point = np.ones(shape=(3,))
    radius = np.sqrt(2.0)
    sphere = Sphere(point, radius)

    rayPoint = np.array([0.0, 0.0, 0.0])
    direction = np.array([0.0, 0.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()

    hit, intersect = sphere.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")


if __name__ == "__main__":
    main()
