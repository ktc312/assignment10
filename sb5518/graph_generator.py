__author__ = 'sb5518'

"""
This  Module contains the grades_by_year_graph_generator(grades_dictionary, graph_name) function which
purpose is to generate the graphs required in question 5. It creates a graph of lines for the total amount of grades by
year. The required input is a dictionary of dictionaries in the form {grade:{year:total_restaurants, ...}, ...}

"""


import matplotlib.pyplot as plt
from matplotlib import patches

def grades_by_year_graph_generator(grades_dictionary, graph_name):
    if not isinstance(grades_dictionary, dict):
        raise TypeError('Please introduce a valid dictionary of dictionaries for grades and number of distict restaurants by year')
    for dictionary in grades_dictionary.values():
        if not isinstance(dictionary, dict):
            raise TypeError('At least one element in the dictionary is not a dictionary')
    if not isinstance(graph_name, str):
        raise  TypeError('The function did not receive a valid string representation to build the file name')
    try:
        plt.close()
        fig, ax = plt.subplots()
        ax.plot(grades_dictionary['A'].keys(), grades_dictionary['A'].values(), color='r')
        ax.plot(grades_dictionary['B'].keys(), grades_dictionary['B'].values(), color='b')
        ax.plot(grades_dictionary['C'].keys(), grades_dictionary['C'].values(), color='g')
        ax.set_xlabel('Year')
        ax.set_xticks([2011,2012,2013,2014,2015], minor=False)
        ax.set_xticklabels(['2011','2012','2013','2014','2015'])
        label_1, label_2, label_3 = patches.Rectangle((0, 0), 1, 1, fc="r"), patches.Rectangle((0, 0), 1, 1, fc="b"), patches.Rectangle((0, 0), 1, 1, fc="g")
        ax.legend([label_1,label_2,label_3],['Grade A', 'Grade B', 'Grade C'], loc='best')
        ax.set_ylabel('Number of grades by Year')
        ax.legend([label_1,label_2,label_3],['Grade A', 'Grade B', 'Grade C'], loc='best')
        plt.savefig("grade_improvement_" + graph_name.lower(), format='pdf')
    except LookupError:
        raise LookupError('Please check that the dictionary of Grades by year has the right format')