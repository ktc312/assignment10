import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from grade_functions import *

def main():
    # load data
    grade = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
    # remove NAs in GRADE
    grade = grade.dropna(subset=['GRADE'])
    # remove invalid grade
    grade = grades_check(grade)
    # generate figure for 5 boroughs
    boroughs = list(set(grade.BORO))
    for boro in boroughs:
        if(boro != 'Missing'):
            plt.clf()
            grade_improvement = []
            grade_subset = grade[grade.BORO == boro]
            camis = list(set(grade_subset.CAMIS))
            for camis_id in camis:
                grade_improvement.append(test_restaurant_grades(grade_subset,camis_id))
            figure_grades_improvement(grade_improvement,boro.lower())
    #  generate figure for NYC
    grade_improvement_nyc = []
    camis_nyc = list(set(grade.CAMIS))
    for camis_nyc_id in camis_nyc:
        grade_improvement_nyc.append(test_restaurant_grades(grade,camis_nyc_id))
    figure_grades_improvement(grade_improvement_nyc,'nyc')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ("Accidently stopped by keyboard interrupt")
    except ValueError:
        print("Accidently stopped by invalid value")
    except TypeError:
        print("Accidently stopped by invalid types")
