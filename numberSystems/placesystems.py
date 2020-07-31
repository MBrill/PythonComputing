# -*- coding: utf-8 -*-

## We convert natural and rational numbers to place systems defined by the base.

## \mainpage
# Examples and functions for place systems.
#
# \image html pdepackweb.png
#
# The input for this page can be found in the file fractions.py.

import math

## Convert a natural number to a place system
#
# \param num: natural number to be converted
# \param base: base of the place system to be used
#              base=2 is the default
# \return the digits in the place system as a string
def natural2placesystem(num, base=2) : 
    result = ""    
    k = math.floor(math.log(num, base)) + 1
    divisor = base**(k-1)
    while (k>0) :         
        digit = num // divisor  
        num = num % divisor 
        result += str(digit);  
        k -= 1        
        divisor //= base       
    return result

## Convert a rational number to a place system
#
# \param m: nominator of rational number q=m/n
# \param n: ndeominator of rational number q=m/n
# \param base: base of the place system to be used
#              base=2 is the default
# @param precision: number of digits used after the point
#                   default value is 10
# \return the digits in the place system as a string
def rational2placesystem(m, n, base, precision = 10) :  
    result = ""   
    g = m // n  
    if g > 0 : 
        result = natural2placesystem(g, base) + "." 
    else:
        result = "0."
    r0 = m - g*n
  
    while (precision>0 and r0>0) :            
        r0 *= base
        d = r0 // n
        result += str(d)
        r0 -= d*n 
        precision -= 1
    return result  
