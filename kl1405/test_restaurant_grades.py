import pandas as pd
from test_grades import test_grades

# author: Kaiwen Liu

'''q4'''
def test_restaurant_grades(df_resturant,camis_id):   
    # this function returns value for each resturant with function test_grades
    df_eachresturant=df_resturant.ix[camis_id]
    df = list(df_eachresturant['GRADE'])
    return test_grades(df)