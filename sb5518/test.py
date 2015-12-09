__author__ = 'sb5518'


from unittest import TestCase

import os
import aggregated_grades_generator as agg
import graph_generator as gg
import data_cleaner as dc
import grades_calculator as gc
import warnings

warnings.filterwarnings("ignore") # This is used to avoid printing some Pandas FutureWarnings

class all_tests(TestCase):

    def test_graph_generator(self):
        try:
            os.remove('./grade_improvement_nyc.pdf')

        except OSError:
            pass

        cleaned_df = dc.data_loader_and_cleaner('DOHMH_New_York_City_Restaurant_Inspection_Results.csv').cleaned_df
        nyc_grades_dictionary = agg._nyc_grades_by_year(cleaned_df)
        gg.grades_by_year_graph_generator(nyc_grades_dictionary, "nyc")

        self.assertTrue(os.path.isfile('grade_improvement_nyc'))


    def test_data_loader_and_cleaner1(self):
        with self.assertRaises(IOError):
            dc.data_loader_and_cleaner('sdjasd.csv')



    def test_test_grades(self):
        not_a_list = 1
        with self.assertRaises(TypeError):
            gc.test_grades(not_a_list)


    def test_test_restaurant_grades(self):
        cleaned_df = dc.data_loader_and_cleaner('DOHMH_New_York_City_Restaurant_Inspection_Results.csv').cleaned_df
        with self.assertRaises(TypeError):
            gc.test_restaurant_grades(cleaned_df, 45234635)




