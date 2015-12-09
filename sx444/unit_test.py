"""This is the unit test"""

import numpy as np 
import pandas as pd
from unittest import TestCase
import unittest
import grade_analysis_functions


class test(TestCase):
    '''this class is for the test of test_grades(grade_list) function'''
    def setUp(self):
        pass

    def test_1(self):
        gradelist = ['A','C']
        self.assertEqual(-1,grade_analysis_functions.test_grades(gradelist))

    def test_2(self):
        gradelist = ['A','C','B']
        self.assertEqual(0,grade_analysis_functions.test_grades(gradelist))

    def test_3(self):
        gradelist = ['A','B','A','A','C']
        self.assertEqual(-1,grade_analysis_functions.test_grades(gradelist))

if __name__ == '__main__':
    unittest.main()
