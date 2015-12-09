"""This module has functions to analyze the grades of restaurant """

import numpy as np 
import pandas as pd


# question 3
def test_grades(grade_list):
    '''the function is to evaluate whether the grade is improving or not. Firstly, I will see A, B, C as 3, 2, 1. And compare the 
    change of two continuous values. I will compute the weighted score. If one has continuous grades of 'A','C','B', then final 
    score = -2(first chage)*0.5(weight)+1(second change)*1(weight) = 0. In this case, it stays the same.
    '''
    dic_grade = {'A':3,'B':2,'C':1} # give the scores
    length = len(grade_list)
    final_score = 0
    if length >=2:
        for i in range(length-1):
            this_score = dic_grade[grade_list[i+1]] - dic_grade[grade_list[i]]
            this_weight = 1.0/float((length-1-i))
            final_score = final_score+this_weight*this_score
    if final_score ==0:
        return 0
    elif final_score>0:
        return 1
    else:
        return -1

# question 4
def test_restaurant_grades(camis_id,data_df):
    '''the function will judge whether the grade of a specific restaurant is improving or not.'''
    df_camis_id = data_df[data_df['CAMIS'] == camis_id]
    df_sorted = df_camis_id.sort('FORMAT_DATE',ascending=1)
    grade_list = df_sorted['GRADE'].tolist()
    return test_grades(grade_list)

def print_restaurant_grades_all(data_df):
    '''the function will print the sum of scores of all restaurants'''
    sum_all = 0
    for res in data_df['CAMIS'].unique():
        sum_all += test_restaurant_grades(res,data_df)
    print "The sum score of all restaurants in New York City is %d" % sum_all
  
def print_restaurant_grades_by_borough(data_df):
    '''the function will print the sum of scores of all boroughs'''
    boroughs = data_df[data_df['BORO']!='Missing']['BORO'].unique() # leave the missing value
    sum_results = []
    for borough in boroughs:
        df_borough = data_df[data_df['BORO'] == borough]
        sum_borough = 0
        print "Computing " + borough + "..."
        for res_b in df_borough['CAMIS'].unique():
            sum_borough += test_restaurant_grades(res_b,df_borough)
        sum_results.append(sum_borough)
    for index_i in range(len(sum_results)):
        print "The sum score of " + boroughs[index_i]+':'
        print sum_results[index_i]
        

def get_grade_count_values(df_data):
    '''the function will return a dataframe of count states of all the unique time'''
    time_series = []
    grade_count_list=[]
    snap_count = {'A':0,'B':0,'C':0}
    appeared_res_dic = {}
    sorted_df= df_data.sort('FORMAT_DATE',ascending = 1)
    time_cur = sorted_df.iloc[0]['FORMAT_DATE'] # current time
    time_series.append(time_cur)
    
    for index_i in range(len(df_data)):
        if sorted_df.iloc[index_i]['FORMAT_DATE']!= time_cur: 
            
            time_cur = sorted_df.iloc[index_i]['FORMAT_DATE']
            time_series.append(time_cur)
            grade_count_list.append(snap_count.copy()) 
        this_id = sorted_df.iloc[index_i]['CAMIS']
        this_grade = sorted_df.iloc[index_i]['GRADE']
        if this_id in appeared_res_dic:  
            if this_grade!= appeared_res_dic[this_id]: 
                snap_count[this_grade] += 1
                snap_count[appeared_res_dic[this_id]] -=1
                appeared_res_dic[this_id] = this_grade
        else:
            #new target
            appeared_res_dic[this_id] = this_grade
            snap_count[this_grade] += 1
    grade_count_list.append(snap_count.copy())
    df_count_plus_time = pd.DataFrame(grade_count_list,time_series)
    return df_count_plus_time
            
