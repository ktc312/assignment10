__author__ = 'ktc312'

'''test_grades takes a list of grades sorted in date order, and return 1 if the grades are improving,
-1 if they are declining, or 0 if they have stayed the same.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def test_grades(grade_list):
    """return 0
            if no changes in grades
        return 1
            if trend go up
        return -1
            if trend go down
    """

    trend = 0
    for i in range(len(grade_list)-1):
        before = grade_list[i]
        after = grade_list[i+1]
        if before == after:
            pass
        elif before == 'A': # can only go down
            trend -= 1
        elif before == 'C': # can only go up
            trend += 1
        else: # before == 'B'
            if after == 'A':
                trend += 1
            else: # after == 'C'
                trend -= 1

    if trend > 0:
        return 1
    elif trend < 0:
        return -1
    else:
        return 0


def test_restaurant_grades(camis_id, data):

    data = data[data.CAMIS == camis_id]
    data = data.sort_values(['GRADE DATE'])
    score = test_grades(data['GRADE'].tolist())
    return score

def grades_over_time(data):
    camis_id = data.CAMIS.unique()
    grade_sum = data.drop_duplicates(subset = 'CAMIS')
    grade_sum = grade_sum[['CAMIS', 'BORO']]
    grade_sum.set_index('CAMIS', inplace = True)
    grade_sum['Summary'] = np.nan
    for i in camis_id:
        summary = test_restaurant_grades(i, data)
        grade_sum.ix[i, 'Summary'] = summary
    summary_by_boro = grade_sum.groupby('BORO').sum()
    summary_NYC = grade_sum['Summary'].sum()
    print 'summary by boro:',summary_by_boro,'\n summary NYC:',summary_NYC

class GradeAnalyzer(object):
    def __init__(self, data, boro_list):
        self.data = data[['BORO','GRADE','GRADE DATE']]
        self.data['Counter'] = 1
        self.boro_list = boro_list

    def grade_over_time(self):
        over_time_data = self.data
        over_time_data_grouped = over_time_data.groupby(['GRADE DATE', 'GRADE']).size().unstack()
        over_time_data_grouped = over_time_data_grouped.resample('Q')
        over_time_data_grouped.plot(kind = 'line', by = ['GRADE DATE', 'GRADE'])
        plt.title('Grade Improvement NYC')
        plt.savefig('Grade Improvement NYC.pdf',format = 'pdf')

    def boroplot(self):
        for i in np.arange(len(self.boro_list)):
            over_time_data = self.data[self.data['BORO'] == self.boro_list[i]]
            over_time_data_grouped = over_time_data.groupby(['GRADE DATE', 'GRADE']).size().unstack()
            over_time_data_grouped = over_time_data_grouped.resample('Q')
            over_time_data_grouped.plot(kind = 'line', by = ['GRADE DATE', 'GRADE'])
            plt.title('Grade Improvement {}'.format(self.boro_list[i]))
            plt.savefig('Grade Improvement {}.pdf'.format(self.boro_list[i]), format = 'pdf')