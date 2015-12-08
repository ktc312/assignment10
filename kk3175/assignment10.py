'''
Main program for running the outputs required in Assignment 10. 
Assignment 10 requires outputs for questions 4 and 5.

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
'''


import pandas as pd
from RestaurantInspectionData import RestaurantInspectionData
from RestaurantGraphs import plotRestaurantGrades
from AssignmentQuestions import questionFour, questionFive


'''
Main function for generating the outputs required in questions 4 and 5.
'''
def main():
	try:
		restaurantData = RestaurantInspectionData()
		questionFour(restaurantData)
		questionFive(restaurantData)

	except EOFError:
		print 'Sorry, the restaurant data file is empty.'	
	except KeyboardInterrupt:
		print 'Goodbye!'
	# Input error if there is an issue with loading the restaurant data csv file.
	# Output error if there is an issue saving a graph to file.
	except IOError:
		print 'Sorry, there was an input output error.'

main()



