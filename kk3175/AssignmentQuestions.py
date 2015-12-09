'''
Module for creating and executing the outputs required in Assignment 10 for questions 4 and 5.

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
'''


import pandas as pd
from RestaurantInspectionData import RestaurantInspectionData
from RestaurantGraphs import plotRestaurantGrades


'''
Performs data wrangling required for Question 4 and prints the results.

Question 4, part 1: Compute the sum of the test_restaurant_grades function over all restaurants in
the dataset.

Question 4, part 2: Compute the sum of the test_restaurant_grades function for each of the five
boroughs.
'''
def questionFour(restaurantData):
	# Question 4, part 1
	uniqueRestaurants = restaurantData.masterDataset.iloc[:, [0,1]].drop_duplicates()
	uniqueRestaurants['GRADE TREND'] = uniqueRestaurants.apply(lambda x: restaurantData.test_restaurant_grades(x['CAMIS']), axis=1)

	sumRestaurantGrades = uniqueRestaurants['GRADE TREND'].sum()

	print 'Question 4, part 1:'
	print 'The sum of the grade scores for all restaurants in the dataset is: %r' % sumRestaurantGrades


	# Question 4, part 2
	restaurantGradesByBoro = uniqueRestaurants.groupby(['BORO']).sum().iloc[:, [1]]
	restaurantGradesByBoro.columns = ['Sum of Grade Scores']

	print '\nQuestion 4, part 2:'
	print 'The sum of the grade scores for all restaurants in the dataset by borough is: %r' % restaurantGradesByBoro


'''
Performs data wrangling required for Question 5. Generates the graphes required for Question 5
and saves these graphs to file. After the graphs are generated, prints an update to the user.

Question 5a: Generate a graph showing total number of restaurants in NYC over time for each grade.

Question 5b: Generate one graph for each of the five boroughs showing the total number of restaurants 	in NYC over time for each grade.
'''
def questionFive(restaurantData):
	# Question 5a
	allNYCRestaurants = restaurantData.masterDataset.drop(['CAMIS', 'BORO'], 1)
	allNYCRestaurants = restaurantData.constructDataForPlot(allNYCRestaurants)

	plotRestaurantGrades(allNYCRestaurants, 'NYC')

	print '\nQuestion 5a:'
	print 'A graph showing the total number of restaurants in NYC for each grade over time has been generated and saved as a pdf file in the figures folder.'


	# Question 5b	
	NYCRestaurantsByBoros = restaurantData.masterDataset
	NYCRestaurantsByBoros = NYCRestaurantsByBoros.drop(['CAMIS'], 1)
	# reorders the columns for plotting purposes
	NYCRestaurantsByBoros = NYCRestaurantsByBoros[['GRADE DATE', 'GRADE', 'BORO']]

	# For each borough, creates a dataframe for plotting and then creates the plot.
	boros = pd.unique(NYCRestaurantsByBoros.BORO)
	for boro in boros:
		NYCRestaurantsByBoro = NYCRestaurantsByBoros[NYCRestaurantsByBoros.BORO == boro]	
		NYCRestaurantsByBoro = restaurantData.constructDataForPlot(NYCRestaurantsByBoro)

		plotRestaurantGrades(NYCRestaurantsByBoro, boro)

	print '\nQuestion 5b:'
	print 'Five graphs showing the total number of restaurants in each borough for each grade over time have been generated and saved as pdf files in the figures folder.'
