#author: fnd212

import pandas as pd
import matplotlib.pyplot as plt

class MalformedDB(Exception):
	pass

class GraphGenerator(object):
	'''
	Class where the necessary functions to generate the plots are impelemented. 
	Class Attributes: 
		- necessary_columns: List specifying the necessary columns in the dataframe used
							to initialize the class. 
		- figures_path: Folder where to save the figures when these are generated. 
	Instance Attributes:
		- db: The database on which it performs the operations.
		- boros: Neighborhoods contained in db. 
	Public methods: 
		- plot_grades_over_time
		- generate_all_plots
	'''

	necessary_columns = ([u'CAMIS', u'BORO', u'GRADE', u'GRADE DATE'])
	figures_path = './figures/'

	def __init__(self,db):

		if not isinstance(db,pd.DataFrame):
			raise TypeError('Expecting a pandas.DataFrame object to initialize class')
		
		for self.necessary_columns in self.necessary_columns:
			if self.necessary_columns not in db.columns:
				raise ValueError('Mandatory column {} not present in db'.format(self.necessary_columns))


		#This db will be a copy and independent of the db received as argument
		self.db = db.copy()
		self.db.sort_values(by=['CAMIS','GRADE DATE'], ascending=True, inplace=True)
		
		
		self._date_to_year()
		#Keep only the last occurrence of each year for each CAMIS ID. 
		self.db.drop_duplicates(subset=['CAMIS','GRADE DATE'], keep='last', inplace=True)

		self.boros = self.db['BORO'].unique()


	def _date_to_year(self):
		'''
		Change the items in GRADE DATE column and only keep year information. 
		'''
		get_year_from_datetime = lambda date: date.year
		try:
			#Change the values on GRADE DATE column and only keep the year
			self.db['GRADE DATE'] = self.db['GRADE DATE'].map(get_year_from_datetime)
		except AttributeError:
			raise TypeError('"GRADE DATE" column must be formed by pandas.datetime objects')
		except KeyError: 
			raise MalformedDB('self.db does not contain GRADE DATE column')



	def _grade_year_count(self, database):
		'''
		Creates a pandas.DataFrame containing the number of restaurants in each class per year.
		'''
		if not isinstance(database, pd.DataFrame):
			raise TypeError('database argument must be a pandas.DataFrame object')

		grades_per_year = pd.DataFrame(columns = database.GRADE.unique(), 
										index=database['GRADE DATE'].unique())

		for grade in grades_per_year.columns:			
			for year in grades_per_year.index:
				grades_per_year[grade][year] = len(database[(database['GRADE']==grade) & (database['GRADE DATE']==year)])

		# Return the dataframe sorted by year in ascending order. 
		return grades_per_year.sort_index(ascending=True)

	def plot_grades_over_time(self, boro='NYC'):
		'''
		Receives a boro and plots the number of restaurant per category per year.
		If boro not specified uses the entire database. 
		'''

		if boro != 'NYC':
			if boro not in self.boros:
				raise ValueError('Specified boro not in self.db')
			else:
				db_boro = self.db[self.db['BORO']==boro]
		else:
			db_boro = self.db

		fig, ax = plt.subplots()

		grades_per_year = self._grade_year_count(db_boro)

		for grade in grades_per_year.columns:
			plt.plot(grades_per_year.index, grades_per_year[grade],
					label=grade, linewidth=1.5)

		ax.set_xticks(grades_per_year.index)
		ax.set_xticklabels([str(year) for year in grades_per_year.index])
		plt.legend(loc='upper left')
		plt.grid()
		plt.title('Number of restaurants per grade in {}'.format(boro))
		plt.xlabel('Year')
		plt.ylabel('Number of restaurants')

	def generate_all_plots(self, save_to='', save=False):
		'''
		Creates one plot per boro contained in self.db using GraphGenerator.plot_grades_over_time()
		If save is True, then it saves the plots in save_to
		'''
		plt.close('all')
		if not save_to:
			save_to = self.figures_path

		for boro in self.boros:
			self.plot_grades_over_time(boro)
			if save:
				try:
					plt.savefig(save_to+'grade_improvement_'+boro.split(' ')[0].lower()+'.pdf',
								 format='pdf')
					
				except IOError:
					raise IOError('Destination directory {} does not exist'.format(save_to))
			else:
				plt.show()

		self.plot_grades_over_time()
		if save:
			try:
				plt.savefig(save_to+'grade_improvement_nyc.pdf', format='pdf')
				
			except IOError:
				raise IOError('Destination directory {} does not exist'.format(save_to))
		else:
			plt.show()