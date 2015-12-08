import unittest
from unittest import TestCase
from functions import *
from data import *
import data

''' test for assignment10'''

class AssignmentTest(TestCase):

	def setUp(self):
		pass

	# test function test_grades
	def test_test_grades_1(self):

		grade_list = ['A', 'B', 'C']
		self.assertEqual(-1, test_grades(grade_list))

	def test_test_grades_2(self):

		grade_list = ['B', 'C', 'A']
		self.assertEqual(1, test_grades(grade_list))

	def test_test_grades_3(self):

		grade_list = ['A', 'B', 'A']
		self.assertEqual(0, test_grades(grade_list))

	def test_test_grades_4(self):

		grade_list = ['B']
		self.assertEqual(0, test_grades(grade_list))

	# test function test_restaurant_grades
	def test_test_restaurant_grades(self):

		initial_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', dtype = 'unicode')
		self.df = data.data(initial_data).clean_data()

		self.assertEqual(0, test_restaurant_grades(self.df, '30075445'))

if __name__ == '__main__':

	unittest.main()


