"""
assignment10.py
===============

Author: Brian Karfunkel (bk1051@nyu.edu)
Date: Dec. 8, 2015

This module outputs graphs about restaurant inspection data. The data can be
downloaded from:
https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59

"""

from RestaurantDataController import RestaurantDataController

def make_plots(rdc):
    for geo in ["NYC", "Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]:
        filename = "grade_improvement_%s.pdf" % (geo.split(" ")[0].lower())
        rdc.output_graph(geography=geo, filename=filename)

def main():
    ''' Main program function '''
    rdc = RestaurantDataController(
        datafile="DOHMH_New_York_City_Restaurant_Inspection_Results.csv")

    for geo in ["NYC", "Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]:
        print "Summed grade trends for %s:" % geo
        print rdc.sum_trends_for_geography(geography=geo)

    make_plots(rdc)




if __name__ == '__main__':
    main()
