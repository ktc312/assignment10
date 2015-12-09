__author__ = 'sb5518'


"""
This  Module contains the data_loader_and_cleaner class which loads and cleans the data required in points 1 and 2
of HW10.

"""

import pandas as pd

class data_loader_and_cleaner:
    def __init__(self, data_file):
    #The constructor executes the cleaning functions in order and creates the cleaned_df attribute of interest.
        df_1 = self.__data_loader(data_file)
        df_2 = self.__grades_and_boros_cleaner(df_1)
        self.cleaned_df = self.__column_name_and_date_cleaner(df_2)

    def __data_loader(self, data_file):
    #This function loads the data into a Dataframe
        if data_file != 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv':
            print Warning("This program was meant to analyze 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv', using another DataBase might result in undesired results")
        try:
            restaurants_df = pd.read_csv(data_file, low_memory=False)
            return restaurants_df
        except IOError:
            raise IOError("Please make sure that 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv' is in the same directory as this program")
        except TypeError as e:
            raise TypeError(str(e))

    def __grades_and_boros_cleaner(self, dataframe):
    #This function cleans NaN values, invalid grades and Missing boro.
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("The input should be a Dataframe got from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
        try:
            dataframe.dropna(axis=0, how='any', subset=['GRADE'], inplace=True)
            dataframe = dataframe[dataframe['GRADE'] != 'Not Yet Graded']
            dataframe = dataframe[dataframe['GRADE'] != 'Z']
            dataframe = dataframe[dataframe['GRADE'] != 'P']
            dataframe = dataframe[dataframe['BORO'] != 'Missing']
            return dataframe
        except LookupError as e:
            raise LookupError(str(e))


    def __column_name_and_date_cleaner(self, dataframe):
    #This function changes the names of the columns, drops the columns that are not used, transforms the 'GRADE DATE' string into pandas date/time format and returns a sorted dataframe by camis ID.
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("The input should be a Dataframe from the __grades_and_boros_cleaner function")
        try:
            simplified_df = dataframe[['CAMIS', 'GRADE DATE', 'GRADE', 'BORO']]
            simplified_df.columns = ['camis','grade_date','grade','boro']
            simplified_df['date'] = pd.to_datetime(simplified_df.grade_date)
            simplified_df.drop('grade_date', axis=1, inplace=True)
            simplified_df.dropna(axis=0, how='any', subset=['date'], inplace=True)
            return simplified_df.sort('camis')
        except LookupError as e:
            raise LookupError(str(e))

