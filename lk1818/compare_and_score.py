'''
This module contains functions that do the calculation work. 
'''


import numpy as np
import pandas as pd


def test_grades(grade_list):
    '''
    This function  takes a list of grades sorted in date order (farthest to nearest), and returns 1 if the grades are improving, -1 if they are declining, or 0 if they have stayed the same. 
    '''
    if not isinstance(grade_list, list):
        raise TypeError('The input for comparison should be a list.')
    grade_type = ['A', 'B', 'C']
    for grade in grade_list:
        if grade not in grade_type:
            raise ValueError('The list of grades should contain only valid grade - A, B, C.')
    if len(grade_list)==0:
        raise InvalidListLength() 
    '''
    The built-in cmp function comes in handy here. cmp returns -1 if the first argument is smaller than the second, 0 if the two arguments equal to each other, and 1 if the first argument is larger. Also, the cmp function takes in strings, where 'A' < 'B' < 'C'.
    '''
    result = cmp(grade_list[0], grade_list[-1]) 
    return result



def test_restaurant_grades(data_clean, camis_id):
    '''
    Takes a database and a camis_id and examines if the grade improves, declines, or stays the same over time. Returns 1 if the grades for the restaurant are improving, -1 if they are declining, or 0 if they have stayed the same.
    '''
    if (not isinstance(data_clean,pd.DataFrame)) or (not isinstance(camis_id, int)):
        raise TypeError('Please check that the inputs are one data frame and one integer.')
    if camis_id not in list(data_clean.CAMIS):
        raise ValueError('The CAMIS ID is not valid.')
    restaurant = data_clean[data_clean.CAMIS == camis_id]
    return test_grades(list(restaurant[restaurant.CAMIS==camis_id].GRADE))
   

def sum_score(data_clean):
    '''
    This function computes the sum of the function over all restaurants in the argument data frame.
    '''
    score = []
    for camis_id in list(data_clean.CAMIS.unique()):
        score.append(test_restaurant_grades(data_clean, camis_id))
    return sum(score)


def print_sum_score(data_clean):
    '''
    This function computes the sum of scores of restaurants all over NYC and in each of the five boros of NYC. It returns a data frame with six rows, each row contains a sum.
    '''
    if not isinstance(data_clean, pd.DataFrame):
        raise TypeError('Input should be a data frame.')
    index = ['All over NYC'] + list(data_clean.BORO.unique())
    sum_all = 0
    sums = {'total': [sum_all]}
    sums = pd.DataFrame(sums, index=index)
    for boro in list(data_clean.BORO.unique()):
        print 'Computing the improvement score for %s... ' % boro
        sums.loc[boro] = sum_score(data_clean[data_clean.BORO==boro]) 
        sums.loc['All over NYC'] = sums.loc['All over NYC'] + sums.loc[boro]
    print 'The sums of scores in NYC and each boros are: \n%r' % sums
        

class InvalidListLength(Exception): #Exception to be raised when the input for test_grades contains insufficient elements.
    def __str__(self):
        return 'The input for comparison cannot be empty.'
