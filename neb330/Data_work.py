import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

'''This file contains the functions needed to generate the visual graphs
of restaurant grade improvements in NYC. It also contains functions that
compute the trends of restaurant grades improving or declining'''

#load and clean data from NYC Open Data (https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59)
try:
    data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory = False)
    data = data.dropna(subset = ['GRADE'])
    data = data[data['GRADE'].isin(['A', 'B', 'C'])]
except:
    print "Dataset unavailable"  
    exit()  


def test_grades(grade_list):
    '''This function takes a list of grades and returns 1 if the grades
    are improving, 0 if they stay the same, and -1 if they are declining.'''
    
    #convert the grades to an integer value
    grade_dict  = {'A' : 95, 'B': 85, 'C':75}
    #create list of these integer values               
    data = [grade_dict.get(i) for i in grade_list]
    if len(set(data)) == 1:
        return 0
    else:
        #divide list into first half and second half, then take the mean of both
        lst1 = [data[i] for i in range(int(len(data)/2))]
        lst2 = [data[i] for i in range(int(len(data)/2), len(data), 1)]
        difference = np.mean(lst2) - np.mean(lst1)
        #create a threshold of two, so if the difference in mean is greater than two, we return -1
        if difference > 2:
            return -1
        else:
            return 1    

def test_restaurant_grades(camis_id):
    '''This function takes in a restaurant ID and returns the trend of that
    restaurant's grades, utilizing the function test_grades'''
    
    df = data.loc[data['CAMIS'] == camis_id]
    if df.shape == 0:
        return 0
    else:
        grades = list(df['GRADE'])
        return test_grades(grades)

     
def sum_over_restaurants(data_frame):
    '''This function takes in a dataframe and returns the numeric representation
    of the trend of restaurant grades in that dataframe'''
    sum = 0
    for x in list(data_frame['CAMIS'].unique()):
        sum = sum + test_restaurant_grades(x)
    return sum    

def sum_over_borough(borough): 
    '''This function takes in a borough name and returns the numeric
    representation of the trend of restaurant grades in that borough over 
    time, utilizing the function sum_over_restaurants.'''
    df = data.loc[data['BORO'] == str(borough)] 
    return sum_over_restaurants(df) 
    

def generate_bar_plot(data_frame, area_name):
    '''This function takes in a dataframe, and the name of the area that
    it represents, and generates a bar plot of the number of restaurants 
    receiving each grade (A, B, or C) over 2012, 2013, 2014, and 2015.
    Note: the input must be a valid borough name in CAPS, adhering to the 
    format of the dataframe.'''
    date_list = []
    for x in data_frame['INSPECTION DATE']:
        date_list.append(x.split('/')[2])
    data_frame['YEAR'] = date_list
    df4 = data_frame.loc[data_frame['YEAR'] == '2012']     
    df1 = data_frame.loc[data_frame['YEAR'] == '2013']
    df2 = data_frame.loc[data_frame['YEAR'] == '2014']
    df3 = data_frame.loc[data_frame['YEAR'] == '2015']
    
    a_list = [(df4['GRADE'] == 'A').sum(),(df1['GRADE'] == 'A').sum(), (df2['GRADE'] == 'A').sum(), (df3['GRADE'] == 'A').sum()]
    b_list = [(df4['GRADE'] == 'B').sum(),(df1['GRADE'] == 'B').sum(), (df2['GRADE'] == 'B').sum(), (df3['GRADE'] == 'B').sum()]
    c_list = [(df4['GRADE'] == 'C').sum(),(df1['GRADE'] == 'C').sum(), (df2['GRADE'] == 'C').sum(), (df3['GRADE'] == 'C').sum()]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N = 4
    ind = np.arange(N)                
    width = 0.15
    rects1 = ax.bar(ind, a_list, width, color='red')
    rects2 = ax.bar(ind+width, b_list, width, color='blue')
    rects3 = ax.bar(ind+2*width, c_list, width, color='green')
   
    ax.set_ylabel('Number of Restaurants With Particular Grade')
    ax.set_title('Grades of Restaurants in ' + str(area_name) + ' by Year')
    xTickMarks = ['2012', '2013', '2014', '2015']
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    ax.legend( (rects1[0], rects2[0], rects3[0]), ('A', 'B', 'C') )
    plt.savefig('grade_improvement_' + str(area_name).lower()+ '.pdf')
    plt.close("all")

def generate_bar_by_location(borough):
    '''This function takes in a borough name and generates a bar plot
    of the number of restaurants receiving each grade (A, B or C) in that
    particular borough over time, utilizing the function generate_bar_plot.
    Note: the input must be a valid borough name in CAPS, adhering to the 
    format of the dataframe.'''
    df = data.loc[data['BORO'] == borough]
    generate_bar_plot(df, borough) 

                   