"""This module is the main program. It generates the answers of homework10. """

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import grade_analysis_functions #functions to analyse the grade
import data_processing
import plotgraph
import sys

#author: Muhe Xie
#netID: mx419
#date: 11/26/2015

def start_analyse_grade():
    print "*******************************************************************"
    print "This is a program to analyse the grade of restaurants in NY. "
    print "Make sure the csv data file is placed under the current directory. "
    print "Several functions may take a bit long time, thank you for your patience."
    print "*******************************************************************"
    print "Reading the data, please wait..."
    try:
        raw_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv',low_memory=False)
    except IOError:
        print "Can not open the data file, please put the DOHMH_New_York_City_Restaurant_Inspection_Results.csv datafile under the current directory "
        sys.exit()

    print "Cleaning the data, please wait..."
    data_process_instance = data_processing.Clean_Raw_Data(raw_data) #create an instance to get the cleaned data
    cleaned_data = data_process_instance.get_cleaned_data()

    try:
        #Q4:print the results of sum of the function results(all restaurants and restaurants by borough)
        print "Calculating the score all restaurants, it takes a bit long(more than 40s in my laptop),please wait..."
        grade_analysis_functions.print_restaurant_grades_all(cleaned_data)
        print "Calculating the score of restaurants by borough,please wait..."
        grade_analysis_functions.print_restaurant_grades_by_borough(cleaned_data)
    except KeyError:
        print "KeyError happens when use grade_analysis_functions"
        command = raw_input('if you want to contiue, please enter yes, otherwise will exit the program')
        if command!= 'yes':
            sys.exit()
    #generate the plots
   # print "Generating a graph of restaurants in New York City for each grade over time"
   # df_whole_city = grade_analysis_functions.get_grade_count_values(cleaned_data)
   # plotgraph.generate_line_graph(df_whole_city,'nyc')
   # for boroname in cleaned_data[cleaned_data['BORO']!='Missing']['BORO'].unique():
    for boroname in cleaned_data['BORO'].unique():
        print "Generating the grade number satistics graph over time in "+boroname+ " ..."
        plotgraph.generate_line_graph(grade_analysis_functions.get_grade_count_values(cleaned_data[cleaned_data['BORO'] == boroname]),boroname.lower())
        
    print "Generating the grade number satistics graph over time in New York City..."
    df_whole_city = grade_analysis_functions.get_grade_count_values(cleaned_data)
    plotgraph.generate_line_graph(df_whole_city,'nyc')
    print "All the 6 graphs are generated and saved, thanks for using"





if __name__ == "__main__":
    try:
        start_analyse_grade()
    except EOFError:
        print "the program has been interrupted by EOFERROR, thanks for trying, Goodbye"

    except OverflowError:
        print "the program has been interrupted by OverflowError, thanks for trying, Goodbye"
        
    except TypeError:
        print "the program has been interrupted by TypeError, thanks for trying, Goodbye"
