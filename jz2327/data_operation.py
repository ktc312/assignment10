import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt 

# DS-GA 1007 Assignment 10
# Author: Junchao Zheng

def test_grades(grade_list):
    '''
    The function takes a list containing grades as input,
    then return 1 if the grade is improving, 0 if the grade stays the same, -1 if the grade is declining.
    Provide a justification for how you calculate this value: I just compare the earlist and the most recent grade to see whether it is improving or not.
    '''

    #dictionary to convert grades to numeric numbers. Easy for comparing the grade.
    grade_numeric_dictionary = {'A':1, 'B':2, 'C':3, 'P':4, 'Z':5}
    
    #get a 'unique' list,e.g. ['A', 'A', 'C', 'C', 'B'] would have a return of ['A','C','B'].
    grade_list_unique = []
    grade = grade_list[0]
    grade_list_unique.append(grade)
    for i in range(len(grade_list)-1):
        if grade_list[i+1] == grade_list[i]:
            pass
        else:
            grade = grade_list[i+1]
            grade_list_unique.append(grade)
    
    #compare the first element and the last element of the list to determine if it is improving or declining.
    if grade_numeric_dictionary.get(grade_list_unique[0]) > grade_numeric_dictionary.get(grade_list_unique[-1]):
        return 1
    elif grade_numeric_dictionary.get(grade_list_unique[0]) == grade_numeric_dictionary.get(grade_list_unique[-1]):
        return 0
    else:
        return -1

def test_restaurant_grades(data, camis_id):
    '''
    The function takes a dataframe and a camis ID as input,
    Then call the test_grades function to return the function value of a particular shop with the given camis ID.
    '''

    data_given_camis = data[data['CAMIS'] == camis_id]    # Choose the data only contains the shop with given camis ID.
    grade_given_camis = data_given_camis.ix[pd.to_datetime(data_given_camis.DATE).order().index]['GRADE'].tolist()    # Sort in date order.
    return test_grades(grade_given_camis)

def plot_grade_dictionary(data):
    '''
    The function takes a dataframe as input,
    Then it calculates the number of each grade respectively grouped by different date.
    The return is a dictionary: keys are different dates and values are a list of total number of each grade.
    '''

    grade_dictionary = {}
    for i in range(data['DATE'].unique().shape[0]):
        data_given_date = data[data['DATE'] == data['DATE'].unique()[i]]
        a,b,c,p,z = 0,0,0,0,0
        # each time a certain grade appears, counts + 1.
        for j in range(len(data_given_date['CAMIS'])):
            if j != 0:
                if data_given_date['CAMIS'][j:j+1].values == data_given_date['CAMIS'][j-1:j].values:
                    pass
                else:
                    if data_given_date['GRADE'][j:j+1].values == 'A':
                        a = a + 1
                    elif data_given_date['GRADE'][j:j+1].values == 'B':
                        b = b + 1
                    elif data_given_date['GRADE'][j:j+1].values == 'C':
                        c = c + 1
                    elif data_given_date['GRADE'][j:j+1].values == 'P':
                        p = p + 1
                    elif data_given_date['GRADE'][j:j+1].values == 'Z':
                        z = z + 1
            else:  #for i = 0 where the iteration is initiated skip the if loop above.
                if data_given_date['GRADE'][j:j+1].values == 'A':
                    a = a + 1
                elif data_given_date['GRADE'][j:j+1].values == 'B':
                    b = b + 1
                elif data_given_date['GRADE'][j:j+1].values == 'C':
                    c = c + 1
                elif data_given_date['GRADE'][j:j+1].values == 'P':
                    p = p + 1
                elif data_given_date['GRADE'][j:j+1].values == 'Z':
                    z = z + 1
        grade_dictionary[data['DATE'].unique()[i]] = [a, b, c, p ,z]
    return grade_dictionary

def plot_grade(data, title):
    '''
    The function takes a dataframe and a string as input,
    Then return plots of the return of plot_grade_dictionary functions, saving to a pdf file.
    '''

    plt.figure()
    grade_dictionary = plot_grade_dictionary(data)
    index_list = ['A', 'B', 'C', 'P', 'Z']
    grade_dictionary_df = pd.DataFrame(grade_dictionary, index = index_list).T
    grade_dictionary_df.index = pd.to_datetime(grade_dictionary_df.index)
    grade_dictionary_df.plot(figsize = (15,10), kind = 'line', label = index_list)
    plt.legend(loc = 'upper left')
    plt.title('All restaurants in %s' %title)
    plt.savefig('grade_improvement_{}.pdf'.format(str.lower(title.split(' ')[0])))
