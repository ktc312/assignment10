'''
Created on Dec 8, 2015

@author: ds-ga-1007
'''
from dataprocessing import *
from grade_sorting import *
from plot_functions import *

cleaned_data=Load_and_CleanData().cleaned_data
total_restaurants_improvement(cleaned_data)
total_restaurants_improvement_by_boro(cleaned_data)
grades_of_nyc_by_year(cleaned_data)
for boro in cleaned_data['boro'].unique():
    grades_of_Boro_by_year(cleaned_data,boro)
    






