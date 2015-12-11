# Author:Yichen Fan
# Date 12/8/2015
#ASS10
import numpy as np
import pandas as pd
from plot10 import *
from grade10 import *
def main():

'''This is the main program where put raw input with exceptions, Calculating overall grade for Restaurants and 
then plot figures for each boro '''

	try:
		while True:
			try:
				question = raw_input('Do you want to import NYC Restaurant Inspection Result file? YorN')#input YorN
				if question in ['Yes','yes','Y','y','yeah','Yeah']:
					data_raw = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")#input raw data
					data_raw = data_setup(data_raw)
					print '\nData has been cleaned!'

					#Question 4 Calcuates wheter restaurant has been upgraded or downgraded overtime

					print 'Calculating'
					boro_grade={} #set an empty grade
					for b in data_raw.uniqe():
						grade=0#set initial value
						boro_df=data_raw[(data_raw.BORO == boro)]
						for c in boro_df.CAMIS.uniqe():
							grade +=test_restaurant_grades(boro_df,camis)
							boro_grade[b]=grade
						boro_grade['nyc']=sum(boro_grade.values())
					print "test_restaurant_grades for each boros: \n"
					print boro_grade
					#Question 5 plots for each borogh and new york city the number of restaurants for each grade over time
					


					print 'Generating plots'#plot six graphs for question 5

					plot_figure(data_raw)
					plot_figure_by_boro(data_raw)

					print 'Plots were Saved'

					break

				elif question in ['No','no','N','n','Nope','nope']:
					sys.exit()
				else:
					raise KeyError('Error: Invalid Input')
			except KeyError:
				print "Invalid Input"
	except KeyboardInterrupt,ValueError:
		print "\n Interrupted!"
if __name__ == '__main__':
	main()

