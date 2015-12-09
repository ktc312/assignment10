import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions1 import *

class data():
    '''
    This class generates cleaned data with useful information
    '''

    def __init__(self,df):
        self.df = df

    def clean_data(self):
        '''
        Question 2
        Clean the data set
        '''
        pd.options.mode.chained_assignment = None
        clean_data1 = self.df[self.df['GRADE'] != 'Not Yet Graded']                     # get rid of 'Not Yet Graded' values from the GRADE column
        clean_data2 = clean_data1[pd.notnull(clean_data1['GRADE'])]                     # get rid of missing values from the GRADE column
        clean_data_3 = clean_data2[pd.notnull(clean_data2['GRADE DATE'])]               # get rid of missing values from the GRADE DATE column
        clean_data_no_p = clean_data_3[clean_data_3['GRADE'] != 'P']                    # get rid of value 'P' from the GRADE column since we are not using them
        clean_data_final = clean_data_no_p[clean_data_no_p['GRADE'] != 'Z']             # get rid of value 'Z' from the GRADE column since we are not using them
        clean_data_final['GRADE DATE'] = pd.to_datetime(clean_data_final['GRADE DATE']) # convert values in GRADE DATE column to datetime objects so we can sort later
        return clean_data_final.sort_values(['GRADE DATE'])                             # return results that are sorted by date
