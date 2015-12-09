import unittest
from unittest import TestCase
from plot import *
from date import *
from test_grades import *
import pandas as pd

# author: Kaiwen Liu
# this is a test for assignment 10

class test(unittest.TestCase):

	def setUp(self):
		pass

		# test if the test_grades function returns the correct value
		def test_grades_test(self):
			self.assertEqual(test_grades(['C','C']), 0)
			self.assertEqual(test_grades(['A','C']), -1)
			self.assertEqual(test_grades(['C','A']), 1)

			def test_plot_columns(self): # test if there are 3 columns in the merged 
				self.assertTrue(len(self.df_date_and_grade.columns) == 4)

				def test_plot_correct_columns(self): # test if the dataframe has the correct columns
					self.assertEqual(self.df_date_and_grade.columns, ['Date','A','B','C'])


if __name__ == '__main__':
    unittest.main() 
