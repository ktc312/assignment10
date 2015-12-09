'''
Created on Dec 8, 2015

@author: jj1745
'''

class Restaurant(object):
    '''
    The restaurant object, where each restaurant is determined by its unique camis_id
    '''


    def __init__(self, camis_id):
        '''
        Constructor
        '''
        self.id = camis_id
    
    def test_grades(self, grade_list):
        '''
        This is the helper function that determines the trend of the grades
        if the ending grade is better return 1; if the beginning grade is better, return -1; else return 0
        '''
        score_book = {'A':3, 'B':2, 'C':1}
        init_grade = grade_list[0]
        final_grade = grade_list[-1]
        
        # get the transformed grade
        init_score = score_book[init_grade]
        final_score = score_book[final_grade]
        
        if final_score > init_score:
            return 1
        elif final_score < init_score:
            return -1
        else:
            return 0
        
    
    def test_restaurant_grades(self, df):
        '''
        given the whole dataframe, compute the trend based on camis_id
        '''
        restaurant_data = df[df['CAMIS'] == self.id]
        restaurant_data = restaurant_data.sort('DATE')
        grade_list = restaurant_data['GRADE'].tolist()
        
        return self.test_grades(grade_list)
        
        