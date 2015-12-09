'''
Created on Nov 26, 2015

@author: Rafael Garcia rgc292
'''
import unittest
import pandas as pd
import load_data as ld
import clean_data as cd

"""This module is intended to test if methods are working as expected"""

class Test(unittest.TestCase):
    
    #Test if exception is handled when file different from .csv is loaded
    def test_load_data(self):
        self.raised = False
        self.load = ld.Load()
        self.frame = pd.DataFrame()
        
        try:
            self.frame = self.load.load_data('DOHMH_New_York_City_Restaurant_Inspection_Results.cs')

        except (IOError, SystemExit):
            self.raised = True
            self.assertFalse(self.raised == False)  
            

    #Test if exception is handled for column's name mismatch
    def test_clean_data(self):
        self.raised = False
        self.clean = cd.Clean()
        self.frame = pd.DataFrame()
        self.frame_empty = pd.DataFrame()
        
        try:
            self.frame2 = self.clean.remove_missing_values(self.frame_empty)
        
        except (KeyError, AttributeError, SystemExit):
            self.raised = True
            self.assertFalse(self.raised == False)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()