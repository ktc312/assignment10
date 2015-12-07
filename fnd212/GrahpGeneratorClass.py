import pandas as pd
import matplotlib.pyplot as plt

class GraphGenerator(object):

	necessary_columns = ([u'CAMIS', u'BORO', u'GRADE', u'GRADE DATE'])
	def __init__(self,db):
		'''

		'''
		if not isinstance(db,pd.DataFrame):
			raise TypeError('Expecting a pandas.DataFrame object to initialize class')
		
		for self.necessary_columns in self.necessary_columns:
			if self.necessary_columns not in db.columns:
				raise ValueError('Mandatory column {} not present in db'.format(self.necessary_columns))



		#This db will be a copy and independent of the db received as argument
		self.db = db.copy()
		self.db.sort_values(by=['CAMIS','GRADE DATE'],ascending=True)
		
		#Keep only the last occurrence of each year for each CAMIS ID. 
		self.db.drop_duplicates(subset=['CAMIS','GRADE DATE'], keep='last', inplace=True)

		self.grades_per_year = self.grade_year_count()

	def date_to_year(self):
		'''
		Change the items in GRADE DATE column and only keep year information. 
		'''
		get_year_from_datetime = lambda date: date.year
		try:
			#Change the values on GRADE DATE column and only keep the year
			self.db['GRADE DATE'] = self.db['GRADE DATE'].map(get_year_from_datetime)
		except AttributeError:
			raise TypeError('"GRADE DATE" column must be formed by pandas.datetime objects')


	def grade_year_count(self,boro = 'NYC'):

		grades_per_year = pd.DataFrame(columns = self.db.GRADE.unique(), 
										index=self.db['GRADE DATE'].unique())

		for grade in grades_per_year.columns:			
			for year in grades_per_year.index:
				grades_per_year[grade][year] = len(self.db[(self.db['GRADE']==grade) & (self.db['GRADE DATE']==year)])

		return grades_per_year



			



		grades_per_year = pd.DataFrame(columns = rdb.GRADE.unique(), 
										index=rdb['GRADE DATE'].unique())