import unittest
from unittest import TestCase
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import cleanData as cl
from cleanData import *
from hw10_functions import *
from visualize_tool import *

# DS-GA 1007 HW10
# Author: Sida Ye
# test file

"""tests for hw10"""

class hw10_unittest(unittest.TestCase):

    def setUp(self):
        pass

    def test_test_grades(self):
        self.assertEqual(1, test_grades(['A', 'C', 'B']))
        self.assertEqual(0, test_grades(['C', 'B', 'C']))
        self.assertEqual(-1, test_grades(['C', 'B', 'A']))
    
    def test_test_restaurant_grades(self):
        data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory=False)
        self.data = cl.cleanData(data).process_data()
        self.assertEqual(0, test_restaurant_grades(self.data, 50042805))
        self.assertEqual(0, test_restaurant_grades(self.data, 30112340))



if __name__ == "__main__":
    unittest.main()

