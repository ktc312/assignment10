import pandas as pd

__author__ = 'obr214'

"""
DataReader Class
It reads a file, creates a dataframe and clean it according to the values needed.
"""

class DataReader:

    def __init__(self, file_name):
        try:
            self.dataframe = pd.read_csv(file_name, usecols=['CAMIS', 'BORO', 'GRADE', 'GRADE DATE'])
            self.clean_dataframe()
        except IOError:
            raise IOError('File Not Founded')
        except LookupError:
            raise LookupError('Columns Not Found in the File')

    def clean_dataframe(self):
        """"
        Cleans the dataframe.
        Deletes the NA values, drop the duplicates.
        Deletes the Invalid Grades (Z, P and Not Yet Graded
        Deletes the Invalid BORO 'Missing'
        """
        try:
            self.dataframe = self.dataframe.dropna()
            self.dataframe = self.dataframe.drop_duplicates()
            self.dataframe['GRADE DATE'] = pd.to_datetime(self.dataframe['GRADE DATE'])

            idx_grades = self.dataframe['GRADE'].isin(['Z', 'P', 'Not Yet Graded'])
            self.dataframe = self.dataframe[~idx_grades]

            idx_boro = self.dataframe['BORO'].isin(['Missing'])
            self.dataframe = self.dataframe[~idx_boro]
        except LookupError:
            raise LookupError('Column Not Found in the Dataframe')

    def get_dataframe(self):
        #Returns the cleaned dataframe
        return self.dataframe
