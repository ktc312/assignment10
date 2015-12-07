#Author: Xing Cui
#NetID: xc918
#Data: 12/3


import pandas as pd 
import numpy as np 

"""This is a class that would be cleaning the raw data."""

class data_cleanser():

	def __init__(self, raw_loading_data):
		self.raw_loading_data = raw_loading_data

	def clean_data(self):
		data = self.raw_loading_data[['CAMIS','BORO','GRADE','GRADE DATE']]
		data = data[(data.BORO) != 'Missing']#There are 55 missing ones in this column.
		data = data[((data.GRADE == 'A')|(data.GRADE == 'B')|(data.GRADE == 'C'))]#A,B,C are only valid grades.
		data = data[pd.isnull(data['GRADE DATE']) == False]#get rid of null in this column.
		data.drop_duplicates(inplace = True)
		return data

