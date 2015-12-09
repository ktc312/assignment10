#Author: Xing Cui
#NetID: xc918
#Data: 12/3



import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import data_cleanser as ds 
from data_cleanser import *
from assignment10_functions import *
from visualization import *
import sys


"""
This is the main program that will show the result of Q4 and get figures of Q5.
"""
try:
	while True:
		try:
			x = raw_input("Please enter \'Y(yes)\' to load data and see results.\nPlease enter \'N(No)\' to exit.\n")
			if x == 'y' or x == 'Y':
				data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory=False)
				data = ds.data_cleanser(data).clean_data()

				#Question4
				print_result_by_camis(data)
				print_result_by_boro(data)

				#Question5
				for neighborhood in data['BORO'].unique():
					generate_bar_plot(data, neighborhood, True)
					generate_bar_plot(data, neighborhood, False)

					print 'Figures have saved into the current dictory.'
				break
			elif x == 'n' or x == 'N':
				sys.exit()

			else:
				raise ValueError
				print 'Invalid input.'

		except ValueError:
			print 'Invalid input.'

except KeyboardInterrupt:
	print "\n Oops! Interrupted!"
except TypeError:
	print "\n Oops!Type error!"
except EOFError:
	print "\n Oops!"







