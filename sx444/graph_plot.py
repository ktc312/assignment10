"""This module has a function to plot graph to show the number of restaurants for each grade over time"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(df_data,plot_title):
    '''this function is to generate a graph that will show the number of restaurants for each grade over time'''
    plt.figure()
    plt.plot_date(df_data.index,df_data['A'],'r--',linewidth = 2, label = 'GRADE A')
    plt.plot_date(df_data.index,df_data['B'],'y--',linewidth = 2,label = 'GRADE B')
    plt.plot_date(df_data.index,df_data['C'],'k--',linewidth = 2,label = 'GRADE C')
    plt.legend()
    plt.title('grade improvement of '+ plot_title)
    if plot_title == 'staten island':
        save_file_name = 'grade_improvement_staten.pdf'
    else:
        save_file_name = 'grade_improvement_'+plot_title+'.pdf'
    plt.savefig(save_file_name)
    return  
