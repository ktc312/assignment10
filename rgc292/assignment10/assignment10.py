# -*- coding: utf-8 -*-
'''
Created on Nov 26, 2015

@author: Rafael Garcia rgc292
'''

"""This main module is intended to run the whole program making use of all needed modules"""

import load_data as ld
import graph_nyc as gn
import graph_borough as gb
import pandas as pd
import sys
import clean_data as cd
import tendency as td

if __name__ == '__main__':
    pass

#Variables
load_data = ld.Load() #Call instance of class within load_data module
frame = pd.DataFrame() #Instantiate a data frame variable
clean_data = cd.Clean() #Call instance of class within clean_data module
iteration = True
tendency = td.Tendency() #Call instance of class within tendency module
graph_nyc = gn.Graph() #Call instance of class within graph_nyc module
graph_borough = gb.Graph() #Call instance of class within graph_borough module
result = [] #Create array for storing the outcomes from test_restaurant_grades(camis_id)
camis_set = [] #Create an array for storing a list with unique CAMIS

try:
    #Read dataset which can be found using this link: https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59
    frame = load_data.load_data('DOHMH_New_York_City_Restaurant_Inspection_Results.csv') 

    #Remove missing values fro the dataset       
    frame = clean_data.remove_missing_values(frame)

    #Parse column DATE GRADE to datetime type
    frame = clean_data.date_column_to_datetime(frame)

    #Store the dataset for using inside clean_data class    
    tendency.frame = frame

    #Plot graph having the total number of restaurants in New York City for each grade over time
    graph_nyc.grades_over_time_nyc(frame)

    #Plot the bar graph having the total number of restaurants in given borough for each grade over time
    graph_borough.grades_over_time_borough(frame)
    
    #Create a list with unique CAMIS numbers
    camis_set = list(clean_data.create_unique_camis_set(frame))

    #Convert list of CAMIS into a data frame
    camis_set_df = pd.DataFrame(camis_set)

    #Rename column with CAMIS numbers as 'CAMIS'
    camis_set_df.columns = ['CAMIS']
    
    print 'Still processing...'
    
    #Iterates over a list of CAMIS numbers to produce an array with the improvement value for all restaurants
    for camis_id in camis_set:
        result.append(tendency.test_restaurant_grades(camis_id))
    
    print 'A few more seconds...'
       
    #Convert the array having the improvement values of all restaurants into a data frame
    result_df = pd.DataFrame(result)

    #Rename column with improvement values as 'Improvement'
    result_df.columns = ['Improvement'] 

    #Merge the improvement values data frame with CAMIS numbers data frame
    result_df = pd.merge(camis_set_df, result_df, how='inner', left_index=True, right_index=True) 
 
    #Print the improvement value in relation to all restaurants in NYC   
    print '\nThe condition of improvement over all restaurants is:'
    print tendency.tendency_over_all(result_df)

    #Print the improvement value in relation to all restaurants for each borough
    print '\nThe condition of improvement over restaurants per borough is:'
    print tendency.tendency_over_borough(result_df)  

    print '\nEnded!'
    
except (KeyboardInterrupt, EOFError, SystemExit):
    print 'Good Bye'
    sys.exit(1)      
   
    
       

    

