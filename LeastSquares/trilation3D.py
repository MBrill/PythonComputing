# -*- coding: utf-8 -*-
"""
Lösung der Trilation im 3D mit Hilfe von Scipy

Wir kennen zwei Punkte P1 und P2 in der Ebene und die Abstände
r1 = d(P, P1) und r2 = d(P, P2) zu einem Punkt P.
Gesucht: die Koordinaten von P.
"""
import numpy as np
from scipy import optimize


# Der Einfachheit halber: Koordinaten der
# Punkte P_1 und P_2 als globale Variable.
# Könnte man auch als args der Zielfunktion übergeben
# und damit variabel machen.
P_1 = np.array([1.0, 1.0, 0.0])
P_2 = np.array([-0.5, 0.5, 0.0])
P_3 = np.array([1.0, 0.5, 1.0])
d_1 = 2.0
d_2 = 0.5
d_3 = 2.25
# Exakte Lösung: P ist der Ursprung


def fun(x):
    """
    Abstand zwischen P,P_1 und P,P_2 zum Quadrat

    Parameters
    ----------
    x : 2D Vektor
        Punkt, an die Funktion ausgewertet wird..

    Returns
    -------
    np.float
        Vektor der Fehlerquadrate.
    """
    return np.array([
                     (x[0]-P_1[0])**2 + (x[1]-P_1[1])**2 + (x[2]-P_1[2])**2 - d_1,
                     (x[0]-P_2[0])**2 + (x[1]-P_2[1])**2 + (x[2]-P_2[2])**2 - d_2,
                     (x[0]-P_3[0])**2 + (x[1]-P_3[1])**2 + (x[2]-P_3[2])**2 - d_3,
                     ])


print('Trilation')
print('Exakte Lösung: der Ursprung!')
print('Ausgaben')
print('')

# Startwert
# Im Tracking nehmen wir die vorherige Position, die sicher
# sehr nahe am gesuchten Minimum ist.
x0 = np.array([0.2, -0.3, 0.2])
result = optimize.least_squares(fun, x0)

if result.success:
    print('Konvergenz!')
    print('Das berechnete Minimum: ', result.x)
    print('Wert der Zielfunktion an diesem Punkt: ', result.cost)
else:
    print('Fehler im Verfahren')
