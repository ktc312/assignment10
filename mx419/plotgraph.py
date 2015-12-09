"""This module contains a function to plot graph to analyze the grade change over time"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#author: Muhe Xie
#netID: mx419
#date: 11/26/2015

def generate_line_graph(df_data,plot_title):
    '''this function will generate a line plot to show the change of count of the grades'''
    plt.figure(figsize = (15,10))
    plt.plot_date(df_data.index,df_data['A'],'r--',linewidth = 2, label = 'GRADE A')
    plt.plot_date(df_data.index,df_data['B'],'y--',linewidth = 2,label = 'GRADE B')
    plt.plot_date(df_data.index,df_data['C'],'k--',linewidth = 2,label = 'GRADE C')
    plt.legend(loc='best')
    plt.title('grade improvement of '+plot_title)
    if plot_title == 'staten island':
        save_file_name = 'grade_improvement_staten.pdf'
    else:
        save_file_name = 'grade_improvement_'+plot_title+'.pdf'
    plt.savefig(save_file_name)
    return  




