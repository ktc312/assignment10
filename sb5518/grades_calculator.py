__author__ = 'sb5518'

"""
This  Module contains the test_grades(camis_id) function which is required to answer question 3.

* The criteria I chose in order to determine if a Restaurant has improved or not, is comparing the first Grade it had
with the last one. In my personal opinion, if the last grade is better than the first one, it is enough to determine
that the restaurant has improved, even if middle grades were worst.

* Clarification: test_restaurant_grades was slightly modified from the required description of the function in HW10 in
order to require a DataFrame as input. The purpose is to made the code as reusable as possible in case further analysis
was to be conducted


The justification on how the actual output is calculated is inside the module
"""

import pandas as pd


def test_grades(grade_list):
    if not isinstance(grade_list, list):
        raise TypeError("The input of grade_list must be a list of 'A', 'B' and 'C' strings")
    try:
        grades_dictionary = {'A':10, 'B':9, 'C':8}
        if grades_dictionary[grade_list[0]] < grades_dictionary[grade_list[-1]]:
            x = 1
        if grades_dictionary[grade_list[0]] > grades_dictionary[grade_list[-1]]:
            x = -1
        if grades_dictionary[grade_list[0]] == grades_dictionary[grade_list[-1]]:
            x = 0
        return x
    except KeyError:
        raise TypeError("The list must have only string representations of 'A', 'B' and 'C'")


def test_restaurant_grades(camis_id, cleaned_df):
    if not isinstance(camis_id, int):
        raise TypeError('camis_id must be an integer, a valid restaurant ID')
    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("Please introduce a valid cleaned DataFrame from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
    try:
        one_restaurant_df = cleaned_df[cleaned_df['camis'] == camis_id]
        one_restaurant_df = one_restaurant_df.sort('date')
        grade_list = one_restaurant_df['grade'].tolist()
        return test_grades(grade_list)
    except LookupError as e:
        raise LookupError('camis_id is not a valid id for a restaurant in the database')

def _nyc_total_restaurant_improvement (cleaned_df):  #This function was created in order to produce the required output of question 4
    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("Please introduce a valid cleaned DataFrame from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
    total_restaurants_improvement = 0
    try:
        for restaurant in cleaned_df['camis'].unique():
            improvement = test_restaurant_grades(restaurant, cleaned_df)
            total_restaurants_improvement = total_restaurants_improvement + improvement
        print 'NYC Restaurants Total improvement was ' + str(total_restaurants_improvement)
    except LookupError as e:
        raise LookupError(str(e))
    except TypeError as e:
        raise TypeError(str(e))

def _total_restaurant_improvement_by_boro(cleaned_df): #This function was created in order to produce the required output of question 4
    if not isinstance(cleaned_df, pd.DataFrame):
        raise TypeError("Please introduce a valid cleaned DataFrame from 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'")
    try:
        for boro in cleaned_df['boro'].unique():
            boro_df = cleaned_df[cleaned_df['boro'] == boro]
            total_restaurants_improvement_by_boro = 0
            for restaurant in boro_df['camis'].unique():
                improvement = test_restaurant_grades(restaurant, cleaned_df)
                total_restaurants_improvement_by_boro = total_restaurants_improvement_by_boro + improvement
            print boro + ' Total improvement was ' + str(total_restaurants_improvement_by_boro)
    except LookupError as e:
        raise LookupError(str(e))
    except TypeError as e:
        raise TypeError(str(e))