# -*- coding: utf-8 -*-
"""
Computing some examples for the Mandelbrot set.
"""
import numpy as np
import iteration as it

c = np.complex(1.0, 1.0)
result = it.iterate_with_barrier(c, 10)

print('Test auf Divergenz')
print('c = ', c)
if result:
    print('c liegt in der Mandelbrotmenge')
else:
    print('c liegt nicht in der Mandelbrotmenge')

c = np.complex(0.0, 1.0)
result = it.iterate_with_barrier(c, 10)
print('c = ', c)
if result:
    print('c liegt in der Mandelbrotmenge')
else:
    print('c liegt nicht in der Mandelbrotmenge')
  