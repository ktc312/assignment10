'''
Varun D N - vdn207@nyu.edu
'''

'''Contains specific functions for the assignment'''

import restaurants as res 
import matplotlib.pyplot as plt 
import custom_exceptions as cexcep
import matplotlib.patches as mpatches 
import numpy as np

def test_grades(grade_list):
	'''Returns whether the grades are increasing, same or decreasing'''

	'''
	Logic: A score is maintained starting from 0. -1 for every fall in the grade. +1 for every rise in the grade. 0 for the same grade maintained.
		   This is basically a cumulative score indicating the trend of the grades.
	'''
	
	if not all(isinstance(grade, str) for grade in grade_list):
		raise cexcep.InvalidGradeList("Pass the grade list with valid dtypes")


	grade_trend_score = 0
	for index in range(len(grade_list) - 1):
		grade_trend_score -= ord(grade_list[index + 1]) - ord(grade_list[index])
		if grade_list[index+1] == 'A' and grade_list[index] == 'A':
			grade_trend_score += 1

	if grade_trend_score == 0:
		return 0
	
	elif grade_trend_score > 0:
		return 1

	return -1

def test_restaurant_grades(restaurants_obj, camis_id):
	'''Returns the score of a restuarant given its CAMIS ID'''

	restaurant_grades = restaurants_obj.get_restaurant_grades(camis_id)
	return test_grades(restaurant_grades)

def get_all_restaurant_scores(restaurants_obj):
	'''Returns the grade of every restaurant in the dataset'''

	unique_restaurant_ids = restaurants_obj.get_unique_values('CAMIS')
	grades = 0.0
	for camis in unique_restaurant_ids:
		grades += test_restaurant_grades(restaurants_obj, camis)

	return grades

def find_scores_by_borough(restaurants_obj):
	'''Returns a dictionary with key=BOROUGH and value=SCORE of all restaurants in the borough'''

	borough_specific = restaurants_obj.groupby_column('BORO')
	unique_boroughs = restaurants_obj.get_unique_values('BORO')
	borough_scores = {}

	for boro in unique_boroughs:
		borough_data = borough_specific.get_group(boro)
		borough_obj = res.Restaurants(borough_data)
		borough_scores[boro] = get_all_restaurant_scores(borough_obj)

	return borough_scores

def get_grade_counts(year_groupby, years):
	'''Returns the grade counts for each year'''

	grade_A = []
	grade_B = []
	grade_C = []

	for year in years:
		year_data = year_groupby.get_group(year)['GRADE']
		
		try:
			grade_A.append(year_data.value_counts()['A'])
		except KeyError:
			grade_A.append(0)

		try:
			grade_B.append(year_data.value_counts()['B'])
		except KeyError:
			grade_B.append(0)

		try:
			grade_C.append(year_data.value_counts()['C'])
		except KeyError:
			grade_C.append(0)

	
	return grade_A, grade_B, grade_C

def plot_grade_improvement(restaurants_obj, plot_name):
	'''Plots the grade improvement in NYC over time (years)'''

	plt.close('all')

	years = restaurants_obj.get_unique_values('YEAR')
	years.sort()
	year_groupby = restaurants_obj.groupby_column('YEAR')

	grade_A, grade_B, grade_C = get_grade_counts(year_groupby, years)

	ax = plt.subplot(111)
	width = .3		
	padding = .1
	fontsize = 15

	# Range of the x-axis
	x_range = np.array(range(1, len(years) + 1))

	# Preparing the bars for each grade
	grade_A_bar = ax.bar(x_range - width, grade_A , width = width, color='r', align='center')
	grade_B_bar = ax.bar(x_range, grade_B, width = width, color='g', align='center')
	grade_C_bar = ax.bar(x_range + width, grade_C, width = width, color='b', align='center')

	# Set ticks
	plt.xticks([ x + width / 2 for x in  x_range],[year for year in years], ha='right')

	ax.set_xlabel('Year ', fontsize = fontsize)
	ax.set_ylabel('Number of restaurants with the corresponding grades', fontsize = fontsize)
	ax.set_title("NYC Restaurants Grade Trend Over Years", fontsize = fontsize)
	ax.autoscale(tight=True) 

	# Padding
	plt.subplots_adjust(left = 0.15, top = 0.85)
	
	#Creating Legend
	grade_A_patch = mpatches.Patch(color='r', label='Grade A')
	grade_B_patch = mpatches.Patch(color='g', label='Grade B')
	grade_C_patch = mpatches.Patch(color='b', label='Grade C')
	ax.legend([grade_A_patch, grade_B_patch, grade_C_patch],['Grade A','Grade B','Grade C'])

	plt.tight_layout()
	plt.savefig(plot_name)


def plot_grade_improvements_by_borough(restaurants_obj):
	'''Plots a graph of the trend of grades in each borough'''

	groupby_boro = restaurants_obj.groupby_column('BORO')
	boroughs = restaurants_obj.get_unique_values('BORO')

	for borough in boroughs:
		plot_grade_improvement(res.Restaurants(groupby_boro.get_group(borough)), 'grade_improvement_' + borough.lower() + ".pdf")