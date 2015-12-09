#author: Michael Higgins
#netid: mch529


import numpy as np
import pandas as pd
import matplotlib as plt
import datetime
from scipy import stats

class Data():
	''' Class to hold and manipulate the data.  No argument is needed to create it
	'''

	def __init__(self):
		
		fileName ="./data/DOHMH_New_York_City_Restaurant_Inspection_Results.csv" 
		
		self.restaurantData = pd.read_csv(fileName,low_memory=False, usecols=['CAMIS','BORO', 'GRADE', 'GRADE DATE'])
		self.cleanData()



	def cleanData(self):
		'''
		responsible for cleaning the data, including removing rows with missing data and duplicated data.
		Sorted by date. 

		'''
		#drop row if GRADE is not valid
		self.restaurantData = self.restaurantData[self.restaurantData['GRADE'].isin(['A','B','C'])]

		#drop row if BORO is not valid
		self.restaurantData = self.restaurantData[self.restaurantData['BORO'].isin(['BROOKLYN','BRONX','QUEENS','MANHATTAN','STATEN ISLAND'])] 

		# drop any remaining row with missing data from any column
		self.restaurantData = self.restaurantData.dropna(how ='any' )   

		#drop data if it is repeated
		self.restaurantData = self.restaurantData.drop_duplicates()
	
		#sort by date
		self.restaurantData['GRADE DATE'] = pd.to_datetime(self.restaurantData['GRADE DATE'])
		self.restaurantData =self.restaurantData.sort(['GRADE DATE'])
		# drop year 2011 as there are only 122 data points there and in one borough
		mask = self.restaurantData['GRADE DATE'] > '2012-01-01' 
		self.restaurantData=self.restaurantData[mask]
		
		 
	
	def test_grades(self, grade_list):
		"""
		takes a list of grades, sorted in date order and returns 1 if the grades improve, -1 if they decline and 0 of they have not change
		The list is split into two sets of equalsize (if there is odd number of grades, the larger set is second)
		The average grade is computed in each of these sets where A=95, B=85, C=75 .
		If the average grade increases more than 2 points the function returns 1.  
		If the average grade decreases more than two points function returns -1. 
		If the average grade changes within 2 points the function returns 0. 
		If there is only one grade then the function returns 0.
		"""
		
		if len(set(np.asarray(grade_list)))==1 :  #if there is just one grade the grade didnt change
			return 0
	
		gradeToScore = {'A':95, 'B':85, 'C':75}

		grade_list = map(lambda x : gradeToScore[x] ,grade_list )
		firstHalf =  grade_list[:int(.5*len(grade_list))]
		secondHalf = grade_list[int(.5*len(grade_list)):]
	
		scoreDif = np.mean(secondHalf) - np.mean(firstHalf)
	
		if scoreDif>2:
			return 1
		elif scoreDif<-2:
			return -1
		else:
			return 0



	def test_restaurant_grades(self , camis_id):
		'''
		input is the restaurant id, output is 1,0, or -1 depending on whether their grades are improving, not changing or getting worse
		'''
		if isinstance(camis_id, int):
			pass
		else:
			print "try it"
			#raise TypeError('input must be integer')
		if camis_id in self.restaurantids:
			pass
		else:
			raise TypeError('Not a valid ID')
		return self.test_grades(np.asarray(self.restaurantData[self.restaurantData["CAMIS"] == camis_id]['GRADE']))
	

	def percentageOfImprovingRestaurantsByBoro(self):
		'''
		
		'''
		groupedByRestaurant = self.restaurantData.groupby("CAMIS")
		trends = groupedByRestaurant.agg({'GRADE':(lambda x:  self.test_grades(x)),'BORO':(lambda x:  stats.mode(x)[0])}) #for each rest did they improve?
		trendPerBoro=trends.groupby("BORO").agg({"GRADE" :(lambda x :x.sum() )})
		trends.groupby("BORO").agg({"GRADE" :(lambda x :x.sum() )})
		return trendPerBoro


	
	def gradesByYear(self, df):   
		'''returns dataFrame where row is year, columns are A,B, and C and values are number of grades of that type in that year.
		'''
		times = pd.DatetimeIndex(df['GRADE DATE'])  
		dataByYear = df.groupby([times.year,'GRADE']).size()  #split by year and grade 
		dataByYear = dataByYear.to_frame()
		dataByYear = dataByYear.unstack()
		dataByYear.columns = dataByYear.columns.droplevel()
		return dataByYear

	
if __name__ =='__main__':
	
	print ""
