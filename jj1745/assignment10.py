'''
Created on Dec 3, 2015

@author: jj1745

The main program
'''

from loader import cleanData
from analysis import computeSumforDiffBoro, plotTotalNum, plotEachBoro

if __name__ == '__main__':
    
    df = cleanData()
    
    # print results
    computeSumforDiffBoro(df)
    
    print 'making plots...'
    # make plots
    plotTotalNum(df)
    plotEachBoro(df)
    
    print 'Your plots have been saved. Thanks!'
    
    