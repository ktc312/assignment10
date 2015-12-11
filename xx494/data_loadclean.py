'''
Created on Dec 8, 2015

@author: Xu Xu
'''
import pandas as pd
import sys
from gradesort import *


class Load_and_CleanData():
    
    def __init__(self):
        self.data = self.load_data()
        self.data = self.clean_data(data)
        
    def load_data(self):
        data=pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        return data
    
#clean the data in Grade column  
    def clean_data(self,data):
        data.dataframe[['CAMIS','BORO','GRADE','GRADE DATE']] 
        data.columns=['camis','boro','grade','grade_date']
        data=data[((data.grade=='A')|(data.grade=='B')|(data.grade=='C'))]
        data=data.dropna(axis=0,how='any')
        data=data.drop_duplicates()
        data['date']=pd.to_datetime(data.grade_date)
        return data