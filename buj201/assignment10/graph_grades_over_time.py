'''
Created on Dec 1, 2015

@author: Benjamin Jakubowski (buj201)
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

def plot_num_restaurants_by_grade_by_year(boro='NYC'):
    '''For each restaurant in the input borough (or citywide, if no borough specified),
    plots the total number of restaurants last given an 'A', 'B', or 'C' grade at the end of each
    calendar year 2011-2015. Shows figure (prints to screen), and saves plot in 'figures' directory.'''
    data = pd.read_csv('data/clean_restaurant_grades.csv',index_col=0, parse_dates=['GRADE DATE'])
    data.sort(columns='GRADE DATE', inplace=True)
    data = data.join(pd.get_dummies(data.GRADE, prefix='grade'))
    if boro=='NYC':
        pass
    elif boro in ['BRONX','MANHATTAN','BROOKLYN','STATEN ISLAND','QUEENS']:
        data = data.loc[data['BORO']==boro,:]
    else:
        raise ValueError("Boro input must all-caps name of borough, or 'NYC'")
    totals = {}
    for EOY in pd.date_range(start='01-01-2011', end='01-01-2016', freq='A'):
        through_EOY = data.loc[data['GRADE DATE'] < EOY,:]
        current_ratings = through_EOY.groupby('CAMIS').last()
        totals[EOY.year] = {'A':current_ratings.grade_A.sum()/len(current_ratings), 'B':current_ratings.grade_B.sum()/len(current_ratings), 'C':current_ratings.grade_C.sum()/len(current_ratings)}
    totals = pd.DataFrame.from_dict(totals,orient='index')
    totals = totals.cumsum(axis=1)
    
    fig, ax = plt.subplots()
    ax.plot(totals.index, totals.A, color='g')
    ax.fill_between(totals.index, 0, totals.A, color='g', alpha=0.5)
    ax.plot(totals.index, totals.B, color='y')
    ax.fill_between(totals.index, totals.A, totals.B, color='y', alpha=0.5)
    ax.plot(totals.index, totals.C, color='r')
    ax.fill_between(totals.index, totals.B, totals.C, color='r', alpha=0.5)
    ax.set_xlabel('Year')
    ax.set_xticks([2011,2012,2013,2014,2015], minor=False)
    ax.set_xticklabels(['2011','2012','2013','2014','2015'])
    ax.set_ylabel('Proportion of restaurants with grades A, B, or C')
    if boro=='NYC':
        Title = 'Change in restaurant grades over time in ' + str(boro)
    else:
        Title = 'Change in restaurant grades over time in ' + str(boro).title()
    ax.set_title(Title)
    l1 = patches.Rectangle((0, 0), 1, 1, fc="g", alpha=0.5)
    l2 = patches.Rectangle((0, 0), 1, 1, fc="y", alpha=0.5)
    l3 = patches.Rectangle((0, 0), 1, 1, fc="r", alpha=0.5)
    ax.legend([l1,l2,l3],['Grade A', 'Grade B', 'Grade C'], loc='best')
    path = 'figures/grade_improvement_' + boro.lower().split(' ')[0] + '.pdf'
    fig.savefig(path)
    plt.show()
    return

def make_all_figures():
    print 'Making figure for NYC'
    plot_num_restaurants_by_grade_by_year(boro='NYC')
    for boro in ['BRONX','MANHATTAN','BROOKLYN','STATEN ISLAND','QUEENS']:
        print 'Making figure for', boro
        plot_num_restaurants_by_grade_by_year(boro)
    return