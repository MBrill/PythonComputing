# -*- coding: utf-8 -*-
"""
Eine Kugel im Raum für einen Ray-Tracer

Quellen: Suffern, Ray-Tracing from the Ground up, A.K. Peters
         Shirley, Morley: Realistic Ray Tracing, A.K. Peters
"""
import numpy as np
import shape
import ray


"""
Repräsentation einer Kugel im 3D-Raum.
"""


class Sphere(shape.Shape):
    """
    Konstruktor
    """

    def __init__(self,
                 midpoint: np.ndarray,
                 radius: np.float64):
        self.m = midpoint
        self.r = radius

    """
    Berechnung eines Schnittpunkt mit einem Strahl.

    Nur der Fall, dass der Strahl die Kugel durchläuft, also nicht streift,
    wird als Schnitt zurückgegeben!

    Returns
    True: falls es einen Schnittpunkt gibt. Dieser liegt dann
          auf dem Parameter intersect.
    False: es gibt keinen Schnittpunkt, intersect enthält den Nullvektor
    """

    def hit(self, r):
        a = np.dot(r.d, r.d)
        if np.abs(a) < np.finfo(float).eps:
            raise ZeroDivisionError
        diff = r.p - self.m
        b = 2.0*np.dot(diff, r.d)
        c = np.dot(diff, diff) - self.r**2
        D = b**2 - 4.0*a*c
        if (np.abs(D) <= np.finfo(float).eps):
            return False, np.zeros(shape=(3,))

        if (D > np.finfo(float).eps):
            t = (-b - np.sqrt(D))/(2.0*a)
            if t >= 0.0:
                if t > np.finfo(float).eps:
                    return True, r.point(t)
                else:
                    return False, np.zeros(shape=(3,))

            t = (-b + np.sqrt(D))/(2.0*a)
            if t >= 0.0:
                if t > np.finfo(float).eps:
                    return True, r.point(t)
                else:
                    return False, np.zeros(shape=(3,))

        # Kein Schnittpunkt gefunden
        return False, np.zeros(shape=(3, ))

    """
    Liegt ein Punkt auf der Kugel?

    Returns
    -------
    True falls der Punkt auf der Kugel liegt,
    False sonst
    """

    def onSphere(self, point: np.ndarray):
        diff = np.array(self.m - point)
        value = np.dot(diff, diff) - self.r**2
        if np.abs(value) <= np.finfo(float).eps:
            return True
        else:
            return False

    """
    Ausgabe der Ebene auf der Konsole
    """

    def print(self):
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
