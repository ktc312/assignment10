import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DS-GA 1007 HW10
# Author: Sida Ye
# Question 2

"""
This class will process the raw data to what we need.
"""
class cleanData(object):

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def process_data(self):
        data = self.raw_data[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']]      # remain useful columns
        data = data[((data.GRADE == 'A') | (data.GRADE == 'B') | (data.GRADE == 'C'))]  # only consider grade A,B,C
        data = data[(data.BORO != 'Missing')]   # delete missing value
        data = data[~pd.isnull(data['GRADE DATE'])] # delete missing value
        data.drop_duplicates(inplace=True)  # drop duplicates
        return data