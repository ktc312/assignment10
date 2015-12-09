'''
Author: Aditi Nair (asn264)
Date: November 3rd 2015
'''

import sys
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 


class HealthDataAnalyzer(object):

	'''Each instance of this class represents a tool for analyzing the NYC DoH data. It relies on the data-cleaning and grade-evaluation functions as static
	methods because their behavior is not dependent on the state of the HealthDataAnalyzer object, but is obviously associated with it.
	Each instance of the class is associated with two dataframes, described below, and functions that compute various statistics or create graphs with respect to them.'''

	def __init__(self):

		#This is just a cleaned version of the provided csv. 
		self.health_grades = self.clean_health_data()

		#Here we sort the data by date, then grouping by BORO and camis_id, take a list of the grades. 
		#For each list of grades (corresponding to a unique boro-camis_id pair), apply the function test_grades and store the result as a series.
		self.progress_evaluation_by_camis = self.health_grades.sort('GRADE DATE').groupby(['BORO', 'CAMIS'])['GRADE'].apply(lambda x: x.tolist()).apply(self.test_grades)



	@staticmethod
	def clean_health_data():

		'''This function cleans and loads the data into a data frame. It removes any rows where the GRADE is not A, B, or C and also 
		removes any rows where BORO is Missing. It also converts the GRADE DATE column to be of datetime type which is useful later. Because
		Git does not allow you to upload files beyond a certain size, you may run into an IOError here.

		(According to NYC DOH the only valid grades are A, B, or C: http://www.nyc.gov/html/doh/downloads/pdf/rii/how-we-score-grade.pdf)
		'''

		try:

			#Load the data, dropping rows where there are NaN values. Setting low_memory to false to 
			health_grades = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory=False).dropna()

			#The only valid health grades are A, B, C. Throw out any other values. 
			health_grades = health_grades[health_grades['GRADE'].isin(['A', 'B', 'C'])]

			#Currently the dates in column GRADE DATE are of type 'object'. Convert to type datetime. 
			health_grades['GRADE DATE'] = pd.to_datetime(health_grades['GRADE DATE'])

			#Drop the columns where the Borough is 'Missing'
			health_grades = health_grades[health_grades['BORO'] != 'Missing']

			return health_grades

		except IOError:
			sys.exit("Please download the file 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv' into this directory and try again.")


	@staticmethod
	def test_grades(grades):

		'''This function accepts a list of grades and returns 1 if they are improving, 0 if they remain the same and -1 if they are getting worse.
		It converts grades to integer values, evaluates differences between consecutive grades, and then takes the weighted average of
		differences, giving greater weight to more recent changes. Please consult README.txt for a full explanation of the methodology.
		Assumes grades is a chronologically sorted list.'''

		#If there is only one grade, then the grades are neither improving or declining
		if len(grades) == 1:
			return 0

		else:

			grade_to_int = {'A':3, 'B':2, 'C':1}

			#Transform the list of letter grades to a list of integer values 
			ints = [grade_to_int.get(i) for i in grades]

			#The difference between each consecutive grade indicates whether the grade is increasing, decreasing, or staying the same between inspections
			differences = np.diff(ints)

			#Now take the weighted average of the differences
			length = len(differences)
			avg = sum([(i+1)*differences[i] for i in range(length)])/float((length*(length+1))/2)

			if avg > 0:
				return 1
			elif avg < 0:
				return -1
			else:
				return 0 


	def test_restaurant_grades(self, camis_id):

		'''Returns the value of test_grades for a list of chronological grades for a single CAMIS id by
		looking at the series self.progress_evaluation_by_camis and returning the row corresponding to the right CAMIS id'''

		return self.progress_evaluation_by_camis.loc[self.progress_evaluation_by_camis.index.get_level_values('CAMIS')==camis_id][0]



	def sum_test_results_by_boro(self):

		'''Computes the sum of the test results in each borough by taking the sum of self.progress_evaluation_by_camis grouping
		by the index at level='BORO'''

		return self.progress_evaluation_by_camis.sum(level='BORO')



	def print_test_results(self):

		'''Prints the results of sum_test_results_by_boro and then prints a sum of the whole series boro_sums to compute the 
		sum of results for the whole city.'''

		boro_sums = self.sum_test_results_by_boro()

		for boro, test_sum in boro_sums.iteritems():
			print "The sum of the scores of all restaurants in", boro, ":", test_sum

		print "The sum of the scores of all the restaurants in NYC:", boro_sums.sum()



	def graph_grade_improvement_nyc(self):

		'''Create a graph that plots the number of restaurants having grades A, B, and C over time, and saves it to PDF.
		Plots the number of restaurants on the y-axis and the dates on the x-axis, with a different line for each grade.'''

		count_by_date = self.health_grades.groupby(['GRADE DATE', 'GRADE']).size().unstack(level=1).sort()
		count_by_date.plot(kind='line')
		plt.title("Grade Distribution NYC")
		plt.ylabel("Number of Restaurants")
		plt.savefig("grade_improvement_nyc.pdf")



	def graph_grade_improvement_by_boro(self):


		'''For each borough, create a graph that plots the number of restaurants having grades A, B, or C over time, and saves it to PDF.
		Plots the number of restaurants on the y-axis and the dates on the x-axis, with a different line for each grade.'''

		count_by_date_by_boro = self.health_grades.groupby(['BORO', 'GRADE DATE', 'GRADE']).size().unstack(level=2).sort()
		for boro in count_by_date_by_boro.index.get_level_values('BORO').unique():
			count_by_date_by_boro.loc[boro].plot(kind='line')
			plt.title("Grade Distribution " + str(boro))
			plt.ylabel("Number of Restaurants")
			plt.savefig("grade_improvement_"+str(boro)+".pdf")

