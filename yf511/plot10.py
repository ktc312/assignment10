# Author:Yichen Fan
# Date 12/8/2015
#ASS10

import pandas as pd
from main10 import *
import numpy as np
import matplotlib.pyplot as plt
def plot_figure(raw_data):
	uniq_date = raw_data.groupby(['DATE','GRADE']).size().unstack()#gruped data by date and grade
	uniq_date = uniq_date.replace(np.nan, 0)#replace none to 0 since sometime there is no grade
	uniq_date.index = pd.to_datetime(uniq_date.index)#convert date and time to useful formate
	uniq_date.plot()
	plt.title('Grade for restaurant in NYC')
	plt.savefig('grade_improvement_NYC.pdf',format = 'pdf')
	plt.close

def plot_figure_by_boro(uniq):
	for boro in ['QUEENS','BRONX','MANHATTAN','BROOKLYN','STATEN ISLAND']:
		per_boro = uniq[uniq['BORO']==boro] #divided data into five regions
		boro_date=per_boro.groupby(['DATE','GRADE']).size().unstack()#grouped data by date and grade
		boro_date.index=pd.to_datetime(boro_date.index)
		boro_date.plot()
		plt.title('GRADE improvement of restaurant is' + boro)
		plt.savefig('grade_improvement_'+ boro+'.pdf',format = 'pdf')
		plt.close()



