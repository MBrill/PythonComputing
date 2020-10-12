# -*- coding: utf-8 -*-
"""
Lösung der Aufgabe float2.

Wir berechnen die Potenzen des goldenen Schnitts
mit verschiedenen Genauigkeiten (np.float16/np.float32/np.float64).
"""
import numpy as np


def compute(tau: np.float32, n: np.int):
    """
    Berechnung der Potenzen des goldenen Schnitts.

    Parameters
    ----------
    tau : np.float32
        Approximation der irrationalen Zahl des goldenen Schnitts
    n : np.int
        Anzahl der Potenzen, die berechnet werden sollen.

    Returns
    -------
    tau : np.float32[n]
        Feld mit den berechneten Potenzen.

    """
    tau0 = np.float32(1.0)
    tau1 = tau
    powerTau = np.zeros(n, dtype=np.float32)
    for i in np.arange(n):
        powerTau[i] = np.float32(tau0) - np.float32(tau1)
        tau0 = tau1
        tau1 = powerTau[i]
    return powerTau


def compute16(tau: np.float16, n: np.int):
    """
    Berechnung der Potenzen des goldenen Schnitts.

    Parameters
    ----------
    tau : np.float16
        Approximation der irrationalen Zahl des goldenen Schnitts
    n : np.int
        Anzahl der Potenzen, die berechnet werden sollen.
    Returns
    -------
    tau : np.float16[n]
        Feld mit den berechneten Potenzen.
    """
    tau0 = np.float16(1.0)
    tau1 = np.float16(tau)
    powerTau = np.zeros(n, dtype=np.float16)
    for i in np.arange(n):
        powerTau[i] = np.float16(tau0) - np.float16(tau1)
        tau0 = tau1
        tau1 = powerTau[i]
    return powerTau


# Annäherung des goldenen Schnitts
tau = np.float32(0.61803398)

# Bis zu welcher Potenz berechnen wir tau^n?
n = 24

powers = compute(tau, n)
print("Wir verwenden np.float32-Gleitpunktzahlen!")
print('Exponent ', 1, ':', tau)
for i in np.arange(n):
    print('Exponent ', i+2, ':', powers[i])

# Annäherung des goldenen Schnitts

n = 14
powers = compute16(tau, n)
print("\nWir verwenden np.float16-Gleitpunktzahlen!")
print('Exponent ', 1, ':', tau)
for i in np.arange(n):
    print('Exponent ', i+2, ':', powers[i])
