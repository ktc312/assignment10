"""Author: Akash Shah (ass502)

unittest for test_restaurant_grades method in the calculate module"""

from calculate import *
from grades import *
from unittest import TestCase

class RestaurantGradesTest(TestCase):

	def test_restaurant(self):
		'''having tested and verified test_grades, we then test test_restaurant_grades against test_grades'''

		grades = Grades()

		self.assertEqual(test_grades(['B','B','B','A','A','A','A','A']),grades.test_restaurant_grades(40363630))
		self.assertEqual(test_grades(['A','A','A','A','A','A','B','B','B','B']),grades.test_restaurant_grades(40364449))