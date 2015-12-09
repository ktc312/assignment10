# -*- coding: utf-8 -*-
'''
Created on Nov 26, 2015

@author: Rafael Garcia rgc292
'''

import pandas as pd
import sys

"""This class is intended to clean the dataset for initial handling"""

class Clean(object):


    def __init__(self):
        pass
    
    #Remove rows with missing values where column = GRADE
    def remove_missing_values(self, frame):
        self.frame = pd.DataFrame()
        self.frame = frame
        self.restart = False
        
        try:
            self.frame = self.frame.dropna(axis=0, how='any', subset=['GRADE'])
            
        except (KeyError, AttributeError):
            
            print 'Your dataset does not have a column called GRADE!'
            print 'The correct dataset is found using this link:'
            print "https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59"
            print 'Good bye!'
            sys.exit(1)
            
        self.frame = self.frame[self.frame.GRADE != 'Not Yet Graded']
        return self.frame
    
    # Convert Date column into datetime type
    def date_column_to_datetime(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        
        try:
            local_frame['GRADE DATE'] = pd.to_datetime(local_frame['GRADE DATE'])
        
        except (KeyError, AttributeError):
            print 'Your dataset does not have a column called GRADE!'
            print 'Try again later with an appropriate dataset.'
            print 'The correct dataset is found using this link:'
            print 'https://data.cityofnewyork.us/Health/DOHMH­New­York­City­Restaurant­Inspection­Result s/xx67­kt59'    
            print 'Good bye!'
            sys.exit(1)
        
        return local_frame
    
    
    # Create a set with unique camis number
    def create_unique_camis_set(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        camis_set = None
        
        try:
            camis_set = local_frame['CAMIS'].unique()
        
        except (KeyError, AttributeError):
            print 'Your dataset does not have a column called CAMIS!'
            print 'The correct dataset is found using this link:'
            print 'https://data.cityofnewyork.us/Health/DOHMH­New­York­City­Restaurant­Inspection­Result s/xx67­kt59'
            print 'Good bye!'
            sys.exit(1)
        
        return camis_set
    
    
    # Filter the dataset by specific CAMIS number
    def filter_by_camis(self, frame, camis):
        local_frame = pd.DataFrame()
        local_frame = frame
        local_frame = local_frame[local_frame.CAMIS == camis]
        return local_frame
    
    
    # Filter only the GRADE and GRADE_DATE columns from the dataset
    def extract_grade_gradedate(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        local_frame = local_frame[['GRADE', 'GRADE DATE']]
        return local_frame
    
    
    # Sort by GRADE_DATE column
    def sort_gradedate(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        local_frame = local_frame.sort_values('GRADE DATE')
        return local_frame
    
    
    # Create array with grades
    def create_grade_set(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        dataset_grade = []
        
        for index, row in local_frame.iterrows():
            dataset_grade.append(row['GRADE'])
        return dataset_grade
    
    
    # Create set of unique grade from dataset
    def create_unique_grade_set(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        grade_set = None
        grade_set = local_frame['GRADE'].unique()
        return grade_set
    
    # Convert grades into weighted numbers
    def convert_grade_to_number(self, dataset_grade, grade_set):
        data_grade = []
        set_grade = []
        data_grade = dataset_grade
        set_grade = grade_set
        result = []
        
        for i in range(len(set_grade)):
            for x in range(len(data_grade)):
                if set_grade[i] == data_grade[x]:
                    result.append(len(data_grade)-x)
        return result            
        
        
        
        
    
    
        
    
    
    