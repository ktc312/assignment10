"""
Unit test to make sure the test_grades function calculates score changes properly.

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
"""


import pandas as pd
from RestaurantInspectionData import RestaurantInspectionData
from unittest import TestCase
from datetime import datetime

class GradeScoresTest(TestCase):
	
	def test__test_grades_function(self):
		restaurantData = RestaurantInspectionData()

		date1 = datetime.strptime('2012-02-22 00:00:00', '%Y-%m-%d %H:%M:%S')
		date2 = datetime.strptime('2015-06-22 00:00:00', '%Y-%m-%d %H:%M:%S')
		dates_testList = [date1, date2]

		
		# test for the case when the grade does not change
		grade_testList = ['C', 'C']
		output = restaurantData.test_grades(grade_testList, dates_testList)
		expectedOutput = 0

		self.assertEqual(output, expectedOutput)


		# test for the case when the grade improves
		grade_testList = ['C', 'A']
		output = restaurantData.test_grades(grade_testList, dates_testList)
		expectedOutput = 1

		self.assertEqual(output, expectedOutput)


		# test for the case when the grade declines
		grade_testList = ['A', 'C']
		output = restaurantData.test_grades(grade_testList, dates_testList)
		expectedOutput = -1

		self.assertEqual(output, expectedOutput)
