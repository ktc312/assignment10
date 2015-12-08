'''
Created on Dec 2, 2015

@author: ams889

This module runs the main program.
'''
from functions import *
from restaurant_grades import *
import sys

if __name__ == "__main__": 
    try:
        df=dataLoad()
        df=dataClean(df)
        gradeClass=variousGrades(df)
        print('All restuarants score: ')+str(gradeClass.allGrades())
        boroughs=["MANHATTAN", "BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND"]
        for boro in boroughs:
            print(str(boro)+' restuarants score: ')+str(gradeClass.boro_grades(boro))
            gradeOverTimePlot(df, boro)
        gradeOverTimePlot(df, 'ALL')
    except KeyboardInterrupt:
        print "Program Terminated"
        sys.exit(1)