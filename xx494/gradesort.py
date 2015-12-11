'''
Created on Dec 8, 2015

@author: Xu Xu
'''
import pandas as pd

def test_grades(grade_list):
    n=len(grade_list)
    grades_dictionary={'A':3,'B':2,'C':1}
    grade_list=[grades_dictionary[key] for key in grade_list]
    if n==1:
            return 0
    else:
        if grade_list[0]>grade_list[-1]:
            return 1
        elif grade_list[0]<grade_list[-1]:
            return -1
        else:
            return 0
        
def test_restaurant_grades(data,camis_id):
    data=[data['camis'==camis_id]]
    data=data.sort('date')
    result=test_grades(data['grade'])
    return result

def total_restaurants_improvement(data):
    camis_list=data['camis'].unique()
    sum=0
    for item in camis_list:
        sum == sum + test_restaurant_grades(data,item)
    print 'The total improvement of restaurants in NYC is'+str(sum)
    
def total_restaurants_improvement_by_borough(data):
    boro_list=data['boro'].unique()
    scores={}
    for boro in boro_list:
        data_borough=data[data['boro']==boro]
        sum=0
        for item in data_borough['camis'].unique():
            sum+=test_restaurant_grades(data,item)
        scores[boro]=sum
        df=pd.DataFrame.from_dict(scores, orient='index')
        df.columns=['Total improvement in Borough']
        df.index.name=['Boro']
        print df
        return df
    return scores