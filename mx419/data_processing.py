"""This module contains a class which has method to clean the data """
import numpy as np
import pandas as pd

#author: Muhe Xie
#netID: mx419
#date: 11/26/2015

class Clean_Raw_Data:
    ''' This class contains the origin data and a method to clean the data'''
    def __init__(self,origin_data):
        '''the constructor will get the raw data'''
        self.raw_data = origin_data

    def get_cleaned_data(self):
        '''the method will return a cleaned dataset for analysis'''
        selected_data = self.raw_data[['CAMIS','BORO','GRADE','GRADE DATE']] #get the columns we need
        selected_data_unique = selected_data.drop_duplicates() #drop duplicates
        #get the rows with valid grades 
        selected_data_unique_valid_grade = selected_data_unique[(selected_data_unique['GRADE']=='A')|(selected_data_unique['GRADE']=='B')|(selected_data_unique['GRADE']=='C')]
        selected_data_final = selected_data_unique_valid_grade.dropna()
        #clean the data with missing boro value
        selected_data_final = selected_data_final[selected_data_final['BORO']!='Missing']
        #create a new dataframe contain the formatted time. Then concatenate the two dataframe 
        #directly add a column to the dataframe based on one existed column will cause slice warning 
        Format_Date_Df = pd.DataFrame(pd.to_datetime(selected_data_final['GRADE DATE']))
        Format_Date_Df.rename(columns={'GRADE DATE': 'FORMAT_DATE'}, inplace=True)
        combined_df = pd.concat([selected_data_final, Format_Date_Df], axis=1)
        
        return combined_df



