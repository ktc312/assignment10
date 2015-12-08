# Author: Lizhen Tan

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

'''required functions for main program'''

def test_grades(grade_list):
    # take a grade_list as input, assign numeric values to the letter grades (i.e. A = 5,
    # B = 3, C = 1), then fit a linear line to the data, find the slope by using the scipy.stats.linregress package,
    # if slope < 0,then grades are declinin (return -1); if slope > 0, then grades are imporoving (return 1);
    # if slope = 0, then grades stay the same (return 0)
    grades = {'A' : 5, 'B' : 3, 'C': 1}
    numeric_grade = [grades[i] for i in grade_list]
    x = np.arange(len(numeric_grade))    # create x-coordinates
    slope, intercept = stats.linregress(x, numeric_grade)[:2]
    if slope > 0:
        return 1
    elif slope < 0:
        return -1
    elif slope == 0:
        return 0

class SingleRecordError(Exception):
    # error raises when there is only one record for a camis ID
    def __str__(self):
        pass

def test_restaurant_grades(data, camis_id):
    # taking the camis_id as input and get the grade list for the camis_id
    # then return the test for restaurant by using the test_grades function
    grade_list = data['GRADE'][data['CAMIS'] == camis_id]
    if len(grade_list) > 1:
        return test_grades(grade_list)
    else:
        # print "Restaurant has only one grade record, can't determine improvement"
        return None
        raise SingleRecordError

def all_restaurant_sum(data):
    camis_id = pd.unique(data.CAMIS.ravel())    # create an array to store unique camis_id
    camis_dic = {}
    for i in camis_id:
        camis_dic[i] = test_restaurant_grades(data,i)
    df = pd.DataFrame(camis_dic.items(), columns =['camis_id', 'restaurant_improvement'])    #create a dataframe using the dictionary
    # print "Count of all grades improvement in NYC is: \n", df.restaurant_improvement.dropna().value_counts()
    print "Sum of all grades improvement in NYC is: \n", df.restaurant_improvement.dropna().sum(), "\n"
    # return df


def sum_by_boro(data):
    boro_camis_id = {}
    frames = []
    for i in pd.unique(data['BORO'][data['BORO'] != 'Missing']):
        boro_camis_id[i] = pd.unique(data['CAMIS'][data['BORO'] == i])
        camis_dic = {}
        for j in boro_camis_id[i]:
            camis_dic[j] = test_restaurant_grades(data,j)
        df = pd.DataFrame(camis_dic.items(), columns =['camis_id', 'restaurant_improvement'])    #create a dataframe using the dictionary
        df['BORO'] = pd.Series([i]*len(camis_dic))
        frames.append(df)
        # print "Count of improvement in", i, "is \n",df.restaurant_improvement.dropna().value_counts()
        print "Sum of all grades improvement in %s is: \n" %i, df.restaurant_improvement.dropna().sum(),"\n"
    data_df = pd.concat(frames)
    return data_df


def graphs(data):
    # plot histogram of the counts for grade improvement for New York City
    plt.figure()
    data['year'] = data['GRADE DATE'].map(lambda x:x.year)
    data_new = pd.DataFrame(data.groupby(['year','GRADE']).size().unstack())
    data_new.plot(kind = 'bar', figsize = (11.5, 8.5))
    plt.title('Grade improvement of all restaurants in New York City')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.savefig('grade_improvement_nyc.pdf')
    plt.clf()

    for i in pd.unique(data['BORO'][data['BORO'] != 'Missing']):
        # plot histogram of counts for grade improvement for each borough
        data_new = pd.DataFrame(data[data['BORO'] == i].groupby(['year','GRADE']).size().unstack())
        data_new.plot(kind = 'bar',figsize = (11.5, 8.5))
        plt.title('Grade improvement of restaurants in ' + i)
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.savefig('grade_improvement_'+ i +'.pdf')
        plt.clf()
