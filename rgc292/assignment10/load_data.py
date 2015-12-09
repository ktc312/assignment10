# -*- coding: utf-8 -*-
'''
Created on Nov 26, 2015

@author: Rafael Garcia rgc292
'''

import pandas as pd
import sys

"""This class is intended to read a dataset file into the program"""

class Load(object):
    
    def __init__(self):
        pass
    
    
    #Read .csv dataset into a data frame
    def load_data(self, dataset):
        self.data = pd.DataFrame()
        self.data = dataset
        self.frame = pd.DataFrame()
        self.restart = False
        print 'Processing...'
        
        try:
            self.frame = pd.read_csv(self.data, delimiter=',', low_memory=False)
            
        except IOError:
            print 'A .csv dataset is needed!'
            print 'Check if your dataset is available.'
            print 'This link contains the dataset:'
            print "https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59"
            print 'Good bye!'
            sys.exit(1)
            
        return self.frame
    
    
    