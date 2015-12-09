"""This module contains the unit tests of the hw10 program"""

import numpy as np 
import pandas as pd
from unittest import TestCase
import unittest
import grade_analysis_functions

#author: Muhe Xie
#netID: mx419
#date: 12/01/2015

class Test_HW10(TestCase):
    '''this class will test the test_grades(grade_list) function in the module grade_analysis_functions'''
    def setUp(self):
        pass

    def test_case1(self):
        gradelist = ['A','B','A']
        self.assertEqual(1,grade_analysis_functions.test_grades(gradelist))

        

    def test_case2(self):
        gradelist = ['A']
        self.assertEqual(0,grade_analysis_functions.test_grades(gradelist))

        

    def test_case3(self):
        gradelist = ['A','C','B']
        self.assertEqual(0,grade_analysis_functions.test_grades(gradelist))

        

    def test_case4(self):
        gradelist = ['A','B','A','A','C']
        self.assertEqual(-1,grade_analysis_functions.test_grades(gradelist))


    def test_case5(self):
        gradelist = ['B','B']
        self.assertEqual(0,grade_analysis_functions.test_grades(gradelist))
        
    def test_case6(self):
        gradelist = ['A','C']
        self.assertEqual(-1,grade_analysis_functions.test_grades(gradelist))
    

        







if __name__ == '__main__':
    unittest.main()


