"""This is a program to evaluate the restaurant grades of NYC establishments across New York City."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/06/2015

import os
import sys
from dataloader import *
from dataanalyzer import *
from visualizer import *

def main():
    try:
        while True:
            try:
                print "\nLoading Data for NYC Restaurants..."
                data = loadrestaurantData()
                listofBoros = data.BORO.unique()
                print "\nAnalyzing Grade Scores over time...."
                nycrestaurantgrades = retaurantGradeAnalyzer(data, listofBoros)
                print "\nPlotting number of restaurants at given grade over time for all of NYC...."
                nycrestaurantgrades.restsbygradeovertime()
                print "\nPlotting number of restaurants at given grade over time for each Borough...."
                nycrestaurantgrades.createsingleborotoplot()
                print "\nComputing Grade Scores for each Borough, this could take a while, so grab a cup of coffee...."
                restaurant_analyzer(data)
                break
            except ValueError:
                print "\nHouston, we have a problem..."
                break
    except KeyboardInterrupt:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"

if __name__ == '__main__':
    main()
