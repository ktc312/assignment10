import unittest
from RestaurantDataController import RestaurantDataController

class RDCTestCase(unittest.TestCase):
    """Test case for RestaurantDataController"""

    @classmethod
    def setUpClass(cls):
        '''Initialize testing'''
        print "Setting up test class"
        cls.longMessage = True
        cls.rdc = RestaurantDataController(
            datafile="DOHMH_New_York_City_Restaurant_Inspection_Results.csv")

    def test_trivial_improving_grades(self):
        improving_grades = ['C', 'B', 'A']
        self.assertEqual(1, self.rdc.test_grades(improving_grades))

    def test_trivial_declining_grades(self):
        declining_grades = ['A', 'B', 'C']
        self.assertEqual(-1, self.rdc.test_grades(declining_grades))

    def test_trivial_steady_grades(self):
        steady_grades = ['B', 'B', 'B']
        self.assertEqual(0, self.rdc.test_grades(steady_grades))

    def test_single_grade_tests_steady(self):
        self.assertEqual(0, self.rdc.test_grades(['A']), "['A']")
        self.assertEqual(0, self.rdc.test_grades(['B']), "['B']")
        self.assertEqual(0, self.rdc.test_grades(['C']), "['C']")

    def test_hard_improving_grades(self):
        improving_grades1 = ['B', 'C', 'B', 'C', 'B', 'B', 'A', 'B', 'A']
        improving_grades2 = ['B', 'C', 'B', 'C', 'B', 'B', 'A', 'A', 'B']
        self.assertEqual(1, self.rdc.test_grades(improving_grades1), 'improving grades 1')
        self.assertEqual(1, self.rdc.test_grades(improving_grades2), 'improving grades 2')

    def test_hard_declining_grades(self):
        declining_grades1 = ['B', 'A', 'B', 'B', 'C', 'D', 'B', 'C']
        declining_grades2 = ['B', 'A', 'B', 'B', 'C', 'D', 'C', 'B']
        declining_grades2 = ['B', 'A', 'B', 'B', 'C', 'C', 'C', 'B']
        self.assertEqual(-1, self.rdc.test_grades(declining_grades1), 'declining grades 1')
        self.assertEqual(-1, self.rdc.test_grades(declining_grades2), 'declining grades 2')

    def test_hard_steady_grades(self):
        steady_grades1 = ['B', 'B', 'C', 'B', 'A', 'B', 'B']
        steady_grades2 = ['B', 'B', 'C', 'B', 'B', 'B', 'A']
        self.assertEqual(0, self.rdc.test_grades(steady_grades1), 'steady_grades1')
        self.assertEqual(0, self.rdc.test_grades(steady_grades2), 'steady_grades2')

    def test_restaurant_grades_for_restaurants(self):

        #print self.rdc.test_restaurant_grades('50044548')
        print self.rdc.get_restaurant_grades(50044548)
        print self.rdc.get_restaurant_grades(11111)
        print self.rdc.get_restaurant_grades('11111')
