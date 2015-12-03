'''
Created on Nov 30, 2015

@author: Benjamin Jakubowski (buj201)
'''

from test_grades import *
import pandas as pd
from scipy import stats

def save_test_restaurant_grades():
    '''For each restaurant in the cleaned data, determines whether grades are increasing, not
    changing, or decreasing. Saves and returns a dataframe with the restaurant CAMIS_ID, boro, and grade
    trend'''
    
    data = pd.read_csv('data/clean_restaurant_grades.csv',index_col=0, parse_dates=['GRADE DATE'])
    data.reset_index(inplace=True, drop=True)
    data.sort(columns='GRADE DATE', inplace=True)
    grouped = data.groupby('CAMIS')
    ##Note we'll use the most common boro (for aggregation).
    trend = grouped.agg({'GRADE':(lambda x: restaurant_grades_over_time(x).test_grades()),'BORO':(lambda x: stats.mode(x)[0])})
    trend.to_csv('data/trend_scores_by_restaurant.csv')
    return

def test_restaurant_grades(camis_id):
    '''Accepts camis_id values as input. Returns the restaurant's grade change score (1,0, or -1).
    Note this function is provided to meet the specifications in the assignment (which made it seems
    like test_restaurant_grades might be needed as public function), though it does not get called otherwise"
    '''
    if isinstance(camis_id, int):
        pass
    else:
        raise TypeError('Input camis_id must be an integer- your input was another datatype.')
    data = pd.read_csv('data/trend_scores_by_restaurant.csv',index_col=0)
    if camis_id in data.index:
        return data.loc[camis_id, 'GRADE']
    else:
        raise ValueError('Input camis_id not in cleaned restaurant grade datset.')

def sum_change_function_output():
    '''Prints (and returns) the sum of all grade change scores citywide, and by borough.
    '''
    data = pd.read_csv('data/trend_scores_by_restaurant.csv',index_col=0)
    grouped = data.groupby('BORO').agg({'GRADE': sum})
    summary = grouped.append(pd.DataFrame.from_dict({'NYC':{'GRADE':grouped.GRADE.sum()}},orient='index'))
    print summary
    return summary
