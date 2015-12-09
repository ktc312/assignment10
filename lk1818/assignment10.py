'''
author: Li Ke
NetID: lk1818
date: 12/05/2015
This is the main program for assignment 10. It loads the restaurant data, prepares it ready for use, computes the total improvements scores, and saves the bar plot of imprements scores over time.
'''

import pandas as pd
import numpy as np
from data_clean import *
from compare_and_score import *
from generate_plot import *

def main():
    try:
        data_path = './DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
        print ('\nLoading and Cleaning Data, Please Wait...\n')
        data = pd.read_csv(data_path, parse_dates=['GRADE DATE'], low_memory=False)
        data_clean = CleanData(data).clean
      
        print ('Printing question 4 restaurant improvement scores...\n')
        print_sum_score(data_clean) # Question 4 printout
 
        print ('Generating question 5 plots...\n')
        for boro in list(data_clean.BORO.unique()):
            print ('Generating restaurant improvement bar plot for ' + boro + '...\n')
            generate_plot_boro(data_clean, boro)
        print ('Generating restaurant improvement bar plot all over NYC...\n')
        generate_plot_nyc(data_clean)
        print ('All plots saved.')

    except KeyboardInterrupt, EOFError:
        print ('Something is interuptting.')
    except ArithmeticError, ZeroDivisionError:
        print ('Calculation is not executable.')
    except OverflowError:
        print ('Calculation is too large to present.')
    except IOError:
        print ('Something is wrong with I/O.')




if __name__ == '__main__':
    main()
