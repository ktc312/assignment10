'''
Main program run from here.  Produces growth numbers and a normalized stacked bar chartby borough and the whole city 

author: Michael Higgins
netid: mch529

'''

import numpy as np
import pandas as pd
import matplotlib as plt
import datetime
import dataManagement
import graphs


restData=dataManagement.Data()

#4 sum of improvement  restaurants for each of the five Boroughs
print restData.percentageOfImprovingRestaurantsByBoro()

# and for all of nyc
print "all of nyc"
print restData.percentageOfImprovingRestaurantsByBoro().sum()['GRADE']


#generateGraphs for each borough
for boro in ['BROOKLYN','BRONX','QUEENS','MANHATTAN','STATEN ISLAND']:
	mask=restData.restaurantData["BORO"]==boro
	dataToGraph = restData.gradesByYear(restData.restaurantData[mask])
	graphs.graphBarChart(dataToGraph, boro)

#generate graph for the whole city
graphs.graphBarChart(restData.gradesByYear(restData.restaurantData), 'NYC')



if __name__ =='__main__':
	print ""

	

