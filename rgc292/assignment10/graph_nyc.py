'''
Created on Dec 2, 2015

@author: Rafael Garcia rgc292
'''

import pandas as pd
import warnings
import numpy as np
import clean_data as cd
import matplotlib.pyplot as plt

'''This class is intended to handle steps to plot the graph for restaurants' grades over time in NYC'''

class Graph(object):
    
    #It used to call the clean_data class and its method extract_grade_gradedate()
    clean_data = cd.Clean()
    
    def __init__(self):
        pass
    
    
    #Plot the bar graph having the total number of restaurants in New York City for each grade over time
    def grades_over_time_nyc(self, dataset):
        frame = pd.DataFrame()
        frame = pd.DataFrame(dataset)
        frame = self.clean_data.extract_grade_gradedate(frame)    
        frame = self.create_column_occurrence(frame)
        frame = self.create_column_year(frame)
        frame = self.drop_gradedate(frame)
        frame = self.groupby_year_grade_count(frame)
        np.seterr(all='ignore')
        self.plot_bar_graph(frame)
        
        
    #Create a column called OCURRENCE receiving value=1 for all rows as a means to count the number of
    #existent grades    
    def create_column_occurrence(self, frame):
        frame_local = pd.DataFrame()
        frame_local = frame
        frame_local['OCURRENCE'] = 1
        return frame_local
    
    
    #Create a column called YEAR as a means to keep only the year part of a date for facilitating a
    #plotting visualization after a group_by 
    def create_column_year(self, frame):
        frame_local = pd.DataFrame()
        frame_local = frame
        frame_local['YEAR'] = frame_local['GRADE DATE'].map(lambda x: x.year)
        return frame_local
    
    
    #Drop the GRADE DATE column since the YEAR column is enough for plotting
    def drop_gradedate(self, frame):
        frame_local = pd.DataFrame()
        frame_local = frame
        frame_local.drop('GRADE DATE', axis=1, inplace=True)
        return frame_local
    
    
    #Group the data frame by two columns: YEAR and GRADE, apply count to have the number of each specific 
    #grade by year
    def groupby_year_grade_count(self, frame):
        frame_local = pd.DataFrame()
        frame_local = frame
        frame_local = frame_local.groupby(by=['YEAR', 'GRADE']).count()
        return frame_local
    
    
    #Plot a bar graph having the Number Of Restaurants For Each Grade Over Time In NYC
    def plot_bar_graph(self, frame):
        warnings.filterwarnings("ignore")
        frame_local = pd.DataFrame()
        frame_local = frame
        
        try:                                   
            fig = plt.figure()
        
        except UnboundLocalError:
            pass
        
        
        frame_local.plot(kind='bar')
        plt.legend('', title='NYC', loc='best')
        plt.title('Number Of Restaurants For Each Grade Over Time In NYC', fontsize=11)
        plt.ylabel('Number Of Restaurants', fontsize=11)
        plt.xticks(rotation=70, fontsize='xx-small')
        plt.tight_layout()
        plt.subplots_adjust(top=.95, left=.12, right=.98 )
        plt.savefig('grade_improvement_nyc.pdf')
        
        plt.close('all')
        plt.clf()
        
        
    
        