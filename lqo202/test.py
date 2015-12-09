__author__ = 'luisa'


import unittest
import Grade
from assignment10 import import_data
from unittest import TestCase
import pandas as pd

class test_import_data(TestCase):
    def test_DB_exists(self):
        """
        Function import_data :
            Must raise an exception is an invalid name is inputted.
            Must create a dataframe if there is no argument or if the correct name is inputted
        :return:
        """
        correct_file = "DOHMH_New_York_City_Restaurant_Inspection_Results.csv"
        incorrect_file="DOHMH_New_York_City_Restaurant_Inspection_Result.csv"

        self.assertRaises(IOError, import_data, incorrect_file)
        assert isinstance(import_data(correct_file), pd.DataFrame)
        assert isinstance(import_data(), pd.DataFrame)




class test_grade(TestCase):
    def test_grade_definition(self):
        data = import_data()

        #If data is ok then a Grade class object must be created
        assert  isinstance(Grade.grades(data), Grade.grades)

        #if there is missing some column, exception should rise
        data = data.drop('BORO',1)
        self.assertRaises(ValueError, Grade.grades, data)


    def test_def_grades(self):
        #Creating an instance of grades class
        data = import_data()
        grades_db = Grade.grades(data)

        #Invalid inputs
        invalid_type = ['a',1,]
        invalid_value = [['A', 1, 1], ['A',1]]

        #Valid inputs
        valid = [['A', 'A', 'A'], ['A','B']]

        #Evaluating
        for grades in invalid_type:
            self.assertRaises(TypeError, grades_db.test_grades, grades)

        for grades in invalid_value:
            self.assertRaises(ValueError, grades_db.test_grades, grades)

        for grades in valid:
            assert isinstance(grades_db.test_grades(grades),int)


if __name__ == '__main__':
    unittest.main()

