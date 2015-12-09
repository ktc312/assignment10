'''
Author: Shixin Li 

This is the main program that used to generate and save graphs, as well as print results. 
'''

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from data import *
from functions import *

# main function 
def main():

	print '\nGenerating results. This will take a while, so please be patient. Thank you!!\n'

	initial_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', dtype = 'unicode')
	df = data(initial_data).clean_data()

	# Question 4
	print '\nthe sum of the grades in NYC is: ' + str(sum_grades_NYC(df))

	print '\nthe sum of the grades in BRONX is: ' + str(sum_grades_BORO(df, 'BRONX'))
	print '\nthe sum of the grades in BROOKLYN is: ' + str(sum_grades_BORO(df, 'BROOKLYN'))
	print '\nthe sum of the grades in MANHATTAN is: ' + str(sum_grades_BORO(df, 'MANHATTAN'))
	print '\nthe sum of the grades in QUEENS is: ' + str(sum_grades_BORO(df, 'QUEENS'))
	print '\nthe sum of the grades in STATEN ISLAND is: ' + str(sum_grades_BORO(df, 'STATEN ISLAND'))

	# Question 5
	print '\n......Generating graphs......'

	generate_graph_NYC(df)

	generate_graph_BORO(df, 'BRONX')
	generate_graph_BORO(df, 'BROOKLYN')
	generate_graph_BORO(df, 'MANHATTAN')
	generate_graph_BORO(df, 'QUEENS')
	generate_graph_BORO(df, 'STATEN ISLAND')

	print '\ngraphs will be saved!'

if __name__ == "__main__":

	try:
		main()
	except EOFError:
		print '\n Interrupted!'
	except TypeError:
		print '\n Incorrect Types!'
	except ZeroDivisionError:
		print '\n Zero Division Error!'
	except ArithmeticError, OverflowError:
		print '\n Math Error!'
	except KeyboardInterrupt, ValueError:
		print '\n Interrupted!'
	except IOError:
		print '\n IOError!'


