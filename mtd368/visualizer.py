"""This module visualizes the data by Borough and over all of NYC."""

#author: Matthew Dunn
#netID: mtd368
#date: 12/12/2015

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class retaurantGradeAnalyzer (object):
    def __init__(self, allrestaurantsData, listofBoros):
        self.allrestaurantsData = allrestaurantsData[['BORO', 'GRADE', 'GRADE DATE']]
        self.allrestaurantsData['Counter'] = 1
        self.listofBoros = listofBoros

    def restsbygradeovertime(self):
        restaurantsovertime = self.allrestaurantsData
        restaurantsovertime1 = restaurantsovertime.groupby(['GRADE DATE', 'GRADE']).size().unstack()
        restaurantsovertime1 = restaurantsovertime1.resample('Q')
        restaurantsovertime1.plot(kind='line', by=['GRADE DATE', 'GRADE'])
        plt.title('NYC Restaurant Grade Imporvement')
        plt.savefig('figures/nyc_grade_improvement_ny.pdf',format = 'pdf')

    def createsingleborotoplot(self):
        for i in np.arange(len(self.listofBoros)):
            restaurantsovertime = self.allrestaurantsData[self.allrestaurantsData['BORO'] == self.listofBoros[i]]
            restaurantsovertime1 = restaurantsovertime.groupby(['GRADE DATE', 'GRADE']).size().unstack()
            restaurantsovertime1 = restaurantsovertime1.resample('Q')
            restaurantsovertime1.plot(kind='line', by=['GRADE DATE', 'GRADE'])
            plt.title('Restaurant Grade Imporvment for ' + self.listofBoros[i])
            plt.savefig('figures/boro_grade_improvement_' + self.listofBoros[i] + '.pdf',format = 'pdf')


