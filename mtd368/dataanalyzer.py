"""This module does the heavy lifting to get the data prepared for analysis and visualization."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/06/2015

import numpy as np
import pandas as pd

def restaurant_analyzer(restaurantData):

    '''This function takes a dataframe with restaurant data and evaluates the
    trend of the restaurant's rating grade over time.
    '''

    camisIDs = restaurantData.CAMIS.unique()
    finalscores = restaurantData.drop_duplicates(subset='CAMIS')
    finalscores = finalscores[['CAMIS', 'BORO']]
    finalscores.set_index('CAMIS', inplace=True)
    finalscores['Score'] = np.nan
    for i in camisIDs:
        score = test_restaurant_grades(i, restaurantData)
        finalscores.ix[i,'Score'] = score
    scoresByBoro = finalscores.groupby('BORO').sum()
    scoreAllNYC = finalscores['Score'].sum()
    print scoresByBoro, '\n\nNYC           ', str(int(scoreAllNYC))

def test_restaurant_grades(camis_id, restaurantData):

    '''This function takes a list of restaurant ids and a dataframe of all restaurant data
    and then returns a score of 1, 0, or -1 depending on the trend of the grades is improving,
    static, or deteriorating.
    '''

    restaurantData = restaurantData[restaurantData.CAMIS == camis_id]
    restaurantData = restaurantData.sort_values(['GRADE DATE'])
    score = test_grades(restaurantData.GRADE.values)
    return score

def test_grades(grade_list):

    ''' The rationale here is that we track the running score of the grade in relation to the precedding value.
    If the net value after running through the list is greater than zero, we return 1, if less than zero we return -1,
    if it = 0 we return 0 to represent the grade didn't change in net value.
    '''

    scorevalue = 0
    for i in range(len(grade_list)-1):
        current = grade_list[i]
        nextGrade = grade_list[i+1]
        if current == nextGrade:
            scorevalue += 0
        elif current == 'A' or current == 'C':
            if current == 'A':
                scorevalue -= 1
            else:
                scorevalue += 1
        else:   # if it wasn't an A or C we know it was a B grade.
            if nextGrade == 'A':
                scorevalue += 1
            else: # if it wasn't an A grade then we know it was a C grade.
                scorevalue -= 1
    if scorevalue > 0:
        return +1
    elif scorevalue < 0:
        return -1
    return 0
