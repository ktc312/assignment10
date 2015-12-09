"""This module loads data from a file and then does basic cleaning and preparation."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/06/2015

import os
import sys
import numpy as np
import pandas as pd


def loadrestaurantData():
    dataDirectoryPath = os.path.join(os.path.dirname(__file__), os.pardir, 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
    restaurantData = pd.read_csv(dataDirectoryPath, dtype=object)
    return prepareData(restaurantData)

def prepareData(restaurantData):
    restaurantData = restaurantData[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE']]
    restaurantData.loc[:,'GRADE DATE'] = pd.to_datetime(restaurantData.loc[:,'GRADE DATE'])
    restaurantData = restaurantData.sort_values(['GRADE DATE'])
    restaurantData.dropna(axis=0, how='any', subset=['GRADE'], inplace=True)
    restaurantData = restaurantData[restaurantData.BORO != 'Missing']
    gradevaluesremove = ['P', 'Z', 'Not Yet Graded']
    for i in gradevaluesremove:
        restaurantData = restaurantData[restaurantData.GRADE != i]
    return restaurantData
