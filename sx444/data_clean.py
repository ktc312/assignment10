"""This module has a class to clean the raw data """

import numpy as np
import pandas as pd

class clean:
    ''' This class has the raw data and will clean it'''

    def __init__(self,origin_data):
        '''the constructor is to get the raw data'''
        self.raw_data = origin_data

    def clean_data(self):
        '''this function is to clean the data and return the cleaned data'''
        selected_data = self.raw_data[['CAMIS','BORO','GRADE','GRADE DATE']] # get the related coloums 
        selected_data_unique = selected_data.drop_duplicates() 
        selected_data_unique_valid_grade = selected_data_unique[(selected_data_unique['GRADE']=='A')|(selected_data_unique['GRADE']=='B')|(selected_data_unique['GRADE']=='C')] # get the grades
        selected_data_final = selected_data_unique_valid_grade.dropna()
        selected_data_final = selected_data_final[selected_data_final['BORO']!='Missing'] # clean the data with missing area value
        Format_Date_Df = pd.DataFrame(pd.to_datetime(selected_data_final['GRADE DATE'])) # get dataframe with time.
        Format_Date_Df.rename(columns={'GRADE DATE': 'FORMAT_DATE'}, inplace=True)
        combined_df = pd.concat([selected_data_final, Format_Date_Df], axis=1)
        
        return combined_df
