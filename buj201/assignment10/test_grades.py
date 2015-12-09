'''
Created on Nov 30, 2015

@author: Benjamin Jakubowski (buj201)
'''
import numpy as np
import itertools
from scipy import stats

class restaurant_grades_over_time(object):
    '''
    A class that encapsulates the data and functions necessary to determine
    if a restaurant's grades have improved, declined, or not changed over time.
    Constructor takes a list of time ordered grades.
    Has methods t:
        - validate_grade_list (to ensure all grades in grade list are valid)
        - test_grades (returns 1 if improved, 0 if not changed, and -1 if declined).
    '''

    def __init__(self, grade_list):
        '''
        Constructor takes a list of grades as an argument.
        '''
        self.grade_list = grade_list
        
    def validate_grade_list(self, grade_list):
        if not isinstance(grade_list, list):
            raise TypeError("grade_list must be a list with entries 'A','B', and/or 'C'")
        if not set(grade_list).issubset(set(['A','B','C'])):
            raise ValueError("grade_list must have only the values 'A', 'B', or 'C'")
        else:
            return grade_list
    
    def test_grades(self):
        '''
        To determine if a list of restaurant grades show improvement, no change, or
        decline we'll use the following approach:
        A. If the list is only one element, return 0 (no change).
        B. If the list has only unique value (i.e. all A's, B's, or C's), return 0 (no change).
        C. Else:
            1. Convert the letter grades A, B, and C to 1, 0, and -1 respectively.
            2. Fit a linear regression model to these numeric grades (using their index as the x
            value since the list is ordered but not scaled). Store the slope as m.
            3. For every permutation of numeric_grades, calculate the slope. Store the slopes
            in a list.
            4. Find the percentile for the observed m among all the permutation slopes.
        '''
        try:
            self.validate_grade_list(self.grade_list)
        except ValueError:
            return np.NaN ## Allows us to construct dataframe with scores for all restaurants.
            
        if len(set(self.grade_list)) == 1:
            return 0
        else:
            grades_to_num ={'A':1, 'B':0, 'C':-1}
            numeric_grades = [grades_to_num[x] for x in self.grade_list]
            xs = range(len(numeric_grades))
            m = np.polyfit(xs, numeric_grades, deg=1)[0]
            permute_scores = []
            for permutation in itertools.permutations(numeric_grades):
                m_perm = np.polyfit(xs, permutation, deg=1)[0]
                permute_scores.append(m_perm)
            ## We use 'weak' to allow for small sample sizes (i.e. if we have two observations
            ## and the grades are improving, weak scoring will return 100, while strong scoring
            ## returns strictiyl less than- only 50).
            score = stats.percentileofscore(permute_scores, m, kind='weak')
            if score < 1.0/3.0*100.0:
                return -1
            elif 1.0/3.0*100.0 <= score <= 2.0/3.0*100.0:
                return 0
            elif 2.0/3.0*100.0 < score:
                return 1