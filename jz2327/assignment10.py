import pandas as pd
from data_operation import *

# DS-GA 1007 Assignment 10
# Author: Junchao Zheng

def main():

    try:
        data_raw = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory = False)
        data = data_raw.dropna()    # Drop the rows where data has NaN values.
        data = data[data['GRADE'].isin(['A', 'B', 'C'])]    # Drop the rows where the grades are 'Not Yet Graded' or 'P' or 'Z'.
        data.rename(columns={'GRADE DATE':'DATE'}, inplace=True)    # Rename the column of 'GRADE DATE' making it efficient for following functions.
        data_short = data[['CAMIS','BORO', 'GRADE', 'DATE']]    # Choose data including certain columns.
        data_clean = data_short.drop_duplicates(['DATE','CAMIS'])   # Delete the duplicate grade for a certain grade date. 
        print 'Data Loaded...'

        # Compute the sum of the function over all restaurants in the dataset.
        print 'Now for Question4.1: compute the sum of the function over all restaurants in the dataset.'
        print 'Computing...\nIt may take several minutes.'
        score_total = 0
        for i in range(len(data_clean['CAMIS'].unique())):
            score_total = score_total + test_restaurant_grades(data_clean, data_clean['CAMIS'].unique()[i])
        print 'The sum of the function is: ' + str(score_total)

        # Compute the sum of the function over all restaurants for each of the five Boroughs.
        print 'Now for Question4.2: compute the sum of the function over all restaurants for each of the five Boroughs.'
        print 'Computing...\nIt may take several minutes.'
        borough_dictionary = {}
        for borough in data_clean['BORO'].unique()[:-1]:
            score_boro = 0
            data_given_borough = data_clean[data_clean['BORO'] == borough]
            for camis in data_given_borough['CAMIS'].unique():
                score_boro = score_boro + test_restaurant_grades(data_given_borough, camis)
            borough_dictionary[borough] = score_boro
        print 'Here list the sum of the function to each boroughs:'
        for key, val in borough_dictionary.items():
            print str(key) + ': ' + str(val)

        #plot the distribution of grade over all restaurants.
        print 'Now generate the plots for Question5.a.'
        plot_grade(data_clean, 'nyc')
        print 'Plots saved to pdf files.'

        #plot the distribution of grade over all restaurants in boroughs respectively.
        print 'Now generate the plots for Question5.b.'
        boro_list = data_clean['BORO'].unique().tolist()[:-1]
        for boro in boro_list:
            plot_grade(data_clean[data_clean['BORO'] == boro], boro)
        print 'Plots saved to pdf files.'

        print 'Program finish now. Bye!'
        
    except KeyboardInterrupt:
        print 'Terminate abnormally'

if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass