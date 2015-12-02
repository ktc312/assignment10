'''
Created on Dec 2, 2015

@author: rjw366
'''
import unittest
from gradeHelper import gradeHelper


class Test(unittest.TestCase):

    def test_test_grades(self):
        gh = gradeHelper('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        self.assertEqual(0, gh.test_grades(['A', 'B', 'A']))
        self.assertEqual(-1, gh.test_grades(['A', 'B', 'C']))
        self.assertEqual(1, gh.test_grades(['C', 'B', 'A']))
        pass
    
    def test_test_restaurant_grades(self):
        gh = gradeHelper('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        self.assertEqual(0, gh.test_restaurant_grades(30075445))
        pass


if __name__ == "__main__":
    unittest.main()