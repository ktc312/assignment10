# Author:Yichen Fan
# Date 12/8/2015
#ASS10

import unittest
from unittest import TestCase
import pandas as pd
import numpy as np
from grade10 import *
from main10 import *

class test10(unittest.TestCase):#test if the grades recorded correctly
	def test_test_grades(self):
		self.assertEqual(1, test_grades(['A','B','C']))
		self.assertEqual(0, test_grades(['A','A','A']))

	def test_setup(self):#check if the data are setup correctly
		self.assertGreater(len(uniq),20)
		self.assertEqual(list(uniq.columns.values),['CAMIS','BORO','GRADE','DATE'])


if __name__ == '__main__':
	unittest.main()