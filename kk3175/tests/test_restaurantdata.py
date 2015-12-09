"""
Unit test to make sure the NYC Restaurant data was properly loaded and cleaned.

Author: kk3175
Date: 12/8/2015
Class: DSGA1007, Assignment 10
"""


import pandas as pd
from RestaurantInspectionData import RestaurantInspectionData
from unittest import TestCase

class RestaurantMasterDatasetTest(TestCase):

	# tests to make sure the master dataset	was loaded and cleaned properly via testing the shape
	def test_masterDataset(self):
		restaurantData = RestaurantInspectionData()
		dataShape = restaurantData.masterDataset.shape

		self.assertEqual(dataShape, (214272, 4))
