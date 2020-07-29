# -*- coding: utf-8 -*-
"""
Beispiel für den Einfluss von Rundungsfehler 
auf eine Berechnung.

Wir berechnen die Potenzen des goldenen Schnitts
mit verschiedenen Genauigkeiten (np.single/np.double).
"""
import numpy as np

print("Wir verwenden np.single-Gleitpunktzahlen!")
tau0 = np.single(1.0)
# Annäherung des goldenen Schnitts
tau1 = np.single((0.5)*(np.sqrt(5.0)-1.0))
print("Exponent",1, " :", tau1)

# Bis zu welcher Potenz berechnen wir tau^n?
n = 25

for i in range(n-1):
    tau = tau0 - tau1
    print("Exponent",i+2, " :", tau)
    tau0 = tau1
    tau1 = tau
    
print("Wir verwenden np.double-Gleitpunktzahlen!")
tau0 = np.double(1.0)
# Annäherung des goldenen Schnitts
tau1 = np.double((0.5)*(np.sqrt(5.0)-1.0))
print("Exponent",1, " :", tau1)

# Bis zu welcher Potenz berechnen wir tau^n?
n = 42

for i in range(n-1):
    tau = tau0 - tau1
    print("Exponent",i+2, " :", tau)
    tau0 = tau1
    tau1 = tau
    

    


