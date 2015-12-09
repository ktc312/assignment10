'''
Created on Dec 3, 2015

@author: Benjamin Jakubowski (buj201)
'''
import unittest
import pandas as pd
from get_and_clean_data import *
from graph_grades_over_time import *
from test_grades import *

class Test(unittest.TestCase):

    def test_clean_Grade(self):
        bad_grades = pd.DataFrame.from_dict({1:{'GRADE':'A'},
                                             2:{'GRADE':'B'},
                                             3:{'GRADE':'C'},
                                             4:{'GRADE':'not_a_grade'}}, orient='index')
        self.assertIs(len(clean_GRADE(bad_grades)), 3) 
    
    def test_clean_BORO(self):
        bad_boros = pd.DataFrame.from_dict({1:{'BORO':'BROOKLYN'},
                                             2:{'BORO':'BRONX'},
                                             3:{'BORO':'MANHATTAN'},
                                             4:{'BORO':'QUEENS'},
                                             5:{'BORO':'STATEN ISLAND'},
                                             6:{'BORO':'not_a_BORO'}}, orient='index')
        self.assertIs(len(clean_BORO(bad_boros)), 5)       
                                   
    def test_plot_num_restaurants_by_grade_by_year(self):
        self.assertRaises(ValueError, plot_num_restaurants_by_grade_by_year, 'not_a_BORO')
        
    def test_restaurant_grades_over_time_class(self):
        self.assertIsInstance(restaurant_grades_over_time(['A', 'B', 'C', 'B', 'A', 'A', 'B']), restaurant_grades_over_time)   
        self.assertRaises(TypeError, restaurant_grades_over_time('a string not a list').validate_grade_list, 'a string not a list')
        self.assertRaises(ValueError, restaurant_grades_over_time(['A', 'B', 'C', 'D']).validate_grade_list, ['A', 'B', 'C', 'D'])
        
    def test_no_change(self):
        self.assertEqual(restaurant_grades_over_time(['A', 'A', 'A']).test_grades(), 0)
    
    def test_improve(self):
        self.assertEqual(restaurant_grades_over_time(['C', 'B', 'A']).test_grades(), 1)  
    
    def test_decline(self):
        self.assertEqual(restaurant_grades_over_time(['A', 'B', 'C']).test_grades(), -1)     
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()