'''
Created on Dec 6, 2015

@author: ams889

This module contains the unit test class for assignment 10
'''
import unittest
import random
from functions import *
from userDefinedErrorHandling import *
from restaurant_grades import *

class Test(unittest.TestCase):
    #testing class for the main components of this assignment
        
    def testingClass(self):
        df=dataLoad()
        df=dataClean(df)
        classInstance1=variousGrades(df)
        #Testing valid input for variousGrades Class
        self.assertIsInstance(variousGrades(df),variousGrades)
        #Testing invalid input
        self.assertRaises(ValueError, classInstance1.test_restaurant_grades, "purple")
        self.assertRaises(CamisError, classInstance1.test_restaurant_grades, 99999999999)
        self.assertRaises(ValueError, classInstance1.boro_grades, "Not a borough")
        
    def testingFunctions(self):
        self.assertRaises(grade_listFormatError, test_grades, [])
    
if __name__ == "__main__":
    unittest.main()