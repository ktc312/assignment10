'''
Created on Dec 8, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import patches

def grades_of_nyc_by_year(data):
    summary=data.groupby(['year','grade']).size().unstack()
    pd.DataFrame(summary).plot(kind='bar')
    plt.savefig('figures/grade_improvement_NYC.pdf',format = 'pdf')
    plt.close()
    
def grades_of_Boro_by_year(data,boro):
    data=data[data['boro']==boro]
    summary = data.groupby(['YEAR','GRADE']).size().unstack()
    pd.DataFrame(summary).plot(kind='bar')
    plt.savefig('figures/grade_improvement_' + boro + '.pdf',format = 'pdf')
    plt.close()
    
    
    
    
    
    