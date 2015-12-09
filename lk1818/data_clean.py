'''
This module is to import and clean the data frame needed for the graphs.
'''

import pandas as pd
import numpy as np

class CleanData(object):
    def __init__(self, data):
        self.raw = data
        self.clean = self.clean_data()
        

    def clean_data(self):
        '''
        This function takes in the restaurant data, keeps the four necessary columns, sorts the records by date, gets rid of missing values in GRADE, GRADE DATE and BORO, deletes unused grades (P, Z, Not Yet Graded), and drops duplicated records of each restaurant on the same date.  
        '''
        if not isinstance(self.raw, pd.DataFrame):
            raise TypeError('The input for clean_data function should be a data frame.')
        use_col = ['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']
        unuse_grade = ['P', 'Z', 'Not Yet Graded']
        data_clean = self.raw[use_col]
        data_clean = data_clean.sort(['GRADE DATE']) #I should've used '.sort_values' instead, but it does not work on my version of ipython.
        data_clean.dropna(axis=0, how='any', subset=['GRADE', 'GRADE DATE'], inplace=True)
        data_clean.drop(data_clean[data_clean.GRADE.isin(unuse_grade)].index, inplace=True)
        data_clean = data_clean[data_clean.BORO!='Missing']
        data_clean = data_clean.drop_duplicates()
        data_clean = data_clean.reset_index()
        data_clean['YEAR'] = 0 
        for date in data_clean['GRADE DATE']: #Create a column that stores the year of grade date
            data_clean['YEAR'][data_clean['GRADE DATE']==date] = date.year 
        return data_clean





    


