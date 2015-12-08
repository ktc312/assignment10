'''
Created on Dec 2, 2015

@author: ams889

This module contains the functions used for the assignment.
'''
import pandas as pd
from userDefinedErrorHandling import *
import sys
import matplotlib.pyplot as plt

def dataLoad():
    '''
    This function loads the csv from the URL used to access the data. It also prints a 
    wait message as loading the data dynamically typically takes about 30 seconds
    '''
    print("Please wait, data loading (may take up to a minute)...")
    try:
        df = pd.DataFrame(pd.read_csv('https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'))
        print("Data loaded!")
        return df
    except IOError:
        print('Data could not be accessed, program closing')
        sys.exit(1)

def dataClean(df):
    '''
    This function cleans the grade column removing pending grades, missing grades 
    and other non-letter grades as well as the boro column
    '''
    gradeMask = df.GRADE.isin(['A', 'B', 'C'])
    df = df.loc[gradeMask,:]
    boroughs=["MANHATTAN", "BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND"]
    gradeMask = df.BORO.isin(boroughs)
    df = df.loc[gradeMask,:]
    df=df.dropna(subset=["GRADE DATE"])
    return df

def test_grades(grade_list):
    '''
    This function returns 1, 0 or -1 if the grade improves, remains the same,
    or decreases (respectively). I chose to use only the first and last letter as
    initially my code iterated through all changes (A to C = -2, A to B = -1 and similarly
    C to A = +2, etc.) and then returned the net, but this is the same as taking the 
    first and the last and since we treat any decrease as '-1' we don't care what
    the overall difference is, just that there was a decrease (and vise versa for an increase)
    '''
    if len(grade_list)==0:
        raise grade_listFormatError('Grade list must contain at least one value')
    if grade_list[-1] > grade_list[0]:
        return -1
    elif grade_list[-1] < grade_list[0]:
        return 1
    else:
        return 0

def gradeOverTimePlot(data,boro):
    '''
    This function plots the grades by month per each borough or for
    the entire NYC dataset (depending on input)
    '''
    if boro=="ALL":
        boro="NYC"
        dfGrades=data
    else:
        dfGrades=data[data["BORO"]==boro]
    dfGrades=dfGrades.reset_index()
    dfGrades['YEARMON']=0
    for i in range(len(dfGrades)):
        dfGrades['YEARMON'][i]=int(str(dfGrades["GRADE DATE"][i][6:10])+str(dfGrades["GRADE DATE"][i][0:2]))
    df1=dfGrades[["GRADE", "YEARMON"]]
    df1=df1.sort(['YEARMON'], ascending=1)
    output=df1.groupby(["YEARMON", "GRADE"]).GRADE.count().unstack("GRADE")
    output=output.fillna(0)
    fig, ax = plt.subplots()
    fig.canvas.draw()
    labelData=df1["YEARMON"] #To be used for labeling the x-ticks
    labelData=labelData.drop_duplicates()
    labelData=labelData.reset_index()
    labelData['MonthYear']=0
    for i in range(len(labelData)):
        labelData['MonthYear'][i]=(str(labelData["YEARMON"][i])[4:6]+"-"+str(labelData["YEARMON"][i])[0:4])
    labels = [labelData['MonthYear'][0], labelData['MonthYear'][10], labelData['MonthYear'][20], labelData['MonthYear'][30], labelData['MonthYear'][40], labelData['MonthYear'][len(labelData)-1]]
    ax.set_xticklabels(labels)
    plt.xlim(0, len(labelData)-1) #To keep the scale reasonable for each borough
    plt.title('Grade Improvement in '+boro+" over time.")
    plt.xlabel('Date')
    plt.ylabel('Number of Restaurants')
    plt.plot(output["A"], label="A")
    plt.plot(output["B"], label="B")
    plt.plot(output["C"], label="C")
    plt.legend(loc="upper left")
    plt.savefig('grade_improvement_'+str(boro)+'.pdf')
    plt.close()
    