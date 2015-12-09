'''
Created on Dec 5, 2015

@author: mc3784
'''

import unittest
from mc3784 import assignment10


class Test(unittest.TestCase):
    restaurants=""
    
    def testload(self):
        self.assert_(assignment10.loadRestaurant(),"")
        
    
    def testGrades(self):
        self.assertIn(assignment10.loadRestaurant().test_restaurant_grades("40363093"), [-1,1,0], "")
        
        
if __name__ == "__main__":
    unittest.main()
