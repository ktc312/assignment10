'''Author: Akash Shah (ass502)
This module contains the Grades class, along with its member functions.
An instance of the grades class consists of the restaurant grades that has been pre-processed
and a dataframe containing the scores for each of the restaurants, indexed by borough and camis id'''

import pandas as pd
import matplotlib.pyplot as plt
import sys
from calculate import *

class Grades(object):

	def __init__(self):
		'''creates an instance of our Grades object'''

		self.data,self.scores = self.load_and_clean_data()

	def load_and_clean_data(self):
		'''helper function that loads and cleans the data set'''

		#load data
		try:
			data = pd.read_csv("../DOHMH_New_York_City_Restaurant_Inspection_Results.csv",low_memory=False)

			#only select rows with valid grades, valid being A, B, or C
			data = data[data['GRADE'] <='C']

			#remove data with missing grade dates
			data['GRADE DATE'].fillna(0,inplace=True)
			data = data[data['GRADE DATE']!=0]

			#remove data with missing borough
			data = data[data['BORO'] != 'Missing']

			#convert grade date column to valid date format
			data['GRADE DATE'] = pd.to_datetime(data['GRADE DATE'])

			#compute grade score for each restaurant, using the helper function test_grades located in calculate.py
			scores = data.sort('GRADE DATE').groupby(['BORO','CAMIS'])['GRADE'].apply(lambda x: x.tolist()).apply(test_grades)

			return [data,scores]

		except IOError: #catch exception if the file cannot be located or read properly
			print "Could not locate/read file"
    		sys.exit()


	def test_restaurant_grades(self,camis_id):
		'''computes the score of a restaurant with the camis_id as input, by using the pre-computed scores dataframe'''

		#get the borough of the restaurant
		borough = pd.unique(self.data[self.data['CAMIS']==camis_id]['BORO'])[0]
		
		#return the score that we already computed
		return self.scores[borough][camis_id]


	def compute_borough_and_city_sums(self):
		'''computes the sum of the scores for all restaurants within each borough, and across New York City'''

		print "Grade score sums for each region:"
		#get sums of scores for the boroughs using our existing scores dataframe
		borough_sum = self.scores.sum(level='BORO')

		#keep track of the total sum across NYC as we go through each borough
		nyc_sum=0

		for borough in pd.unique(self.data['BORO'].values.ravel()): 
			print borough.title() + ": " + str(borough_sum[borough])
			nyc_sum+=borough_sum[borough]
		
		print "NYC: " + str(nyc_sum)

	def plot_grade_improvement_boroughs(self):
		'''creates a plot showing restaurant grades over time for each of the boroughs'''

		#plot for each borough
		for borough in pd.unique(self.data['BORO'].values.ravel()): 
			#filter data for current borough
			borough_data = self.data[self.data['BORO']==borough]
			#get grade counts for each grade date
			grade_counts = borough_data.groupby(['GRADE DATE','GRADE']).size()
			#convert to a dataframe by unstacking, sort by grade date
			grade_counts_df = grade_counts.unstack(level=-1).sort()

			#now we plot
			plt.clf()
			grade_counts_df.plot(kind='line')
			plt.ylabel('Number of Grades')
			plt.title('Distribution of Restaurant Grades in '+borough.title())
			#when saving figure, want lower case letters and only the first word of the borough (staten, not staten island)
			plt.savefig("grade_improvement_"+str(borough).lower().partition(' ')[0]+".pdf",format='pdf')

	def plot_grade_improvement_nyc(self):
		'''creates a plot showing restaurant grades over time for all of NYC'''

		#get grade counts for each grade date
		grade_counts = self.data.groupby(['GRADE DATE','GRADE']).size()
		#convert to a dataframe by unstacking, sort by grade date
		grade_counts_df = grade_counts.unstack(level=-1).sort()

		#plot
		plt.clf()
		grade_counts_df.plot(kind='line')
		plt.ylabel('Number of Grades')
		plt.title('Distribution of Restaurant Grades across NYC')
		plt.savefig("grade_improvement_nyc.pdf",format='pdf')
		
