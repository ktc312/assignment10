import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# author: Kaiwen Liu
# this class contains function to first create a dictionary with 'date' and 'count', then they will take as dataframes 
# and join them together to create a dataframe that has 4 columns 'Date' 'A' 'B' 'C', and then to plot
# the number of each grade for the given boro over time (based on the date)

class plots:

    def __init__(self, df, boro):

        self.df = df
        self.boro = boro

    def plot(self):
    
        # this is a function to plot the number of each grade for each boro over time
    
        # a  dataframe grouped by the date
        self.df_date=self.df.groupby('Date')
        # an empty dictionary
        count_date={'date':[],'count':[]}
        for date,group in self.df_date:
            dates=group.set_index('Date')
            dates=dates.ix[date]
            date_and_grade=list(dates.GRADE)
            # counter to find grades on a date
            count = Counter(date_and_grade)
            count_date['date'].append(date)
            count_date['count'].append(count)
        # take the dictionary as two dataframes
        self.df_grade=pd.DataFrame.from_dict(count_date['count'], orient='columns', dtype=None)
        self.df_date=pd.DataFrame.from_dict(count_date['date'])
        self.df_date_and_grade=self.df_date.join(self.df_grade)
        # label the columns
        self.df_date_and_grade.columns=['Date','A','B','C']
        self.df_date_and_grade=self.df_date_and_grade.set_index('Date')

        plt.figure()
        # plot with dates and counts
        plt.plot(self.df_date_and_grade.index, self.df_date_and_grade['A'],'r', linewidth=1, label = 'A')
        plt.plot(self.df_date_and_grade.index, self.df_date_and_grade['B'],'m', linewidth=1, label = 'B')
        plt.plot(self.df_date_and_grade.index, self.df_date_and_grade['C'],'b', linewidth=1, label = 'C')
        plt.title('Number of restaurants in '+ self.boro + ' for each grade')
        plt.ylabel("Number of Restaurants")
        plt.legend(loc = 2)
        plt.savefig('grade_improvement_ ' + self.boro + ' .pdf')
    