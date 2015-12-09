from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


__author__ = 'obr214'

"""
RestaurantGrader Class
Constructor Receives a Dataframe
Contains functions to get the Scores of each Borough and to create the Plots
"""


class RestaurantGrader:

    def __init__(self, dataframe):
        self.inspection_df = dataframe

    @staticmethod
    def test_grades(grade_list):
        """
        Evalates the tendency of the grades and calculates a score.
        0 if the tendency is the same
        -1 if the tendency goes downwards
        1 if the tendency goes upwards
        :param grade_list: Receives a List of Grades. Ex. ['A','B','C']
        :return: Integer, 0, -1, 1
        """
        try:
            map_grades = {'A': 1, 'B': .5, 'C': 0}

            number_grades = np.array([map_grades[x] for x in grade_list])

            total_grades = np.array(range(len(number_grades)))

            slope, intercept, r_value, p_value, std_err = linregress(total_grades, number_grades)

            if slope > 0:
                return 1
            elif slope < 0:
                return -1
            else:
                return 0
        except LookupError:
            raise LookupError("Grade Not Found")

    def test_restaurant_grades(self, camis_id):
        """
        Gets the grades given to a restaurant and calculate its score.
        :param camis_id: A CAMIS Identifier
        :return: Int -1, 0. 1
        """
        try:
            list_grades = self.inspection_df.loc[self.inspection_df['CAMIS'] == camis_id].sort(
                ['GRADE DATE'])['GRADE'].tolist()
            return self.test_grades(list_grades)
        except LookupError:
            raise LookupError("Column Not Found in Dataframe")

    def get_boroughs_scores(self):
        """
        Calculates the score of every borough in NYC by summing the grades of each of their restaurantes.
        It prints the result in console,
        :return: None
        """
        try:
            boroughs = self.inspection_df['BORO'].unique()

            ny_score = 0
            for boro in boroughs:
                boro_score = 0
                list_boro_camis = self.inspection_df.loc[self.inspection_df['BORO'] == boro]['CAMIS'].unique()
                for camis_id in list_boro_camis:
                    boro_score += self.test_restaurant_grades(camis_id)
                print boro + " Score:" + str(boro_score)
                ny_score += boro_score

            print "Overall NYC Score:" + str(ny_score)
        except LookupError:
            raise LookupError("Column Not Found in Dataframe")

    @staticmethod
    def __plot_grades(inspection_df, boro=None):
        """
        Function that groups the dataframe by Date and Grade.
        :param boro: Name of the Borough to Plot. If its None, the labels correspond to the entire NYC
        :return: None
        """
        try:
            boro_str = ''
            if boro:
                boro_str = str(boro.split(' ')[0]).lower()
            else:
                boro_str = 'nyc'

            times = pd.DatetimeIndex(inspection_df['GRADE DATE'])
            year_groups = inspection_df.groupby([times.year, 'GRADE']).size().to_frame()

            grouped_df = year_groups.unstack()
            #Get the indexes
            years_ids = grouped_df.index.values
            #Get the columns
            grouped_df.columns = grouped_df.columns.droplevel()
            grade_columns = grouped_df.columns.values
            grouped_df = grouped_df.fillna(0)
            try:
                for grade in grade_columns:
                    plt.plot(years_ids, grouped_df[grade], label='Grade '+str(grade))
            except LookupError:
                pass

            try:
                plt.xticks(years_ids, years_ids)
                plt.xlabel("YEAR", fontsize=14)
                plt.ylabel("Number of Grades", fontsize=14)
                if boro:
                    plt.title("GRADES OF " + str(boro), fontsize=14)
                else:
                    plt.title("GRADES OF NYC", fontsize=14)
                plt.legend(loc=2)
                plt.savefig("grade_improvement_" + boro_str + ".pdf")
                print "File Created: grade_improvement_" + boro_str + ".pdf"
                plt.show()
            except IOError:
                raise IOError("Cannot create the file: grade_improvement_" + boro_str + '.pdf')
        except LookupError:
            raise LookupError("Column Not Found In Dataframe")

    def grade_improvement_plots(self):
        try:
            #Creates the plots for NYC
            self.__plot_grades(self.inspection_df)

            #Creates the plots for the 5 Boroughs
            boroughs = self.inspection_df['BORO'].unique()

            for boro in boroughs:
                boro_df = self.inspection_df.loc[self.inspection_df['BORO'] == boro]
                self.__plot_grades(boro_df, boro)
        except IOError as io_message:
            raise IOError(io_message)
        except LookupError as lu_error:
            raise LookupError(lu_error)
