'''
Created on Dec 2, 2015

@author: Rafael Garcia rgc292
'''

import pandas as pd
import warnings
import numpy as np
import graph_nyc as gr
import matplotlib.pyplot as plt

'''This class is intended to handle steps to plot the graph for the restaurants' grades over 
   time given each Borough'''

class Graph(object):
    
    #It used for calling methods in the graph_nyc module
    graph_nyc = gr.Graph()
    
    #List with unique boroughs for plotting iteration 
    borough_set = list()
    
    def __init__(self):
        pass
    
    
    #Plot the bar graph having the total number of restaurants in given borough for each grade over time
    def grades_over_time_borough(self, dataset):
        frame = pd.DataFrame()
        frame = pd.DataFrame(dataset)
        self.borough_set = list(frame['BORO'].unique())
        self.borough_set.remove('Missing')
        frame = self.extract_boro_grade_gradedate(frame) 
        frame = self.graph_nyc.create_column_occurrence(frame)
        frame = self.graph_nyc.create_column_year(frame)
        frame = self.graph_nyc.drop_gradedate(frame)
        frame = self.groupby_boro_year_grade_count(frame)
        np.seterr(all='ignore')
        self.plot_bar_graph(frame)
        
    
    # Filter only the BORO, GRADE and GRADE_DATE columns from the dataset
    def extract_boro_grade_gradedate(self, frame):
        local_frame = pd.DataFrame()
        local_frame = frame
        local_frame = local_frame[['BORO', 'GRADE', 'GRADE DATE']]
        return local_frame
    
    
    #Group the data frame by three columns: BORO, YEAR, and GRADE, apply count to have the number of each specific 
    #grade by boro and year
    def groupby_boro_year_grade_count(self, frame):
        frame_local = pd.DataFrame()
        frame_local = frame
        frame_local = frame_local.groupby(by=['BORO', 'YEAR', 'GRADE']).count()
        return frame_local
    
    
    #Plot a bar graph having the Number Of Restaurants For Each Grade Over Time Given A Borough
    def plot_bar_graph(self, frame):
        warnings.filterwarnings("ignore")
        frame_local = pd.DataFrame()
        frame_local = frame 
        
        for i in self.borough_set: 
                                            
            fig = plt.figure()
            frame_local.loc[i].plot(kind='bar')
            plt.legend('', title=i, loc='best')
            plt.title('Number Of Restaurants For Each Grade Over Time Given A Borough', fontsize=11)
            plt.ylabel('Number Of Restaurants', fontsize=11)
            plt.xticks(rotation=70, fontsize='xx-small')
            plt.tight_layout()
            plt.subplots_adjust(top=.95, left=.12, right=.98 )
            plt.savefig('grade_improvement_'+i.lower()+'.pdf')
            
            plt.close('all')
            plt.clf()
        