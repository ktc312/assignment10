'''
Created on Dec 7, 2015

@author: Xu Xu
'''
import sys
from data_loadclean import *
from gradesort import *
from visualization import *

def main():
    
    cleandata = Load_and_CleanData()
    cleandata.total_restaurants_improvement()
    cleandata.total_restaurants_improvement_by_borough()
    cleandata.grades_of_nyc_by_year()
    cleandata.grades_of_Borough_by_year(cleandata,boro)
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
