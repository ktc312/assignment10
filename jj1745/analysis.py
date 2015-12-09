'''
Created on Dec 8, 2015

@author: jj1745

The module where we go through all restaurants in the dataset, print value and plot graphs
'''

import pandas as p
import matplotlib.pyplot as plt
from restaurant import Restaurant


def computeSumforDiffBoro(df):
    '''
    For the last part of question 4 
    '''
    all_boros = df['BORO'].unique()
    for boro in all_boros:
        # get the data of the corresponding boro
        df_boro = df[df['BORO'] == boro]
        count = 0
        all_ids = df_boro['CAMIS'].unique()
        for id in all_ids:
            r = Restaurant(id)
            count = count + r.test_restaurant_grades(df_boro)
        
        text = boro + ': the total change in restaurant grades is ' + str(count)
        print text
        

def plotTotalNum(df):
    '''
    for question 5 part a
    '''
    trend_nyc = df.groupby(['YEAR','GRADE']).size().unstack()
    p.DataFrame(trend_nyc).plot(kind = 'line')
    plt.ylabel('Number of Restaurants')
    plt.title('Restaurants in NYC with Each Grade Over Time')
    plt.savefig('grade_improvement_nyc', format = 'pdf')


def plotEachBoro(df):
    '''
    for question 5 part b
    '''
    all_boros = df['BORO'].unique()
    for boro in all_boros:
        plt.clf()
        df_boro = df[df['BORO'] == boro]
        trend_boro = df_boro.groupby(['YEAR','GRADE']).size().unstack()
        p.DataFrame(trend_boro).plot(kind = 'line')
        plt.ylabel('Number of Restaurants')
        plt.title('Restaurants in ' + boro + ' with Each Grade Over Time')
        plt.savefig('grade_improvement_' + boro.lower(), format = 'pdf')
        
    
        




