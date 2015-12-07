from unittest import TestCase
from assignment10 import *
from GraphGeneratorClass import *
import pandas as pd
import numpy as np

DB = pd.read_csv('./DOHMH_New_York_City_Restaurant_Inspection_Results.csv', parse_dates=['GRADE DATE'])

class Assignment10Test(TestCase):       

    def setUp(self):        
        self.original_db = DB
        self.malformed_db = pd.DataFrame([1, 2, 3, 4, 5, 6])
        self.malformed_grades_list = ['A','C','Z',1]
        self.valid_grades_return_value_0 = ['A','B','A']
        self.valid_grades_return_value_1 = ['C','B','A']
        self.valid_grades_return_value_minus1 = ['A','B','B']

    def test_clean_database(self):
        #Check that no exceptions are raised when using the right DB
        clean_database(self.original_db)

        #ValueError should be raised when using a malformed DB
        with self.assertRaises(ValueError):
            clean_database(self.malformed_db)        

     
    def test_test_grades(self):

        self.assertEqual(test_grades(self.valid_grades_return_value_0),0)
        self.assertEqual(test_grades(self.valid_grades_return_value_1),1)
        self.assertEqual(test_grades(self.valid_grades_return_value_minus1),-1)

        with self.assertRaises(ValueError):
            test_grades(self.malformed_grades_list)


class GraphGeneratorClassTest(TestCase):
    def setUp(self):
        # Initialize with correct DB
        self.graph = GraphGenerator(clean_database(DB))

        self.malformed_db = pd.DataFrame([1, 2, 3, 4, 5, 6])

    def test__date_to_year(self):
        #Try to run the function when the db in the object is broken
        tmp = self.graph.db
        self.graph.db = self.malformed_db

        with self.assertRaises(MalformedDB):
            self.graph._date_to_year()

        self.graph.db = tmp
        
        with self.assertRaises(TypeError):
            #This one should fail with TypeError because the object is already initialized
            #and thus GRADE DATE items are no longer datetime objects
            self.graph._date_to_year()




