import unittest
from Data_work import *

class tests(unittest.TestCase):
    def test_grade_func(self):
        self.assertEquals(0, test_grades(['A', 'A', 'A', 'A']))
        self.assertEquals(-1, test_grades(['A', 'B', 'C']))
        self.assertEquals(1, test_grades(['C', 'A', 'B']))
        self.assertEquals(0, test_grades(['A']))
        

