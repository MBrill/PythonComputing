# -*- coding: utf-8 -*-
"""
Relative condition number in exercise lgs10.

We use the row sum norm for the matrix norms!
"""
import numpy as np
from scipy import linalg


def main():
    """
    Computing the condition number

    Returns
    -------
    None.
    """
    a = np.array([
        [0.29412, 0.41176, 0.52941, 0.58824],
        [0.42857, 0.57143, 0.71429, 0.64286],
        [0.36842, 0.52632, 0.42105, 0.36842],
        [0.38462, 0.53846, 0.46154, 0.38462]
        ])

    inv = linalg.inv(a)
    print(inv)
    print('The output should be near the 4x4 unit matrix')
    print(a @ inv)
    
    normA = np.linalg.norm(a, ord=1)
    normAinv = np.linalg.norm(inv, ord=1)
    print('Relative condition number of A is ', normA*normAinv)


if __name__ == "__main__":
    main()
