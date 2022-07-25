# -*- coding: utf-8 -*-
"""
Unittest für das Modul lgs33
"""
import unittest
import numpy as np
import numpy.testing as npt
import lgs33


class LGS(unittest.TestCase):
 
    def testBacksub(self):
        a = np.array([[2.0, 3.0, -1.0, 1.0],
                      [0.0, 4.0, -3.0, 1.0],
                      [0.0, 0.0,  1.0, 1.0]])
        correct = np.array([-0.5, 1.0, 1-0])
        
        npt.assert_almost_equal(correct, lgs33.backSubstitution(a))
        

    def testElimination(self):
        a = np.array([[1.0, -1.0, 0.0,  5.0],
                      [-1.0, 2.0, -1.0, 0.0],
                      [0.0, -1.0,  2.0, 1.0]])
        #  Matrix unterhalb der Diagonale wird nicht verändert!
        ac = np.array([[1.0, -1.0, 0.0,  5.0],
                       [-1.0, 1.0, -1.0, 5.0],
                       [0.0, -1.0,  1.0, 6.0]])
        lgs33.gauss(a)
        npt.assert_almost_equal(ac, a)   
        
    def testEliminationAndBack(self):
        a = np.array([[1.0, -1.0, 0.0,  5.0],
                      [-1.0, 2.0, -1.0, 0.0],
                      [0.0, -1.0,  2.0, 1.0]])
        correct = np.array([16.0, 11.0, 6.0])
        lgs33.gauss(a)
        npt.assert_almost_equal(correct, lgs33.backSubstitution(a)) 
        

    def testSolve(self):
        a = np.array([[1.0, -1.0, 0.0,  5.0],
                      [-1.0, 2.0, -1.0, 0.0],
                      [0.0, -1.0,  2.0, 1.0]])
        correct = np.array([16.0, 11.0, 6.0])
        ok, solution = lgs33.solve(a)
        self.assertTrue(self, ok)
        npt.assert_almost_equal(correct, solution) 


if __name__ == "__main__":
    unittest.main()
