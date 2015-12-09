# -*- coding: utf-8 -*-
"""

Author: Yili Yu
Date: December 7 2015 

Description: This file contains the functions required in Problem 3-5. 


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Perform data processing and load into dataframes.
def data_setup():
    #import data
    data = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")

    #clean data: change date format for sorting purpose later; delete missing values
    data2 = data[data['GRADE'].isin(['A','B','C'])]
    data2['DATE'] = pd.to_datetime(data2['GRADE DATE'])
    data2 = data2[data2.BORO != "Missing"]
    data3 = data2[['CAMIS','BORO','GRADE', 'DATE']]
    data3 = data3.sort('CAMIS')
    
    return data3



#The function below takes a list of grades and returns 1 if the grades are improving
# -1 if they are declining, or 0 if they have stayed the same
def test_grades(grade_list):
    begin = grade_list[0]
    end = grade_list[-1]
    diff = -(ord(end) - ord(begin))
    if diff < 0:
        grade = -1
    elif diff > 0:
        grade = 1
    else:
        grade = diff
        
    return grade
    

# Test Restaurants Grades 
def test_restaurant_grades(group) :
    group = group.sort('DATE')
    
    grade_list = list(group['GRADE'])
    final_grade = test_grades(grade_list)
    return final_grade

#Preparing Data for Graphing 
def graphing_setup(data):
    result = data.groupby(['CAMIS','BORO']).agg(test_restaurant_grades).reset_index()
    result.rename(columns={0:'Improvement'}, inplace=True)
    
    result2 = result.groupby(['BORO','Improvement']).size().reset_index()
    result3 = result.groupby('Improvement').size().reset_index()
    result3['BORO']= 'NYC'
    results = result2.append(result3)
    results.rename(columns={0:'Count'}, inplace=True)
    return results
    
#generate graphs
def plot(results):
    
    BORO_list = list(results.BORO.unique())
    
    for boro in BORO_list:
        temp = results[(results.BORO == boro)].reset_index()
        plt.clf()
        my_xticks = ['Decline','Stay the Same','Improve']
        plt.xticks(temp['Improvement'], my_xticks)
        plt.bar(temp['Improvement'],temp['Count'],width=0.4,color='b',align='center')
        plt.ylabel('Restaurants Count')
        plt.title('Grade Improvement ' + str(boro))
        plt.savefig('grade_improvement_' + str(boro)+'.pdf')

  
    


