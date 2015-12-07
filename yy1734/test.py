# -*- coding: utf-8 -*-
"""
Author: Yili Yu
Date: December 7 2015 

Description: this module contains unit-testing for test_grades and data_setup functions

"""

import unittest
from unittest import TestCase
from hw10functions import *


class CommandTest(TestCase):
    
    def test_data_setup(self):
        data = data_setup()
        self.assertGreater(len(data), 10)
        self.assertEqual(list(data.columns.values), ['CAMIS', 'BORO', 'GRADE', 'DATE'])

    def test_test_grades(self):
        self.assertEqual(test_grades(['A','B','C']),-1)
        self.assertEqual(test_grades(['B','B','C']),-1)
        self.assertEqual(test_grades(['C','B','C']),0)
        self.assertEqual(test_grades(['C','B','B','C','A']),1)
        
if __name__ == '__main__':
    unittest.main()