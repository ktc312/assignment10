__author__ = 'ktc312'

from read_data import *
from test_grades import *

data = clean_data(get_data())
boro_list = data.BORO.unique()

data_to_analyze = GradeAnalyzer(data, boro_list)
data_to_analyze .grade_over_time()
data_to_analyze.boroplot()
grades_over_time(data)
