import pandas as pd
import numpy as np

class InvalidGradeException(Exception):
    '''Exception raised if grade being tested is invalid'''
    pass

class RestaurantDataController(object):
    """Class to load and manipulate restaurant inspection data"""
    def __init__(self, datafile):

        # Column 6 (phone number) has mixed type, so will throw an warning
        # if we don't specify the dtype
        self.data = self.clean_data(pd.read_csv(datafile, dtype={6: object}))

    def clean_data(self, dataframe):
        '''Return cleaned version of dataframe'''
        # The data contains a row for each violation, for each inspection
        # Keep only one grade per inspection date for each CAMIS ID
        dataframe.drop_duplicates(subset=['CAMIS', 'INSPECTION DATE'],
                                    inplace=True)

        # Replace Z, P, and "Not Yet Graded" (all meaning a pending grade)
        # with missing
        dataframe['GRADE'].replace(["Z", "P", "Not Yet Graded"],
                                    value=None, inplace=True)

        # Sort by CAMIS and then inspection date
        dataframe.sort(columns=['CAMIS', 'INSPECTION DATE'], inplace=True)
        return dataframe


    def test_grades(self, grade_list, margin=.15):
        """Test the grades in a list, ordered by date.
        If grades are improving, return 1. If they are declining, return -1.
        If they are staying the same, return 0.

        To classify, we regress the grade on the index (i.e. where it is in the
        list). Essentially, we are calculating the average grade increase one
        would expect from moving from grade i to grade i+1.

        margin is the range around 0 to classify as "steady". When the slope
        (i.e. coefficient) is within that value of 0, returns 0."""
        # Convert strings to a categorical series
        categorical = pd.Categorical(grade_list,
                                    categories=['C', 'B', 'A'],
                                    ordered=True)
        # Drop any grades that are not in the listed categories (e.g. P, Z)
        categorical = categorical.dropna()

        # Create a series using the codes from the categorical object
        # This converts the categories into numbers but preserves the ordering
        # specified in the categories= parameter array
        grade_series = pd.Series(categorical.codes)

        # Convert to an array that can be used for a linear regression
        # see http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
        indep_var_array = np.vstack([grade_series.index, np.ones(len(grade_series))]).T

        try:
            slope, intercept = np.linalg.lstsq(indep_var_array, grade_series)[0]

            if slope > margin:
                return 1
            if slope < -1.*margin:
                return -1
            # Steady
            return 0
        except ValueError:
            return np.nan


    def get_restaurant_grades(self, camis_id):
        '''Return list of grades for a given restaurant'''
        return list(self.data.ix[self.data.CAMIS==int(camis_id), 'GRADE'])


    def test_restaurant_grades(self, camis_id):
        """Method to test the grades of a particular restaurant, as identified
        by its CAMIS ID"""
        return self.test_grades(self.get_restaurant_grades(camis_id))

    def output_graph(self, geography="nyc", filename=None):
        """Output a PDF of a plot showing the grades over time in a certain
        geography, either 'nyc' for the whole city, or each
        borough ('bronx', 'queens', 'brooklyn', 'manhattan', 'staten')."""
        pass
