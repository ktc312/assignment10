# Author: Lizhen Tan

import unittest
import numpy as np
import pandas as pd
from data_func import *
from Data import Data

class Test(unittest.TestCase):
	'''test made for assignment 10'''
	def setUp(self):
		pass

	def test_Data(self):
		# test if data contains any empty entries
		filename = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
		raw_data = Data(filename)    # create data instance
		df = raw_data.clean()
		self.assertFalse(df.empty)

	def test_test_grades(self):
		# test the output of function test_grade
		self.assertEqual(test_grades(['A','B','C','C']), -1)
		self.assertEqual(test_grades(['C','C','B','A']), 1)
		self.assertEqual(test_grades(['C','C','C','C']), 0)

if __name__ == "__main__":
	unittest.main()