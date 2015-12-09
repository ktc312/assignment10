#autor: fnd212
#date: 12/06/15
#Homework #10 DS-GA-1007 
#
#Loads a restaurant database from New York City data and analyzes
#the grades of restaurantes over time. 

import pandas as pd
import numpy as np
import GraphGeneratorClass as gg
import sys

DB_LOCATION = './DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
# DB downloaded from https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD

def test_restaurant_grades(camis_id, db):
	'''
	Receives a database and a camis_id and returns whether that restaurant
	imrpoved or not its grades over time. 
	'''

	#First filter the db and sort by date.
	camis_db = db[db.CAMIS == camis_id].sort_values(by='GRADE DATE', ascending=True)

	return test_grades( list( camis_db[camis_db.CAMIS==camis_id].GRADE ) )

def test_grades(grade_list):
	'''
	Receives a list of grades and determine if the grade improved or not
	over time. 
	Returns: 
		- 1 if improved
		- 0 if is the same
		- -1 if is lower than at the begining
	'''
	#If the last grade is higher than the first one, there was an overall improvement in quality.
	#If is lower, there is an overall deterioration of quality
	#If both are equal, then the overall rate is the same
	#cmp(a,b) returns 1 if a>b, -1 if a<b, 0 if a==b (letter A is lower than letter B)
	valid_grades = ['A','B','C']

	try:
		tmp = grade_list[0]
	except TypeError:
		raise TypeError('grade_list argument must be an array')

	for grade in grade_list: 
		if grade not in valid_grades:
			raise ValueError('Grade list contains invalid grades')

	return cmp(grade_list[0],grade_list[-1])


def clean_database(db):
	'''
	Receives a dataframe with columns 'CAMIS', 'BORO', 'GRADE', 'GRADE DATE', removes rows with 
	missing values and rows with invalid grades in column GRADE. 
	Returns a new database.
	'''

	used_columns = [u'CAMIS', u'BORO', u'GRADE', u'GRADE DATE']

	if not isinstance(db,pd.DataFrame):
		raise TypeError('Expecting a pandas.DataFrame object to initialize class')
		
	for column in used_columns:
		if column not in db.columns:
			raise ValueError('Malformed Database: Mandatory column {} not present in db'.format(used_columns))

	unused_grades = ['Not Yet Graded', 'Z','P']
	boro_missing_values = ['Missing']

	#Make a copy of the dataframe not to change the received dataframe. Keep only the necessary columns
	clean_db = db[used_columns].copy()

	clean_db.dropna(axis=0,how='any',inplace=True)
	clean_db.drop(clean_db[clean_db.GRADE.isin(unused_grades)].index,inplace=True)
	clean_db.drop(clean_db[clean_db.BORO.isin(boro_missing_values)].index,inplace=True)

	return clean_db
     

def main():
	try: 
		restaurant_db = pd.read_csv(DB_LOCATION, parse_dates=['GRADE DATE'])
		#Use parse_dates to convert the column GRADE DATE to dtype=datetime64
	except IOError:
		print('Restaurants database not found in {}'.DB_LOCATION)
		print('Exiting program')
		#Exit program with errors.
		sys.exit(1)
	
	restaurant_db = clean_database(restaurant_db)	
	graph = gg.GraphGenerator(restaurant_db)


	try:
		graph.generate_all_plots(save=True)
	except IOError:
		print('Folder to save figures {} not found or not enough permissions to write there'.format(graph.figures_path))
		#Exit program with errors.
		sys.exit(1)


if __name__ == '__main__':
	main()




	


	






