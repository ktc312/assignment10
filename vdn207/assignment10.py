'''
Varun D N - vdn207@nyu.edu
'''

'''Run this module to get the output of the scores per borough'''

import pandas as pd 
import restaurants as res
import specific_functions as specfunc 

if __name__ == '__main__':
	'''Main program'''

	restaurants = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv", low_memory = False)	
	restaurants_obj = res.Restaurants(restaurants)

	borough_scores = specfunc.find_scores_by_borough(restaurants_obj)
	for borough in borough_scores.keys():
		print borough + ": " + str(borough_scores[borough])

	# Plotting the graphs of entire NYC
	specfunc.plot_grade_improvement(restaurants_obj, 'grade_improvement_nyc.pdf')

	# Plotting the graphs of every borough
	specfunc.plot_grade_improvements_by_borough(restaurants_obj)
	