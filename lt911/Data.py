# Author: Lizhen Tan
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

class Data:
    '''a class to stroe Data'''
    def __init__(self, f):
        # read in a data file can clean the data for future use
        self.df = pd.read_csv(f,low_memory=False)

    def clean(self):
        df = self.df[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']]
        df = df.dropna()
        df['GRADE DATE'] = pd.to_datetime(df['GRADE DATE'], errors = "coerce")
        df.sort_index(by = 'GRADE DATE')
        df = df.sort_index(by = 'GRADE DATE')
        df = df[df['GRADE'].isin(['A','B','C'])]
        df.drop_duplicates(inplace = True)
        self.df = df
        return self.df
        # print self.df.head() # show a few rows of the dataframe