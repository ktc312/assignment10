'''
Created on Dec 8, 2015

@author: ds-ga-1007
'''
import pandas as pd

class Load_and_CleanData():
    
    def __init__(self):
        df1=self.load_data()
        self.cleaned_data=self.process_data(df1)
        
    def load_data(self):
        raw_data=pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv',low_memory=False)
        return raw_data
       
    def process_data(self,dataframe):
        data=dataframe[['CAMIS','BORO','GRADE','GRADE DATE']] #extrace useful data
        data.columns=['camis','boro','grade','grade_date']
        data=data[((data.grade=='A')|(data.grade=='B')|(data.grade=='C'))]
        data=data.dropna(axis=0,how='any')
        data=data.drop_duplicates()
        data['date']=pd.to_datetime(data.grade_date)
        return data
        
        
        