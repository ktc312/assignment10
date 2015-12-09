'''
Created on Dec 8, 2015

@author: jj1745
'''
import unittest
from restaurant import Restaurant

class Test(unittest.TestCase):
    '''
    test the test_grades funciton in the Restaurant class
    '''

    def testFunction(self):
        r = Restaurant('sample')
        
        self.assertEqual(-1, r.test_grades(['A','B']))
        
        self.assertEqual(1, r.test_grades(['C','B','B']))
        
        self.assertEqual(0, r.test_grades(['A']))
        
        self.assertEqual(0, r.test_grades(['C','B','C']))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()