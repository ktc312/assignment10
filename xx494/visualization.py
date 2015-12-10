'''
Created on Dec 8, 2015

@author: Xu Xu
'''
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import patches

#generate the grade of restaurant in nyc
def grades_of_nyc_by_year(data):
    totaldata=data.groupby(['year','grade']).size().unstack()
    pd.DataFrame(totaldata).plot(kind='bar')
    plt.savefig('grade_improvement_NYC.pdf',format = 'pdf')
    plt.close()
    
#generate the grade of restaurant in every borough    
def grades_of_Borough_by_year(data,boro):
    data=data[data['boro']==boro]
    summary = data.groupby(['YEAR','GRADE']).size().unstack()
    pd.DataFrame(summary).plot(kind='bar')
    plt.savefig('grade_improvement_' + boro + '.pdf',format = 'pdf')
    plt.close()