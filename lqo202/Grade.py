'''
Class grades manages all concerning grades calculations and plotting.
It is a subclass of pandas dataframe
More details in each function
'''
__author__ = 'lqo202'


import pandas as pd
from matplotlib import pyplot as plt
import datetime

class grades(pd.DataFrame):

    def __init__(self, *args, **kw):
        '''
        Inherits the super class properties and functions, validates that the neccesary columns exists in the input,
        if not raises ValueError
        '''

        #Inheriting from pandas
        super(grades, self).__init__(*args, **kw)

        #Validation of columns
        for key in ['BORO', 'GRADE','CAMIS']:
            if key not in self.columns:
                raise ValueError('Database does not contain "{}" label to filter.'.format(key))
            else:
                self.unique_grades = self.GRADE.unique()

    @property
    def _constructor(self):
        '''
        THis part allows that any object constructed from the class, is of the same class
        :return:
        '''
        return grades

    #This was a first approach to calculating the test of the list. However it was not considered because it was too
    #resource consuming
    #@staticmethod
    #def test_grades(grades_list):
    #    '''
    #    A utils functions, that tests the grades in the input 1 if improving, 0 if the same, -1 otherwise.
    #    Compares each element with the the inmediate following. With a list of n elements, it would return a list of
    #    n-1 elements.
    #    :param grades_list:
    #    :return: a list results
    #    '''
    #    n = len(grades_list)
    #    grade_result = []
    #    for i in range(n-1):
    #        if grades_list[i+1] < grades_list[i]:
    #           grade_result.append(1)
    #        elif grades_list[i+1] > grades_list[i]:
    #            grade_result.append(-1)
    #        else:
    #            grade_result.append(0)
    #    return  grade_result

    @staticmethod
    def test_grades(grades_list):
        '''
        A utils functions, that tests the grades in the input 1 if improving, 0 if the same, -1 otherwise.
        Compares the first and last elements inputted, so the list has to be ordered by date.
        It just considers the overall improvement of the first date and
         the last one (as computing a small regression)
        :param grades_list:
        :return: a integer (-1, 1, 0)
        '''

        if isinstance( grades_list, list)== False:
            raise  TypeError
        for i in  range(len(grades_list)):
            if isinstance(grades_list[i],str)== False:
                raise ValueError

        n = len(grades_list)
        if n==1:
            grade_result = 0
        else:
            if grades_list[-1] < grades_list[0]:
                grade_result = 1
            elif grades_list[-1] > grades_list[0]:
                grade_result = -1
            else:
                grade_result = 0
        return  grade_result



    def test_restaurant_grades(self,camis_id):
        """
        This functions calculates the overall grade of a restaurant given its camis id.
        It must be runned inside a Grade class object.
        First filters the data from the camis and then sorts the info by date to finally compute the indicator
        MUST have and additional columns Date, otherwise an exception is raised
        :param camis_id:
        :return: int 0, 1 -1 accordingly to the result of improvement or not of the restaurant
        """
	#Making sure column Date exists
        if 'Date' not in self.columns:
                raise ValueError('Database does not contain "{}" label to filter.'.format('Date'))
        else:
            grades = self[self['CAMIS']==camis_id]
            grades = grades.sort('Date', ascending = True)
            return grades.test_grades(list(grades['GRADE']))

    def test_restaurant_in_boro(self,boro):
        '''
        Function to compute the score of the boro.
        First selects the database by copying it, and adds the column Date to be used later in test_restaurant_grades
        :param boro name (str)
        :return:the overall score (sum of each restaurant) numeric
        '''
        #Select the DB from the boro
        boro_selected = self[self['BORO']==boro].copy()
        boro_selected['Date'] =pd.to_datetime(boro_selected['GRADE DATE'])
        results_boro = []
	#Obtaining results
        for camis in list(self.CAMIS.unique()):
            results_boro.append(boro_selected.test_restaurant_grades(camis))
        return sum(results_boro)

    def plot_by_boro(self, boro='NYC'):
        """
        Function that plots the grades of the selected boro. It saves a line plot as figure and pdf. In it
        each line corresponds to a grade. If no boro is inputted, in default returns NYC.
        The input object MUST be filtered with the info of the boro.

        :param boro, str
        :return: a figure , a pdf file saved in the current directory route
        """
        grades = self.unique_grades
        fig = plt.figure()
        for grade in grades:
            data_boro = pd.Series(self._generate_db_for_summary(grade))
            plt.plot(data_boro.keys(), data_boro, '-s', label=grade)
            plt.legend(loc="lower right")
            plt.title("Evolution of Grades in %s" %boro)

        plt.ylabel('Number of restaurants')
        plt.xlabel('Year')
        #Small conditional to print with the appropiate name
        if boro == 'STATEN ISLAND':            valueprint= 'staten'
        else:            valueprint = '%s' %str(boro).lower()
        #Saving file
        plt.savefig('grade_improvement_'+valueprint+'.pdf')
        return fig

    def _generate_db_for_summary(self, grade):
        """
        Filters the db to have rows of a certain grade, in order to generate an input to the plot.
        It is an internal function, not part of the API
        :param grade:
        :return: dictionary with the quantity  by year for the grade inputted
        """
        data = self.copy()
        data['Year'] =pd.to_datetime(data['GRADE DATE']).dt.year
        Years = data.Year.unique()
        data_by_grade = {}
        for year in Years:
            data_grade_year = data[(data['GRADE'] == grade) & (data['Year'] == year)]
            data_by_grade[datetime.datetime.strptime(str(year), '%Y')] = len(data_grade_year)
        return data_by_grade
