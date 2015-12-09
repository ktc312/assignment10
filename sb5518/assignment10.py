__author__ = 'sb5518'


"""
This program is meant to answer Homework 10 of DS-GA 1007 course and analyze data of NYC restaurants inspections.
It does not requires user input

It is structured in different modules:

* data_cleaner contains the data_loader_and_cleaner class which loads the data from
'https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59' in a Pandas DataFrame
and then executes the required cleaning process in steps. This answers questions 1 and 2.

* The grades_calculator Module contains the _test_grades(camis_id) function which is required to answer question 3.
The justification on how the actual output is calculated is inside the module.

It also contains the _test_restaurant_grades(camis_id, cleaned_df) function required in question 4. Please note that my
version of the function contains one extra argument which is the actual dataframe of interest, in order to make it
potentially reusable.

_nyc_total_restaurant_improvement and _total_restaurant_improvement_by_boro functions are functions I created to
complete the answer to question 4 and print the required output.

* aggregated_grades_generator module has two functions to compute the required agregated metrics to produce the required
graphs in question 5.

* graph_generator is the last module which contains the required function to create and save the graphs of question 5
in separate files.

* assignment10 is the module that executes all the functions in order to produce the required output of HW10.


"""

import data_cleaner as dc #Module with class to clean Data
import graph_generator as gg  #Module with function to generate graph
import aggregated_grades_generator as agg #Module with functions to calculate aggregated metrics
import grades_calculator as gc #Module with functions to calculate improvement metrics.

import warnings

warnings.filterwarnings("ignore") # This is used to avoid printing some Pandas FutureWarnings


try:
    #creates an instance of the data_loader_and_cleaner with the proper route. A cleaned DF is returned
    cleaned_df = dc.data_loader_and_cleaner('DOHMH_New_York_City_Restaurant_Inspection_Results.csv').cleaned_df

    # This function returns the total improvement for NYC required in question 4 of Assignment 10.
    # It sums the test_restaurant_grades function output of each restaurant in the city and prints it.
    gc._nyc_total_restaurant_improvement(cleaned_df)

    # This function returns the total improvement for each borough of NYC required in question 4 of Assignment 10.
    # It sums the test_restaurant_grades function output of each restaurant in each borough and prints it.
    gc._total_restaurant_improvement_by_boro(cleaned_df)

    # The following two functions aggregate the total number of distinct grades/restaurants by year and saves them in
    # two dictionaries, one for the whole city and one for each borough.
    nyc_grades_dictionary = agg._nyc_grades_by_year(cleaned_df)
    boros_grades_dictionary = agg._nyc_boros_grades_by_year(cleaned_df)

    # Next, we generate the chart of the total number of restaurants in New York City for each grade over time.
    gg.grades_by_year_graph_generator(nyc_grades_dictionary, "nyc")

    # Finally, we generate the charts of the total number of restaurants by borough for each grade over time.
    for boro in boros_grades_dictionary.keys():
        if boro == 'STATEN ISLAND':
            boro_name = 'staten' #This condition was added to produce correct filename for the Staten Island borough graph file required in problem 5
        else:
            boro_name = boro
        gg.grades_by_year_graph_generator(boros_grades_dictionary[boro], boro_name)

except LookupError as e:
    print str(e)
except TypeError as e:
    print str(e)
except IOError as e:
    print str(e)







