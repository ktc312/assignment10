'''
Created on Dec 5, 2015

@author: mc3784
'''

import unittest
from mc3784 import assignment10


class Test(unittest.TestCase):
    restaurants=""
    
    def loadingTest(self):
        self.restaurants = assignment10.loadRestaurant()
    
    def gradingTest(self):
        self.restaurants.test_restaurant_grades("40363093")
        self.restaurants.test_restaurant_grades("30075445")
        self.restaurants.test_restaurant_grades("50043387")
        
if __name__ == "__main__":
    unittest.main()