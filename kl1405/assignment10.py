import numpy as np
import pandas as pd
from test_restaurant_grades import *
from plot import *
from date import *

# Author: Kaiwen Liu
# this main functionw will clean the data and return values for each boro and then plot the graphs for each boro using
# the functions 

def main():
    
    try:
        while True:

            #import data as dataframe and remove missing values
            data=pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
            data=pd.DataFrame(data)
            keep=['A','B','C']
            df_clean=data[data['GRADE'].isin(keep)]
            # clean the NAN grade date
            df_clean=df_clean[df_clean['GRADE DATE'].isnull()==False]
            # make the grade date as a list and then format the date
            list_d=list(df_clean['GRADE DATE'])  
            # format the grade date
            #df_clean = data[pd.isnull('GRADE DATE') = False]
            # df_clean = data[data['GRADE DATE'] != np.nan]
            formatted_date = format_date(list_d)
            df_clean['Date']= formatted_date
            df_resturant=df_clean.set_index('CAMIS')

            '''
            q4. compute the sum of values over all trstaurants in the dataset and for each of the boroughs 
            '''
            # a dataframe grouped by boro column
            df_boro=df_resturant.groupby('BORO')
            print 'Sum for each boro:'
            #  value for each CAMIS in each boro
            for boros,resturant in df_boro:
                df_resturantgroup=resturant.groupby(level='CAMIS',sort=True)
                value = 0
                for CAMIS, resturant_2 in df_resturantgroup:
                    # to get the vlue apply the test_restaurant_grades function
                    value = value +test_restaurant_grades(resturant_2,CAMIS)
                print boros
                print value
        
            '''
            q5. plot the six graphs 
            '''
            plots(df_clean, 'nyc').plot() 
             # remove the boro 'missing'
            boro=['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']
            df_clean_remove_missing=df_clean[df_clean['BORO'].isin(boro)]
            # rename the label so that the files name match the instruction
            df_boroname=df_clean_remove_missing.replace(['BRONX','QUEENS','BROOKLYN','MANHATTAN','STATEN ISLAND'] , ['bronx','queens','brooklyn','manhattan','staten']) 
            df_boroughs=df_boroname.groupby('BORO')

            # get the value for each boro
            for boroughs,group in df_boroughs:
                plots(group, boroughs).plot()
                print 'graph generated and saved'

            result=open('results.txt','w')
            result.write('Q5) According to the plots, we can see that the amount of grade A are expanding for both nyc as a whole or in each boro. Therefore we can say that the grading system motivates resturant improving their quality')
            result.write('\n')
            result.write('\nQ6) There are many other information we can find out using this data. For example, using the cuisine column with our test_Grades function, we can see which cuisine presents the best quality. Also, for some large resturant chains we can see their quality at different boros.')
            result.write('\n\nI think this data is useful for assessing the quality of new york city, for example, if a resturant constantly graded below A, then this kind of restuant can be considered as bad quality resturant because they are likely not working for a higher grade. On the opposite resturants that constantly graded as A can be considered as high quality resturants. Using this logic, we can have a close look at the quality of new york resturant.')
            result.close()
            print 'results.text saved'
            break

    except ZeroDivisionError:
        print "\n Math Error"
    except ArithmeticError, OverflowError:
        print "\n Math Error"

if __name__ == '__main__':
    main()