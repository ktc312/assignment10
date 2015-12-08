from data1 import *
from functions1 import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
    This is the main function that generates graphes and prints results
    '''
    print '\nGenerating results...\n'

    raw_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory=False)[['CAMIS','BORO','GRADE','GRADE DATE']]
    # load the data set into pandas and extract the useful columns

    sorted_data = data(raw_data).clean_data()                                              # get the cleaned data set

    id_list = list(set(sorted_data['CAMIS']))                                              # get list of unique restaurant IDs in NYC
    grade_all_city = [test_restaurant_grades(sorted_data,i) for i in id_list]              # get a list of scores of all restaurants in NYC
    # Question 4
    # print the sum of grade in NYC
    print '\n\nAnswers:'
    print '\n\nThe sum of grades of all restaurants in NYC is ' + str(np.sum(grade_all_city))
    # Question 5(a)
    # generate a graph for grades of restaurants in NYC
    graph_generator(sorted_data,'nyc')

    # Question 5(b)
    for boro in ['QUEENS', 'BRONX', 'MANHATTAN', 'BROOKLYN', 'STATEN ISLAND']:
        per_boro_data = sorted_data[sorted_data['BORO'] == boro]                            # get data for one borough
        id_list_boro = list(set(per_boro_data['CAMIS']))                                    # get list of restaurant IDs in that borough
        grade_per_boro = [test_restaurant_grades(per_boro_data,i) for i in id_list_boro]    # get the list of grades of all restaurants in that borough
        graph_generator(per_boro_data,boro.lower())                                         # generate a graph for grades of restaurants in that borough
        print '\n\nThe sum of grades of all restaurants in ' + str(boro) + ' is ' + str(np.sum(grade_per_boro))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Program terminated by keyboard interruption, please re-run the program if you would like to continue'
    except TypeError:
        print 'Incorrect types, please re-run the program if you would like to continue'
    except ValueError:
        print 'Invalid values, please re-run the program if you would like to continue'