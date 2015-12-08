import pandas as pd
import numpy as np
from datetime import datetime
import sys
import matplotlib.pyplot as plt
from plotting import percentage_graph, bar_graph

class InvalidGradeException(Exception):
    '''Exception raised if grade being tested is invalid'''
    pass

class RestaurantDataController(object):
    """Class to load and manipulate restaurant inspection data"""
    def __init__(self, datafile):
        print "%s Loading data file..." % datetime.now()
        sys.stdout.flush()
        # Column 6 (phone number) has mixed type, so will throw an warning
        # if we don't specify the dtype
        self.data = pd.read_csv(datafile,
                                    usecols=['CAMIS', 'BORO', 'INSPECTION DATE',
                                                'GRADE'],
                                    #dtype={6: object},
                                    parse_dates=['INSPECTION DATE'])
        print "%s Done loading" % datetime.now()
        sys.stdout.flush()
        self.clean_data()


    def clean_data(self):
        '''Clean the RDC's data'''
        print "%s Cleaning data..." % datetime.now()
        sys.stdout.flush()
        # The data contains a row for each violation, for each inspection
        # Keep only one grade per inspection date for each CAMIS ID
        self.data.drop_duplicates(subset=['CAMIS', 'INSPECTION DATE'],
                                    inplace=True)

        # Replace Z, P, and "Not Yet Graded" (all meaning a pending grade)
        # with missing
        self.data['GRADE'].replace(["Z", "P", "Not Yet Graded"],
                                    value=None, inplace=True)

        # Drop all rows with missing borough or grade, or with date <
        self.data = self.data[self.data['INSPECTION DATE'] > datetime(1900,1,1)]
        self.data.dropna(subset=['CAMIS', 'INSPECTION DATE', 'GRADE', 'BORO'],
                        inplace=True)


        # Create numeric grade column
        self.grade_mapping = {"A": 3, "B": 2, "C": 1}
        self.data['grade_value'] = self.data.GRADE.map(self.grade_mapping)

        # Create year variable
        self.data['year'] = self.data['INSPECTION DATE'].apply(lambda x: x.year)

        # Sort by CAMIS and then inspection date
        self.data.sort(columns=['CAMIS', 'INSPECTION DATE'], inplace=True)

        print "%s Done cleaning" % datetime.now()
        sys.stdout.flush()
        return self.data


    def test_grade_values(self, grade_values, margin=0.15):
        '''
        If grades are improving, return 1. If they are declining, return -1.
        If they are staying the same, return 0.

        grade_values is a list of grades in NUMERICAL form.

        To classify, we regress the grade on the index (i.e. where it is in the
        list). Essentially, we are calculating the average grade increase one
        would expect from moving from grade i to grade i+1.'''
        # Convert to an array that can be used for a linear regression
        # see http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
        indep_var_array = np.vstack([np.arange(len(grade_values)),
                                    np.ones(len(grade_values))]).T
        try:
            slope, intercept = np.linalg.lstsq(indep_var_array, grade_values)[0]
            if slope > margin:
                return 1
            if slope < -1.*margin:
                return -1
            # Steady
            return 0
        except ValueError:
            return np.nan

    def test_grades(self, grade_list, **kwargs):
        """Test the grades in a list, ordered by date.

        Convert grade_list to numerical form, then call test_grade_values."""
        grade_series = pd.Series(grade_list)
        return self.test_grade_values(grade_series.map(self.grade_mapping),
                                        kwargs)



    def get_restaurant_grades(self, camis_id, grade_col='grade_value'):
        '''Return list of grades for a given restaurant.

        Default is to return grade values, but if grade_col is set to another
        column name (e.g. GRADES), that will be returned.'''
        return list(self.data.ix[self.data.CAMIS==int(camis_id), 'grade_value'])


    def test_restaurant_grades(self, camis_id):
        """Method to test the grades of a particular restaurant, as identified
        by its CAMIS ID"""
        return self.test_grade_values(self.get_restaurant_grades(camis_id, grade_col='grade_value'))

    def cut_to_geography(self, geography="nyc"):
        '''Return data cut to only a certain geography'''
        geography = geography.upper()
        if geography != "NYC":
            return self.data[self.data['BORO']==geography]
        else:
            return self.data

    def get_grade_counts_by_year(self, data):
        '''Return a dataframe with grade counts by year'''
        counts = data.groupby("year")['GRADE'].value_counts().unstack()
        pcts = counts.divide(counts.sum(axis=1), axis=0) * 100
        return counts, pcts

    def test_grouped_restaurant_grades(self, data):
        '''Group data by CAMIS and return test results'''
        grouped = data.groupby('CAMIS')
        return grouped.grade_value.apply(self.test_grade_values)

    def sum_trends_for_geography(self, geography="nyc"):
        '''Get the sum of the trends (i.e. the results of test_grades)
        for every restaurant in a certain geography.

        Geography can be (case insensitive):
        nyc (default)
        bronx
        brooklyn
        manhattan
        queens
        staten island
        '''
        grade_trends = self.test_grouped_restaurant_grades(
                            self.cut_to_geography(geography=geography)
                        )
        return np.sum(grade_trends)


    def output_graph(self, geography="nyc", filename=None):
        """Output a PDF of a plot showing the grades over time in a certain
        geography, either 'nyc' for the whole city, or each
        borough ('bronx', 'queens', 'brooklyn', 'manhattan', 'staten')."""
        print "Outputting figure...%s" % filename
        sys.stdout.flush()

        # Get counts and percents
        counts, pcts = self.get_grade_counts_by_year(self.cut_to_geography(geography))

        # Create axes and figure
        fig, axes = plt.subplots(2, 1, sharex=False)
        fig.set_size_inches(8.5, 11)
        fig.subplots_adjust(right=2)

        percentage_graph(pcts, axes[0])
        bar_graph(counts, axes[1])

        if filename is not None:
            fig.savefig(filename)
        else:
            plt.show()
