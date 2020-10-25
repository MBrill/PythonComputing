# -*- coding: utf-8 -*-
"""
 We convert natural and rational numbers to place systems defined by the base.
"""

import math


def natural2placesystem(num, base=2):
    """
    Convert a natural number to a place system

    Parameters
    ----------
    num : int
        natural number to be converted.
    base : int, optional
        base of the place system to be used. The default is 2.

    Returns
    -------
    result : string
        The digits in the place system as a string.

    """
    result = ""
    k = math.floor(math.log(num, base)) + 1
    divisor = base**(k-1)
    while (k > 0):
        digit = num // divisor
        num = num % divisor
        result += str(digit)
        k -= 1
        divisor //= base
    return result


def rational2placesystem(m, n, base, precision=10):
    """
    Convert a rational number to a place system ror a given base

    Parameters
    ----------
    m : int
        nominator of rational number q=m/n.
    n : int
        denominator of rational number q=m/n.
    base : int
        base of the place system to be used.
    precision : int, optional
        number of digits used after the point. The default is 10.

    Returns
    -------
    result : string
        the digits in the place system.

    """
    result = ""
    g = m // n
    if g > 0:
        result = natural2placesystem(g, base) + "."
    else:
        result = "0."
    r0 = m - g*n

    while (precision > 0 and r0 > 0):
        r0 *= base
        d = r0 // n
        result += str(d)
        r0 -= d*n
        precision -= 1
    return result
