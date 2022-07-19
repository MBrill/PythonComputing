# -*- coding: utf-8 -*-
"""
Berechnungen mit Gleitpunktarithmetik

Source: Schuppar, Elementare Numerik für die Sekundarstufe, Springer, 2015.
"""
import numpy as np


def T1(s):
    """
    Version T1.

    Parameters
    ----------
    s : float
        Approximation for sqrt(2)

    Returns
    -------
    Computed value.
    """
    return 5000.0/(3363.0+2378.0*s)


def T2(s):
    """
    Version T1.

    Parameters
    ----------
    s : float
        Approximation for sqrt(2)

    Returns
    -------
    Computed value.
    """
    return 5000.0*(3363.0-2378.0*s)


def main():
    """
    Evaluate the expressions T1 and T2 for approximations of sqrt 2.

    We use np.float16, np.float32 and np.float64.

    Returns
    -------
    None.
    """
    print('Using np.float64 for sqrt(2)')
    s = np.float64(np.sqrt(2.0))
    print('Value for T1: ', T1(s))
    print('Value for T2: ', T2(s))

    print('Using np.float32 for sqrt(2)')
    s = np.float32(np.sqrt(2.0))
    print('Value for T1: ', T1(s))
    print('Value for T2: ', T2(s))

    print('Using np.float16 for sqrt(2)')
    s = np.float16(np.sqrt(2.0))
    print('Value for T1: ', T1(s))
    print('Value for T2: ', T2(s))


if __name__ == "__main__":
    main()
