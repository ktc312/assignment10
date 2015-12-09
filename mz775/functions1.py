import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data1 import *

def test_grades(grade_list):
    '''
    Question 3
    This function tests grades list and returns scores.
    Justification of my scoring system --
        Use ord() to assign score to each letter. ord('A') = 65, ord('B') = 66, ord('C') = 67,
        If the score of last letter is smaller than average of the list, it is improving
        If the score of last letter is larger than average of the list, it is declining
        If the score of last letter is the same as average of the list, it is staying the same
    '''
    score_list = map(ord,grade_list)                # convert list of letters to list of integers by mapping ord()
    if score_list[-1] == np.mean(score_list):
        return 0
    elif score_list[-1] < np.mean(score_list):
        return 1
    elif score_list[-1] > np.mean(score_list):
        return -1

def test_restaurant_grades(df,camis_id):
    '''
    Question 4
    This returns a score for a restaurant
    '''
    grade_list = df[df['CAMIS'] == camis_id]['GRADE']                   # get a list of grades of a restaurant over time
    return test_grades(grade_list)                                      # evaluate the list by test_grades function defined above

def graph_generator(df,area):
    '''
    Question 5
    This function plots graphs for each grade over time
    '''
    pd.options.mode.chained_assignment = None                       # to handle a warning
    df['YEAR'] = df.loc[:,'GRADE DATE'].dt.year                     # extract the year from GRADE DATE and build a new column for it
    df = df.drop('GRADE DATE',1)                                    # drop GRADE DATE column, since I will count the number of restaurant for each grade by year
    df.drop_duplicates(inplace = True)                              # drop duplicated rows so the number of restaurants for each grade is more accurate
    data_to_plot = df.groupby(['YEAR','GRADE']).size().unstack()    # group the data by year and grade, then count the number of each grade
    plt.figure()                                                    # plot the graph
    data_to_plot.plot(kind='bar')
    plt.title('The number of restaurants for each grade in ' + area)
    plt.savefig('grade_improvement_' + area + '.pdf',format = 'pdf')