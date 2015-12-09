#Author: Xing Cui
#NetID: xc918
#Data: 12/3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""This is a py file that contains functions will be used. """
#Question3
def test_grades(grade_list):
	"""
	This function is going to compare grades. It will return 1 if the grade is improving, 
	0 if the grade stays the same, -1 if the grade is declining."""


	grade_dic = {'A' : 1, 'B' : 2, 'C' : 3}
	i = len(grade_list)
	number_grade = []
	for n in grade_list:
		number_grade.append(grade_dic[n])
	if i > 1:
		if number_grade[0] > number_grade[-1]:
			return 1
		if number_grade[0] < number_grade[-1]:
			return -1
		if number_grade[0] == number_grade[-1]:
			return 0
	else:
		if i == 1:
			return 0
		else:
			pass



#Question4
def test_restaurant_grades(data, camis_id):
	"""
	call function test_grades to see the performance of a restaurant, but looking at camis_id.
	"""
	#grade_list = list(data['CAMIS'])
	performance = test_grades(data[data['CAMIS'] == camis_id]['GRADE'])
	return performance

def print_result_by_camis(data):
	"""
	getting sum of all restaurant.
	"""
	camis_list = data['CAMIS'].unique()
	result1 = 0
	for j in camis_list:
		result1 += test_restaurant_grades(data, j)
	print 'Summary of the trend in New York: {}'.format(result1)

def print_result_by_boro(data):
	"""
	getting sum of improvement in grade for each boro.
	"""
	boros = data['BORO'].unique()
	mark = {}
	for boro in boros:
		boro_data = data[data['BORO'] == boro]
		result2 = 0
		for m in boro_data['CAMIS'].unique():
			result2 += test_restaurant_grades(data, m)
		mark[boro] = result2
	#return mark

	#summary_boro = print_result_by_boro(data)
	for key in mark:
		print 'Summary of the trend in {} is {}'.format(key, mark[key])







