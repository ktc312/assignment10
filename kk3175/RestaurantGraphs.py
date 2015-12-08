'''
Module for creating a line graph representing NYC restaurant grades over time by region as specified by 
user.

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
'''


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


'''
Creates a line graph representing NYC restaurant grades over time by region.

Accepts the following arguments:
(1) Data containing the restaurant date and grade. The data must be formatted as a pandas dataframe
with the following columns (from left to right): Date, Total number of A Grades, Total number of B Grades, and Total number of C Grades.
(2) Geographical region as a string.

Saves the figure to the figures folder.
'''
def plotRestaurantGrades(data, region):
	colors = ['yellowgreen', 'magenta', 'black']
	data.plot(color = colors)
	plt.title('Restaurant Grades for %s' %region)
	plt.ylabel('Number of Restaurants')
	plt.savefig('figures/grade_improvement_%s.pdf' %region.lower())
