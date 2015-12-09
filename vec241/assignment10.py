__author__ = "Vincent"


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def clean_df():

    global df

    df= pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")

    df = df.dropna()

    #Remove invalid grades (P & Z = grade pending)
    mask = df.GRADE.isin(['P','Z','Not Yet Graded'])
    df = df[~mask]

    return df


def test_grades(grade_list):
    '''This function states whereas grades are improving overall
    To do this, we compare whereas most recent grade is better than the average grade or not
    input = list of grades ordered (from most to less recent)
    output = 1 if grade improved, 0 if status quo, -1 if decreased'''

    improving = 0

    # convert letter grades into numerical grades
    numerical_grade_list = grade_list
    for index, grade in enumerate(grade_list):
        if grade == 'A':
            numerical_grade_list[index] = 3
        elif grade == 'B':
            numerical_grade_list[index] = 2
        elif grade == 'C':
            numerical_grade_list[index] = 1

    average_grade = sum(numerical_grade_list) / float(len(numerical_grade_list))

    if grade_list[0] > average_grade:
        improving = 1
    elif grade_list[0] == average_grade:
        improving = 0
    elif grade_list[0] < average_grade:
        improving = -1

    return improving

def test_restaurant_grades(camis_id):

    grade_list = (((df[df['CAMIS']==camis_id]).sort(columns='GRADE DATE'))['GRADE']).tolist()
    return test_grades(grade_list)


def borough_evolution():

	for boro in df['BORO'].unique().tolist():
	    camis_ids = ((df[df['BORO']==boro])['CAMIS']).unique().tolist()

	    sum = 0
	    for camis_id in camis_ids:
	        sum = sum + test_restaurant_grades(camis_id)

	     print "The evolution of borough {0} is {1}".format(boro,sum)


def grade_counter(df):

    grades = ['A','B','C']
    grouped_grade = {}
    grade_count = {}

    for grade in grades:
        grades_df = df[df["GRADE"] == grade]
        grades_df['GRADE DATE'] = pd.to_datetime(grades_df["GRADE DATE"])
        grades_df = grades_df.sort(columns = 'GRADE DATE', ascending = True )
        grouped_grade[grade] = grades_df.groupby(grades_df['GRADE DATE'].map(lambda x: x.year)).count()

    for grade in grade_dict:
        count = grouped_grade[grade]['GRADE'].tolist()
        if len(count)==4:
            count.insert(0, 0)
        grade_count[grade] = count

    return grade_count


def plot():
    #Plot for nyc
    grade_count = grade_counter(df)
    plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['A'], label="A")
    plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['B'], label="B")
    plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['C'], label="C")
    plt.title("Evolution of number of restaurant per grades - nyc")
    plt.xlabel("Year")
    plt.xticks([2011, 2012, 2013, 2014, 2015])
    plt.legend(loc = 2)
    plt.savefig("grade_improvement_nyc.pdf")

    plt.close()

    # plot for the different boroughs
    for boro in df['BORO'].unique().tolist():
        grade_count = grade_counter(df[df['BORO']==boro])

        plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['A'], label="A")
        plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['B'], label="B")
        plt.plot([2011, 2012, 2013, 2014, 2015], grade_count['C'], label="C")
        plt.title("Evolution of number of restaurant per grades - {0}".format(boro))
        plt.xlabel("Year")
        plt.xticks([2011, 2012, 2013, 2014, 2015])
        plt.legend(loc = 2)
        plt.savefig("grade_improvement_{0}.pdf".format(str(boro).lower()))
        plt.close()

def main():

	borough_evolution()
	plot()


if __name__ == '__main__':
	clean_df()
	main()
