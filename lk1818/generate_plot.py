'''
This module contains functions to generate plots in this assignment.
'''


import pandas as pd
import matplotlib.pyplot as plt
from data_clean import *
from compare_and_score import *


def get_summary(data_clean):
    '''
    This functions is used to get a summary of the restaurant data. It returns a data frame with the counts of restaurants of each grade in each year. 
    '''
    if not isinstance(data_clean, pd.DataFrame):
        raise TypeError('Please input the restaurant data as a data frame.')
    summary = pd.DataFrame(data_clean.groupby(['YEAR','GRADE']).size().unstack())
    summary = summary.fillna(0)
    return summary
    

def generate_plot_boro(data_clean, boro):
    '''
    This function generates a bar plot of the number of restaurants in each grade from 2011 to 2015, given a boro.
    '''
    data_boro = data_clean[data_clean['BORO']==boro]
    summary = get_summary(data_boro)
    summary.plot(kind='bar')
    plt.title('Restaurant grades in ' + boro)
    plt.savefig('./grade_improvement_' + boro + '.pdf',format = 'pdf')
    plt.close()


def generate_plot_nyc(data_clean):
    '''
    This function generates a bar plot of the number of retaurants in each grade from 2011 to 2015, all over NYC.
    '''
    summary = get_summary(data_clean)
    summary.plot(kind='bar')
    plt.title('Restaurant grades in NYC')
    plt.savefig('./grade_improvement_nyc.pdf',format = 'pdf')
    plt.close()






