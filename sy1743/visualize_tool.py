import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hw10_functions import *


# DS-GA 1007
# HW10
# Author: Sida Ye

"""
This function is going to plots the number of restaurants 
in a boro with each grade over time and save it to 'figure' dictory
"""

def generate_bar_plot(data, boro, nyc):
    data['YEAR'] = [yr.split('/')[2] for yr in data['GRADE DATE']]
    df = data[data['YEAR'] != '2011'] # drop 2011 data, since number of restaurants in 2011 is less in this dataset
    if nyc == False:
        dfboro = df[df['BORO'] == boro]
        summary = dfboro.groupby(['YEAR','GRADE']).size().unstack()
        pd.DataFrame(summary).plot(kind='bar')
        plt.title('Grade improvement of restaurant is ' + boro)
        plt.savefig('figures/grade_improvement_' + boro + '.pdf',format = 'pdf')
        plt.close()
    elif nyc == True:
        summary = df.groupby(['YEAR','GRADE']).size().unstack()
        pd.DataFrame(summary).plot(kind='bar')
        plt.title('Grade improvement of restaurant is ' + boro)
        plt.savefig('figures/grade_improvement_NYC.pdf',format = 'pdf')
        plt.close()

    else: 
        raise KeyError('nyc is a binary input!')



