# -*- coding: utf-8 -*-
"""
Ein Dreieck im Raum für einen Ray-Tracer

Quellen: Suffern, Ray-Tracing from the Ground up, A.K. Peters
         Shirley, Morley: Realistic Ray Tracing, A.K. Peters
"""
import numpy as np
import shape
import ray
import lgs33
        
        
"""
Repräsentation eines dreicks im 3D-Raum durch drei Punkte.
"""
class Triangle(shape.Shape):
    """
    Konstruktor
    """
    def __init__(self, 
                 p1: np.ndarray, 
                 p2: np.float64,
                 p3: np.float64):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def checkBaryCoords(self, coords):
        """
        Überprüfen ob wir baryzentrische Koordinaten eines Punkts haben.
        

        Parameters
        ----------
        coords : float64
                 Vektor mit baryzentrischen Koordinaten

        Returns
        -------
        True, falls die Summe der Zahlen 1 ist, und der dadurch gegebene Punkt
              im Innern des Dreiecks liegt..

        """
        alpha, beta, gamma = coords
        a = (0.0 <= alpha) and (alpha <= 1.0)
        b = (0.0 <= beta) and (beta <= 1.0)
        c = (0.0 <= gamma) and (gamma <= 1.0)
        if a and b and c:
            return True
        else:
            return False    
    

    def hit(self, r):
        """
        Berechnung eines Schnittpunkt mit einem Strahl.
    
        Wir stelen ein 3x3 lineares Gleichungssystem auf,
        lösen das mit den Funktion aus lgs33 und verwenden
        die Lösung, falls es einen Schnitt gibt, um die Koordinaten
        des Schnittpunkts zu berechnen.
    
        Parameter
        ---------
    
        r : Instanz der Klasse Ray
        
       Returns
        -------
        True: falls es einen Schnittpunkt gibt. Dieser liegt dann
              auf dem Parameter intersect.
        False: es gibt keinen Schnittpunkt, intersect enthält den Nullvektor
        """
        # Matrix besetzen
        A = np.zeros(shape=(3,4), dtype=np.float64)
        A[0:,0] = self.p2 - self.p1
        A[0:,1] = self.p3 - self.p1
        A[0:,2] = -r.d
        A[0:,3] = r.p -  self.p1

        ok, solution = lgs33.solve(A)
        if not ok:
            return False, np.zeros(shape=(3,))
        if ok:
            if solution[2] < 0.0:
                return False, np.zeros(shape=(3,))
            else:
                coords = np.array([1.0-solution[0]-solution[1], 
                                   solution[0],
                                   solution[1]])

                if  self.checkBaryCoords(coords):
                    return True, r.point(solution[2])
        
     
    """
    Liegt ein Punkt im Dreieck?
    
    Returns
    -------
    True falls der Punkt im Dreieck oder auf dem Rand liegt,
    False sonst
    """
    def inTriangle(self, point:np.ndarray):
        A = np.zeros(shape=(3,4), dtype=np.float64)
        A[0:,0] = self.p1
        A[0:,1] = self.p2
        A[0:,2] = self.p3
        A[0:,3] = point
        
        ok, solution = lgs33.solve(A)
        if not ok:
            return False
        else:            
            return self.checkBaryCoords(solution) 
     
        
    def print(self):
        """
        Ausgabe des Dreiecks auf der Konsole
        

        Returns
        -------
        None.

        """
        print("Dreieck")
        print("Punkt 1", self.p1)
        print("Punkt 2", self.p2)
        print("Punkt 3", self.p3)        
        

def main():
    """
    Beispiel-Code für die Verwendung der Klassen Shape und Triangle

    Returns
    -------
    None.

    """
    point1 = np.array([-1.0, 0.0, 1.0])
    point2 = np.array([1.0, 1.0, 1.0])
    point3 = np.array([0.0, 2.0, 1.0])

    triangle = Triangle(point1, point2, point3)
    
    triangle.print()
    
    c = np.array([0.1, 0.4, 0.5])
    if triangle.checkBaryCoords(c):
        print("Koordinaten sind ok")
    else:
        print("Koodinaten sind nicht ok")
 
    c = np.array([0.2, 0.8, 0.5])
    if triangle.checkBaryCoords(c):
        print("Koordinaten sind ok")
    else:
        print("Koodinaten sind nicht ok")
        
    x1 = np.array([0.0, 1.0, 1.0])
    x2 = np.array([2.0, 2.0, 3.0])
    
    if triangle.inTriangle(x1):
        print("Der Punkt ", x1, " liegt im Dreieck")
    else:
        print("Der Punkt ", x1, " liegt nicht im Dreieck")
    
    if triangle.inTriangle(x2):
        print("Der Punkt ", x2, " liegt im Dreieck")
    else:
        print("Der Punkt ", x2, " liegt nicht im Dreieck")
        
    rayPoint = np.array([0.0, 1.0, 0.0])
    direction = np.array([0.0, 0.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    print('\n')
    r.print()
    
    hit, intersect = triangle.hit(r)
    if hit:
        print("Korrekter Schnittpunkt ist", np.array([0.0, 1.0, 1.0]))
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")
       
    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([0.0, 0.0, 1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()
    
    hit, intersect = triangle.hit(r)
    if hit:
        print("Korrekter Schnittpunkt ist", np.array([1.0, 1.0, 1.0]))
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")
    
    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([1.0, 0.0, 0.0])
    r = ray.Ray(rayPoint, direction)
    r.print()
    
    hit, intersect = triangle.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")  
    
    # Beispiel für einen Strahl, der von der Kugel wegzeigt  
    rayPoint = np.array([1.0, 1.0, -1.0])
    direction = np.array([0.0, 0.0, -1.0])
    r = ray.Ray(rayPoint, direction)
    r.print()
    
    hit, intersect = triangle.hit(r)
    if hit:
        print("Berechneter Schnittpunkt ist ", intersect)
    else:
        print("Kein Schnittpunkt!")  
        

if __name__ == "__main__":
    main()