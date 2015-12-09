'''
Created on Nov 30, 2015

@author: mc3784
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class loadRestaurant():
    df=0
    def __init__(self):
        """
            Constructor of the class that load the data in the file DOHMH_New_York_City_Restaurant_Inspection_Results.csv
        """
        df=pd.DataFrame.from_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
        self.df = df.dropna()
        self.df = self.df[self.df.BORO != "Missing"]
        
    def test_grades(self,grade_list):
        """
            Evaluate if the passed list of grades are improving (returned value 1), keeping the same (return 0) or declining (return -1).
            The chosen creteria is obtained comparing the last grade in the list with the max of all the previous ones. 
            Improving if the last value is greater thant the max, keeping the same if it is equal and declining otherwise.  
        """
        fromLetterTonumber={'A':10, 'B':9, 'C':8, 'P':5, 'Z':0}
        gradeConverted = [fromLetterTonumber[x] for x in grade_list]
        if gradeConverted[-1] > np.mean(gradeConverted[:-1]):
            return 1
        elif gradeConverted[-1] == np.mean(gradeConverted[:-1]):
            return 0
        else:
            return -1
    
    def test_all_restaurant_grades(self):
        """
            This function evaluate the total score of the restaurant in each boro in the data set.
        """
        boros = self.df["BORO"].unique()
        scorePerBoros = np.zeros([len(boros)])
        for nBoro,boro in enumerate(boros):
            print "Start evaluation for ",boro
            totalSum=0
            dfForBoro = self.df[self.df.BORO==boro]
            for id_restaurant in np.unique(dfForBoro.index.values):
                try: 
                    subDFOrdered = dfForBoro.loc[id_restaurant].sort("GRADE DATE")
                    evaluation = self.test_grades(subDFOrdered["GRADE"].tolist())
                except:
                    evaluation=0
                totalSum+=evaluation
            scorePerBoros[nBoro]=totalSum
            print "total sum=", totalSum
        return scorePerBoros
 
    def test_restaurant_grades(self,camis_id):
        """
            This function evauate the score of the restaurant with id camis_id.
        """
        try: 
            subDFOrdered = self.df.loc[camis_id].sort("GRADE DATE")
            score = self.test_grades(subDFOrdered["GRADE"].tolist())
        except:
            score=0
        return score
    
    def plot(self,dataToPlot,boro):
        """
            This function plot the data inside the dataToPlot in one line for each grade, and it saves it in a pdf file with the name of the boro.  
        """
        plotName="grade_improvement_"+boro+".pdf"
        plt.plot(dataToPlot.index.values,dataToPlot["A"],label="A")
        plt.plot(dataToPlot.index.values,dataToPlot["B"],label="B")
        plt.plot(dataToPlot.index.values,dataToPlot["C"],label="C")
        plt.plot(dataToPlot.index.values,dataToPlot["P"],label="P")
        plt.xticks(dataToPlot.index.values,dataToPlot.index.values)
        plt.xlabel("YEAR")
        plt.ylabel("# of restaurants")
        plt.title(boro)
        plt.legend(loc=2)
        plt.savefig(plotName)
        plt.clf()
                    
    def savePlot(self):
        """
            This function 
        """
        print "Start plot for all restaurants in nyc"
        a = self.df.groupby([pd.DatetimeIndex(self.df['GRADE DATE']).year,'GRADE']).size()
        a = a.unstack()
        self.plot(a,"nyc")
    
        boros = self.df["BORO"].unique()
        for boro in boros:
            print "Start plot for restaurants in ",boro.lower()
            dfForBoro = self.df[self.df.BORO==boro]
            a = dfForBoro.groupby([pd.DatetimeIndex(dfForBoro['GRADE DATE']).year,'GRADE']).size()
            a = a.unstack()
            self.plot(a,boro.lower())
    
if __name__=="__main__":
    restaurants=loadRestaurant()
    restaurants.test_all_restaurant_grades()
    restaurants.savePlot()
    
    
    
    
    
    
