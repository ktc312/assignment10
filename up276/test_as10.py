'''
Created on Dec 04, 2015
@author: Urjit Patel - up276
'''

from unittest import TestCase

import assignment10
import os
import glob

__author__ = 'up276'

class Test(TestCase):
    '''
    This Test class has total 4 test functions which are used to test the program functionality
    '''

    #Below function tests the cleaning function. Whether all unnecessary data has been removed or not.
    def test_cleaning_function(self):

        raw_data = assignment10.load_data()
        raw_data = raw_data.ix[:30000]
        cleaned_data = assignment10.clean_data(raw_data)
        columnNames = cleaned_data.columns.values
        for colname in columnNames:
            self.assertEqual(cleaned_data[colname].isnull().sum(),0)

        self.assertEqual(cleaned_data.GRADE.isin(['P','Z','Not Yet Graded']).sum(),0)

    #Below function tests the function "test_grades_function"
    def testing_for_test_grades_function(self):

        self.assertEqual(assignment10.test_grades(['A','A','A']),0)
        self.assertEqual(assignment10.test_grades(['C','B','A']),1)
        self.assertEqual(assignment10.test_grades(['A','B','C']),-1)

    #Below function tests the function "test_restaurant_grades". Here to save the time I am only loading first 30000 rows of data
    def testing_for_test_restaurant_grades_function(self):

        raw_data = assignment10.load_data()
        raw_data = raw_data.ix[:30000]
        cleaned_data = assignment10.clean_data(raw_data)
        self.assertEqual(assignment10.test_restaurant_grades(40358429,cleaned_data),1)

    #Below function tests whether all necessary files are getting generated or not at the end of the program. Here to save the time I am only loading first 30000 rows of data
    def test_existance_of_generated_files(self):
        try:
            for filename in glob.glob('grade_improvement*.pdf') :
                os.remove( filename )  #first remove all files which are already presented
        except IOError:
            pass

        raw_data =  assignment10.load_data()
        raw_data =  raw_data.ix[:30000]
        cleaned_data =  assignment10.clean_data(raw_data)
        NYC_grade_count =  assignment10.GradeCount(cleaned_data)
        assignment10.PlotGraphs.Plot(NYC_grade_count,'grade_improvement_nyc.pdf')
        Boroughs_grade_count =  assignment10.BoroughsGradeCount(cleaned_data)
        assignment10.PlotGraphs.PlotBoroughsGraphs(Boroughs_grade_count)
        self.assertTrue(os.path.isfile('./grade_improvement_nyc.pdf'))
        self.assertTrue(os.path.isfile('./grade_improvement_bronx.pdf'))
        self.assertTrue(os.path.isfile('./grade_improvement_brooklyn.pdf'))
        self.assertTrue(os.path.isfile('./grade_improvement_manhattan.pdf'))
        self.assertTrue(os.path.isfile('./grade_improvement_queens.pdf'))
        self.assertTrue(os.path.isfile('./grade_improvement_statn.pdf'))

