'''
Assignment 10 takes in the restaurant dataset and evaluates the grades over time
Only user related action is to make sure the dataset is in the same directory as
assignment10.py

Created on Dec 2, 2015

@author: rjw366
'''
import matplotlib.pyplot as plt
import numpy as np
from gradeHelper import gradeHelper
import sys
from collections import Counter

if __name__ == '__main__':
    try:
        #Checks to make sure the file is in correct location
        gh = gradeHelper('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
    except IOError:
        print('File was not found, exiting program')
        sys.exit(1)
    #Only user related action. If it passes no other exception handling is needed
    
    boroughs = gh.df['BORO'].unique()
    allGrades = []
    nyScore = 0
    for boro in boroughs:
        #Utilize function to calculate grades per boro
        grades_per_boro = list(map(gh.test_restaurant_grades, gh.df[gh.df['BORO'] == boro]['CAMIS'].unique()))
        unique = [-1,0,1]
        count = [0,0,0]
        sumBoroGrades=0
        if(boro != "Missing"):
            #Ignore missing boro
            #Collect the unique values and their counts and store them in order
            c = Counter(grades_per_boro)
            for uniqueVal in list(c):
                sumBoroGrades = sumBoroGrades + (c[uniqueVal]*uniqueVal)
                count[uniqueVal + 1] = c[uniqueVal]
            print("Sum of " + str(boro) + " grades: " + str(sumBoroGrades))
            #Plots
            plt.bar(np.array(unique)-.4,count)
            plt.title("Grades of " + str(boro.lower()))
            plt.savefig('grade_improvement_' + str(boro.lower()) + '.pdf')
        
        allGrades = allGrades + grades_per_boro
        nyScore = nyScore + sumBoroGrades
    
    #Do same actions but with cumulative data for NYC
    unique = [-1,0,1]
    count = [0,0,0]
    c = Counter(allGrades)
    sumBoroGrades=0
    for uniqueVal in list(c):
        count[uniqueVal + 1] = c[uniqueVal]
    print("Sum of New York grades: " + str(nyScore))
    plt.bar(np.array(unique)-.4,count)
    plt.title("Grades of New York")
    plt.savefig('grade_improvement_nyc.pdf')