# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe num6.
"""
import numpy as np


def pt_in_circle(p, midpoint, diam):
    """
    Examine, if given points are in the circle
    including the perimeter.

    Parameters
    ----------
    p : float
        points to to be examined.
    midpoint : float-array of lenght 2
        coordinates of the center point of the circle.
    diam : float
        diameter of the circle.

    Returns
    -------
    TRUE is point is contained in the circle
    """
    radius2 = 0.25*(diameter**2)
    distances = (x - midpoint[0])**2 + (y - midpoint[1])**2
    return distances <= radius2


x = np.arange(40, 130, 10, dtype=np.float64)
y = np.full_like(x, 60.0)
points = np.column_stack((x, y))

midpoint = np.array([80.0, 60.0], dtype=np.float64)
diameter = 60.0

result = pt_in_circle(points, midpoint, diameter)
print("Die Punkte, die im Kreis liegen sind")
print(points[result])
