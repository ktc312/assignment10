'''
Author: Aditi Nair (asn264)
Date: December 8 2015

'''


from unittest import TestCase
from HealthDataAnalyzer import *

#Create an instance of the class
Analyzer = HealthDataAnalyzer()

class dataCleaningTest(TestCase):

	#Make sure clean_health_data() returns a dataframe. This test fails if the csv is not in the current directory.
	def test_clean_health_data(self):
		self.assertIsInstance(Analyzer.health_grades, pd.DataFrame)

class testGradesTest(TestCase):

	#Make sure the test_grades function computes results as expected. 0 value is manually computed. 
	def test_test_grades(self):
		self.assertEqual(Analyzer.test_grades(['A', 'B', 'C', 'B']), 0)


class HealthDataAnalyzer(TestCase):

	#Test whether the test_restaurant_grades function returns the right value for a given camis_id. 0 value was manually computed.
	def test_test_restaurant_grades(self):
		self.assertEqual(Analyzer.test_restaurant_grades(30075445),0)

	#Test whether the sum_test_results_by_boro function computes five separate sums, one for each boro
	def test_sum_test_results_by_boro(self):
		self.assertEqual(Analyzer.sum_test_results_by_boro().size, 5)
