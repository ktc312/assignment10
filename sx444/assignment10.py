# Homework 10
# Siyi Xie (sx444)

"""This module is the main program. It generates the answers of homework10. """

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import grade_analysis_functions
import data_clean
import graph_plot
import sys


def generate_answers():
    try:
        raw_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv',low_memory=False) 
    except IOError:
        sys.exit()

    print "The program has got the raw data. Now it is cleaning the data... Please wait."
    raw_data_cleaning = data_clean.clean(raw_data) 
    cleaned_data = raw_data_cleaning.clean_data()

    # question 4: compute the performance of all restaurants and print the sum for different Boroughs.
           
    print "Computing the performance of all restaurants..."
    grade_analysis_functions.print_restaurant_grades_all(cleaned_data)
    print "Camputing the performance of restaurants in different boroughs..."
    grade_analysis_functions.print_restaurant_grades_by_borough(cleaned_data)


    # question 5: generate the graphs  
    print "Generating the graphs..."      
    df_whole_city = grade_analysis_functions.get_grade_count_values(cleaned_data)
    graph_plot.generate_graph(df_whole_city,'nyc')
    for boroname in cleaned_data['BORO'].unique():
        graph_plot.generate_graph(grade_analysis_functions.get_grade_count_values(cleaned_data[cleaned_data['BORO'] == boroname]),boroname.lower())
    print "The graphs have been generated. Please check the current directory. Thanks!"

if __name__ == "__main__":
    try:
        generate_answers()
    except EOFError:
        pass
    except OverflowError:
        pass       
    except TypeError:
        pass
