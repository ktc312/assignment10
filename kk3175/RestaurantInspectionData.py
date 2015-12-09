'''
Class that handles the NYC restaurant inspections data.

Performs the necessary data wrangling and cleaning to create the class attribute, a cleaned master dataset.

Contains public functions that:
- evaluate restaurant grade trends from the restaurant data, and 
- create datasets appropriate for plotting restaurant grades over time by region

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
'''


import pandas as pd
import datetime as dt
from bisect import bisect
import numpy as np


class RestaurantInspectionData(object):
	# data downloaded to csv from https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59
	restaurantInspectionDataFile = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'

	# Class attribute
	masterDataset = None
		
	def __init__(self):
		self.__constructMasterDataset()

	def __constructMasterDataset(self):
		self.masterDataset = pd.read_csv(self.restaurantInspectionDataFile, low_memory=False)
		self.__keepRelevantColumnsOnly()
		self.__dropIncompleteRecords()
		self.__dropPendingGrades()
		self.masterDataset.drop_duplicates()
		self.__convertToDateTimeFormat()
		self.__sortDates()


	# HELPER FUNCTIONS FOR CONSTRUCTING THE CLASS ATTRIBUTE
	def __keepRelevantColumnsOnly(self):
		relevantColumns = ['CAMIS', 'BORO', 'GRADE DATE', 'GRADE']
		tempDataset = pd.DataFrame()

		for relevantColumn in relevantColumns:
			tempDataset[relevantColumn] = self.masterDataset[relevantColumn]
		
		self.masterDataset = tempDataset

	'''
	Drops any records with missing values (NaN)
	'''
	def __dropIncompleteRecords(self):
		self.masterDataset = self.masterDataset[~(self.masterDataset.isnull().any(axis=1))]
		self.masterDataset = self.masterDataset[self.masterDataset.BORO != 'Missing']

	'''
	The following 3 grade types are removed from the dataset:
		(1) Z (Pending), 
		(2) P (Grade Pending issued on re-opening following an initial inspection that resulted 			in a closure), and
		(3) Not Yet Graded 
	'''
	def __dropPendingGrades(self):
		pendingGrades = ['Z', 'P', 'Not Yet Graded']

		for pendingGrade in pendingGrades:
			self.masterDataset = self.masterDataset[self.masterDataset.GRADE != pendingGrade]

	'''
	Converts the 'GRADE DATE' column to datetime format, which is needed for subsequent date
	manipulations.     
	''' 
	def __convertToDateTimeFormat(self):
		self.masterDataset['GRADE DATE'] = pd.to_datetime(self.masterDataset['GRADE DATE'])

	'''
	Sorts the dataset based on 'GRADE DATE'; the first row is the earliest grade date while
	the last row is the most recent grade date.
	'''
	def __sortDates(self):
		self.masterDataset = self.masterDataset.sort_values(['GRADE DATE'], ascending=True)

	
	# HELPER FUNCTIONS FOR THE PUBLIC FUNCTIONS
	'''
	Constructs and returns a chronological list of grades and a chronological list of corresponding
	dates for one restaurant identified by its CAMIS id.

	Takes a restaurant's CAMIS id as an argument.
	'''
	def __constructGradeComponentsByRestaurant(self, camis_id):
		dataByCamis = self.masterDataset.loc[self.masterDataset['CAMIS'] == camis_id]
		camisGrades = dataByCamis['GRADE'].tolist()
		camisDates = dataByCamis['GRADE DATE'].tolist()
		return camisGrades, camisDates

	'''
	Evaluates whether NYC restaurant grades are improving, declining, or staying the same over a 
	given time frame. The grades are grouped into two different groups. The first group of grades
	represents grades from the first chronological half of the time frame. The second group of grades
	represents grades from the last chronological half of the time frame. The grades from the first group
	are then compared to the grades from the second group to evaluate the overall grade trend.

	Grouping grades by date instead of splitting the list in half accounts for cases when multiple
	grades are entered on one date, which could incorrectly represent results.

	Accepts two arguments: 
	(1) A list of restaurant grades. The grades must be A, B, or C. The grades must be sorted
		chronologically and correspond with the list of dates.
	(2) A list of dates corresponding to when the grades were issued. These dates must be
		chronologically ordered and formatted as datetime in the form of Year-Month-Day
		Hour:Minute:Second.

	Generates a score from the grades of the first chronological half of the grades list and the last 		chronological half of the grades list. The scores are generated as follows:
	(1) Grades are enumerated (A=3, B=2, C=1).
	(2) The midpoint date between the first and last dates is calculated.
	(3) Grade scores are calculated for the first chronological half of the grades list and the last 			chronological half of the grades list. A grade score represents the average grade over
		the specified time period.
	(4) Compare grade scores between the first and last chronological halves of the grade list.

	Returns a 1 if the grade score improved. Returns a -1 if the grade score declined. Returns a 0 if 		the grade score stayed the same.
	'''
	def test_grades(self, grade_list, dates_list):
		self.__enumerateGrades(grade_list)
		midpointDateIndex = self.__calculateMidpointDate(dates_list)
	
		# Calculate grade scores
		firstHalfGradeScore = np.mean(grade_list[:midpointDateIndex])
		lastHalfGradeScore = np.mean(grade_list[midpointDateIndex:])

		return self.__gradeScoreEvaluation(firstHalfGradeScore, lastHalfGradeScore)

	'''
	Helper function that enumerates the list of grades so A=3, B=2, and C=0.
	'''
	def __enumerateGrades(self, grade_list):
		for index, letterGrade in enumerate(grade_list):
			if letterGrade == 'A': grade_list[index] = 3
			elif letterGrade == 'B': grade_list[index] = 2
			# else letterGrade is C
			else: grade_list[index] = 1		

	'''
	Helper function to calculate the midpoint date between the first and last dates.

	Accepts a list of chronologically ordered dates formatted as datetime in the form of 
	Year-Month-Day Hour:Minute:Second.

	Returns the index that corresponds to the midpoint date from the list of dates.
	'''
	def __calculateMidpointDate(self, dates_list):
		firstDate = dt.datetime.strptime(str(dates_list[0]), "%Y-%m-%d %H:%M:%S")
		lastDate = dt.datetime.strptime(str(dates_list[-1]), "%Y-%m-%d %H:%M:%S")
		midpointDate = (firstDate + ((lastDate - firstDate) / 2)).replace(hour=0, minute=0, second=0)
		
		# Finds the index that corresponds to the midpoint date. If the list does not include the exact 		# midpoint date, the index that corresponds to the date closest to the midpoint date is found.
		# Credit to Padraic Cunningham from http://stackoverflow.com/questions/29700214/get-the-closest-datetime-from-a-list
		midpointDateIndex = bisect(dates_list, midpointDate, hi=len(dates_list)-1)
			
		return midpointDateIndex

	'''
	Helper function that evaluates the grade scores from the first and last chronological halves of the 	grade list.

	Accepts the grade score from the first chronological half and the last chronological half as
	arguments.
	 
	Returns a 1 if the grade score improved. Returns a -1 if the grade score declined. Returns a 0 if the 		grade score stayed the same.
	'''
	def __gradeScoreEvaluation(self, firstHalfGradesScore, lastHalfGradesScore):
		if firstHalfGradesScore > lastHalfGradesScore: return -1
		elif firstHalfGradesScore == lastHalfGradesScore: return 0
		else: return 1


	# PUBLIC FUNCTIONS
	'''
	Accepts a restaurant CAMIS ID as an argument. A CAMIS IDs is a unique restaurant identification
	number used by the NYC Department of Health and Mental Hygiene.

	Evaluates the restaurant's grade trends over time and returns a grade score. 

	Returns a 1 if the restaurant's grade score improved over time. Returns a -1 if the grade score
	declined. Returns a 0 if the grade score stayed the same.
	'''
	def test_restaurant_grades(self, camis_id):
		camis_grade_list, camis_dates_list = self.__constructGradeComponentsByRestaurant(camis_id)
		
		score = None
		# If there is only one grade for the restaurant, there is no change in the restaurant's 
		# grade trend.
		if len(camis_grade_list) == 1: score = 0
		else: score = self.test_grades(camis_grade_list, camis_dates_list)
		
		return score

	'''
	Performs data wrangling on a dataset so it is formatted for plotting as a line graph representing
	restaurant grades over time.

	Accepts a pandas dataframe as an argument. From left to right, the columns in the dataframe need to
	be: column index, GRADE DATE, and GRADE.

	Returns the formatted dataset as a pandas dataframe consisting of the following columns (from left 
	to right): Date, Total number of A Grades, Total number of B Grades, and Total number of C Grades.
	'''
	def constructDataForPlot(self, data):
		# change data grouping
		data = data.groupby(['GRADE DATE', 'GRADE']).size().reset_index()
		# rename columns
		data.columns = ['DATE', 'GRADE', 'Total Grade Count']
		# pivot data so each grade is a separate column
		data = data.pivot('DATE', 'GRADE', 'Total Grade Count')
		# since some dates won't have a grade, changes total grade counts with nan to zero
		data = data.fillna(0)
		# groups the data by quarter for a cleaner graph
		data = data.resample('Q')

		return data
