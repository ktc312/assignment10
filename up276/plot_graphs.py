'''
Created on Dec 04, 2015
@author: Urjit Patel - up276
'''

import matplotlib.pyplot as plt
import numpy as np

class PlotGraphs:

    @staticmethod
    def Plot(GradeCountData,plot_name):
        Years = ['2011','2012','2013','2014','2015']
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title('Year - Grades count')
        x_values=np.arange(1,6)
        plt.legend(loc="upper left")
        plt.figure(figsize=(10,12))

        for grade in GradeCountData:
            clr = (np.random.rand(), np.random.rand(), np.random.rand())
            plt.plot(x_values , GradeCountData[grade] , color=clr, label = 'grade'+grade )
            plt.legend(loc="upper left")

        plt.xticks(x_values,Years, rotation='vertical')
        plt.savefig(plot_name)
        plt.clf()
        #plt.show()
        #plt.clf()

    @staticmethod
    def PlotBoroughsGraphs(BoroughData):

        PlotGraphs.Plot(BoroughData['BRONX'],'grade_improvement_bronx.pdf')
        PlotGraphs.Plot(BoroughData['BROOKLYN'],'grade_improvement_brooklyn.pdf')
        PlotGraphs.Plot(BoroughData['MANHATTAN'],'grade_improvement_manhattan.pdf')
        PlotGraphs.Plot(BoroughData['STATEN ISLAND'],'grade_improvement_statn.pdf')
        PlotGraphs.Plot(BoroughData['QUEENS'],'grade_improvement_queens.pdf')



