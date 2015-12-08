import pandas as pd
import matplotlib.pyplot as plt
from data1 import *
from functions1 import *
import numpy as np
import unittest

class test_hw10(unittest.TestCase):
    '''
    Test if test_grades function produces the correct results
    '''
    def setUp(self):
        pass

    def test_grade_test1(self):
        grade_list = ['A','B','C']
        self.assertTrue(test_grades(grade_list)==-1)

    def test_grade_test2(self):
        grade_list = ['A','B','A']
        self.assertTrue(test_grades(grade_list)==1)

    def test_grade_test3(self):
        grade_list = ['B']
        self.assertTrue(test_grades(grade_list)==0)

if __name__ == '__main__':
    unittest.main()