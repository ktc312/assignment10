"""Author: Akash Shah (ass502)

unittest for test_grades method in the calculate module"""

from calculate import *
from unittest import TestCase

class GradesTest(TestCase):

	def test_static_grades(self):
		self.assertEqual(test_grades(['A','A','A']),0)
		self.assertEqual(test_grades(['B']),0)

	def test_increasing_grades(self):
		self.assertEqual(test_grades(['C','B','A']),1)
		self.assertEqual(test_grades(['B','C','B','A']),1)

	def test_decreasing_grades(self):
		self.assertEqual(test_grades(['A','B','C']),-1)
		self.assertEqual(test_grades(['A','B','C','B']),-1)