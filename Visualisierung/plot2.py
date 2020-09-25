# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe plot2.

Wir verwenden das Modul fctvis, das wir in der Lösung
von aufgabe plot1 bereits definiert haben.
"""
import numpy as np
import fctVis as fp

h = lambda x: (1.0/np.sqrt(2.0*np.pi)) * np.exp(-0.5*x*x)

xlist = np.linspace(-4.0, 4.0, 41, dtype=np.float64)
hlist = h(xlist)

a = -4.0
b = 4.0
n = 100
title = ''
fp.simple_plotter(h, a, b, n, title, True)
