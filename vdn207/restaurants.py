'''
Varun D N - vdn207@nyu.edu
'''

'''Class definition for restaurants evaluation data'''

import pandas as pd
import re
import custom_exceptions as cexcep

class Restaurants:
	'''Class definition'''

	def __init__(self, dataframe):
		'''Constructor'''
		if not isinstance(dataframe, pd.core.frame.DataFrame):
			raise cexcep.NotADataFrameException("The data given is not a dataframe")

		temp_dataframe = self.__clean_restaurants_data(dataframe)
		self.dataframe = self.__create_year(temp_dataframe)
		self.restaurants_groupby = self.dataframe.groupby(by = 'CAMIS')

	def __clean_restaurants_data(self, dataframe):
		'''Returns the cleaned data'''

		cleaned_df = dataframe.dropna(subset = ['GRADE', 'GRADE DATE'])
		cleaned_df = cleaned_df[(cleaned_df['GRADE'] != 'P') & (cleaned_df['GRADE'] != 'Z') & (cleaned_df['GRADE'] != 'Not Yet Graded')]
		cleaned_df = cleaned_df[cleaned_df['BORO'] != 'Missing']

		return cleaned_df

	def __create_year(self, dataframe):
		'''Creates the column YEAR from the column GRADE DATE as it is not explicitly available'''

		dataframe['YEAR'] = ""
		grade_dates = dataframe['GRADE DATE'].values 
		dataframe['YEAR'] = pd.Series([re.findall('\d+$', date)[0] for date in grade_dates])
		dataframe = dataframe.dropna(subset=['YEAR'])

		return dataframe

	def get_shape(self):
		'''Returns the shape of the dataframe'''

		return self.dataframe.shape

	def get_rows(self, column_name, column_value):
		'''Gets the specific rows having the value - 'column_value' in the column - 'column_name' '''
		try:
			return self.dataframe[self.dataframe[column_name] == column_value, ]

		except KeyError as ke:
			print str(ke)

	def get_unique_values(self, column_name):
		'''Returns the unique values pertaining to the column in the dataset'''

		return self.dataframe[column_name].unique()

	def get_restaurant_grades(self, camis_id):
		'''Returns the grades pertaining to CAMIS ID'''

		return self.restaurants_groupby.get_group(camis_id)['GRADE'].values

	def groupby_column(self, column_name):
		'''Returns the groupby object pertaining to a COLUMN NAME'''

		return self.dataframe.groupby(by=column_name)
