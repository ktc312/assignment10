'''
Created on Dec 3, 2015

@author: Benjamin Jakubowski (buj201)
'''
if __name__ == '__main__':
    
    import os.path
    import pandas as pd
    from test_restaurant_grades import save_test_restaurant_grades, sum_change_function_output, test_restaurant_grades 
    from graph_grades_over_time import *
    from get_and_clean_data import *
    
    def main():
        '''
        The main program in the assignment. Checks if clean and processed data already
        saved. If not, gets, cleans, and processes data. Then prints summary table describing
        sum of restaurant change scores citywide and by borough. Finally produces, saves, and
        displays figures showing change in restaurant grade distributions citywide and by
        borough for years between 2011 and 2015.
        '''
        
        ##Questions 1-3 don't require any output be produced, but we need to check that the cleaned
        ##and processed data have already been saved:
            
        if not os.path.exists('figures/'):
            os.makedirs('figures/')
                
        if not os.path.isfile('data/clean_restaurant_grades.csv'):
            clean_and_save_restaurant_data()
            
        if not os.path.isfile('data/trend_scores_by_restaurant.csv'):
            save_test_restaurant_grades()
            
        ##Question 4 requires we print the sum of all resaturant change scores citywide and by borough:
            
        print 'Question 4 output:\n'
        print "Sum of restaurant change scores citywide and by borough"
        print '(1: improving, 0: not changing, -1: declining)'
        print '------------------------------------------------------'
        sum_change_function_output()
        
        ##Question 5 requires we graph restaurant grades overtime- note we first check the
        ##directory 'figures/' exists.
            
        if not os.path.exists('data/'):
            os.makedirs('data/')
            
        make_all_figures()
        return 
    
    
    try:
        main()
    except KeyboardInterrupt:
        pass