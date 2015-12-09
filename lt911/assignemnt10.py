# Author: Lizhen Tan

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from Data import Data
from data_func import *



def program():
    '''main program for the Assignment 10'''
    
    plt.close('all')
    filename = raw_input('Please enter the filename of the restaurant_grade:\n')
    print '\n '
    print "Data procession, please wait patiently...\n"
    raw_data = Data(filename)    # create data instance
    df = raw_data.clean()       # use class method to process data into a cleaner dataframe
    print '\n '
    all_restaurant_sum(df)      # print out answer to Q4
    sum_by_boro(df)    # print out answer to Q4
    graphs(df)              # generate plots for Q5
    print "Please check the save pdf files for the corresponding graphs."


if __name__ == "__main__":
    try:
        program()
    except SingleRecordError:
        pass
    except KeyboardInterrupt:
        print "Program ends by KeyboardInterrupt"
    except IOError:
        print 'Program ends becasue data loadin fails'
        print 'Please have the dataset downloaded to your current working directory from ' \
              'https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59'




