import unittest
from unittest import TestCase
import pandas as pd
import numpy as np
from Assignment10 import *


class CommandTest(TestCase):
	
	def setUp(self):
		pass

	def testing_read_data(self):
		df = read_data()
		self.assertEqual(len(df.columns.values)=4)


	def testing_test_grades(self):
		self.assertEqual(test_grades(['C','B','A'],1)
		self.assertEqual(test_grades(['A','B','C'],-1)
		self.assertEqual(test_grades(['A','A','A'],0)

	def testing_test_restaurant_grades(self):
		self.assertEqual(test_restaurant_grades(41524607),-1)

	if __name__ == "__main__":
		unittest.main()