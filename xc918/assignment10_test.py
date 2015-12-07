#Author: Xing Cui
#NetID: xc918
#Data: 12/3

import unittest
from unittest import TestCase
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import data_cleanser as ds 
from data_cleanser import *
from assignment10_functions import *
from visualization import *

class hw10_unittest(unittest.TestCase):

	"""This class is testing for assigment10.
	"""
	
	def setUp(self):
		pass

	def test_test_grades(self):
		self.assertTrue(1, test_grades(['C', 'B', 'A']))
		self.assertEqual(-1, test_grades(['A', 'B', 'C']))
		self.assertEqual(0, test_grades(['B', 'B', 'B']))


if __name__ == "__main__":
	unittest.main()


