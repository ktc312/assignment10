'''
This module creates the class clean_DB which is in charge of cleaning the base inputed.
It is a subclass of a pandas Dataframe, so it inherits its properties (in first line of __init__
More details in each part of the functions
'''

__author__ = 'lqo202'
import pandas as pd


class clean_DB(pd.DataFrame):

    def __init__(self, *args, **kw):
        super(clean_DB, self).__init__(*args, **kw)

    def clean_boro(self):
        '''
        Cleans the dataframe inplace keeping valid boroughs
        '''
        valid_boro = ['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']
        self= self[self['BORO'].isin(valid_boro)]
        return  self


    def clean_grade(self):
        """
        Cleans the database inplace keeping valid grades A B or C
        """
        valid_grades = ['A', 'B', 'C']
        self= self[self['GRADE'].isin(valid_grades)]
        return  self

    def clean_dupli(self):
        """
        Cleand the dataframe inplace by eliminating duplicate rows
        """
        return self.drop_duplicates()

    def clean_na(self):
        """
        Cleans the dataframe inplace by eliminating nans (any)
        """
        return self.dropna()

    def clean_all(self):
        """
        Cleans duplicates, nans, grades and boros
        """
        return  self.clean_boro().clean_grade().clean_dupli().clean_na()

    @property
    def _constructor(self):
        """
        To assure that any object created from this class returns an object of the same class
        """
        return clean_DB