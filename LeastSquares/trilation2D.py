# -*- coding: utf-8 -*-
"""
Lösung der Trilation im 2D mit Hilfe von Scipy

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
P_1 = np.array([1.0, 1.0])
P_2 = np.array([-0.5, 0.5])
d_1 = 2.0
d_2 = 0.5
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
                     (x[0]-P_1[0])**2+(x[1]-P_1[1])**2 - d_1,
                     (x[0]-P_2[0])**2+(x[1]-P_2[1])**2 - d_2
                     ])


print('Trilation')
print('Exakte Lösung: der Ursprung!')
print('Ausgaben')
print('')

# Startwert
x0 = np.array([0.5, -0.5])
result = optimize.least_squares(fun, x0)

if result.success:
    print('Konvergenz!')
    print('Das berechnete Minimum: ', result.x)
    print('Wert der Zielfunktion an diesem Punkt: ', result.cost)
else:
    print('Fehler im Verfahren')
