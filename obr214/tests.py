from unittest import TestCase
import os
from data_cleaner import DataReader
from restaurant_grades import RestaurantGrader

__author__ = 'obr214'


class Test(TestCase):

    def test_datareader_file_not_found(self):
        """
        Passing wrong filename to the DataReader Object

        Result: It should raise IO exception
        """
        wrong_filename = 'wrong_file.csv'

        with self.assertRaises(IOError):
            data_reader = DataReader(wrong_filename)

    def test_test_grades(self):
        """
        Passing the list of grades ['A', 'C', 'C', 'C', 'C', 'C', 'A'] to the function test_grades

        Result: The grade should be 1
        """
        self.assertEqual(1, RestaurantGrader.test_grades(['A', 'C', 'C', 'C', 'C', 'C', 'A']))

    def test_test_restaurant_grades(self):
        """
        Passing the Camis Id: 30112340 to the function test_restaurant_grades

        Result: The grade should be 0
        """
        data_reader = DataReader('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        inspections_df = data_reader.get_dataframe()
        restaurant_grades = RestaurantGrader(inspections_df)

        self.assertEqual(0, restaurant_grades.test_restaurant_grades(30112340))

    def test_create_plots_files(self):
        """
        Creates the plots for the Boroughs

        Result: Should create 6 plots
        """

        try:
            os.remove('grade_improvement_bronx.pdf')
            os.remove('grade_improvement_brooklyn.pdf')
            os.remove('grade_improvement_manhattan.pdf')
            os.remove('grade_improvement_nyc.pdf')
            os.remove('grade_improvement_queens.pdf')
            os.remove('grade_improvement_staten.pdf')
        except OSError:
            pass

        data_reader = DataReader('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        inspections_df = data_reader.get_dataframe()

        restaurant_grades = RestaurantGrader(inspections_df)
        restaurant_grades.grade_improvement_plots()

        self.assertTrue(os.path.isfile('grade_improvement_bronx.pdf'))
        self.assertTrue(os.path.isfile('grade_improvement_brooklyn.pdf'))
        self.assertTrue(os.path.isfile('grade_improvement_manhattan.pdf'))
        self.assertTrue(os.path.isfile('grade_improvement_nyc.pdf'))
        self.assertTrue(os.path.isfile('grade_improvement_queens.pdf'))
        self.assertTrue(os.path.isfile('grade_improvement_staten.pdf'))
