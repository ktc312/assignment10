import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

class data():

	'''
	class used to generate cleaned data
	'''

	def __init__(self, initial_data):

		self.initial_data = initial_data 

	# function used to clean data
	def clean_data(self):

		df = self.initial_data[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']] # keep useful columns
		df = df.dropna(subset = ['GRADE', 'CAMIS', 'BORO', 'GRADE DATE'])
		df = df[df['GRADE'].isin(['A', 'B', 'C'])] # keep only grades A, B, C
		df['GRADE DATE'] = pd.to_datetime(df['GRADE DATE'])

		return df 
