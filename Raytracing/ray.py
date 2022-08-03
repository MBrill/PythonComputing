# -*- coding: utf-8 -*-
"""
Ein Strahl für einen Ray-Tracer
"""
import numpy as np

"""
Ein Strahl, gegeben durch einen Punkt im Raum und einen Richtungsvektor.
"""


class Ray:
    """
    Konstruktor
    """

    def __init__(self,
                 point,
                 direction):
        self.p = point
        self.d = direction

    """
    Punkt auf dem Strahl für einen Parameterwert t
    """

    def point(self, t: np.float64):
        return(self.p + t*self.d)

    """
    Ausgabe auf der Konsole
    """

    def print(self):
        print("Strahl")
        print("Punkt:", self.p)
        print("Richtungsvektor", self.d)


def main():
    """
    Beispiel-Code für die Verwendung der Klasse Ray

    Returns
    -------
    None.

    """
    point = np.zeros(shape=(3,))
    direction = np.ones(shape=(3,))
    ray = Ray(point, direction)

    ray.print()

    print("Ein Punkt auf dem Strahl für t=2:", ray.point(2.0))


if __name__ == "__main__":
    main()
