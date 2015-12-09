'''
Created on Nov 30, 2015

@author: Benjamin Jakubowski (buj201)
'''

import pandas as pd

def get_raw_data():
    url = 'https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
    return pd.read_csv(url, usecols=['CAMIS','BORO', 'GRADE', 'GRADE DATE'],parse_dates=['GRADE DATE'])

def clean_GRADE(df):
    '''
    From NYC Open Data: allowed values of GRADE are:
        -N = Not Yet Graded
        -A = Grade A
        -B = Grade B
        -C = Grade C
        -Z = Grade pending
        -P = Grade pending issued on re-opening following
        in an initial inspection that resulted in a closure.
    Note grades N, Z, and P are essentially unlabeled, and as such can be excluded
    from our analysis.
    '''
    allowed_grades = ['A','B','C']
    mask = (df.GRADE.isin(allowed_grades))
    df = df.loc[mask,:]
    return df

def clean_BORO(df):
    allowed_boro = ['BROOKLYN', 'BRONX', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
    mask = (df.BORO.isin(allowed_boro))
    df = df.loc[mask,:]
    return df

def clean_GRADE_DATE(df):
    '''Cleans GRADE DATE column- note valid values are datetimes, and 
    invalid values are NaT (not a time). Returns all records with
    datetime entries for GRADE DATE'''
    df.dropna(axis=0, subset=['GRADE DATE'], inplace=True)
    return df

def clean_and_save_restaurant_data():
    '''Cleans a saves the restaurant grade data from NYC Open data. Saves cleaned data
    in a csv file in the 'data' directory.'''
    rest_data = get_raw_data()
    rest_data = clean_GRADE(rest_data)
    rest_data = clean_BORO(rest_data)
    rest_data = clean_GRADE_DATE(rest_data)
    rest_data.drop_duplicates(inplace=True) ##Needed since grades entered multiple times on same date
    rest_data.to_csv('data/clean_restaurant_grades.csv')
    return