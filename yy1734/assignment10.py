# -*- coding: utf-8 -*-
"""

Author: Yili Yu
Date: December 7 2015 

Description: This is the main module from which the program is run. 
It loads the required data frames as necessary, formats them appropriately, 
and generates 6 histograms of the improvement by region into pdf files.

"""

from hw10functions import *
import sys

if __name__ == '__main__':
    print 'loading...'

    # Perform all necessary data processing and load into dataframes. 
    data = data_setup()    
    
    print 'data cleaning...'    
    # clean and format data for graphing 
    cleanData = graphing_setup(data)
    
    #generate graphs
    plot(cleanData)    
    print 'Graphs are saved'

    
