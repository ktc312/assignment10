'''
Varun D N, vdn207
DS-GA 1007 - Assignment 10
'''

'''Unit tests for functions handling different calls for data extraction'''

from unittest import TestCase
import restaurants as res
import custom_exceptions as cexcep
import specific_functions as specfunc
import matplotlib.pyplot as plt
import pandas as pd 

class FunctionalityTests(TestCase):
	'''Unit Tests for testing supporting functions of the software'''

	def setUp(self):
		'''Setting up the test environment'''

		self.input1 = [1, 10, 100, -1]
		restaurant_data = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv", low_memory = False)	
		self.restaurants_obj = res.Restaurants(restaurant_data)
		self.invalid_column_name = 'BLUE'
		self.random_column_value = 33
		self.invalid_camis = 7787

	def test_not_a_dataframe_exception_raised(self):
		'''Raises the NotADataFrameException'''

		self.assertRaises(cexcep.NotADataFrameException, res.Restaurants, self.input1)

	def test_get_rows_exception_is_raised(self):
		'''Raises the KeyError as an invalid column name is passed'''

		self.assertRaises(cexcep.InvalidColumnName, self.restaurants_obj.get_rows, self.invalid_column_name, self.random_column_value)

	def test_get_unique_values_exception_is_raised(self):
		'''Raises the KeyError as the column name passed in invalid'''

		self.assertRaises(KeyError, self.restaurants_obj.get_unique_values, self.invalid_column_name)

	def test_get_restaurant_grades_exception_is_raised(self):
		'''Raises the KeyError as the CAMIS ID passed is not found in the dataset'''

		self.assertRaises(KeyError, self.restaurants_obj.get_restaurant_grades, self.invalid_camis)

	def test_groupby_column_exception_is_raised(self):
		'''Raises the KeyError as the column name passed in invalid for the groupby function'''

		self.assertRaises(KeyError, self.restaurants_obj.groupby_column, self.invalid_column_name)

	def test_grades_list_exception(self):
		'''Raises because the datatype of the grades passed is not valid or consistent'''

		self.assertRaises(cexcep.InvalidGradeList, specfunc.test_grades, self.input1)

 
