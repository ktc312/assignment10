import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import sys
import cleanData as cl
from cleanData import *
from hw10_functions import *
from visualize_tool import *


# DS-GA 1007
# HW10
# Author: Sida Ye
"""
This is the main program to perform all the process required by assignment 10.
It will display the results from question 4 and generate plots for question 5.
"""

# Q1
def main():
    try:
        while True:
            try:    # try to catch the invalid input and still run the program
                x = raw_input('Import data file? \nPlease enter Yes or No: \n') 
                if x in ['Yes', 'yes', 'Y', 'y']:
                    data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory=False)
                    data = cl.cleanData(data).process_data()
                    print "\nData is cleaned!"


                # Q4 part 1
                    print 'Calculating....'
                    print_total_trend(data)

                # Q4 part 2
                    result = boro_trend(data)
                    for key in result.keys():
                        print 'Summation of the trending identifiers in {} is {}'.format(key, result[key])

                # Q5
                    print 'Generating plots....'
                    
                    for area in data['BORO'].unique():
                        generate_bar_plot(data, area, False)
                    generate_bar_plot(data, area, True)

                    print 'Saved plots into figures dictory.'

                    break
             
                elif x in ['No', 'no', 'N', 'n']:
                    sys.exit()

                elif x == 'quit':
                    sys.exit()

                else:
                    raise KeyError('Error: Invalid Command!\n')

            except KeyError:
                    print "\n Invalid input! \nPlease follow input instruction.\n"
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except ArithmeticError, OverflowError:
        print "\n Math Error"
    except ZeroDivisionError:
        print "\n ZeroDivision Error"
    except TypeError:
        print "\n Type Wrong!"
    except EOFError:
            print "\n Interrupted!"

if __name__ == '__main__':
    main()


