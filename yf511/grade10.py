# Author:Yichen Fan
# Date 12/8/2015
#ASS10

import numpy as np
import pandas as pd

def data_setup(data_raw):#clean data to drop missing and duplicate values, get only useful features
	
	data = data_raw.dropna()
	data_clean=data[data['GRADE'].isin(['A','B','C'])]# remain useful data only with a,b or c in 'grade' since p means pending 
	data_clean.rename(columns={'GRADE DATE':'DATE'}, inplace=True)#rename grade date to date
	data_col=data_clean[['CAMIS','BORO','GRADE','DATE']]#remain four useful columns for further process
	data_frame=pd.DataFrame(data_col)#forms data frame
	cleaned_missing = data_frame[data_frame.BORO!="Missing"]#drop missing values in boro
	uniq=cleaned_missing.drop_duplicates(['DATE','CAMIS'])#drop duplicate rows that have same date and camis keep only one of it
				
	return uniq




def test_grades(grade_list):#i compare the first grade to last grade to estimate for improvements grade over time
	first = grade_list[0]
	last = grande_list[-1]
	
	if last < first:
		return -1
	elif last> first:
		return = 1
	else:
		return =0
	

def test_restaurant_grades(data_raw,camis_id):
	data_rest = data_raw[(data_raw.CAMIS==camis_id)]
	return test_grades(data_rest['GRADE'].tolist())