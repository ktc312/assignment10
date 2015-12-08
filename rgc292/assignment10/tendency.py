'''
Created on Nov 30, 2015

@author: Rafael Garcia rgc292
'''

import numpy as np
import pandas as pd
import clean_data as cd

'''This class is intended to evaluate the tendency of a list of grades as
    improving, declining, or the same'''

class Tendency(object):
    
    #It is used for calling methods from clean_data's module  
    clean_data = cd.Clean()
    
    # It gives easy access to the dataset by the methods
    frame = pd.DataFrame()

    def __init__(self):
        pass
    
    
    #Test the ordered by date grades of a given restaurant evaluating if they are improving, decreasing, or 
    #stable over time 
    def test_restaurant_grades(self, camis_id):
        dataset_grade = self.clean_data.create_unique_grade_set(self.frame)
        new_frame = self.clean_data.filter_by_camis(self.frame, camis_id)
        new_frame = self.clean_data.extract_grade_gradedate(new_frame)
        new_frame = self.clean_data.sort_gradedate(new_frame)
        grade_set = self.clean_data.create_grade_set(new_frame)
        grade_list = self.clean_data.convert_grade_to_number(dataset_grade, grade_set)
        tendency = self.test_grades(grade_list)
        return tendency
    
    
    #Test the grades of a given list evaluating if they are improving, decreasing, or 
    #stable over time 
    def test_grades(self, grade_list):
        """Justification is in results.txt"""
        grade_set = []
        tendency = 0
        grade_set = grade_list
        tendency = np.diff(grade_set)
        increase = sum(tendency) > 0
        decrease = sum(tendency) < 0
        
        if increase == True and decrease == False:
            tendency = 1
        elif increase == False and decrease == True:
            tendency = -1
        elif increase == False and decrease == False:
            tendency = 0
            
        return tendency
    
    
    #Test the grades of restaurants in a given borough evaluating if they are improving, decreasing, or 
    #stable over time
    def tendency_over_borough(self, result_df):
        frame = pd.DataFrame()
        frame = self.frame
        result = pd.DataFrame()
        result = result_df
        borough = list(frame['BORO'].unique())
        borough.remove('Missing')
        borough_value = 0
        borough_improvement = {}
        frame = frame.drop_duplicates('CAMIS')
        frame = pd.merge(frame, result, left_on='CAMIS', right_on='CAMIS', how='inner')
        
        for i in borough:
            borough_value = frame.loc[frame['BORO'] == i, 'Improvement'].sum()
            
            if borough_value > 0:
                borough_value = 1
                
            elif borough_value < 0:
                borough_value = -1
                
            else:
                borough_value = 0
                            
            borough_improvement.update({i: borough_value})
            
        return borough_improvement
    
    
    #Test the grades of restaurants in NYC evaluating if they are improving, decreasing, or 
    #stable over time
    def tendency_over_all(self, result_df):
        result = pd.DataFrame()
        result = result_df
        total = sum(result.Improvement)
        
        if total > 0:
            return 1
        elif total < 0:
            return -1
        else:
            return 0

        
        
        
        
        
        
        
    
    
    
    
        