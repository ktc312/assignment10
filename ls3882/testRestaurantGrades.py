import unittest
from RestaurantGrades import *
import os

class TestCase(unittest.TestCase):
    '''This class will test the RestaurantGrades class.'''
    def setUp(self):
        self.r = RestaurantGrades()


    def test_init(self):
        self.r = RestaurantGrades()
        self.assertTrue(len(self.r.grades.columns) == 5)
        self.assertTrue(len(self.r.grades_counts.keys()) == 6)

    def test_test_restaurant_grades(self):
        self.r = RestaurantGrades()
        self.assertTrue(self.r.test_restaurant_grades(30075445) == 0)
        self.assertTrue(self.r.test_restaurant_grades(40363630) == 1)

    def test_grade_changes(self):
        self.r.grade_changes()
        self.assertTrue(len(self.r.boro_changes) == 5)

    def test_count_grades(self):
        self.r.count_grades()
        self.assertTrue(self.r.grades_counts['total'].isnull().values.any() == False)


if __name__ == '__main__':
    unittest.main()
