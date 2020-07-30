# -*- coding: utf-8 -*-


## \example
# Driver for place system functions
#
# We convert natural and rational numbers
# from and to place systems with base 10, 2, 8
# and 16.


import placesystems as ps

if __name__ == "__main__" : 
  
    # Natural numbers
    n = 125   
    base = 2
    sol = ps.natural2placesystem(n, base)
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)
    
    base = 8
    sol = ps.natural2placesystem(n, base)
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)
    
    n = 6
    base = 2
    sol = ps.natural2placesystem(n, base)
    
    print("Die Darstellung von ", n, "zur Basis ", base, " ist ", sol)   
    
    # Rational numbers
    m = 5
    n = 4
    precision = 2
    base = 10
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision)) 

    m = 5
    n = 4
    precision = 2
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision)) 
  
    m = 4
    n = 3
    precision = 10
    base = 10
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision)) 
    
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision)) 

    m = 1
    n = 10
    precision = 5
    base = 2
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision)) 
    
    precision = 5
    base = 8
    print("Die Darstellung von ", m, "/", n, " zur Basis ", base, " ist " , 
          ps.rational2placesystem(m, n, base, precision))