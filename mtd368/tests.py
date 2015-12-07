# test case

"""This runs tests on the program to confirm intended functionality is occur."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/06/2015

import os
import unittest
from unittest import TestCase
from dataanalyzer import *
from dataloader import *

"""test function in dataanalyzer.py"""

class unittestsforHW10(unittest.TestCase):

    def setUp(self):
        pass

    def test_test_grades(self):
        self.assertEqual(1, test_grades(['C', 'B', 'A']))
        self.assertEqual(0, test_grades(['C', 'B', 'C']))
        self.assertEqual(-1, test_grades(['A', 'B', 'B']))

    def test_loadrestaurantData(self):                     #test the data tranformer to confirm the shape is correct
        loadeddata = loadrestaurantData()
        loadeddatacolumnheaders = list(loadeddata.columns.values)
        self.assertEquals(loadeddatacolumnheaders,['CAMIS', 'BORO', 'GRADE', 'GRADE DATE'])

if __name__ == '__main__':
    unittest.main()
