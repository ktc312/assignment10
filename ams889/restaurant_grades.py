'''
Created on Dec 2, 2015

@author: ams889

This module contains the class used to generate the restaurant grades
for a given CAMIS sorted by date ascending
'''
import numpy as np
from userDefinedErrorHandling import *
from functions import *

class variousGrades(object):
    '''
    This class contains logic to sort df and return to list of a restaurants
    grades in ascending date (earliest is first entry and latest is the last entry)
    This will allow us to simply feed the returned data into our test_grades function
    '''    
    def __init__(self, data):
        self.data=data
    
    def test_restaurant_grades(self, camis_id):
        '''
        This function generates a grade list for a given camis
        ID and then runs the test_grades function to calculate
        if the scores improve, worsen or remain stable
        '''
        try: 
            camis_id = int(camis_id)
        except:
            raise ValueError('CAMIS ID must be in numeric format.')
        data = self.data[self.data['CAMIS']==camis_id]
        sorteddf = data.sort(['GRADE DATE'], ascending=1)
        gradeList=sorteddf["GRADE"]
        gradeList=gradeList.tolist()
        if len(gradeList)<1:
            raise CamisError('CAMIS ID cannot be found.')
        else:
            return test_grades(gradeList)
    
    def boro_grades(self, boro_id):
        '''
        This function generates a camid ID list for a given Boro
        and then runs the test_restaurant_grades function to calculate
        the grade lists for all camis IDs within a given boro and their
        test grades results
        '''
        if boro_id in ['MANHATTAN', 'BRONX', 'QUEENS', 'BROOKLYN', 'STATEN ISLAND']:
            data = self.data[self.data['BORO']==boro_id]
            camisBoro=data["CAMIS"]
            camisBoro=camisBoro.drop_duplicates()
            print("Calculating "+boro_id+" Score...")
            boroGrades=[]
            for camisID in camisBoro:
                grade=self.test_restaurant_grades(camisID)
                boroGrades.append(grade)
            return np.sum(boroGrades)
        else:
            raise ValueError("Invalid borough value")
      
    def allGrades(self):
        '''
        This function uses a full list of all Camis IDs in the data
        and then runs the test_restaurant_grades function to calculate
        the grade lists for all camis IDs and their test grades results
        '''    
        data = self.data
        camisAll=data["CAMIS"]
        camisAll=camisAll.drop_duplicates()
        allGrades=[]
        print("Calculating NYC Score...")
        for camisID in camisAll:
            grade=self.test_restaurant_grades(camisID)
            allGrades.append(grade)
        return np.sum(allGrades)
    