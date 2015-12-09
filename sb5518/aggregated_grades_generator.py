__author__ = 'sb5518'

import numpy as np
import pandas as pd

"""
This  Module contains the _nyc_grades_by_year(cleaned_df) and _nyc_boros_grades_by_year(cleaned_df) functions which 
purpose is to generate dictionaries of dictionaries of aggregated Data in order to produce the graphs required in 
question 5 of HW10

"""


def _nyc_grades_by_year(cleaned_df):
    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("Please introduce a valid cleaned DataFrame from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
    try:
        cleaned_df['year'] = cleaned_df.date.dt.year
        nyc_grades_dict = dict()
        for grade in cleaned_df.grade.unique():
            nyc_grades_dict[grade] = dict()
            for year in np.sort(cleaned_df.date.dt.year.unique()):
                filtered_df = cleaned_df.loc[(cleaned_df['year'] == year) & (cleaned_df['grade'] == grade)]
                nyc_grades_dict[grade][year] =filtered_df.camis.nunique()
        return nyc_grades_dict
    except LookupError as e:
        raise LookupError(str(e))

def _nyc_boros_grades_by_year(cleaned_df):
    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("Please introduce a valid cleaned DataFrame from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
    try:
        grade_dict_by_boro = dict()
        for boro in cleaned_df.boro.unique():
            grade_dict_by_boro[boro] = dict()
            df_filtered_by_boro = cleaned_df[cleaned_df.boro == boro]
            for grade in df_filtered_by_boro.grade.unique():
                grade_dict_by_boro[boro][grade] = dict()
                for year in np.sort(df_filtered_by_boro.date.dt.year.unique()):
                    filtered_df = df_filtered_by_boro.loc[(df_filtered_by_boro['year'] == year) & (df_filtered_by_boro['grade'] == grade)]
                    grade_dict_by_boro[boro][grade][year] =filtered_df.camis.nunique()
        return grade_dict_by_boro
    except LookupError as e:
        raise LookupError(str(e))
