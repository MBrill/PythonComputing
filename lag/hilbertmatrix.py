# -*- coding: utf-8 -*-
"""
Fallstudie: die Hilbert-Matrx
"""
import numpy as np
from scipy import linalg

n = 3
print('n=',n)
print(linalg.hilbert(n))

n = 4
print('n=',n)
print(linalg.hilbert(n))

print('Inverse Hilbert-Matrizen')
n = 3
print('n=',n)
print(linalg.invhilbert(n))

# Exakte und angehäherte Werte 
n = 4
print('n=',n)
print(linalg.invhilbert(n))


# invhilbert(n, exact = False) ab n>=15 verwenden.
n=15
k = 14
x = linalg.invhilbert(n, exact=True)[k,k]
y = linalg.invhilbert(n, exact=False)[k,k]
print(x)
print(y)

n=25
k = 24
x = linalg.invhilbert(n, exact=True)[k,k]
y = linalg.invhilbert(n, exact=False)[k,k]
print(x)
print(y)

# Ist das Produkt gleich der Einheitsmatrix?
print('Tests für das Produkt')
n = 5
H = linalg.hilbert(n)
Hinv = linalg.invhilbert(n)

if np.allclose(H @ Hinv, np.identity(n)):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')

n = 7
H = linalg.hilbert(n)
Hinv = linalg.invhilbert(n)

if np.allclose(H @ Hinv, np.identity(n)):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
    
n = 8
H = linalg.hilbert(n)
Hinv = linalg.invhilbert(n)

if np.allclose(H @ Hinv, np.identity(n)):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
    
n = 15
H = linalg.hilbert(n)
Hinv = linalg.invhilbert(n)

if np.allclose(H @ Hinv, np.identity(n)):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')

# Eigene Berechnung der inversen Hilbert-Matrix
print('Mit linalg.solve berechnete inverse Hilbert-Matrix')
n=5
rhs = np.identity(n)
computed_inv = np.linalg.solve(linalg.hilbert(n), rhs)
Hinv = linalg.invhilbert(n, exact=False)
if np.allclose(computed_inv -  Hinv, np.zeros(shape=(n,n)), atol=0.001):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
  
n=7
rhs = np.identity(n)
computed_inv = np.linalg.solve(linalg.hilbert(n), rhs)
Hinv = linalg.invhilbert(n, exact=False)
if np.allclose(computed_inv -  Hinv, np.zeros(shape=(n,n)), atol=0.001):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
    
n=12
rhs = np.identity(n)

computed_inv = np.linalg.solve(linalg.hilbert(n), rhs)
Hinv = linalg.invhilbert(n, exact=False)
if np.allclose(computed_inv -  Hinv, np.zeros(shape=(n,n)), atol=0.001):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
 
# Jetzt mit SciPy, dann erhalten wir eine Warnung
n=12
rhs = np.identity(n)

computed_inv = linalg.solve(linalg.hilbert(n), rhs)
Hinv = linalg.invhilbert(n, exact=False)
if np.allclose(computed_inv -  Hinv, np.zeros(shape=(n,n)), atol=0.001):
    print('Bei n =', n, ' ist alles ok')
else:
    print('Bei n =', n, ' ist etwas schief gegangen')
    