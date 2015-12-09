'''
Created on Dec 04, 2015
@author: Urjit Patel - up276
'''

import pandas as pd
from plot_graphs import PlotGraphs
import sys

def main_function():
    '''
    Body of main_function from where all necessary execution of the program starts. First it loads the raw data, cleans it and then analyze whether restaurant grades are increasing or decreasing.
    Then it prints the final values for each of the borough.
    '''
    try:
        print "====================================="
        print "New York Restaurants Grades Analysis :"
        print "====================================="
        raw_data = load_data()
        cleaned_data = clean_data(raw_data)
        analysis_of_boroughs(cleaned_data)
        NYC_grade_count = GradeCount(cleaned_data)
        PlotGraphs.Plot(NYC_grade_count,'grade_improvement_nyc.pdf')
        Boroughs_grade_count = BoroughsGradeCount(cleaned_data)
        PlotGraphs.PlotBoroughsGraphs(Boroughs_grade_count)

    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except GradeAnalysis_Exception as exception:
        print "Error : ", exception
        sys.exit()

def load_data():
    '''
    This function loads the data of the necessary columns 'CAMIS','BORO','GRADE','GRADE DATE'
    '''
    try:
        dataframe = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv',low_memory = False, usecols=['CAMIS','BORO','GRADE','GRADE DATE'])
        return dataframe
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While loading the data")

def clean_data(data):
    '''
    This function removes  null value rows, removes rows having invalid grades
    '''
    try:
        data = data.dropna()
        mask = data.GRADE.isin(['P','Z','Not Yet Graded'])
        data = data[~mask]
        return data
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While cleaning the data")

def test_grades(grades):
    '''
    This function decides whether the grades of the perticular restauraant is increasing or decreasing.
    We use the weights for grades A,B and C. And we check for each pair of grades whether they are increasing or decreasing.
    We weight this difference using the time. As an example Grades in 2015 are more important than grades in 2011.
    So we multiply the difference by (i+1). So most recent change will be recorded with more weight.
    '''
    try:
        grade_value = {'A':3, 'B':2 , 'C':1 }
        grade_sum = 0
        for i in range(0,len(grades)-1):
            grade_sum = grade_sum + ((grade_value[grades[i+1]] - grade_value[grades[i]]) * (i+1) )

        if grade_sum<0:
            return -1
        elif grade_sum >0:
            return 1
        else:
            return 0
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While calculating the test_grades function")

def test_restaurant_grades(camis_id,data):
    '''
    This function uses "test_grades" function to compute the decreament or increament in grades for perticular restaurant
    '''
    try:
        restaurant_data = data[data["CAMIS"] == camis_id]
        restaurant_data['GRADE DATE'] = pd.to_datetime(restaurant_data["GRADE DATE"])
        restaurant_data = restaurant_data.sort(columns = 'GRADE DATE', ascending = True ) # This now sorts in date order  .sort(columns='GRADE DATE')
        restaurant_grade_list = list(restaurant_data['GRADE'])
        restaurant_grade_value = test_grades(restaurant_grade_list)
        return restaurant_grade_value
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While calculating the test_restaurant_grades function")

def analysis_of_boroughs(data):
    '''
    This function computes the overall change in restaurants for each borough
    '''
    try:
        print"\nBelow numbers will give you the idea whether restaurants for that perticular borough on an avergae is improving or not."
        print"+ve values shows there is an improvement.\n"
        boroughs = ['BRONX','BROOKLYN','MANHATTAN','STATEN ISLAND','QUEENS']
        boroughs_final_grade_value = {'BRONX':0,'BROOKLYN':0,'MANHATTAN':0,'STATEN ISLAND':0,'QUEENS':0}
        for borough in boroughs:
            borough_data = data[data["BORO"] == borough]
            restaurant_ids = borough_data["CAMIS"].unique()
            for restaurant_id in restaurant_ids:
                restaurant_data = borough_data[borough_data["CAMIS"] == restaurant_id]
                restaurant_grade_value = test_restaurant_grades(restaurant_id,restaurant_data)
                boroughs_final_grade_value[borough] = boroughs_final_grade_value[borough] + restaurant_grade_value
            print "Sum over all restaurants grades analysis values for borough ",borough," is = ",boroughs_final_grade_value[borough]

    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While calculating the analysis_of_boroughs function")


def BoroughsGradeCount(data):
    '''
    This function calls "GradeCount" function for each borough.
    '''
    try:
        boroughs = ['BRONX','BROOKLYN','MANHATTAN','STATEN ISLAND','QUEENS']
        boroughs_data = {}
        for borough in boroughs:
            borough_data = data[data["BORO"] == borough]
            boroughs_data[borough] = GradeCount(borough_data)

        return boroughs_data

    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While calculating the BoroughsGradeCount function")


def GradeCount(data):
    '''
    This function counts the number of grades in the received data for each individual grade.
    '''
    try:
        grades_nyc = ['A','B','C']
        grade_dict = {}
        grade_count = {}

        for grade in grades_nyc:
            grade_data = data[data["GRADE"] == grade]
            grade_data['GRADE DATE'] = pd.to_datetime(grade_data["GRADE DATE"])
            grade_data = grade_data.sort(columns = 'GRADE DATE', ascending = True ) # This now sorts in date order  .sort(columns='GRADE DATE')
            grade_dict[grade] = grade_data.groupby(grade_data['GRADE DATE'].map(lambda x: x.year)).count()

        for grade in grade_dict:
            count_list = list(grade_dict[grade]['GRADE'])
            length = len(count_list)
            if length==4:                  # when we dont have any grades for 2011, we place 0 for year 2011
                count_list.insert(0, 0)
            grade_count[grade] = count_list

        return grade_count

    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise GradeAnalysis_Exception("While calculating the GradeCount function")


class GradeAnalysis_Exception(Exception):
    '''
    User defined exception for NYC Restaurants grade analysis
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == "__main__":
    try:
        main_function()       #call to main function
    except KeyboardInterrupt:
        print "Program Interrupted...Plz run the program again...Thanks!!!"

"""
SAMPLE OUTPUT :

=====================================
New York Restaurants Grades Analysis :
=====================================

Below numbers will give you the idea whether restaurants for that perticular borough on an avergae is improving or not.
+ve values shows there is an improvement.

Sum over all restaurants grades analysis values for borough  BRONX  is =  510
Sum over all restaurants grades analysis values for borough  BROOKLYN  is =  1238
Sum over all restaurants grades analysis values for borough  MANHATTAN  is =  2148
Sum over all restaurants grades analysis values for borough  STATEN ISLAND  is =  177
Sum over all restaurants grades analysis values for borough  QUEENS  is =  1117
C:/Users/Urjit Patel/PycharmProjects/Assignment10/up276/assignment10.py:153: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  grade_data['GRADE DATE'] = pd.to_datetime(grade_data["GRADE DATE"])
C:\Users\Urjit Patel\Anaconda\lib\site-packages\matplotlib\axes\_axes.py:475: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
  warnings.warn("No labelled objects found. "

Process finished with exit code 0


"""