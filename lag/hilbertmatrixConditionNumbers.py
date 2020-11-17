# -*- coding: utf-8 -*-
"""
Relative condition numbers of the Hilbert matrix.

We use the column sum norm for the matrix norms!
"""
import numpy as np
from scipy import linalg


def main():
    """
    Computing the condition numbers

    Returns
    -------
    None.
    """
    n = 16
    print('Relative condition numbers of the Hilbert matrix')
    print('Dimension, condition number')
    for i in np.arange(3, n):
        normH = np.linalg.norm(linalg.hilbert(i), ord=np.inf)
        normHinv = np.linalg.norm(linalg.invhilbert(i), ord=np.inf)
        print(i, normH*normHinv)


if __name__ == "__main__":
    main()
