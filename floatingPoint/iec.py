# -*- coding: utf-8 -*-
"""
Handling von IEC 754 Exceptions in NumPy
"""
import numpy as np

x = np.arange(10.0)
x[3] = np.nan
print('Das Array x\n', x)
print('Die Summe dieser Werte mit sum berechnet:1', x.sum())
print('Die Summe dieser Werte mit nansum berechnet:', np.nansum(x))
