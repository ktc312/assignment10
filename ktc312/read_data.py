__author__ = 'ktc312'

import pandas as pd



def get_data():
    data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv',
                       usecols=['CAMIS', 'BORO', 'GRADE', 'GRADE DATE'],
                       parse_dates=['GRADE DATE'])
    return data

def clean_data(data):
    ''' Grade, Boro, and Date'''

    valid_grades = ['A','B','C']
    valid_boro = ['BROOKLYN', 'BRONX', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']

    mask = data.GRADE.isin(valid_grades)
    data = data.loc[mask,:]

    mask = data.BORO.isin(valid_boro)
    data = data.loc[mask,:]

    data.dropna(axis = 0, subset = ['GRADE DATE'], inplace = True)

    return data