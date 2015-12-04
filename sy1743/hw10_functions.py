import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# DS-GA 1007 HW10
# Author: Sida Ye
# Question 3 and 4


# Q3
""" 
This function shows the grade improvement of a restaurant
Logistic: I want to compare the first and last grade. Because the difference between the last grade
and first grade will indicate the improvement trend of a restaurant directly.
Since the date is sorted from nearest to farthest, if first grade is less than last grade, it mean that
the grade is declining, vice versa.
"""

def test_grades(grade_list):
    grades = {'A':3, 'B':2, 'C':1}
    n = len(grade_list)
    num_grade = [grades[g] for g in grade_list]
    if n == 1:
        return 0
    else:
        if num_grade[0] > num_grade[-1]:
                return 1
        elif num_grade[0] < num_grade[-1]:
                return -1
        else:
            return 0

# Q4 part 1

"""
This function takes data and camis id. It will return improvement with input camis id.
"""

def test_restaurant_grades(data, camis_id):
    result = test_grades(data[data['CAMIS'] == camis_id]['GRADE'])
    return result

# Q4 part 2

"""
This function prints the result of calculating the sum of overall restaurants.
"""

def print_total_trend(data):
    camis_list = data['CAMIS'].unique()
    total = 0
    for item in camis_list:
        total += test_restaurant_grades(data, item)
    print 'Summation of the trending identifiers in NYC: {}'.format(total)

"""
This function calculates sum of grade improvement for each boro.
"""
def boro_trend(data):
    boros = data['BORO'].unique()
    scores = {}
    for boro in boros:
        data_boro = data[data['BORO'] == boro]
        print 'Calculating {}...'.format(boro)
        result = 0
        for index in data_boro['CAMIS'].unique():
            result += test_restaurant_grades(data, index)
        scores[boro] = result
    return scores








