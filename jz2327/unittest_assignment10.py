import unittest
from unittest import TestCase
import pandas as pd
from data_operation import *

# DS-GA 1007 Assignment 10
# Author: Junchao Zheng

class assignment10_test(TestCase):

	def test_grades_improving(self):
		''' Test if the test_grades function returns 1 if the grades for the restaurant are improving.'''
		
		new_instance = ['C', 'B', 'A']
		self.assertTrue(test_grades(new_instance), 1)

	def test_grades_same(self):
		''' Test if the test_grades function returns 0 if they have stayed the same.'''
		
		new_instance = ['C', 'C', 'C']
		self.assertEqual(test_grades(new_instance), 0)

	def test_grades_declining(self):
		''' Test if the test_grades function returns -1 if they are declining.'''

		new_instance = ['A', 'C', 'B']
		self.assertTrue(test_grades(new_instance), -1)

if __name__ == '__main__':
	unittest.main()
