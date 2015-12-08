from data_cleaner import DataReader
from restaurant_grades import RestaurantGrader

__author__ = 'obr214'

"""
This program creates a score according to the grades of the restaurants in each of the 5 boroughs of NYC.
It also creates the plots for the number of grades in each borough.
"""

def main_restaurants_quality():

    try:
        data_reader = DataReader('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        inspections_df = data_reader.get_dataframe()

        restaurant_grades = RestaurantGrader(inspections_df)
        restaurant_grades.get_boroughs_scores()
        restaurant_grades.grade_improvement_plots()

    except IOError as io_message:
        print io_message
    except LookupError as lookup_message:
        print lookup_message

if __name__ == "__main__":
    try:
        main_restaurants_quality()
    except EOFError:
        pass

