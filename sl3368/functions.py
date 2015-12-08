import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from data import *

# Question 3: function used to show grades trend 

'''
Question 3: I first let A = 2, B = 1, C = 0, because by doing this, I can know how grades changed over time 
when comparing these numbers. When we have the grade list sorted in date order (for example, from 2011 - 2015), 
we can simply know the trend after calculating the difference between the first grade and the last grade(last - first).
(1): If the last grade is larger than the first grade (last - first > 0), we can say that the grade is improving.
(2): If the last grade is smaller than the first grade (last - first < 0), we can say that the grade is declining.
(3): If the last grade is equal to the first grade (last - first = 0), we can say that the grade is staying the same.
'''
def test_grades(grade_list):
 
	grade_dict = {'A': 2, 'B': 1, 'C': 0}

	change = grade_dict[grade_list[-1]] - grade_dict[grade_list[0]]

	if change > 0:

		return 1

	elif change < 0:

		return -1

	else:

		return 0 

# function used to show how grade changed for a specific restaurant.
def test_restaurant_grades(df, camis_id):

	df_camis_id = df[df['CAMIS'] == camis_id]

	sorted_df = df_camis_id.sort(['GRADE DATE'], ascending = True)

	grade_list = list(sorted_df['GRADE'])

	return test_grades(grade_list)

# Question 4 part 2
def sum_grades_NYC(df):

	camis_list = list(df['CAMIS'].unique())

	sum_grades = sum([test_restaurant_grades(df, camis_id) for camis_id in camis_list])

	return sum_grades

# Question 4 part 2
def sum_grades_BORO(df, boro):

	df_BORO = df[df['BORO'] == boro]

	camis_list = list(df_BORO['CAMIS'].unique())

	sum_grades = sum([test_restaurant_grades(df, camis_id) for camis_id in camis_list])

	return sum_grades

# Question 5(a): function used to generate and save graph
def generate_graph_NYC(df):

	df.drop_duplicates(inplace = True) # drop duplicates

	for i in ['A', 'B', 'C']:

		df_grade = df[df['GRADE'] == i]

		df_grade.groupby(by = 'GRADE DATE')['GRADE'].count().plot(label = i)

	plt.title('total number of restaurants in NYC for each grade')
	plt.legend(loc = 'best')
	plt.ylabel('number of restaurants')
	plt.savefig('grade_improvement_nyc.pdf')
	plt.close()

# Question 5(b): function used to generate and save graphs
def generate_graph_BORO(df, boro):

	df.drop_duplicates(inplace = True) # drop duplicates

	df_BORO = df[df['BORO'] == boro]

	for i in ['A', 'B', 'C']:

		df_grade = df_BORO[df_BORO['GRADE'] == i]

		df_grade.groupby(by = 'GRADE DATE')['GRADE'].count().plot(label = i)

	plt.title('total number of restaurants in {} for each grade'.format(boro))
	plt.legend(loc = 'best')
	plt.ylabel('number of restaurants')
	plt.savefig('grade_improvement_{}.pdf'.format(boro).lower())
	plt.close()


