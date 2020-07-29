# -*- coding: utf-8 -*-
"""
@author: brill
"""
# Driver code  
import fractions as fr

if __name__ == "__main__" : 
  
    # Natürliche Zahlen
    n = 125   
    base = 2
    sol = fr.Natural2Placesystem(n, base)
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)
    
    base = 8
    sol = fr.Natural2Placesystem(n, base)
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)
    
    n = 6
    base = 2
    sol = fr.Natural2Placesystem(n, base)
    
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)   
    
    # Rationale Zahlen
    m = 5
    n = 4
    precision = 2
    base = 10
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision)) 

    m = 5
    n = 4
    precision = 2
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision)) 
  
    m = 4
    n = 3
    precision = 10
    base = 10
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision)) 
    
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision)) 

    m = 1
    n = 10
    precision = 5
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision)) 
    
    precision = 5
    base = 8
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          fr.rationalToPlacesystem(m, n, base, precision))