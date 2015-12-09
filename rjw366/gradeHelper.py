'''
Created on Dec 2, 2015

@author: rjw366
'''
import pandas as pd

class gradeHelper(object):
    
    def __init__(self,dataName):
        df = pd.read_csv(dataName)
        #Dropping rows with: NaN, Not Yet Graded, and Pending(P or Z) values
        df = df.dropna(subset=['GRADE'])
        df = df[df.GRADE != 'Not Yet Graded']
        df = df[df.GRADE != 'P']
        self.df = df[df.GRADE != 'Z']

    def test_grades_old(self,grade_list):
        '''Test whether grades are decreasing or increasing overtime
            Only tests steps up or steps down in grades(eg. [A to B] == [A to C])
            There are only three grades so size of step is not worth weighting.
            
            In an extreme case ['A', 'B', 'C', 'A', 'B', 'C', 'A'] 
                The start and end are A's - seemingly good.
                Averaging or weighting the grades/steps would lean towards an A - One more A than anything else
                When in reality the place is constantly decreasing until it hits rock bottom and spikes
        '''
        if(len(grade_list) > 0):
            score_over_time = 0
            for ix, grade in enumerate(grade_list):
                if(len(grade_list)-1 == ix):
                    break;
                #Using ASCII - A < B < C
                if(grade > grade_list[ix + 1]):
                    score_over_time += 1
                elif(grade < grade_list[ix + 1]):
                    score_over_time -=1
    
    def test_grades(self,grade_list):
        ''' Test whether grades are decreasing or increasing overtime
            See test_grades_old for old implementation, was taking way to much time, but this is quicker and
            has just as much logic
            
            Thinking mathematically, change in grade over time would be the slope of the grades, and slope
            would be most defined between the earliest and latest value we have, or the first and most recent grade.
            So the score is purely based on the first and last grade.
        '''
        if(len(grade_list) > 0):
            if(grade_list[0] < grade_list[-1]):
                return -1
            elif(grade_list[0] > grade_list[-1]):
                return 1
            return 0
    
    def test_restaurant_grades(self,camis_id):
        grade_list = self.df.loc[self.df['CAMIS'] == camis_id]['GRADE'].values
        return self.test_grades(grade_list)


