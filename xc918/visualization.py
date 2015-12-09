#Author: Xing Cui
#NetID: xc918
#Data: 12/3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from assignment10_functions import *


def generate_bar_plot(data, boro, NYC):

	"""
	This function is going to plot the number of restaurants in a boro 
	with each grade overtime and save it to current dictory.
	"""
	year_list = []
	for yr in data['GRADE DATE']:
		year_list.append(yr.split('/')[2])
	data['YEAR'] = year_list
	if NYC == True:
		#run for restaurants in NYC takes time. Separate it from others can get other boros done first.
		summary = data.groupby(['YEAR', 'GRADE']).size().unstack()
		pd.DataFrame(summary).plot(kind = 'bar')
		plt.title('Grade improvement of restaurant is ' + boro)
		plt.savefig('grade_improvement_NYC.pdf',format = 'pdf')
		plt.close()
	elif NYC == False:
		boro_df = data[data['BORO'] == boro]
		summary = boro_df.groupby(['YEAR','GRADE']).size().unstack()
		pd.DataFrame(summary).plot(kind = 'bar')
		plt.title('Grade improvement of restaurants is ' + boro)
		plt.savefig('grade_improvement_' + boro + '.pdf',format = 'pdf')
		plt.close()

	else:
		raise KeyError
		print 'NYC here is boolean.'





