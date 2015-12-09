# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

def grades_check(grade):
    '''
    The grade column in NYC restaurant inspection data has 6 different kinds of grades: N = Not Yet Graded, A = Grade A
    B = Grade B, C = Grade C, Z = Grade Pending, P = Grade Pending issued on re-opening following an initial inspection
    that resulted in a closure.
    The function test_grades only accepts grade_list containing 'A', 'B' and 'C', so we have to check the grade_list and
    remove invalid grades
    '''
    #print list(set(grade.GRADE)) # return unique values of grade_list, ['A', 'C', 'B', 'Not Yet Graded', 'P', 'Z']
    # remove invalid input
    grade = grade[grade.GRADE != 'Not Yet Graded']
    grade = grade[grade.GRADE != 'P']
    grade = grade[grade.GRADE != 'Z']
    return grade

def test_grades(grade_list):
    '''
    For grade_list, we only consider the first and last values. For example, grade_list = [’A’,‘B’,‘C’,‘B’,‘A’,‘A’,‘B’])
    Since 'A'<'B', return -1 for declining.
    '''
    if(len(grade_list) > 0):
        if(grade_list[0] < grade_list[-1]):
            return -1
        if(grade_list[0] > grade_list[-1]):
            return 1
        else:
            return 0

def test_restaurant_grades(grade,camis_id):
    # function returns the improvement value of a restaurant with camis_id
    grade_list = grade.loc[grade.CAMIS == camis_id]['GRADE'].values
    return test_grades(grade_list)

def figure_grades_improvement(grade_improvement,boro):
    # function creates histograms for the numbers of restaurants for each grade over time within a certain borough
    plt.hist(grade_improvement,color='b')
    plt.xlabel("Grade Improvement")
    plt.ylabel("Number of Restaurants")
    plt.title('Grade Improvement of {0}'.format(boro))
    #plt.show()
    plt.savefig('grade_improvement_{0}.pdf'.format(boro))



