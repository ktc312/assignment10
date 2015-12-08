'''
Author: Aditi Nair
Date: November 27 2015

This is my submission for assignment 10. Please see README.txt for an explanation of the organization and methodology.
'''

from HealthDataAnalyzer import *

def main():

	print "Cleaning and preparing the data..."

	#Creates an instance of the HealthDataAnalyzer object which is associated with a cleaned dataframe and 
	#a series which contains the test_grades result for each (borough, camis_id) pair.
	Analyzer = HealthDataAnalyzer()

	print "Evaluating results..."

	#Prints the sum of test_grades for each borough, and then for the city as a whole.
	Analyzer.print_test_results()
	
	print "Creating graphs..."

	#Creates and saves a PDF that plots restaurant grades over time, over the whole city. 
	Analyzer.graph_grade_improvement_nyc()

	#Creates and saves a PDF that plots restaurant grades over time, by borough. 
	Analyzer.graph_grade_improvement_by_boro()
	
	print "Program complete!"


#Run the program
if __name__ == "__main__":
	main()


