import unittest
import pandas as pd
from grade_functions import *

class gradetest(unittest.TestCase):

    # test if function grade_check removed invalid grades from dataset
    def test_grade_check(self):
        grade = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
        grade = grade.dropna(subset=['GRADE'])
        self.assertEqual(list(set(grades_check(grade).GRADE)),["A","C","B"])
        pass

    # test if function test_grades returns correct value
    def test_test_grades(self):
        self.assertEqual(0,test_grades(["A","B","A"]))
        self.assertEqual(-1,test_grades(["A","B","C"]))
        self.assertEqual(1,test_grades(["C","B","A"]))
        pass


if __name__ == "__main__":
    unittest.main()