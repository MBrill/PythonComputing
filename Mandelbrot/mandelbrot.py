# -*- coding: utf-8 -*-
"""
Code aus WWW

@author: brill
"""

import numpy as np
from imageio import imwrite
 
m = 480
n = 320

x = np.linspace(-2.0, 1.0, num=m).reshape((1, m))
y = np.linspace(-1, 1, num=n).reshape((n, 1))
C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

Z = np.zeros((n, m), dtype=np.complex)
M = np.full((n, m), True, dtype=np.bool)
for i in range(100):
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > 2] = False
 
imwrite('images/mandelbrot.png', np.uint8(np.flipud(1 - M) * 255))
