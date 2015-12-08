'''
Created on Dec 5, 2015

@author: jj1745

The module where we load and process data
'''
import pandas as p

def readData():
    '''
    read in data from the main directory
    '''
    file_name = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
    try:
        df = p.read_csv(file_name)
        return df
    except IOError:
        print 'The file is not in the correct folder. Please check'

def cleanData():
    '''
    get rid of invalid grades
    '''
    df = readData()
    
    # only keep records with valid grades
    idx = df.GRADE.isin(['A','B','C'])
    df = df.loc[idx,:]
    
    # keep data with valid boro entries
    df = df[df.BORO != 'Missing']
    
    df = df[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']]
    df.columns = ['CAMIS', 'BORO', 'GRADE', 'DATE']
    df.dropna(subset = ['DATE'], inplace = True)
    df['DATE'] = p.to_datetime(df.DATE)
    
    # This is for later plots
    df['YEAR'] = [str(date).split('-')[0] for date in df['DATE']]
    
    return df
    
    
    
