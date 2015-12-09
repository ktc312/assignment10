'''
This module contains unittests for the computing functions in this assignment.
'''

import unittest
from data_clean import *
from compare_and_score import *
from unittest import TestCase

data_path = './DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
data = pd.read_csv(data_path, parse_dates=['GRADE DATE'])
df_class = CleanData(data)
data_clean = df_class.clean


class Test_Assign10(TestCase):
  
    def setUp(self):
        pass

    def test_clean_data(self): #Test the exception handling of clean_data(data)
        a = 'aaaa'
        self.assertRaises(TypeError, clean_data, a)

    def test_test_grades(self): #Test the exception handling and outcome of test_grades(grade_list)
        b = [1, 10, 100, 1000]
        c = 'A'
        d = []
        e = ['A', 'C', 'B']
        f = ['A', 'A', 'A', 'B', 'A']
        self.assertRaises(ValueError, test_grades, b)
        self.assertRaises(TypeError, test_grades, c)
        self.assertRaises(InvalidListLength, test_grades, d)
        self.assertEqual(test_grades(e), -1)
        self.assertEqual(test_grades(f), 0)

    
    def test_test_restaurant_grades(self): #Test the outcome of test_restaurant_grades(data_clean, camis_id)
        g = 40482597
        h = 40941055
        self.assertEqual(test_restaurant_grades(data_clean, g), 1)
        self.assertEqual(test_restaurant_grades(data_clean, h), -1)

        

if __name__ == '__main__':
    unittest.main()
